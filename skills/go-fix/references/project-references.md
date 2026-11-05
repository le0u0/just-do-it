# Project References

The project being changed owns its rules. Before code or test work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the caller lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, then read and follow the matching ones. They win over this skill's defaults where they conflict.
- The team's glossary and ADRs, when the caller names them. Use the terms as written.
- The nearest comparable feature or spec, found by searching the checkout for a folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code. Cite project rules instead of copying them.
