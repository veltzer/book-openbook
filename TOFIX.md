# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `doc/coding_style.txt:13` - the contributor docs still describe the retired Mako/Make setup: "Currently we are using pythons Mako", song files named `*.mako` (lines 31-36; songs are `src/<book>/<song>.ly.tera` now), and "`make check_all` ... is currently not part of the build" (line 21; `[processor.explicit.check_all]` runs in the default build). The same stale Mako/`.mako` guidance is in `doc/design.txt:35`, `doc/osx.txt:1` ("install the python mako templating system"), `doc/vim.txt:1` and `doc/moving_to_new_lilypond_version.txt:1` (`find . -name "*.mako"` matches nothing under `src/`). Update them to tera / `.ly.tera` / rsconstruct.
- `doc/version_of_lilypond_in_this_project.txt:3` - says the project sticks to the LilyPond 2.14 feature set on Ubuntu 11.04-12.04; the build stamps whatever `lilypond --version` reports (`scripts/drivers.py:102`, currently 2.24.x). Rewrite with the real minimum version (or delete).
- `scripts/build_on_docker.sh:1` - no `set -e` (or `-euo pipefail`), so a failed `apt-get`, `curl`, `rsconstruct tools install-deps` or `uv sync` is ignored and the script carries on to a confusing later failure; it also pipes `install.sh` from the network straight into `sh` (line 18). Add `set -euo pipefail`.

## Low

- `rsconstruct.toml:249` - the "opt-in targets (disabled by default)" section says "Each stanza ships with enabled = false", but `check_all`, `demo_smoke` and `tidy` in that section are enabled and part of the default build; move them out or fix the comment. Line 362 still describes `real_books` as "`make real_books_archive.gi`".
- `rsconstruct.toml:31` - `src_dirs` for `ruff` and `mypy` (line 35) include `config`, which holds only `.lua` files, and `shellcheck` (line 44) includes `docs` and `config`, which hold no shell scripts; list only the dirs that hold the file type.
- `pyproject.toml:33` - leftover `[[tool.mypy.overrides]]` with an empty `module = []` list; delete it.
- `doc/python_usage.txt:9` - says the author uses Python 3.5.2, while `pyproject.toml` requires `>=3.14`; update or delete the file.
- `staging/openbook/laurent/Makefile:1` - `staging/` (~190 imported `.ly`/`.mako`/`.txt` files, including this Makefile driving long-gone `ly2dvi` and uploading to a third-party host) is not mentioned anywhere in README or `doc/`; document what staging is for and the conversion process into `src/`, or drop the dead Makefile.
