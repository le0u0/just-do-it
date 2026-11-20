# Unit Test Setup (`public/jdi-config.md`)

## Find or create it

1. Check `~/.just-do-it/{project}/public/jdi-config.md` first per [public-docs.md](../../go-setup/references/public-docs.md#jdi-configmd).
   - **Exists:** use the `## Unit` runner, paths, and focused command directly without re-checking.
   - **Missing:** run `go-setup` to detect and confirm the test setup.
2. Use exactly that runner, command, placement, and convention.

## No setup

- When `public/jdi-config.md` records `Runner: none` (or no runner, script, or existing spec exists and the user confirms `none`): skip writing and running specs, record `no unit test setup` in `agent-view/ut.md`, and set one up only when the user asks.

## Partial setup

- Such as a runner without a script: ask the user and record the confirmed command in `public/jdi-config.md`.
