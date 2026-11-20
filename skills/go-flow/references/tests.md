# Tests

## Configuration

Before running or writing unit or E2E tests, check `~/.just-do-it/{project}/public/test-config.md`. If it does not exist, run `go-setup`'s test configuration step to detect candidates, confirm with the user, and save `public/test-config.md`.

## When

When the user or plan authorizes tests:
- Each `go-work` worker runs its step's unit specs via `go-ut` (writing `dev-view/ut.md`) and step E2E specs when assigned via `go-e2e` (writing `dev-view/e2e.md`).
- In `go-flow`, `go-e2e` runs once after the last step passes if `agent-view/plan.md`'s `E2E` line is not `none`, updating `dev-view/e2e.md`.
- On a rerun after a fix: rerun the failed specs and update `dev-view/ut.md` or `dev-view/e2e.md`.
- A kind with `Runner: none` in `public/test-config.md` is skipped.

## E2E scope

- Slow: run once after implementation steps pass, before `go-review`.
- The plan's `E2E` line in `## Testing` is the whitelist: `go-e2e` writes those specs, runs exactly those files, and writes `dev-view/e2e.md`.
- A folder, tag, or full suite runs only when the user asks.
- A result in `dev-view/ut.md` or `dev-view/e2e.md` counts as current when its `HEAD` matches the reviewed state.
