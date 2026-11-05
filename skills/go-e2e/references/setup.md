# E2E Setup and Project References

## Setup

- Find what the project uses: the e2e runner config, its scripts, the e2e folder and existing specs, plus the base URL, auth state, and test data the project documents.
- Write and run with exactly that runner, command, placement, and convention. Install and configure nothing.
- No runner, no script, and no existing spec: skip writing and running, and say `no e2e test setup`. Set one up only when the user asks.
- Partial setup, such as a runner without a script: ask the user.

## Project references

This plugin holds no framework or domain rules; the project owns them. Before e2e work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the caller lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, then read and follow the matching ones. They win over this plugin's defaults where they conflict.
- The caller's glossary and ADRs, when supplied. Use the terms as written.
- The nearest comparable spec, found by searching the checkout for a folder, file, or class name.

Nothing applies: say so and follow the nearest comparable spec. Link to project rules instead of copying them.
