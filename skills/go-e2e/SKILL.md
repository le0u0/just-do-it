---
name: go-e2e
description: 'E2E tests with Playwright: author specs and test data, explore UI for locators, run, debug failures. Use for "add an e2e test", "find the locator for X", "run the e2e tests", "fix this e2e failure".'
---

# E2E

## Scope

- Output: specs and test data in the repository; everything else returns in the reply, as the caller specifies.

## Workflow

1. Find the e2e setup and project references per [setup.md](references/setup.md). No setup: write and run nothing, say so.
2. Use `playwright-cli` for every browser step: [playwright-cli.md](references/playwright-cli.md).
3. Pick one branch:
   - **Author** a spec or its data: explore, then [authoring.md](references/authoring.md).
   - **Explore** UI or find locators: explore only.
   - **Run or debug**: [running.md](references/running.md).

## Rules

- Production changes, including missing test selectors, go to `go-work`.
- Writing a spec never runs it. Run only when the request or approved plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests.
- A run changes no files and never resets environments or test data unless asked.
- Shared helper, selector, or test data changed: list other specs using it under `Affected`.
- Format only changed files.
- Formal review goes to `go-review`.
