---
name: go-fix
description: 'Fix selected findings from a supplied code review, and return numbered dispositions. Use for "fix review findings 1 and 3".'
---

# Fix

Report as the caller specifies. Write no `review.md` or checklist; the caller records results.

1. Take the review and the user's dispositions from the caller (text or path). Ask when ambiguous.
2. Read the plan and checklist if supplied, project rules per [project-references.md](references/project-references.md), and the checkout. Compare repository, branch, reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
3. Keep finding IDs. Record each disposition: accepted, deferred, disputed, ignored. Already fixed or unsupported: explain with evidence.
4. Fix each accepted finding: production code per `go-work`, unit specs per `go-ut`.
   - e2e findings: return as `Open` for `go-e2e` (finding ID, scope, files, test authorization, commit rules).
   - Authorized unit runs: `go-ut`; e2e runs: `Open` for `go-e2e`.
   - Leave changes uncommitted unless the user approves the work and an exact commit message.
5. Check the diff against the selected findings. Reply per [dispositions.md](references/dispositions.md).

Done when each selected finding has an evidenced outcome. Report resolved and open IDs and validation limits. Re-review: `go-review`. Reply to an external review only when asked.
