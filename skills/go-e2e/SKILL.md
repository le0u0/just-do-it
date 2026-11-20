---
name: go-e2e
description: 'E2E tests with Playwright: author specs and test data, explore UI for locators, run, debug failures, and write test results to dev-view/e2e.md.'
---

# E2E

## Scope & Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
- Output: specs and test data in the repository; test run results written to `~/.just-do-it/{project}/{branch}/dev-view/e2e.md` per [Test report](../go-flow/references/reports.md#test-report-dev-viewutmd-and-dev-viewe2emd).

## Workflow

1. Resolve the E2E setup and project references per [setup.md](references/setup.md) (`~/.just-do-it/{project}/public/test-config.md`). If `public/test-config.md` does not exist yet, trigger `go-setup`'s test configuration check to detect candidates, confirm with the user, and save `public/test-config.md`. If E2E runner is `none`, write and run no specs, record `no e2e test setup` in `dev-view/e2e.md`, and stop.
2. Use `playwright-cli` for every browser step: [playwright-cli.md](references/playwright-cli.md).
3. Pick one branch:
   - **Author** a spec or its data: require the E2E folder path (from `public/test-config.md` or located directly) and confirmed scenario(s) (from `agent-view/plan.md` or user confirmation). Read relevant files and follow [authoring.md](references/authoring.md).
   - **Explore** UI or find locators: explore only.
   - **Run or debug**: follow [running.md](references/running.md) and write the result to `dev-view/e2e.md`.

## Rules

- Production changes, including missing test selectors, go to `go-work`.
- Writing a spec never runs it. Run only when the request or approved plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests.
- A run changes no repository files and never resets environments or test data unless asked. It always updates `dev-view/e2e.md`.
- Shared helper, selector, or test data changed: list other specs using it under `Affected` in `dev-view/e2e.md`.
- Format only changed files.
- Formal review goes to `go-review`.
