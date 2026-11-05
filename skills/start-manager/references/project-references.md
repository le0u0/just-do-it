# Project References

This plugin holds no framework or domain rules; the project owns them. Before code or test work, read what applies:

- `AGENTS.md`, `CLAUDE.md`, rules in `.agents/rules/` or `.claude/rules/` (only those the plan step lists, if any).
- Matching project-local skills in `.claude/skills/` and `.agents/skills/` (such as `create-*`, `testing-*`); they win over this plugin's defaults.
- `~/.just-do-it/{project}/docs/glossary.md` and `docs/adr/`: use terms as written; confirm with the user before adding or changing one.
- The nearest comparable feature or spec.

Nothing applies: say so, follow nearest comparable code. Link rules; do not copy them into task docs.

## Context cache

- With a branch folder, `state/context.md` holds one line per applicable rule file, project-local skill, comparable spec.
- Exists: read it, do not search. Missing: search once, save it. No longer fits the job: search again, update in place.
