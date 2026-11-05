# Project References

This plugin holds no framework or domain rules. The project being changed owns them. Before code or test work, find and read what applies.

## Sources

- `AGENTS.md`, `CLAUDE.md`, rule files in `.agents/rules/` or `.claude/rules/`.
  - Plan step lists relevant rule files: read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`.
  - Match the job against each name and description, such as a `create-*` or `testing-*` skill; read and follow matches.
  - They win over this plugin's defaults on conflict.
- `~/.just-do-it/{project}/docs/glossary.md` and `~/.just-do-it/{project}/docs/adr/`: confirmed terms and decisions.
  - Use terms as written; ask the user to confirm before adding or changing one.
- Nearest comparable feature or spec: search the checkout for a folder, file, or class name.

## Rules

- Nothing applies: say so, follow nearest comparable code.
- Link to project rules; do not copy them into task docs.

## Context cache

- With a branch folder, `state/context.md` holds what the search found: one line per rule file, project-local skill, comparable spec that applies.
- File exists: read it instead of searching.
- File missing: search once, then save it.
- What it names no longer fits the job: search again, update in place.
