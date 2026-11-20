# go-setup

Resolves or initializes `~/.just-do-it/{project}/{branch}/` (`agent-view/`, `dev-view/`, and project-level `public/`). Triggered automatically by any skill when the current branch folder cannot be found, or called directly.

## What it does

1. Computes `{branch}` from `git branch --show-current` with `/` replaced by `-` (for example, `fix-workflow-failures-triage-changelog`).
2. Checks if `~/.just-do-it/*/{branch}` already exists.
   - **Exists:** reuses `{project}` and ensures `agent-view/`, `dev-view/`, and `public/` exist.
   - **Missing:** **always asks and confirms `{project}` with the user** before creating directories.
3. On a direct call, lists all editable settings and current values: retry limit; unit runner, paths, and command; E2E runner, folder, base URL, command, authentication state, and test data. Updates requested fields while preserving the rest.
4. When a skill needs test settings, confirms missing settings and saves them in `public/jdi-config.md`.
5. `public/glossary.md` and `public/adr/` are not pre-created empty; they are created and updated on demand when unknown domain terms or hard-to-reverse decisions are confirmed with the user.

[Skill](../skills/go-setup/SKILL.md) · [Storage layout](../skills/go-setup/references/storage.md) · [Public docs](../skills/go-setup/references/public-docs.md)
