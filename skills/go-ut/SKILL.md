---
name: go-ut
description: 'Write, fix or run unit specs for changed code, following the project''s own test setup and conventions, and write test results to dev-view/ut.md.'
---

# Unit Tests

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user. After any test run, write or update `~/.just-do-it/{project}/{branch}/dev-view/ut.md` per [Test report](../go-flow/references/reports.md#test-report-dev-viewutmd-and-dev-viewe2emd) and return the summary to the caller.

## Modes

- **Write or fix specs:** no production change. Report production defects; `go-work` fixes them. When running is authorized, run the focused spec and record the result in `dev-view/ut.md`.
- **Test run:** run the named specs per [running.md](references/running.md), write `dev-view/ut.md`, and report. Change no repository files.

## Rules

- Run specs only when the request or plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests. Otherwise write specs and hand back unrun.
- Focused specs only; the full suite only when the user asks.
- Leave the protected files in `running.md` and unrelated specs unchanged.
- E2E specs go to `go-e2e`.

## Workflow

1. Read the [project references](references/project-references.md) for the feature type; follow their conventions for mocking, setup, and file placement.
2. Resolve the unit test setup per [test-setup.md](references/test-setup.md) (`~/.just-do-it/{project}/public/test-config.md`). If `public/test-config.md` does not exist yet, trigger `go-setup`'s test configuration check to detect candidates, confirm with the user, and save `public/test-config.md`. If unit runner is `none`, write and run no specs, record `no unit test setup` in `dev-view/ut.md`, and stop.
3. Read [test-quality.md](references/test-quality.md) and [examples.md](references/examples.md), plus [mocking.md](references/mocking.md) when a spec needs a mock.
4. Write one spec for one behavior in the spec file the project places beside the code, with the coverage comment from `test-quality.md`.
5. When authorized, run the focused spec per `running.md`, write or update `dev-view/ut.md`, and report the result and saved path.
6. Self-check by reading: setup reaches the intended state; assertions would fail on the regression; no mock of the code's own modules; no expected value recomputed from the code's formula. Rewrite a spec that fails this check, and rerun it when running is authorized (updating `dev-view/ut.md`), before reporting. Format only changed files.
