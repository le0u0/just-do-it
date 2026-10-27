# Project References

This plugin holds no framework or domain rules. The project being changed owns them. Before code or test work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the plan step lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, such as a `create-*` or `testing-*` skill, then read and follow the matching ones. They win over this plugin's defaults where they conflict.
- `~/.agent-workflow/{project}/docs/glossary.md` and `~/.agent-workflow/{project}/docs/adr/`: the team's confirmed terms and decisions. Use the terms as written, and ask the user to confirm before adding or changing one.
- The nearest comparable feature or spec, found by searching the checkout for a folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code. Link to project rules instead of copying them into task docs.

## Context cache

With a branch folder, `state/context.md` holds what the search above found: one line per rule file, project-local skill, and comparable spec that applies. When it exists, read it instead of searching. When it is missing, search once, then save it. When what it names no longer fits the job, search again and update it in place.
