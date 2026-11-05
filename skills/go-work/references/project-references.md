# Project References

This plugin holds no framework or domain rules; the project owns them. Before code work, read:

- `AGENTS.md`, `CLAUDE.md`, `.agents/rules/`, `.claude/rules/`. When the plan step lists rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/` whose name or description matches the job, such as `create-*`. They win over this plugin's defaults.
- `GLOSSARY.md`, `docs/adr/`, and any glossary or ADR text the caller passes. Use the terms as written.
- The nearest comparable feature, found by searching for a folder, file, or class name.

Nothing applies: say so and follow the nearest comparable code.
