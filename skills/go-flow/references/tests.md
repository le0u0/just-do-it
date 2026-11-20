# Tests

## Configuration

Before running or writing unit or E2E tests, check `~/.just-do-it/{project}/public/jdi-config.md`. If it does not exist or lacks a valid retry limit, run `go-setup`'s test configuration step to confirm and save the missing settings.

## When

When the user or plan authorizes tests:
- Each `go-work` worker returns step-local unit test evidence through `go-ut` in evidence-only mode. The coordinator collects those results. The coordinator publishes `agent-view/ut.md` after final verification on the delivered snapshot using the final run's results. Earlier results support step delivery only. Run assigned step E2E specs via `go-e2e` (writing `agent-view/e2e.md`).
- In `go-flow`, `go-e2e` runs once after the last step passes if `agent-view/plan.md`'s `E2E` line is not `none`, updating `agent-view/e2e.md`.
- On a rerun after a fix: rerun the failed specs and update `agent-view/ut.md` or `agent-view/e2e.md`.
- A kind with `Runner: none` in `public/jdi-config.md` is skipped.

## E2E scope

- Slow: run once after implementation steps pass, before `go-review`.
- The plan's `E2E` scenario and the exact E2E spec paths in the adjacent `<sub>` line in `## Testing` are the whitelist: `go-e2e` writes those specs, runs exactly those files, and writes `agent-view/e2e.md`.
- A folder, tag, or full suite runs only when the user asks.
- A result counts as current only when its recorded snapshot matches the reviewed state, including HEAD, index, tracked working-tree contents, and untracked non-ignored files. A missing snapshot or changed snapshot makes the result stale.
