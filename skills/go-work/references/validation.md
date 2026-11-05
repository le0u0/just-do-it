# Final Validation

1. Compare delivered behavior and the full task diff, untracked files included, with the plan.
2. Run every spec file of the change through `go-ut`. Report each command, outcome, and missing evidence; keep environment failures apart from implementation failures.
3. Report `Open: run e2e` when the plan's `E2E` line is not `none`, else `Open: ready for review`. Include the initial baseline and the plan's test authorization. The caller assigns `go-e2e`, then `go-review`.
4. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, not passes.
5. Report discovered work as `Open`; ask before expanding scope.
6. A required check still failing: keep working per [step-execution.md](step-execution.md); ask only at its stop conditions.

Finish with delivered behavior, validation limits, and uncommitted files or commit SHAs.
