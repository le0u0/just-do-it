---
name: go-fix
description: 'Fix selected findings from a supplied code review, and return numbered dispositions. Use for "fix review findings 1 and 3".'
---

# Fix

Report as the caller specifies. Write no `review.md` or checklist; the caller records your results.

1. Take the review report and the user's dispositions from the caller, as text or a named path. Ask when ambiguous.
2. Read the plan and checklist when the caller supplied them, the project's own rules per [project-references.md](references/project-references.md), and the checkout. Compare repository, branch, and reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
3. Keep finding IDs. Record each disposition: accepted, deferred, disputed, or ignored. When a finding is already fixed or unsupported, explain with evidence.
4. Fix each accepted finding yourself: production code and unit specs, per `go-work` for production code and `go-ut` for unit specs. Return e2e spec findings as `Open`, for `go-e2e` to fix, with the finding ID, scope, files, test authorization, and commit rules. Run authorized unit specs with `go-ut`, and return authorized e2e runs as `Open`, for `go-e2e`. Leave changes uncommitted unless the user approves the work and an exact commit message.
5. Check the diff against the selected findings. Reply with the result per [dispositions.md](references/dispositions.md).

Finish when each selected finding has an evidenced outcome. Report resolved and open IDs and validation limits. Use `go-review` for a re-review. Reply to an external review only when asked.
