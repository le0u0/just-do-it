# Project References

Before code work, read:

- `AGENTS.md`, `CLAUDE.md`, `.agents/rules/`, `.claude/rules/`. When the plan step lists rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/` whose name or description matches the job, such as `create-*`. They win over this plugin's defaults.
- `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), plus repository `GLOSSARY.md` and `docs/adr/`. Use the terms as written. If you hit an unknown domain term or product section ("Section B", "patient history"), never guess—ask the user and update `public/glossary.md` per [public-docs.md](../../go-setup/references/public-docs.md).
- Existing reusable project components and shared primitives; prefer them over raw elements when the project provides them.
- The nearest comparable feature, found by searching for a folder, file, or class name; match its imports and patterns.

Nothing applies: say so and follow the nearest comparable code.
