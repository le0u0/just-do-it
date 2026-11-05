# Test Setup and Project References

## Test setup

Each project has its own unit and e2e setup, and some have none. Find what the project uses:

- **Unit:** the runner config, the `package.json` scripts or build files, the existing spec files with their location and naming, and any project test rule or skill.
- **E2E:** the e2e runner config, its scripts, the e2e folder and existing specs, plus the base URL, auth state, and test data the project documents.

When a kind has no setup, meaning no runner, no script, and no existing spec, write `none: no setup` in the plan's `Test` or `E2E` line. Set one up only when the user asks. When the setup is partial, such as a runner without a script, ask the user.

## Project references

This plugin holds no framework or domain rules. The project owns them. Before planning, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, then read and follow the matching ones. They win over this plugin's defaults where they conflict.
- The glossary and ADRs the caller supplies, and the repository's own. Use the terms as written, and ask the user to confirm before adding or changing one.
- The nearest comparable feature or spec, found by searching the checkout for a folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code. Link to project rules instead of copying them into the plan. Name the relevant rule files in the plan's step `Files` or `Do` so the implementer reads only those.
