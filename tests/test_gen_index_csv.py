"""
Tests for scripts.gen_index_csv, the forScore index.csv generator (issue #121).

The PDF-reading helpers shell out to pdfinfo/pdftotext, so they are exercised
by the real build; here we pin the pure logic: splitting a TOC line's body
into title and composer, and turning parsed TOC entries into rows with correct
start/end pages (including the single-page and last-tune cases).
"""

from pathlib import Path

from scripts import gen_index_csv


def test_split_title_composer_basic():
    assert gen_index_csv.split_title_composer("A Foggy Day / George Gershwin, Ira Gershwin") == (
        "A Foggy Day",
        "George Gershwin, Ira Gershwin",
    )


def test_split_title_composer_no_composer():
    assert gen_index_csv.split_title_composer("Always") == ("Always", "")


def test_build_rows_pages(monkeypatch):
    # Three tunes: the first spans two pages (next starts on 7), the second is
    # one page, the last runs to the end of a 10-page book.
    entries = [
        ("First", "Composer A", 5),
        ("Second", "Composer B", 7),
        ("Third", "Composer C", 8),
    ]
    monkeypatch.setattr(gen_index_csv, "parse_toc", lambda _pdf: entries)
    monkeypatch.setattr(gen_index_csv, "pdf_page_count", lambda _pdf: 10)

    rows = gen_index_csv.build_rows(Path("dummy.pdf"), "OpenBook")
    assert [(r["Title"], r["Start Page"], r["End Page"]) for r in rows] == [
        ("First", 5, 6),
        ("Second", 7, 7),
        ("Third", 8, 10),
    ]
    assert all(r["Book Name"] == "OpenBook" for r in rows)


def test_build_rows_single_page_when_successor_shares_page(monkeypatch):
    # Two tunes engraved onto the same page: end must not fall below start.
    entries = [("First", "A", 5), ("Second", "B", 5)]
    monkeypatch.setattr(gen_index_csv, "parse_toc", lambda _pdf: entries)
    monkeypatch.setattr(gen_index_csv, "pdf_page_count", lambda _pdf: 5)

    rows = gen_index_csv.build_rows(Path("dummy.pdf"), "OpenBook")
    assert rows[0]["Start Page"] == 5
    assert rows[0]["End Page"] == 5
