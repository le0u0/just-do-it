# Test Setup and Project References

## Test setup

Each project has its own unit and e2e setup, and some have none. Find what the project uses:

- **Unit:**
  - Runner config.
  - `package.json` scripts or build files.
  - Existing spec files, their location and naming.
  - Any project test rule or skill.
- **E2E:**
  - E2E runner config and its scripts.
  - E2E folder and existing specs.
  - Base URL, auth state, and test data the project documents.

When a kind has no setup (no runner, no script, no existing spec):

- Write `none: no setup` in the plan's `Test` or `E2E` line.
- Set one up only when the user asks.
- Partial setup, such as a runner without a script: ask the user.

## Project references

The project owns framework and domain rules. Before planning, read what applies:

- `AGENTS.md`, `CLAUDE.md`, rule files in `.agents/rules/` or `.claude/rules/`.
- Project-local skills in `.claude/skills/` and `.agents/skills/`:
  - Match the job against each skill's name and description.
  - Read and follow the matching ones. They win over this plugin's defaults.
- The glossary and ADRs the caller supplies, and the repository's own. Use the terms as written; ask the user to confirm before adding or changing one.
- The nearest comparable feature or spec, found by searching the checkout for a folder, file, or class name.

Nothing applies: say so, follow the nearest comparable code. Link to project rules, never copy them into the plan. Name the relevant rule files in a step's `Files` or `Do` so the implementer reads only those.
