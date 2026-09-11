"""
Tests for scripts.embed_pdf_bookmarks, the build step that writes the book's
table of contents directly into the PDF as outline entries (issue #121).

We pin the wiring, not pypdf itself: one outline item per parsed tune, each
pointing at the tune's start page (0-based), and the document Title set to
the book name. The tune list comes from scripts.gen_index_csv, which is
covered by its own tests.
"""

from pathlib import Path

from pypdf import PdfReader, PdfWriter

from scripts import embed_pdf_bookmarks, gen_index_csv


def _blank_pdf(path: Path, pages: int) -> None:
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(612, 792)
    with open(path, "wb") as stream:
        writer.write(stream)


def test_embed_bookmarks_writes_one_outline_per_tune(tmp_path, monkeypatch):
    entries = [
        ("First", "Composer A", 2),
        ("Second", "Composer B", 4),
        ("Third", "Composer C", 5),
    ]
    monkeypatch.setattr(gen_index_csv, "parse_toc", lambda _pdf: entries)
    monkeypatch.setattr(gen_index_csv, "pdf_page_count", lambda _pdf: 6)

    src = tmp_path / "book.pdf"
    _blank_pdf(src, 6)
    out = tmp_path / "book-out.pdf"

    count = embed_pdf_bookmarks.embed_bookmarks(src, out, "OpenBook")
    assert count == 3

    reader = PdfReader(str(out))
    outline = reader.outline
    assert [item.title for item in outline] == ["First", "Second", "Third"]
    ref_to_index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    assert [ref_to_index[item["/Page"].indirect_reference.idnum] for item in outline] == [1, 3, 4]
    assert reader.metadata["/Title"] == "OpenBook"
    assert len(reader.pages) == 6
