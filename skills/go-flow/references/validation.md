# Final Validation

Run after the last plan step is done, before final review.

1. Compare delivered behavior and the full diff (including untracked files) with `agent-view/plan.md`. Read diffs and untracked files directly.
2. When authorized, verify all changed unit specs through `go-ut` in evidence-only mode. The coordinator writes `agent-view/ut.md` from this final verification. Note each command, outcome, and missing evidence; keep environment failures apart from implementation failures.
3. Hand the work to the next flow step (`go-e2e` when the plan's `E2E` line is not `none`, updating `agent-view/e2e.md`, else `go-review`). Pass the initial baseline and the plan's test authorization.
4. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, not passes.
5. Record discovered work in `agent-view/checklist.md`; ask before expanding scope.
6. A required test failing: follow the project's [test retry limit](../../go-setup/references/public-docs.md#jdi-configmd). For other failed required checks, assign the failure to a `go-work` worker as a new step; ask the user when `go-work` reports a stop condition.

Finish with delivered behavior, validation limits, and uncommitted files or commit SHAs.
