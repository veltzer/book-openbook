#!/usr/bin/env python

"""
Join the engraved pieces of a chunked book into the book's PDF and PS.

See scripts/drivers_chunked.py for why big books are engraved in chunks.
Invoked per the rsconstruct explicit-processor contract:

    python -m scripts.merge_chunks \\
        --inputs <dir>/front.pdf <dir>/front.next <dir>/front_probe.next \\
                 <dir>/c00.pdf <dir>/c00.next ... \\
        --output-files <book>.pdf <book>.ps

The pieces go front first, then the chunks in name order. Before writing
anything, it checks that the page numbers the chunks were engraved with
really match where they land in the merged book: the front matter must
take as many pages as the probe said it would (or every page number in
the table of contents would be off), and each chunk must start right
after the previous one.

The table of contents links each tune to the URI chunkpage:<N> (the tunes
are in other PDFs when the front matter is engraved); here those links
become internal links to page N. Printed page numbers equal physical page
numbers, as the book starts at page 1.

The PS is converted from the merged PDF with pdftops (poppler-utils).
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject

URI_PREFIX = "chunkpage:"
RE_CHUNK_NAME = re.compile(r"^c\d+$")


def read_next(path: Path) -> int:
    """ the page number stored in a .next file """
    return int(path.read_text(encoding="utf-8"))


def by_name(paths: list[Path], name: str, suffix: str) -> Path:
    """ the single input called name+suffix """
    found = [p for p in paths if p.name == name + suffix]
    if len(found) != 1:
        raise ValueError(f"expected exactly one {name}{suffix} input, got {paths}")
    return found[0]


def link_toc(writer: PdfWriter, front_pages: int) -> int:
    """ turn the front matter's chunkpage: links into internal links;
    returns how many were converted """
    converted = 0
    for page in writer.pages[:front_pages]:
        for ref in page.get("/Annots", []):
            annot = ref.get_object()
            action = annot.get("/A")
            if action is None:
                continue
            uri = action.get_object().get("/URI")
            if uri is None or not str(uri).startswith(URI_PREFIX):
                continue
            target = int(str(uri)[len(URI_PREFIX):])
            if not 1 <= target <= len(writer.pages):
                raise ValueError(f"table of contents links to page {target} of {len(writer.pages)}")
            annot[NameObject("/A")] = DictionaryObject({
                NameObject("/S"): NameObject("/GoTo"),
                NameObject("/D"): ArrayObject([
                    writer.pages[target - 1].indirect_reference,
                    NameObject("/Fit"),
                ]),
            })
            converted += 1
    return converted


def merge(inputs: list[Path], pdf_out: Path, ps_out: Path) -> None:
    """ check and merge the pieces """
    front = by_name(inputs, "front", ".pdf")
    front_next = read_next(by_name(inputs, "front", ".next"))
    probe_next = read_next(by_name(inputs, "front_probe", ".next"))
    if front_next != probe_next:
        raise ValueError(
            f"the front matter takes {front_next - 1} pages but the chunks were numbered "
            f"for {probe_next - 1}; the table of contents would be wrong"
        )
    chunks = sorted(
        (p for p in inputs if p.suffix == ".pdf" and RE_CHUNK_NAME.match(p.stem)),
        key=lambda p: p.name,
    )
    if not chunks:
        raise ValueError(f"no chunk PDFs among {inputs}")
    writer = PdfWriter()
    writer.append(PdfReader(str(front)))
    front_pages = len(writer.pages)
    for chunk in chunks:
        start = len(writer.pages) + 1
        writer.append(PdfReader(str(chunk)))
        end = read_next(by_name(inputs, chunk.stem, ".next"))
        if end != len(writer.pages) + 1:
            raise ValueError(
                f"{chunk} lands on pages {start}-{len(writer.pages)} "
                f"but was engraved to end before page {end}"
            )
    links = link_toc(writer, front_pages)
    if links == 0:
        raise ValueError(f"no {URI_PREFIX} links found in the table of contents of {front}")
    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    with open(pdf_out, "wb") as stream:
        writer.write(stream)
    subprocess.run(["pdftops", str(pdf_out), str(ps_out)], check=True)


def main() -> int:
    """ main entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--output-files", nargs="+", required=True, dest="output_files")
    args = parser.parse_args()
    outputs = [Path(p) for p in args.output_files]
    pdf_out = [p for p in outputs if p.suffix == ".pdf"]
    ps_out = [p for p in outputs if p.suffix == ".ps"]
    if len(pdf_out) != 1 or len(ps_out) != 1 or len(outputs) != 2:
        raise ValueError(f"expected one .pdf and one .ps output, got {args.output_files}")
    try:
        merge([Path(p) for p in args.inputs], pdf_out[0], ps_out[0])
    except Exception:
        for path in outputs:
            path.unlink(missing_ok=True)
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
