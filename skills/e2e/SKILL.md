---
name: e2e
description: 'Write or fix end-to-end specs, helpers and test data, find locators, explore UI, or run e2e tests with the project''s own command. Use for "add an e2e test", "find the locator for X", "reproduce this in the UI" or "run the e2e tests".'
---

# E2E

Report per [reports.md](../manager/references/reports.md). Production changes, including missing test selectors, go to `develop`.

1. Find the e2e test setup per [test-setup.md](../manager/references/test-setup.md); with none, write and run nothing and say so. Read the [project references](../manager/references/project-references.md) for e2e: rules, project-local e2e skills, the runner config, `package.json` scripts, and the closest spec. Resolve the auth state, test data, helpers, and base URL they use.
2. Read one branch:
   - Author a spec or its data: [exploration.md](references/exploration.md) first, then [authoring.md](references/authoring.md).
   - Explore UI or discover locators: [exploration.md](references/exploration.md).
   - Run tests, or open the e2e UI only when the user asks: [running.md](references/running.md).
3. Do only the requested work. When you change a shared helper, selector, or test data, search for other specs that use it and list them in your report under `Affected`.
4. After authoring, check by reading: each requested behavior has an observable assertion, stable locator, deterministic wait, and repository-owned test data.

Writing a spec never runs it, even after a fix. Run specs only when the request or approved plan authorizes it; a later no-tests instruction wins. A run changes no files and never resets environments or test data unless the user explicitly asks. Diagnose a failure only when asked, per [running.md](references/running.md). Format only changed files. Formal review goes to `review`.
