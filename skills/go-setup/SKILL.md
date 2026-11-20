---
name: go-setup
description: 'Set up and resolve the ~/.just-do-it/{project}/{branch}/ storage directory (agent-view/, dev-view/, and public/). Triggered automatically by any skill when the current branch folder is missing, or called directly to initialize project storage and test-config.md.'
---

# Setup Storage

Resolve or initialize `~/.just-do-it/{project}/{branch}/` for the current checkout and branch. Every storage-writing skill resolves its branch directory through this contract before writing.

## Branch slug

1. Run `git branch --show-current` and replace every `/` with `-` (for example, `fix/workflow-failures-triage-changelog` becomes `fix-workflow-failures-triage-changelog`).
2. Detached `HEAD` or non-git directory: ask the user for a short kebab-case task name to use as `{branch}`.

## Resolve or create storage

1. Check whether `~/.just-do-it/*/{branch}` already exists:
   - **Unique match found:** reuse that `{project}` and `~/.just-do-it/{project}/{branch}/`. Ensure `agent-view/`, `dev-view/`, and `../public/` directories exist.
   - **No match (or multiple matches across projects):** **always ask and confirm `{project}` with the user** before creating folders. Suggest the repository folder name in lowercase kebab-case as the recommended option, or list existing `~/.just-do-it/*/` project names if multiple match, but never pick or create `{project}` without user confirmation.
2. Once `{project}` is confirmed, check write permission and create:
   - `~/.just-do-it/{project}/public/`
   - `~/.just-do-it/{project}/{branch}/agent-view/`
   - `~/.just-do-it/{project}/{branch}/dev-view/`
3. Do **not** pre-create empty `public/glossary.md`, `public/adr/`, or `public/test-config.md` during basic folder setup. Those files are created only when needed per [public-docs.md](references/public-docs.md).

## Test configuration (`public/test-config.md`)

Run this section **only** when a skill needs to handle tests (`go-ut`, `go-e2e`, or when the user explicitly asks `go-setup` to configure tests):

1. Check if `~/.just-do-it/{project}/public/test-config.md` already exists.
   - **Exists:** read and use it directly. Do not re-prompt.
   - **Missing:** inspect the repository (`package.json`, runner configs, test folders) to detect candidate unit and E2E setups, then **ask and confirm with the user**:
     - **Unit test:** framework/runner (or `none`), config/spec path pattern, and focused run command.
     - **E2E test:** framework/runner (or `none`), E2E folder path, base URL if documented, and focused run command.
2. Save the confirmed answers to `~/.just-do-it/{project}/public/test-config.md` per [public-docs.md](references/public-docs.md#test-configmd).

## Layout and shared references

- Directory structure and file ownership: [storage.md](references/storage.md)
- Concise document style rules: [written-docs.md](references/written-docs.md)
- On-demand `public/glossary.md`, `public/adr/`, and `public/test-config.md`: [public-docs.md](references/public-docs.md)
- Human-readable HTML rendering for `dev-view/*.html`: [html-render.md](references/html-render.md)

## Done when

- `~/.just-do-it/{project}/{branch}/agent-view/`, `dev-view/`, and `~/.just-do-it/{project}/public/` exist for a user-confirmed `{project}`.
- If test setup was requested and `public/test-config.md` was missing, it is confirmed with the user and written.
