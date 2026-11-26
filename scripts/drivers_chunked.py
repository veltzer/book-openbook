#!/usr/bin/env python

"""
Generate the driver templates of a book engraved in chunks.

Why: lilypond holds every score of a book in memory until it has broken
the whole book into pages (about 10MB per tune), so the openbook, with
1600+ tunes, peaked at 16GB in a single lilypond run and was OOM-killed.
The chunked build engraves the same book as several lilypond runs, each
small enough to fit comfortably in memory, and merges the PDFs:

    front_probe   title page + table of contents with placeholder page
                  numbers; engraved only to learn how many pages the
                  front matter takes (the count depends on the number of
                  entries, not on the numbers in them)
    c00 .. cNN    consecutive runs of tunes, in book order. Each chunk is
                  engraved with its first page number following the
                  previous chunk's last page, and reports the page every
                  tune starts on (src/include/chunked.ly.tera)
    front         the real front matter: the table of contents filled in
                  from the chunks' reports

scripts/wrapper_lilypond_chunk.py engraves each of these and
scripts/merge_chunks.py joins the PDFs into the book. The per-tune
material comes from the same weave master (src/include/common.ly.weave)
and the same partial evaluator (scripts/drivers.py's DriverEmitter) as
the single-run book driver, so a chunk engraves its tunes exactly as the
whole book would. scripts/drivers.py itself is untouched: it still makes
the per-song drivers, the small books' drivers, and the openbook's
one-file .ly that the website publishes as a source download.

A chunk driver depends on its own tunes only, with no build date or git
data in it, so editing one tune re-engraves one chunk; the later chunks
re-engrave only if that changes where they start.

Contracts (rsconstruct explicit processors):

    python -m scripts.drivers_chunked drivers \\
        --inputs <weave+scripts+derived tomls...> \\
        --output-files <dir>/front_probe.ly.tera <dir>/c00.ly.tera ...
        The chunk count is the number of cNN outputs; the book is named
        by the output directory.

    python -m scripts.drivers_chunked front \\
        --inputs <weave+scripts+derived tomls+chunk .labels files...> \\
        --output-files <dir>/front.ly.tera
"""

import argparse
import re
import sys
from pathlib import Path

from scripts.drivers import (
    BOOK_VARS,
    COMMON,
    COMMON_TERA,
    GATTR_BOOK,
    SHELL_VARS,
    SRC,
    DriverEmitter,
    SongMeta,
    compute_scratch,
    driver_header,
    song_meta_from_derived,
    toml_to_song,
)

CHUNKED_TERA = SRC / "include/chunked.ly.tera"

# the only shell value a chunk needs (common.ly.tera's \version line); the
# rest (date, git data) appear on the title page only
CHUNK_VARS = ["lilypond_version"]

# the page number the probe's table of contents shows for every tune
PROBE_PAGE = "999"

# Pieces of the weave the chunk drivers cut or replace. Matched verbatim:
# if the weave changes shape, generation fails loudly instead of quietly
# producing a book that differs from the single-run one.
WEAVE_TITLE_START = "% if gattr['book']:\n%% book header\n"
WEAVE_TITLE_END = "% endif\n\n% if gattr['toc']:\n"
WEAVE_TOC_LINE = "\\markuplist \\table-of-contents\n"
WEAVE_TOC_BLOCK = (
    "% if gattr['toc']:\n"
    + WEAVE_TOC_LINE
    + "% if gattr['break_after_toc']:\n\\pageBreak\n% endif\n% endif\n"
)
TOC_MARKER = "@@CHUNKED-TABLE-OF-CONTENTS@@\n"
COMMON_INCLUDE = '{% include "' + COMMON_TERA.as_posix() + '" %}\n'
CHUNKED_INCLUDE = '{% include "' + CHUNKED_TERA.as_posix() + '" %}\n'
# tunes are bookparts and every bookpart starts a page, so number a
# chunk's first page like any other
CHUNK_PAPER = "\\paper { print-first-page-number = ##t }\n"

