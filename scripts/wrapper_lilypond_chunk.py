#!/usr/bin/env python

"""
Engrave one piece of a chunked book (see scripts/drivers_chunked.py).

Invoked per the rsconstruct explicit-processor contract:

    python -m scripts.wrapper_lilypond_chunk \\
        --inputs <piece>.ly [<previous piece>.next] [files the piece reads...] \\
        --output-files <piece>.pdf <piece>.next [<piece>.labels]

Inputs: exactly one .ly to engrave. An optional .next file (written by
this wrapper for the previous piece) holds the page number this piece
starts on; without one it starts on page 1. Other inputs (the logo the
front matter embeds, this script) are listed only so rsconstruct rebuilds
when they change.

Outputs, all sharing one basename:
    .pdf     the engraved piece
    .next    the page number the following piece starts on
    .labels  the start page of every tune (written by lilypond via
             src/include/chunked.ly.tera); declared for tune chunks only
             and discarded otherwise

Like scripts/wrapper_lilypond_explicit.py: lilypond's console noise is
shown only on failure, and no partial outputs are left behind.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


def remove_if_exist(paths: list[Path]) -> None:
    """ best-effort removal of output files """
    for path in paths:
        path.unlink(missing_ok=True)


def one(paths: list[Path], suffix: str, *, required: bool) -> Path | None:
    """ the single path with the given suffix (None if optional and absent) """
    found = [p for p in paths if p.suffix == suffix]
    if len(found) > 1 or (required and not found):
        raise ValueError(f"expected {'exactly' if required else 'at most'} one {suffix} file, got {paths}")
    return found[0] if found else None


def main() -> int:
    """ main entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--output-files", nargs="+", required=True, dest="output_files")
    args = parser.parse_args()
    inputs = [Path(p) for p in args.inputs]
    outputs = [Path(p) for p in args.output_files]
    source = one(inputs, ".ly", required=True)
    previous = one(inputs, ".next", required=False)
    pdf = one(outputs, ".pdf", required=True)
    next_file = one(outputs, ".next", required=True)
    labels = one(outputs, ".labels", required=False)
    assert source is not None
    assert pdf is not None
    assert next_file is not None
    stems = {p.parent / p.stem for p in outputs}
    if len(stems) != 1:
        raise ValueError(f"outputs must share one basename, got {args.output_files}")
    base = stems.pop()
    # lilypond writes the labels report for every piece; drop it if undeclared
    report = base.with_suffix(".labels")

    first_page = int(previous.read_text(encoding="utf-8")) if previous else 1
    remove_if_exist([*outputs, report])
    command = ["lilypond", "--pdf", "-o", str(base), str(source)]
    env = {**os.environ, "CHUNK_FIRST_PAGE": str(first_page)}
    result = subprocess.run(command, capture_output=True, text=True, check=False, env=env)
    expected = [pdf] + ([labels] if labels else [])
    missing = [p for p in expected if not p.is_file()]
    if result.returncode != 0 or missing:
        remove_if_exist([*outputs, report])
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        print(f"{sys.argv[0]}: [{' '.join(command)}] failed "
              f"(rc={result.returncode}, missing={missing})", file=sys.stderr)
        return 1
    if labels is None:
        report.unlink(missing_ok=True)
    pages = len(PdfReader(str(pdf)).pages)
    next_file.write_text(f"{first_page + pages}\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
