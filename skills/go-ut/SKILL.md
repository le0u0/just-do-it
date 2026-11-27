---
name: go-ut
description: 'Write, fix or run unit specs for changed code, following the project''s own test setup and conventions, and write test results to agent-view/ut.md.'
---

# Unit Tests

Resolve `~/.just-do-it/{project}/{branch}/` per [go-setup](../go-setup/SKILL.md) and [storage.md](../go-setup/references/storage.md). If no existing project and branch artifacts explicitly identify this repository and exact branch, run `go-setup` first to confirm `{project}` with the user. After any test run outside evidence-only mode, write or update `~/.just-do-it/{project}/{branch}/agent-view/ut.md` per [Test report](../go-flow/references/reports.md#test-report-agent-viewutmd-and-agent-viewe2emd) and return the summary to the caller.

In a worktree step, use the assigned checkout for code and use the caller's ticket storage for configuration. Evidence-only mode replaces all writes to the shared report, including missing-runner results.

## Modes

- **Write or fix specs:** no production change. Report production defects; `go-work` fixes them. When running is authorized, run the focused spec and record the result in `agent-view/ut.md`.
- **Test run:** run the named specs per [running.md](references/running.md), write `agent-view/ut.md`, and report. Change no repository files.

**Evidence-only mode:** When the coordinator requests it, return the test report fields, including the snapshot, for every outcome. Skip writing the shared report, including on retries, blocked selections, and missing setup.

## Rules

- Apply the project's [test retry limit](../go-setup/references/public-docs.md#jdi-configmd) across callers; if missing or invalid, trigger `go-setup` to confirm it before retrying. Report exhausted retries to the caller or ask the user when running standalone. Preserve the caller's expected TDD red-run context.
- Run specs only when the request or plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests. Otherwise write specs and hand back unrun.
- Focused specs only; the full suite only when the user asks.
- Cover all observable behaviors of the touched component or unit. Limit any added code comment to 1 line (`// ...`), only when non-obvious.
- Leave the protected files in `running.md` and unrelated specs unchanged.
- E2E specs go to `go-e2e`.

## Workflow

1. Read the [project references](references/project-references.md) for the feature type; follow their conventions for mocking, setup, and file placement.
2. Resolve the unit test setup per [test-setup.md](references/test-setup.md) (`~/.just-do-it/{project}/public/jdi-config.md`). If `public/jdi-config.md` does not exist yet, trigger `go-setup`'s test configuration check to detect candidates, confirm with the user, and save `public/jdi-config.md`. If unit runner is `none`, write and run no specs, record `no unit test setup` in `agent-view/ut.md`, and stop.
3. Use the nearest relevant suite and its fixtures. Verify this precedent against project rules before adding or changing a test. For annotated UI changes identify the assertion for the exact element and an affected neighboring behavior if applicable. Read [test-quality.md](references/test-quality.md) and [examples.md](references/examples.md), plus [mocking.md](references/mocking.md) when a spec needs a mock.
4. Write specs covering the behavior and all observable behaviors of the touched component or unit in the spec file the project places beside the code.
5. When authorized, run the focused spec per `running.md`, write or update `agent-view/ut.md`, and report the result and saved path. When authoring, report the spec path, suite/fixture reused, asserted behavior and whether the test ran.
6. Self-check by reading: setup reaches the intended state; assertions would fail on the regression; no mock of the code's own modules; no expected value recomputed from the code's formula. Rewrite a spec that fails this check, and rerun it when running is authorized (updating `agent-view/ut.md`), before reporting. Format only changed files.
