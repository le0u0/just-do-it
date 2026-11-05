# Test Setup and Project References

## Test setup

Find what the project uses:

- **Unit:** runner config, `package.json` scripts or build files, existing specs (location, naming), any project test rule or skill.
- **E2E:** runner config and scripts, e2e folder and specs, documented base URL, auth state, test data.

Kind with no setup (no runner, script, or spec):

- Write `none: no setup` in the plan's `Test` or `E2E` line.
- Set one up only when asked.
- Partial setup, such as a runner without a script: ask.

## Project references

The project owns the rules. Read what applies:

- `AGENTS.md`, `CLAUDE.md`, `.agents/rules/`, `.claude/rules/`.
- Project-local skills in `.claude/skills/` and `.agents/skills/`: follow those matching the job; they win over this plugin.
- Glossary and ADRs, the caller's and the repository's. Terms as written; confirm with the user before adding or changing one.
- The nearest comparable feature or spec, found by searching the checkout.

Nothing applies: say so, follow the nearest comparable code. Name relevant rule files in a step's `Files` or `Do`.
