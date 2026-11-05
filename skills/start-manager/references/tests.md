# Tests

## When

When the user or plan authorizes tests, the manager runs unit specs of its own steps per `go-work` and assigns `go-e2e`:

- Once, after the last step passes, if the plan's `E2E` line is not `none`.
- A rerun after a fix: the failed specs.
- The user asks for a run or a review.

- A kind with no setup is skipped per [test-setup.md](test-setup.md). Any other change triggers no run.
- Reset environments or test data only on the user's explicit request.

## e2e scope

- Slow: once, before review, never per step.
- The plan's `E2E` line in `## Testing` is the whitelist: `go-e2e` writes those specs, then runs exactly those files; put the paths in the handoff.
- A folder, tag, or full suite only when the user asks.
- A result counts only for the `HEAD` and diff it ran on.

## Review request

Unit specs always run. e2e runs when `review.md` has no e2e result for the current `HEAD` and diff, unless the user skips it. In order:

1. `go-review` returns the report; save it as `review.md`.
2. Run `go-ut` on the specs in the diff; assign `go-e2e` the plan's `E2E` specs (no plan: the e2e specs in the diff).
   - Reuse a result only when `review.md` `Tests` or `checklist.md` records it for the current `HEAD` and diff.
   - Skip e2e only when a current result exists, the user skips it, or no spec is in scope.
3. Write both results into `review.md`'s `Tests`, replacing `Unit` and `E2E`; `not run: <reason>` for a skipped kind. Only you edit `Tests`.
4. Not done until `Tests` shows both lines. Report a failed spec with the review; fix it with `go-work` when asked.