RE_CHUNK_NAME = re.compile(r"^c(\d+)$")
RE_TERA_VAR = re.compile(r"\{\{ (\w+) \}\}")
RE_LABEL_LINE = re.compile(r"^tune(\d+) (\d+)$")


class ChunkEmitter(DriverEmitter):
    """ a DriverEmitter that can leave out the per-song loop while still
    knowing the song list (the title page prints the tune count) """

    def __init__(self, gattr: dict, songs: list[SongMeta], *, with_songs: bool):
        super().__init__(gattr, songs)
        self.with_songs = with_songs

    def unroll_loop(self, rest: list[str]) -> int:
        if self.with_songs:
            return super().unroll_loop(rest)
        songs = self.songs
        self.songs = []
        try:
            return super().unroll_loop(rest)
        finally:
            self.songs = songs


def replace_once(text: str, old: str, new: str) -> str:
    """ replace exactly one occurrence of old, or fail """
    count = text.count(old)
    if count != 1:
        raise ValueError(f"expected exactly one {old!r} in the weave/driver, found {count}")
    return text.replace(old, new)


def chunk_weave(weave: str) -> str:
    """ the weave without the title page and the table of contents """
    start = weave.find(WEAVE_TITLE_START)
    end = weave.find(WEAVE_TITLE_END, start)
    if start < 0 or end < 0 or weave.count(WEAVE_TITLE_START) != 1:
        raise ValueError("cannot find the title page block in the weave")
    weave = weave[:start] + weave[end + len("% endif\n"):]
    return replace_once(weave, WEAVE_TOC_BLOCK, "")


def front_weave(weave: str) -> str:
    """ the weave with the table of contents replaced by a marker """
    return replace_once(weave, WEAVE_TOC_LINE, TOC_MARKER)


def sorted_songs(inputs: list[str]) -> list[SongMeta]:
    """ the book's songs in canonical book order (as scripts.drivers book) """
    tomls = [Path(p) for p in inputs if p.endswith(".ly.toml")]
    tomls.sort(key=lambda p: "src/" + str(toml_to_song(p).relative_to(SRC)))
    return [song_meta_from_derived(p) for p in tomls]


def split_chunks[T](songs: list[T], count: int) -> list[list[T]]:
    """ cut the book into count consecutive runs of near-equal length """
    if count < 1 or len(songs) < count:
        raise ValueError(f"cannot split {len(songs)} songs into {count} chunks")
    base, extra = divmod(len(songs), count)
    chunks = []
    start = 0
    for index in range(count):
        end = start + base + (1 if index < extra else 0)
        chunks.append(songs[start:end])
        start = end
    return chunks


def check_vars(body: str, var_names: list[str]) -> None:
    """ every shell value the driver uses must be set by its header """
    used = {name for name in RE_TERA_VAR.findall(body) if name in SHELL_VARS}
    missing = used - set(var_names)
    if missing:
        raise ValueError(f"driver uses {sorted(missing)} but its header does not set them")


def write(driver: Path, var_names: list[str], body: str) -> None:
    """ write one driver template """
    check_vars(body, var_names)
    driver.parent.mkdir(parents=True, exist_ok=True)
    driver.write_text(driver_header(var_names) + body, encoding="utf-8")


def chunk_driver(songs: list[SongMeta]) -> str:
    """ the driver body of one chunk of tunes """
    emitter = ChunkEmitter(GATTR_BOOK, songs, with_songs=True)
    body = emitter.run(chunk_weave(COMMON.read_text(encoding="utf-8")))
    return replace_once(body, COMMON_INCLUDE, COMMON_INCLUDE + CHUNKED_INCLUDE + CHUNK_PAPER)


def scheme_string(text: str) -> str:
    """ a scheme string literal holding a tocname.

    The tocname is written as-is: the single-run driver splices it raw
    into a lilypond string ("..."), so the song sources already escape
    it for that (a title quote is written \\"), and scheme strings take
    the same escapes. Escaping again would print the backslashes.
    """
    return '"' + text + '"'


