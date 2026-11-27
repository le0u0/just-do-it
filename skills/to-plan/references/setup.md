# Test Setup and Project References

Read applicable project [standards and ADRs](../../go-setup/references/public-docs.md#standardsmd) from shared storage. Apply repository rules first and verify cited precedents.

## Test setup

1. Read `~/.just-do-it/{project}/public/jdi-config.md` if it already exists.
2. Otherwise inspect what the project uses:
   - **Unit:** runner config, `package.json` scripts or build files, existing specs (location, naming), any project test rule or skill.
   - **E2E:** runner config and scripts, e2e folder and specs, documented base URL, auth state, test data.

Kind with no setup (no runner, script, or spec):

- Write `none: no setup` in the plan's `Test` or `E2E` line.
- Set one up only when asked.
- Partial setup, such as a runner without a script: ask.

## Project references

The project owns the rules. Read what applies:

- `AGENTS.md`, `CLAUDE.md`, and the active host's rules.
- Project-local skills for the active host: follow those matching the job; they win over this plugin.
- `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), plus repository `GLOSSARY.md` and `docs/adr/`. Use terms as written; never guess unknown terms—confirm with the user and save to `public/glossary.md` or `public/adr/` per [domain-docs.md](domain-docs.md).
- The nearest comparable feature or spec, found by searching the checkout.

Nothing applies: say so, follow the nearest comparable code. Name relevant rule files in a step's `Files` or `Do`.
