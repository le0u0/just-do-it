# go-setup

Resolves or initializes `~/.just-do-it/{project}/{branch}/` (`agent-view/`, `dev-view/`, and project-level `public/`). Triggered automatically by any skill when repository and exact branch identity is missing or ambiguous, or called directly.

## What it does

1. Computes `{branch}` from `git branch --show-current` encoded as UTF-8 hexadecimal with a `branch-` prefix (for example, `branch-666978...`), or asks for a short kebab-case task name on detached `HEAD` or non-git directories.
2. Resolves `{project}` for the current repository and exact branch:
   - **Verified match:** reuses `{project}` (and `{branch}`, including verified legacy `/` → `-` directories) only when existing artifacts explicitly identify both the current repository and exact branch, and ensures `agent-view/`, `dev-view/`, and `public/` exist.
   - **Missing or ambiguous:** **always asks and confirms `{project}` with the user** before creating directories or reading/writing task data.
3. On a direct call, lists all editable settings and current values: retry limit; unit runner, paths, and command; E2E runner, folder, base URL, command, authentication state, and test data. Updates requested fields while preserving the rest.
4. When a skill needs test settings, confirms missing settings and saves them in `public/jdi-config.md`.
5. `public/glossary.md` and `public/adr/` are not pre-created empty; they are created and updated on demand when unknown domain terms or hard-to-reverse decisions are confirmed with the user.

[Skill](../skills/go-setup/SKILL.md) · [Storage layout](../skills/go-setup/references/storage.md) · [Public docs](../skills/go-setup/references/public-docs.md)
