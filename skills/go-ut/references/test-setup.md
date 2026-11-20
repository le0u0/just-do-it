# Unit Test Setup (`public/test-config.md`)

## Find or create it

1. Check `~/.just-do-it/{project}/public/test-config.md` first per [public-docs.md](../../go-setup/references/public-docs.md#test-configmd).
   - **Exists:** use the `## Unit` runner, paths, and focused command directly without re-checking.
   - **Missing:** inspect runner config (`vitest.config.*`, `karma.conf.*`, `jest.config.*`), `package.json` scripts or build files, existing specs (location, naming), and any project test rule or skill. Present the detected unit (and E2E) setup to the user, **confirm with the user**, and save `~/.just-do-it/{project}/public/test-config.md`.
2. Use exactly that runner, command, placement, and convention.

## No setup

- When `public/test-config.md` records `Runner: none` (or no runner, script, or existing spec exists and the user confirms `none`): skip writing and running specs, record `no unit test setup` in `dev-view/ut.md`, and set one up only when the user asks.

## Partial setup

- Such as a runner without a script: ask the user and record the confirmed command in `public/test-config.md`.
