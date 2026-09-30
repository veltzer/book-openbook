#!/usr/bin/env python

"""
Download and unpack the scanned real-books reference archive. Replaces the
old `make real_books_archive.gi` target. The archive is extracted at the
repository root (creating real_books_archive.gi/, which is gitignored via
the /*.gi pattern).

Invoked per the rsconstruct explicit-processor contract:

    python -m scripts.download_real_books \
        --inputs scripts/download_real_books.py \
        --output-files out/real_books/real_books.stamp

Every argument has a default matching the rsconstruct.toml entry, so it can
also be run bare:

    python -m scripts.download_real_books
"""

import argparse
import io
import sys
import tarfile
from pathlib import Path

import requests

URL = "https://www.dropbox.com/s/birwhwe6g7ojqnh/real_books_archive.gi.tar.gz?dl=1"
DEFAULT_INPUTS = ["scripts/download_real_books.py"]
DEFAULT_OUTPUT_FILES = ["out/real_books/real_books.stamp"]


def main() -> int:
    """ main entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inputs",
        nargs="+",
        default=DEFAULT_INPUTS,
        help="dependency inputs (unused, accepted for the rsconstruct contract)",
    )
    parser.add_argument(
        "--output-files",
        nargs="+",
        default=DEFAULT_OUTPUT_FILES,
        dest="output_files",
        help="stamp files to touch after extraction",
    )
    parser.add_argument("--url", default=URL, help="archive URL to download")
    args = parser.parse_args()
    response = requests.get(args.url, timeout=600)
    response.raise_for_status()
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as archive:
        archive.extractall(filter="data")
    for output in args.output_files:
        stamp = Path(output)
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text("", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
