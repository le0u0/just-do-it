# Project References

The project being reviewed owns its rules. Before the review pass, find and read what applies.

## Sources

- `AGENTS.md`, `CLAUDE.md`, rule files in `.agents/rules/` or `.claude/rules/`.
  - Caller lists relevant rule files: read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`.
  - Match the job against each name and description; read and follow matches.
  - They win over this skill's defaults on conflict.
- Glossary and ADRs, when the caller names them. Use terms as written.
- Nearest comparable feature or spec: search the checkout for a folder, file, or class name.

## Rules

- Nothing applies: say so, follow nearest comparable code.
- Cite project rules; do not copy them.
