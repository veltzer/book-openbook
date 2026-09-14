#!/usr/bin/env python

""" Embed the book's table of contents as PDF bookmarks (outlines).

forScore (https://forscore.co/) reads a PDF's embedded Table of Contents
natively: users can tap a title to jump to its page and can import the whole
TOC as a set of bookmarks, with each piece's end page inferred as the page
before the next item starts. See book-openbook issue #121 and
https://forscore.co/developers-pdf-metadata/ ("Table of Contents" section).

That makes the separate forScore ``index.csv`` (scripts.gen_index_csv)
unnecessary: embedding the outlines directly in the PDF gives every PDF
reader the same navigation, not just forScore.

Why a post-processing script instead of having LilyPond do it natively:
LilyPond >= 2.24 does generate PDF bookmarks by itself from
``\\markuplist \\table-of-contents`` (which this book already uses) -- but
upstream issue lilypond/lilypond#6355 ("PDF bookmarks don't work with
bookparts", open since May 2022) means no bookmarks are emitted as soon as
the file uses ``\\bookpart``, which OpenBook does for every tune. That is
why the published PDF, built with LilyPond 2.24.4, contains zero outlines.
If upstream ever fixes #6355 this script becomes redundant and can be
dropped; until then post-processing is the only way to get bookmarks.

The tune list is parsed from the book's own rendered table of contents with
the same code that builds the CSV, so the two can never disagree. The book's
printed page numbers match physical PDF pages 1:1, so a tune's start page
maps directly to a 0-based page index.

Wired into rsconstruct as the step that publishes the book to the website:
it reads the engraved PDF and writes the bookmarked copy into docs/output,
so the generator that copies the other books there skips this one.

Usage:
    python -m scripts.embed_pdf_bookmarks --inputs <book.pdf> --output-files <out.pdf>
"""

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from scripts import gen_index_csv


def embed_bookmarks(pdf: Path, out: Path, book_name: str) -> int:
    """ Copy *pdf* to *out*, adding one outline entry per tune. Returns the
    tune count. """
    entries = gen_index_csv.parse_toc(pdf)
    if not entries:
        raise ValueError(f"parsed no tunes from the TOC of {pdf}")
    reader = PdfReader(str(pdf))
    if reader.outline:
        print(
            f"warning: {pdf} already has {len(reader.outline)} outline entries; "
            "they will be replaced",
            file=sys.stderr,
        )
    writer = PdfWriter()
    writer.append(reader)
    for title, _composer, start in entries:
        # parse_toc reports 1-based pages aligned with physical PDF pages.
        writer.add_outline_item(title, start - 1)
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    metadata.setdefault("/Title", book_name)
    writer.add_metadata(metadata)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "wb") as stream:
        writer.write(stream)
    return len(entries)


def main() -> None:
    """ main entry point """
    parser = argparse.ArgumentParser(
        description="Embed the book TOC as PDF bookmarks (forScore-native navigation)"
    )
    parser.add_argument("--inputs", nargs="+", required=True, help="the built book PDF")
    parser.add_argument(
        "--output-files",
        nargs="+",
        required=True,
        dest="output_files",
        help="the PDF to write with embedded bookmarks",
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

    count = embed_bookmarks(pdf, out, book_name)
    print(f"embedded {count} bookmarks in {out}")


if __name__ == "__main__":
    main()
