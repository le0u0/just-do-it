---
name: go-e2e
description: 'E2E tests with Playwright: author specs and test data, explore UI for locators, run, debug failures, and write test results to agent-view/e2e.md.'
---

# E2E

## Scope & Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [go-setup](../go-setup/SKILL.md) and [storage.md](../go-setup/references/storage.md). If no existing project and branch artifacts explicitly identify this repository and exact branch, run `go-setup` first to confirm `{project}` with the user.
- Output: specs and test data in the repository; test run results written to `~/.just-do-it/{project}/{branch}/agent-view/e2e.md` per [Test report](../go-flow/references/reports.md#test-report-agent-viewutmd-and-agent-viewe2emd).
- In a worktree step, run in the assigned checkout, read configuration and plan from the caller's ticket storage, and return evidence directly. Evidence-only mode replaces all writes to the shared report, including missing-runner results.

## Workflow

1. Resolve the E2E setup and project references per [setup.md](references/setup.md) (`~/.just-do-it/{project}/public/jdi-config.md`). If `public/jdi-config.md` does not exist yet, trigger `go-setup`'s test configuration check to detect candidates, confirm with the user, and save `public/jdi-config.md`. If E2E runner is `none`, write and run no specs, record `no e2e test setup` in `agent-view/e2e.md`, and stop.
2. Use `playwright-cli` for every browser step: [playwright-cli.md](references/playwright-cli.md).
3. Pick one branch:
   - **Author** a spec or its data: require the E2E folder path (from `public/jdi-config.md` or located directly) and confirmed scenario(s) (from `agent-view/plan.md` or user confirmation). Read relevant files and follow [authoring.md](references/authoring.md).
   - **Explore** UI or find locators: explore only.
   - **Run or debug**: follow [running.md](references/running.md) and write the result to `agent-view/e2e.md`.

## Rules

- Apply the project's [test retry limit](../go-setup/references/public-docs.md#jdi-configmd) across callers; if missing or invalid, trigger `go-setup` to confirm it before retrying. Report exhausted retries to the caller or ask the user when running standalone. Preserve the caller's expected TDD red-run context.
- Production changes, including missing test selectors, go to `go-work`.
- Writing a spec never runs it. Run only when the request or approved plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests.
- A run changes no repository files and never resets environments or test data unless asked. Outside evidence-only mode, update `agent-view/e2e.md`.
- Shared helper, selector, or test data changed: list other specs using it under `Affected` in `agent-view/e2e.md`.
- Format only changed files.
- Formal review goes to `go-review`.
