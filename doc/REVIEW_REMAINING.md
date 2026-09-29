# Review — Remaining Work

Follow-ups from the September 2026 code-review pass. Items done in that pass
were moved to `DONE.txt`; this file tracks what is still open.

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
- **CI cache for `out/` keyed by song hashes.** The `.rsconstruct` cache
  is fine but a full cold build engraves 200+ tunes. A song-hash-keyed
  cache would turn CI from cold-slow to warm-fast.

