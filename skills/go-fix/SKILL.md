---
name: go-fix
description: 'Fix selected findings from a supplied code review, and return numbered dispositions. Use for "fix review findings 1 and 3".'
---

# Fix

- Report as the caller specifies.
- Write no `review.md` or checklist; the caller records your results.

## Steps

1. Take the review report and the user's dispositions from the caller, as text or named path. Ask when ambiguous.
2. Read:
   - the plan and checklist, when supplied
   - the project's rules per [project-references.md](references/project-references.md)
   - the checkout
3. Compare repository, branch, reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
4. Keep finding IDs. Record each disposition: accepted, deferred, disputed, or ignored. Already fixed or unsupported: explain with evidence.
5. Fix each accepted finding yourself.
   - Production code: per `go-work`. Unit specs: per `go-ut`.
   - e2e spec findings: return as `Open` for `go-e2e`, with finding ID, scope, files, test authorization, commit rules.
   - Authorized unit runs: `go-ut`. Authorized e2e runs: return as `Open` for `go-e2e`.
   - Leave changes uncommitted unless the user approves the work and an exact commit message.
6. Check the diff against the selected findings. Reply per [dispositions.md](references/dispositions.md).

## Done

- Each selected finding has an evidenced outcome.
- Report resolved and open IDs and validation limits.
- Re-review: use `go-review`.
- Reply to an external review only when asked.
