# Unit Test Setup

Before writing or running unit specs, find what the project uses: the runner config, the `package.json` scripts or build files, the existing spec files with their location and naming, and any project test rule or skill.

Write and run with exactly that runner, command, placement, and convention. Install and configure nothing.

When there is no runner, no script, and no existing spec:
- Skip writing and running specs.
- Say `no unit test setup` in the report.
- Set one up only when the user asks.

When the setup is partial, such as a runner without a script, ask the user.
