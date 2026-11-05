---
name: go-e2e
description: 'E2E tests with Playwright: author specs and test data, explore UI for locators, run, debug failures. Use for "add an e2e test", "find the locator for X", "run the e2e tests", "fix this e2e failure".'
---

# E2E

Write specs and test data in the repository only; write no plugin docs (plan, checklist, review, triage). Report as the caller specifies.

## Workflow

1. Find the e2e setup per [setup.md](references/setup.md). None: write and run nothing, say so.
2. Read the project references for e2e per [setup.md](references/setup.md):
   - Rules and project-local e2e skills.
   - Runner config, `package.json` scripts, closest spec.
   - Auth state, test data, helpers, base URL.
3. Use `playwright-cli` for every browser step: [playwright-cli.md](references/playwright-cli.md).
4. Pick one branch:
   - **Author** a spec or its data: explore, then [authoring.md](references/authoring.md).
   - **Explore** UI or find locators: explore only.
   - **Run or debug**: [running.md](references/running.md).
5. Do only the requested work.

## Rules

- Production changes, including missing test selectors, go to `go-work`.
- Writing a spec never runs it.
- Run only when the request or approved plan authorizes it. A later no-tests instruction wins.
- A run changes no files and never resets environments or test data unless asked.
- Shared helper, selector, or test data changed: search for other specs using it, list them under `Affected`.
- Format only changed files.
- Formal review goes to `go-review`.
