# Tests

The manager runs the unit specs of its own steps, per `develop`, and assigns `e2e`, at these points, when the user or plan authorizes tests:

- Once, after the last step passes and the plan's `E2E` line is not `none`.
- A rerun after a fix: the failed specs.
- When the user asks for a run, or for a review.

A kind with no setup in the project is skipped, per [test-setup.md](test-setup.md). Any other change triggers no run. Resetting environments or test data happens only on the user's explicit request.

## e2e scope

e2e is slow, so it runs once, before review, never per step. The plan's `E2E` line in `## Testing` is the whitelist: assign `e2e` to write the specs it names, then run exactly those files. Put the exact spec paths in the handoff. A folder, a tag, or the full suite runs only when the user asks. A result counts only for the `HEAD` and diff it ran on; any other change needs a new run.

## Review request

Every review request runs unit specs. e2e runs too when `review.md` has no e2e result for the current `HEAD` and diff, unless the user says to skip it. In this order:

1. `review` writes `review.md`.
2. Run `develop` in test-run mode yourself on the specs in the diff, and assign `e2e` the plan's `E2E` specs, or the e2e specs in the diff when there is no plan. Reuse a result only when `review.md` `Tests` or `checklist.md` records it for the current `HEAD` and diff, such as the e2e run just before review in the ticket flow. Always run unit. Skip e2e only when a current result exists, the user says to skip it, or there is no spec in scope, per [test-setup.md](test-setup.md).
3. Collect both results. Write them yourself into `review.md`'s `Tests` section, replacing its `Unit` and `E2E` lines, and write `not run: <reason>` for a skipped kind. Only you edit `Tests`.
4. A review is not reported done until `Tests` shows both lines. A failed spec is reported to the user with the review, and you fix it with `develop` when the user asks.
