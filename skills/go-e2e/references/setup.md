# E2E Setup and Project References

## Setup

- Find what the project uses: runner config, scripts, e2e folder, existing specs, documented base URL, auth state, test data.
- Use exactly that runner, command, placement, and convention. Install and configure nothing.
- No runner, script, or spec: write and run nothing, say `no e2e test setup`. Set one up only when asked.
- Partial setup: ask the user.

## Project references

The project owns the rules. Read what applies:

- `AGENTS.md`, `CLAUDE.md`, `.agents/rules/`, `.claude/rules/`. Only the files the caller lists, when it lists any.
- Project-local skills in `.claude/skills/` and `.agents/skills/`: follow those matching the job; they win over this plugin.
- The caller's glossary and ADRs, terms as written.
- The nearest comparable spec, found by searching the checkout.

Nothing applies: say so, follow the nearest spec. Link rules, never copy them.
