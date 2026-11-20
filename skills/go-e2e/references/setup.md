# E2E Setup and Project References (`public/test-config.md`)

## Setup

1. Check `~/.just-do-it/{project}/public/test-config.md` first per [public-docs.md](../../go-setup/references/public-docs.md#test-configmd).
   - **Exists:** use the `## E2E` runner, folder, base URL, and focused command directly without re-checking.
   - **Missing:** inspect runner config (`playwright.config.*`, `cypress.config.*`), scripts, e2e folder, existing specs, documented base URL, auth state, and test data. Present the detected setup to the user, **confirm with the user**, and save `~/.just-do-it/{project}/public/test-config.md`.
2. Use exactly that runner, command, placement, and convention. Install or configure no project test infrastructure.
3. When `public/test-config.md` records `Runner: none`: write and run nothing, record `no e2e test setup` in `agent-view/e2e.md`, and set one up only when asked.
4. Browser exploration needs `playwright-cli`; a browser connector alone does not satisfy that contract. Check CLI/browser availability per [playwright-cli.md](playwright-cli.md); report unavailable tooling and obtain approval before installing it.

## Project references

The project owns the rules. Read what applies:

- `AGENTS.md`, `CLAUDE.md`, `.agents/rules/`, `.claude/rules/`. Only the files the caller lists, when it lists any.
- Project-local skills in `.claude/skills/` and `.agents/skills/`: follow those matching the job; they win over this plugin.
- `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), terms as written.
- The nearest comparable spec, found by searching the checkout.

Nothing applies: say so, follow the nearest spec.
