# Final Validation

Run after the last plan step is done, before e2e and review.

1. Compare delivered behavior and the full task diff, untracked files included, with the plan.
2. Run every spec file of the change through `go-ut`. Note each command, outcome, and missing evidence; keep environment failures apart from implementation failures.
3. Plan's `E2E` line is not `none`: assign `go-e2e` per [tests.md](tests.md). Else send the work to `go-review`. Pass the initial baseline and the plan's test authorization.
4. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, not passes.
5. Record discovered work in `checklist.md`; ask before expanding scope.
6. A required check still failing: send the failure to `go-work` as a new step. Ask the user only when `go-work` reports a stop condition.

Finish with delivered behavior, validation limits, and uncommitted files or commit SHAs.
