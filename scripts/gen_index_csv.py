""" Generate a forScore-compatible index.csv from a built book PDF.

forScore (https://forscore.co/) imports an ``index.csv`` and turns each row
into a bookmark, so a musician who loads the OpenBook PDF on an iPad lands on
any tune with a couple of taps. See book-openbook issue #121.

The CSV columns are exactly what forScore expects::

    Title,Book Name,Start Page,End Page,Composer
    All The Things You Are,OpenBook,18,18,"J.Kern, O.Hammerstein"

Page numbers come from the book's own table of contents: LilyPond renders a
``\\table-of-contents`` whose every line is ``Title / Composer   <page>`` in
book order. We read the TOC pages of the PDF, take each tune's start page from
its TOC line, and set its end page to the next tune's start page minus one
(the last tune runs to the final page of the book). The Book Name is taken
from the PDF's basename so the same script serves openbook, israeli, etc.

Usage (wired into rsconstruct as an explicit processor):
    python -m scripts.gen_index_csv --inputs <book.pdf> --output-files <index.csv>
"""

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

# A TOC line: "<title> / <composer(s)>   <page>". The title may itself be
# empty of a composer (no " / "), so the composer group is optional. The
# trailing integer is the page label.
_TOC_LINE = re.compile(r"^(?P<body>.+?)\s{2,}(?P<page>\d+)\s*$")


def pdf_page_count(pdf: Path) -> int:
    """ Total number of pages in the PDF, via pdfinfo. """
    out = subprocess.run(
        ["pdfinfo", str(pdf)], capture_output=True, text=True, check=True
    ).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise ValueError(f"pdfinfo reported no page count for {pdf}")


def toc_page_range(pdf: Path) -> tuple[int, int]:
    """ First and last PDF page (1-based, inclusive) that hold TOC entries.

    A TOC page is one whose lines are overwhelmingly "text ... <number>"
    entries; song pages are not. We scan from the front until we find TOC
    pages and stop at the first page after them that has none. """
    first = None
    total = pdf_page_count(pdf)
    for page in range(1, total + 1):
        text = subprocess.run(
            ["pdftotext", "-layout", "-f", str(page), "-l", str(page), str(pdf), "-"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        hits = sum(1 for line in text.splitlines() if _TOC_LINE.match(line.strip()))
        if hits >= 5:
            if first is None:
                first = page
        elif first is not None:
            return first, page - 1
    if first is None:
        raise ValueError(f"no table-of-contents pages found in {pdf}")
    return first, total


def split_title_composer(body: str) -> tuple[str, str]:
    """ Split a TOC entry body "Title / Composer, Composer" into the two.

    A tune with no composer keeps an empty composer field. """
    if " / " in body:
        title, composer = body.split(" / ", 1)
        return title.strip(), composer.strip()
    return body.strip(), ""


def parse_toc(pdf: Path) -> list[tuple[str, str, int]]:
    """ Return (title, composer, start_page) for every tune, in book order. """
    lo, hi = toc_page_range(pdf)
    text = subprocess.run(
        ["pdftotext", "-layout", "-f", str(lo), "-l", str(hi), str(pdf), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    entries: list[tuple[str, str, int]] = []
    for line in text.splitlines():
        match = _TOC_LINE.match(line.strip())
        if not match:
            continue
        title, composer = split_title_composer(match.group("body"))
        if not title:
            continue
        entries.append((title, composer, int(match.group("page"))))
    return entries


def build_rows(pdf: Path, book_name: str) -> list[dict[str, object]]:
    """ Turn the parsed TOC into forScore rows with start and end pages. """
    entries = parse_toc(pdf)
    if not entries:
        raise ValueError(f"parsed no tunes from the TOC of {pdf}")
    total = pdf_page_count(pdf)
    rows: list[dict[str, object]] = []
    for index, (title, composer, start) in enumerate(entries):
        # End page is the page before the next tune starts; the last tune
        # runs to the end of the book.
        end = entries[index + 1][2] - 1 if index + 1 < len(entries) else total
        # a single-page tune whose successor starts on the same page
        end = max(end, start)
        rows.append(
            {
                "Title": title,
                "Book Name": book_name,
                "Start Page": start,
                "End Page": end,
                "Composer": composer,
            }
        )
    return rows


def write_csv(rows: list[dict[str, object]], out: Path) -> None:
    """ Write the rows as forScore's index.csv (quoting only where needed). """
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["Title", "Book Name", "Start Page", "End Page", "Composer"]
    with open(out, "w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """ main entry point """
    parser = argparse.ArgumentParser(description="Generate a forScore index.csv from a book PDF")
    parser.add_argument("--inputs", nargs="+", required=True, help="the built book PDF")
    parser.add_argument(
        "--output-files", nargs="+", required=True, dest="output_files", help="the index.csv to write"
    )
    args = parser.parse_args()

    pdfs = [Path(p) for p in args.inputs if p.endswith(".pdf")]
    if len(pdfs) != 1:
        print(f"expected exactly one .pdf input, got {args.inputs}", file=sys.stderr)
        sys.exit(1)
    pdf = pdfs[0]
    out = Path(args.output_files[0])

    # Book Name is the PDF stem, capitalised the way OpenBook presents it.
    stem = pdf.stem
    book_name = "OpenBook" if stem == "openbook" else stem

    rows = build_rows(pdf, book_name)
    write_csv(rows, out)
    print(f"wrote {len(rows)} tunes to {out}")


if __name__ == "__main__":
    main()