def front_driver(songs: list[SongMeta], pages: list[str]) -> str:
    """ the driver body of the front matter, its TOC showing pages """
    emitter = ChunkEmitter(GATTR_BOOK, songs, with_songs=False)
    body = emitter.run(front_weave(COMMON.read_text(encoding="utf-8")))
    body = replace_once(body, COMMON_INCLUDE, COMMON_INCLUDE + CHUNKED_INCLUDE)
    entries = "".join(
        f"\n\t({scheme_string(compute_scratch(song.attrs)['tocname'])} {scheme_string(page)})"
        for song, page in zip(songs, pages, strict=True)
    )
    # raw: tune titles are data, tera must not read them as template syntax
    toc = (
        "{% raw %}\\markuplist \\static-table-of-contents #'("
        + entries
        + "\n){% endraw %}\n"
    )
    return replace_once(body, TOC_MARKER, toc)


def read_labels(labels: Path, tunes: int) -> list[str]:
    """ the start pages of a chunk's tunes, from its .labels report """
    pages: dict[int, str] = {}
    for line in labels.read_text(encoding="utf-8").splitlines():
        match = RE_LABEL_LINE.match(line)
        if match is None:
            raise ValueError(f"{labels}: unexpected line {line!r}")
        pages[int(match.group(1))] = match.group(2)
    if sorted(pages) != list(range(1, tunes + 1)):
        raise ValueError(f"{labels}: expected pages for tunes 1..{tunes}, got {sorted(pages)}")
    return [pages[index] for index in range(1, tunes + 1)]


def parse_contract(args: list[str]) -> argparse.Namespace:
    """ the rsconstruct explicit-processor contract """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--output-files", nargs="+", required=True, dest="output_files")
    return parser.parse_args(args)


def cmd_drivers(args: list[str]) -> int:
    """ write the probe front matter and the chunk drivers """
    parsed = parse_contract(args)
    outputs = [Path(p) for p in parsed.output_files]
    probe = [p for p in outputs if p.name == "front_probe.ly.tera"]
    chunks = sorted(
        (p for p in outputs if RE_CHUNK_NAME.match(p.name.removesuffix(".ly.tera"))),
        key=lambda p: p.name,
    )
    if len(probe) != 1 or len(probe) + len(chunks) != len(outputs):
        raise ValueError(f"expected front_probe.ly.tera and cNN.ly.tera outputs, got {outputs}")
    songs = sorted_songs(parsed.inputs)
    for driver, chunk in zip(chunks, split_chunks(songs, len(chunks)), strict=True):
        write(driver, CHUNK_VARS, chunk_driver(chunk))
    write(probe[0], BOOK_VARS, front_driver(songs, [PROBE_PAGE] * len(songs)))
    return 0


def cmd_front(args: list[str]) -> int:
    """ write the front matter, its TOC filled in from the chunk reports """
    parsed = parse_contract(args)
    if len(parsed.output_files) != 1:
        raise ValueError(f"expected exactly one driver output, got {parsed.output_files}")
    labels = sorted((Path(p) for p in parsed.inputs if p.endswith(".labels")), key=lambda p: p.name)
    songs = sorted_songs(parsed.inputs)
    pages: list[str] = []
    for report, chunk in zip(labels, split_chunks(songs, len(labels)), strict=True):
        pages.extend(read_labels(report, len(chunk)))
    write(Path(parsed.output_files[0]), BOOK_VARS, front_driver(songs, pages))
    return 0


def main() -> int:
    """ main entry point """
    commands = {
        "drivers": ("write the probe front matter and the chunk drivers", cmd_drivers),
        "front": ("write the front matter from the chunks' page reports", cmd_front),
    }
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print(f"usage: {sys.argv[0]} <command> --inputs ... --output-files ...\n", file=sys.stderr)
        print("commands:", file=sys.stderr)
        for name, (description, _) in commands.items():
            print(f"  {name:8} {description}", file=sys.stderr)
        return 1
    return commands[sys.argv[1]][1](sys.argv[2:])


if __name__ == "__main__":
    sys.exit(main())
