---
name: go-fix
description: 'Fix selected findings from agent-view/review.md, record dispositions in agent-view/review.md, dev-view/review.html, and agent-view/checklist.md, and update agent-view/CHANGELOG.md. Use for "fix review findings 1 and 3".'
---

# Fix

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.

Apply the project's [test retry limit](../go-setup/references/public-docs.md#jdi-configmd), including delegated work. If test configuration lacks a valid limit, run `go-setup` to confirm it before retrying.

1. Read `~/.just-do-it/{project}/{branch}/agent-view/review.md` (or a user-supplied review) and the user's selected findings/dispositions. Ask when ambiguous.
2. Read `agent-view/plan.md` and `agent-view/checklist.md` if present, project rules per [project-references.md](references/project-references.md) (including `public/glossary.md` and `public/adr/` when present), and the checkout. Compare repository, branch, reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
3. Identify selected findings by their current `TODO` numbers. Record each disposition: accepted, deferred, disputed, ignored. Already fixed or unsupported: explain with evidence.
4. Fix each accepted finding: production code per `go-work`, unit specs per `go-ut` (updating `agent-view/ut.md`).
   - Authorized unit runs: `go-ut` (writes `agent-view/ut.md`).
   - E2E findings and E2E runs: run or hand to `go-e2e` (writes `agent-view/e2e.md`) or return as `Open` when E2E runs are not authorized.
   - Commit when authorized by an approved plan's per-step/fix delivery or when the user approves the work and an exact commit message; update `agent-view/CHANGELOG.md` on every commit or amend. Otherwise leave changes uncommitted.
5. Recheck the selected findings against the resulting code and affected checks. Update `agent-view/review.md`, `dev-view/review.html` when present, and `agent-view/checklist.md` per [dispositions.md](references/dispositions.md). Apply the [review template](../go-setup/references/html-render.md#plan-and-review-templates) to the HTML.

Done when each selected finding has an evidenced outcome and the relevant reports are updated. Report closed findings by title, open findings by number, and any validation limits. In the flow, the coordinator requests the full delivery review once the focused fixes are settled.
