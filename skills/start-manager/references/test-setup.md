# Test Setup

Each project has its own unit and e2e setup; some have none. Before writing or running tests of a kind, find what the project uses.

## Find

- **Unit:** runner config, `package.json` scripts or build files, existing spec files (location, naming), project test rule or skill.
- **E2E:** e2e runner config, scripts, e2e folder and existing specs, plus the documented base URL, auth state, test data.

## Use

- Write and run with exactly that runner, command, placement, convention.
- Install and configure nothing.

## No setup

A kind has no runner, no script, and no existing spec:

- Skip writing and running that kind.
- Say `no <unit|e2e> test setup` in the report, and under `Evidence` in `checklist.md`.
- Set one up only when the user asks.

## Partial setup

- Such as a runner without a script: ask the user.
