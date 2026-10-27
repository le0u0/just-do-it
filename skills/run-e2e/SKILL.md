---
name: run-e2e
description: 'Run end-to-end tests with the project's own command and report, changing no files. Open the e2e runner UI only when the user asks. Use for "run the e2e tests".'
effort: low
metadata:
  tier: light
---

# Run E2E

Report per [reports.md](../manager/references/reports.md). Spec fixes go to `write-e2e`; production fixes go to `develop`.

1. Find the e2e test setup per [test-setup.md](../manager/references/test-setup.md); with none, run nothing and say so. Read the [project references](../manager/references/project-references.md) for e2e: the runner config, `package.json` scripts, and any project-local e2e skill. Resolve the project, auth state, and base URL the way they say.
2. Run the target per [running.md](references/running.md) and report per [reports.md](../manager/references/reports.md). Leave diagnosis to `developer`.

Run tests only when the request or approved plan authorizes them; a later no-tests instruction wins. Never reset environments or test data unless the user explicitly asks; a run never authorizes it. Change no files.
