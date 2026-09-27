# Review — Remaining Work

Follow-ups from the September 2026 code-review pass. Items done in that pass
were moved to `DONE.txt`; this file tracks what is still open.

## Genuine work remaining (repo-local)

### Deduplicate front-matter parsing

`scripts/derive_metadata.py` and `scripts/drivers.py:cmd_songs` both call
`parse_song_meta` on the same `src/**/*.ly.tera` on every build. The
derived `.ly.toml` already contains everything a driver needs, so the
second parse can be dropped: teach `cmd_songs` to load the derived TOML
directly and construct a `SongMeta` from it.

**Cost:** small refactor. Changes `SongMeta`'s construction path and one
call site.
**Value:** halves the front-matter parse work per song per build.
**Care:** the driver ordering (`derive_metadata` before `song_drivers`)
is already enforced by rsconstruct's output-path matching, so the input
change is safe.

### Preexisting engraving bug in `src/musicals/memory.ly`

Surfaces on `rsconstruct build --iset generator.songs_pdf.enabled=true`:

    out/tera/src/musicals/memory.ly:494:2: error: Unfinished main input

Not related to any recent change. The book build (default `rsconstruct
build`) does not compile per-song, so this only fires when someone
enables per-song engraving. Needs a musician's eye on the source.

## Blocked here (needs fleet-template edits, not this repo)

The following live in files that `rsmultigit check-same` treats as
byte-identical across the fleet; editing them here would diverge from
every other repo. Do them in the shared template / rsmultigit config,
not here.

- **Add `pull_request` trigger to `.github/workflows/build.yml`.**
  External contributors' PRs currently do not build.
- **Reconsider the `ubuntu-26.04` runner.** Only just GA; `ubuntu-latest`
  or `ubuntu-24.04` may be safer for the fleet.
- **Narrow `cancel-in-progress`.** On `push` to master with Pages
  deploy, cancelling an in-flight run can race the deploy. Consider
  `cancel-in-progress: ${{ github.ref != 'refs/heads/master' }}`.
- **Swap the black badge for a ruff badge in
  `tera.templates/README.md.tera`.** Nothing in the repo uses black —
  ruff is the formatter and linter.
- **CI cache for `out/` keyed by song hashes.** The `.rsconstruct` cache
  is fine but a full cold build engraves 200+ tunes. A song-hash-keyed
  cache would turn CI from cold-slow to warm-fast.

## Nice-to-have polish

- **Move `scripts/serve_pages.py` under a `dev-scripts/` directory.**
  It is never invoked by the build. Cosmetic; would need a matching
  `rsconstruct.toml` src_dirs entry so it stays linted. Not worth doing
  on its own.

## Bigger, deliberate changes (not yet committed to)

- **CREDITS from `git shortlog` at build time.** The current `CREDITS`
  file is a manual snapshot of `git shortlog -sn`; it will drift.
  Generating it via a rsconstruct product (a small python wrapper
  around `git shortlog`) removes the drift and picks up new
  contributors automatically. Depends on the build tolerating a `git`
  invocation, which the existing `SHELL_VARS` block already relies on.
