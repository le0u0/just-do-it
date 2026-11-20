# go-setup

Resolves or initializes `~/.just-do-it/{project}/{branch}/` (`agent-view/`, `dev-view/`, and project-level `public/`). Triggered automatically by any skill when the current branch folder cannot be found, or called directly.

## What it does

1. Computes `{branch}` from `git branch --show-current` with `/` replaced by `-` (for example, `fix-workflow-failures-triage-changelog`).
2. Checks if `~/.just-do-it/*/{branch}` already exists.
   - **Exists:** reuses `{project}` and ensures `agent-view/`, `dev-view/`, and `public/` exist.
   - **Missing:** **always asks and confirms `{project}` with the user** before creating directories.
3. When a skill needs to handle tests (`go-ut`, `go-e2e`, or explicit test setup) and `~/.just-do-it/{project}/public/test-config.md` does not exist yet, detects the repo's unit and E2E runners/paths/commands, confirms with the user, and writes `public/test-config.md`.
4. `public/glossary.md` and `public/adr/` are not pre-created empty; they are created and updated on demand when unknown domain terms or hard-to-reverse decisions are confirmed with the user.

[Skill](../skills/go-setup/SKILL.md) · [Storage layout](../skills/go-setup/references/storage.md) · [Public docs](../skills/go-setup/references/public-docs.md)
