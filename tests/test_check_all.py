"""
Tests for scripts.check_all: the cross-file uniqueness check on song uuids.
"""

from pathlib import Path

from scripts import check_all

SONG = '{#\n[attributes]\ntitle = "X"\nuuid = "%s"\n#}\n'


def _check(tmp_path: Path, uuids: list[str]) -> check_all.Checker:
    checker = check_all.Checker()
    for num, uuid in enumerate(uuids):
        path = tmp_path / f"song{num}.ly.tera"
        path.write_text(SONG % uuid, encoding="utf-8")
        checker.check_file(path)
    return checker


def test_unique_uuids_pass(tmp_path):
    assert _check(tmp_path, ["u1", "u2"]).errors == 0


def test_duplicate_uuid_is_reported(tmp_path):
    checker = _check(tmp_path, ["u1", "u2", "u1"])
    assert [f.reason for f in checker.findings] == [
        f"duplicate uuid (also in {tmp_path / 'song0.ly.tera'})",
    ]
