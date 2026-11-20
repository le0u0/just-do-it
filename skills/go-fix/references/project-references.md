# Project References

The project owns its rules. Before code or test work, read what applies:

- `AGENTS.md`, `CLAUDE.md`, rules in `.agents/rules/` or `.claude/rules/` (only the ones the caller lists, if any).
- Matching project-local skills in `.claude/skills/` and `.agents/skills/`; they win over this skill's defaults.
- `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), plus repository `GLOSSARY.md` and `docs/adr/`; use terms as written.
- The nearest comparable feature or spec.

Nothing applies: say so, follow nearest comparable code. Cite rules; do not copy them.
