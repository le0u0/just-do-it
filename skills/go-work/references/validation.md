# Final Validation

1. Compare delivered behavior and the full task diff, including untracked files, with the plan.
2. Run every spec file of the change through `go-ut`. Report each command, outcome, and missing evidence in the reply, keeping environment failures apart from implementation failures.
3. Report `Open: run e2e` when the plan's `E2E` line is not `none`, else `Open: ready for review`. Include the initial baseline and the plan's test authorization. The caller assigns `go-e2e` and then `go-review`.
4. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, never passes.
5. Report discovered work as `Open`; ask before expanding scope.
6. When a required check still fails after the fixes, keep working per [step-execution.md](step-execution.md); stop and ask only at its stop conditions.

Finish with delivered behavior, validation limits, and uncommitted files or commit SHAs.
