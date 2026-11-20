---
name: go-fix
description: 'Fix selected findings from dev-view/review.md, record dispositions in dev-view/review.md and agent-view/checklist.md, and update agent-view/CHANGELOG.md. Use for "fix review findings 1 and 3".'
---

# Fix

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.

1. Read `~/.just-do-it/{project}/{branch}/dev-view/review.md` (or a user-supplied review) and the user's selected findings/dispositions. Ask when ambiguous.
2. Read `agent-view/plan.md` and `agent-view/checklist.md` if present, project rules per [project-references.md](references/project-references.md) (including `public/glossary.md` and `public/adr/` when present), and the checkout. Compare repository, branch, reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
3. Keep finding IDs. Record each disposition: accepted, deferred, disputed, ignored. Already fixed or unsupported: explain with evidence.
4. Fix each accepted finding: production code per `go-work`, unit specs per `go-ut` (updating `dev-view/ut.md`).
   - Authorized unit runs: `go-ut` (writes `dev-view/ut.md`).
   - E2E findings and E2E runs: run or hand to `go-e2e` (writes `dev-view/e2e.md`) or return as `Open` when E2E runs are not authorized.
   - Commit when authorized by an approved plan's per-step/fix delivery or when the user approves the work and an exact commit message; update `agent-view/CHANGELOG.md` on every commit or amend. Otherwise leave changes uncommitted.
5. Update `dev-view/review.md` (`RESOLVED`, `TODO`, `IGNORED`, and `Issue Count`) and `agent-view/checklist.md` with the evidenced dispositions per [dispositions.md](references/dispositions.md).

Done when each selected finding has an evidenced outcome and `dev-view/review.md` (plus `agent-view/CHANGELOG.md` on commit and `agent-view/checklist.md` if present) is updated. Report resolved and open IDs and validation limits. Re-review: `go-review`.
