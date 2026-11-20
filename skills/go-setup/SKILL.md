---
name: go-setup
description: 'Set up and resolve the ~/.just-do-it/{project}/{branch}/ storage directory (agent-view/, dev-view/, and public/). Triggered automatically by any skill when the current branch folder is missing, or called directly to initialize project storage and jdi-config.md.'
---

# Setup Storage

Resolve or initialize `~/.just-do-it/{project}/{branch}/` for the current checkout and branch. Every storage-writing skill resolves its branch directory through this contract before writing.

## Branch slug

1. Run `git branch --show-current`. Encode the branch name as UTF-8 hexadecimal, prefixed with `branch-`; use that as the directory name. This encoding distinguishes every branch name.
2. Detached `HEAD` or non-git directory: ask the user for a short kebab-case task name to use as `{branch}`.

## Resolve or create storage

1. Resolve the project for the current repository first. Reuse a project only when its existing artifacts explicitly identify this repository; otherwise confirm the project with the user. Do not identify a project from a matching branch directory alone.
   - Within that project, reuse the encoded branch directory only when its existing artifacts identify the current repository and exact branch. If identity is missing or conflicting, confirm it before reading or writing task data.
   - For legacy directories with `/` replaced by `-`, reuse the legacy directory only when existing task artifacts identify both the current repository and exact branch. Leave ambiguous legacy data untouched and create the encoded directory instead. Do not move or overwrite legacy data.
2. Once `{project}` is confirmed, check write permission and create:
   - `~/.just-do-it/{project}/public/`
   - `~/.just-do-it/{project}/{branch}/agent-view/`
   - `~/.just-do-it/{project}/{branch}/dev-view/`
3. Do **not** pre-create empty `public/glossary.md`, `public/adr/`, or `public/jdi-config.md` during basic folder setup. Those files are created only when needed per [public-docs.md](references/public-docs.md).

## Project configuration (`public/jdi-config.md`)

Run this section when a skill needs test settings or the user calls `go-setup` directly. Follow [public-docs.md](references/public-docs.md#jdi-configmd).

On every direct `go-setup` call, show all configurable fields and their current values (or `not configured`): retry limit; unit runner, config/spec path pattern, and focused command; E2E runner, folder, base URL, focused command, authentication state, and test data. Ask which fields to update. If the user already specified changes, show the full list, apply the requested changes, and report the result. Preserve all other fields. Confirm newly detected or ambiguous values before saving. A request to view settings alone makes no changes.

1. Check if `~/.just-do-it/{project}/public/jdi-config.md` already exists.
   - **Exists:** read and use it. If the retry limit is missing or invalid, ask the user to confirm it and update the existing file.
   - **Missing:** inspect the repository (`package.json`, runner configs, test folders) to detect candidate unit and E2E setups, then **ask and confirm with the user**:
     - **Unit test:** framework/runner (or `none`), config/spec path pattern, and focused run command.
     - **E2E test:** framework/runner (or `none`), E2E folder path, base URL, focused run command, authentication state, and test data where applicable.
     - **Test retry limit:** a non-negative integer; recommend `1` retry after the initial failed verification run.
2. Save the confirmed answers to `~/.just-do-it/{project}/public/jdi-config.md` per [public-docs.md](references/public-docs.md#jdi-configmd).

## Layout and shared references

- Directory structure and file ownership: [storage.md](references/storage.md)
- Concise document style rules: [written-docs.md](references/written-docs.md)
- On-demand `public/glossary.md`, `public/adr/`, and `public/jdi-config.md`: [public-docs.md](references/public-docs.md)
- Human-readable HTML rendering for `dev-view/*.html`: [html-render.md](references/html-render.md)

## Done when

- `~/.just-do-it/{project}/{branch}/agent-view/`, `dev-view/`, and `~/.just-do-it/{project}/public/` exist for a user-confirmed `{project}`.
- On a direct call, all configurable fields and current values were shown; requested changes were saved or remaining questions reported.
- If required configuration was missing, confirmed settings were written without losing existing values.
