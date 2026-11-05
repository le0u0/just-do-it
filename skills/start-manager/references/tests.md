# Tests

## When

The manager runs the unit specs of its own steps, per `go-work`, and assigns `go-e2e`, when the user or plan authorizes tests:

- Once, after the last step passes and the plan's `E2E` line is not `none`.
- A rerun after a fix: the failed specs.
- The user asks for a run, or for a review.

Rules:

- A kind with no setup in the project is skipped, per [test-setup.md](test-setup.md).
- Any other change triggers no run.
- Reset environments or test data only on the user's explicit request.

## e2e scope

- e2e is slow: run once, before review, never per step.
- The plan's `E2E` line in `## Testing` is the whitelist: assign `go-e2e` to write the specs it names, then run exactly those files.
- Put the exact spec paths in the handoff.
- A folder, a tag, or the full suite runs only when the user asks.
- A result counts only for the `HEAD` and diff it ran on; any other change needs a new run.

## Review request

- Every review request runs unit specs.
- e2e runs too when `review.md` has no e2e result for the current `HEAD` and diff, unless the user says to skip it.

In this order:

1. `go-review` returns the report; you save it as `review.md`.
2. Run `go-ut` yourself on the specs in the diff; assign `go-e2e` the plan's `E2E` specs, or the e2e specs in the diff when there is no plan.
   - Reuse a result only when `review.md` `Tests` or `checklist.md` records it for the current `HEAD` and diff, such as the e2e run just before review in the ticket flow.
   - Always run unit.
   - Skip e2e only when a current result exists, the user says to skip it, or no spec is in scope, per [test-setup.md](test-setup.md).
3. Collect both results.
   - Write them yourself into `review.md`'s `Tests` section, replacing its `Unit` and `E2E` lines.
   - Write `not run: <reason>` for a skipped kind.
   - Only you edit `Tests`.
4. A review is not reported done until `Tests` shows both lines.
   - A failed spec is reported to the user with the review.
   - You fix it with `go-work` when the user asks.
