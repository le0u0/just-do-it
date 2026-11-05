# Test Setup

Before writing or running tests of a kind, find what the project uses:

- **Unit:** runner config, `package.json` scripts or build files, existing specs (location, naming), project test rule or skill.
- **E2E:** runner config, scripts, e2e folder and specs, documented base URL, auth state, test data.

- Use exactly that runner, command, placement, convention.
- No runner, script, or spec for a kind: skip it, say `no <unit|e2e> test setup` in the report and under `Evidence` in `checklist.md`; set one up only when asked.
- Partial setup (runner without a script): ask the user.
