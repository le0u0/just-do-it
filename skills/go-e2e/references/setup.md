# E2E Setup and Project References

## Setup

- Find what the project uses:
  - E2E runner config and its scripts.
  - E2E folder and existing specs.
  - Base URL, auth state, and test data the project documents.
- Write and run with exactly that runner, command, placement, and convention. Install and configure nothing.
- No runner, no script, no existing spec: skip writing and running, say `no e2e test setup`. Set one up only when the user asks.
- Partial setup, such as a runner without a script: ask the user.

## Project references

The project owns framework and domain rules. Before e2e work, read what applies:

- `AGENTS.md`, `CLAUDE.md`, rule files in `.agents/rules/` or `.claude/rules/`. When the caller lists relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`:
  - Match the job against each skill's name and description.
  - Read and follow the matching ones. They win over this plugin's defaults.
- The caller's glossary and ADRs, when supplied. Use the terms as written.
- The nearest comparable spec, found by searching the checkout for a folder, file, or class name.

Nothing applies: say so, follow the nearest comparable spec. Link to project rules, never copy them.
