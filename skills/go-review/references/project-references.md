# Project References

The project owns its rules. Before the review pass, read what applies:

- `AGENTS.md`, `CLAUDE.md`, rules in `.agents/rules/` or `.claude/rules/` (only the ones the caller lists, if any).
- Matching project-local skills in `.claude/skills/` and `.agents/skills/`; they win over this skill's defaults.
- Glossary and ADRs the caller names; use terms as written.
- The nearest comparable feature or spec.

Nothing applies: say so, follow nearest comparable code. Cite rules; do not copy them.
