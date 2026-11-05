# Project References

This plugin holds no framework or domain rules. The project being changed owns them. Before spec work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the plan step lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, such as a `testing-*` skill, then read and follow the matching ones. They win over this plugin's defaults where they conflict.
- The repo's `GLOSSARY.md` and `docs/adr/`, plus any glossary or ADR text the caller passes: the team's confirmed terms and decisions. Use the terms as written.
- The nearest comparable spec, found by searching the checkout for a folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code.
