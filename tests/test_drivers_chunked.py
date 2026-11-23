"""
Tests for the chunked book driver generator (scripts/drivers_chunked.py).

The key property: cutting a book into chunk drivers must not change the
tune material, so the chunks' tune sections, concatenated, equal the
single-run book driver's.
"""

from pathlib import Path

import pytest

from scripts.drivers import GATTR_BOOK, DriverEmitter, parse_song_meta
from scripts.drivers_chunked import (
    CHUNKED_INCLUDE,
    TOC_MARKER,
    chunk_driver,
    chunk_weave,
    front_driver,
    front_weave,
    read_labels,
    scheme_string,
    split_chunks,
)

DEMO_SONG = Path("src/test/demo.ly.tera")
WEAVE = Path("src/include/common.ly.weave")
LOOP_START = "{% set meta = load_toml"
LOOP_END = "% book footer"


def tune_blocks(driver: str) -> list[str]:
    """ the per-song blocks of a driver (trailing blank lines stripped:
    they differ only at chunk boundaries) """
    section = driver[driver.index(LOOP_START):driver.rindex(LOOP_END)]
    return [block.rstrip("\n") for block in section.split(LOOP_START)[1:]]


def test_split_chunks_is_contiguous_and_balanced():
    """ chunks keep book order and differ in length by at most one """
    items = list(range(10))
    chunks = split_chunks(items, 3)
    assert chunks == [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_split_chunks_rejects_too_many_chunks():
    """ every chunk must hold at least one song """
    with pytest.raises(ValueError, match="cannot split 2 songs into 3"):
        split_chunks([1, 2], 3)


def test_chunk_weave_drops_title_page_and_toc():
    """ the chunk weave keeps the tunes but not the front matter """
    weave = chunk_weave(WEAVE.read_text(encoding="utf-8"))
    assert "book header" not in weave
    assert "table-of-contents" not in weave
    assert "% for file in gattr['files']:" in weave


def test_front_weave_marks_the_toc():
    """ the front weave has a marker where the TOC goes """
    weave = front_weave(WEAVE.read_text(encoding="utf-8"))
    assert TOC_MARKER in weave
    assert "table-of-contents" not in weave


def test_chunks_concatenate_to_the_whole_book():
    """ the chunks' tune sections are exactly the single-run book's """
    songs = [parse_song_meta(DEMO_SONG)] * 3
    whole = DriverEmitter(GATTR_BOOK, songs).run(WEAVE.read_text(encoding="utf-8"))
    parts = [chunk_driver(chunk) for chunk in split_chunks(songs, 2)]
    assert all(CHUNKED_INCLUDE in part for part in parts)
    assert all("book header" not in part for part in parts)
    joined = [block for part in parts for block in tune_blocks(part)]
    assert len(joined) == 3
    assert joined == tune_blocks(whole)


def test_front_driver_lists_every_tune_with_its_page():
    """ the front matter has the title page and a static TOC """
    songs = [parse_song_meta(DEMO_SONG)] * 2
    front = front_driver(songs, ["3", "5"])
    assert "book header" in front
    assert "Number of tunes: 2" in front
    assert "{% raw %}\\markuplist \\static-table-of-contents" in front
    assert front.count('" "3")') == 1
    assert front.count('" "5")') == 1
    assert "{% set meta" not in front


def test_scheme_string_keeps_lilypond_escapes():
    """ a tocname is already escaped for a lilypond string, which is
    also a valid scheme string: it goes in unchanged """
    assert scheme_string('The \\"Medic\\" Theme') == '"The \\"Medic\\" Theme"'


def test_read_labels(tmp_path):
    """ the labels report maps tune indexes to start pages """
    report = tmp_path / "c00.labels"
    report.write_text("tune2 7\ntune1 5\n", encoding="utf-8")
    assert read_labels(report, 2) == ["5", "7"]
    with pytest.raises(ValueError, match=r"expected pages for tunes 1\.\.3"):
        read_labels(report, 3)
