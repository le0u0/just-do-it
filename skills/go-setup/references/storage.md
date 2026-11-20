# Storage

Task and project documents live outside the repository under `~/.just-do-it/{project}/` (or a user-supplied root directory).

## Directory tree

```text
~/.just-do-it/
  {project}/
    public/                             # shared across branches of {project}
      glossary.md                       # domain terms, created/updated on demand
      adr/                              # NNN-short-title.md, created/updated on demand
      test-config.md                    # UT & E2E runner/path/command, created when handling tests
    {branch}/                           # git branch with '/' replaced by '-'
      agent-view/
        research.md                     # go-research
        attachments/{ticket}/           # go-research cached ticket attachments
        plan.md                         # go-plan
        checklist.md                    # go-plan, updated by go-work and go-fix
        commit-format.md                # go-plan
        diagnose.md                     # go-plan, go-work
        CHANGELOG.md                    # go-work, go-fix
      dev-view/
        research.html                   # go-research (human-readable brief + inline attachment images)
        plan.html                       # go-plan (human-readable plan + statechart + attachment images)
        review.md                       # go-review (references dev-view/ut.md and dev-view/e2e.md)
        review.html                     # go-review (human-readable interactive review page)
        ut.md                           # go-ut
        e2e.md                          # go-e2e
        pr.md                           # to-pr
        testing-guide.md                # to-test-doc (Markdown option)
        testing-guide.html              # to-test-doc (HTML option)
        handoff.md                      # to-handoff
```

## Skill ownership

Every skill resolves `~/.just-do-it/{project}/{branch}/` before reading or writing task files. If `{branch}` does not exist under `~/.just-do-it/*/{branch}`, trigger [`go-setup`](../SKILL.md) first so `{project}` is confirmed with the user.

| Skill | Reads from storage (when present) | Writes to storage |
| --- | --- | --- |
| `go-setup` | `~/.just-do-it/*/{branch}` | Creates `public/`, `agent-view/`, `dev-view/`; writes `public/test-config.md` when test setup is requested |
| `go-research` | `public/glossary.md` | `agent-view/research.md`, `agent-view/attachments/{ticket}/`, `dev-view/research.html` |
| `go-plan` | `agent-view/research.md`, `agent-view/attachments/`, `public/glossary.md`, `public/adr/`, `public/test-config.md` | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/commit-format.md`, `agent-view/diagnose.md`, `dev-view/plan.html`, plus on-demand updates to `public/glossary.md` and `public/adr/` |
| `go-work` | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/research.md`, `agent-view/attachments/`, `agent-view/commit-format.md`, `public/glossary.md`, `public/adr/` | Updates `agent-view/checklist.md`, `agent-view/CHANGELOG.md`, `agent-view/diagnose.md`, plus on-demand updates to `public/glossary.md` and `public/adr/` |
| `go-ut` | `public/test-config.md` (triggers test-config setup if missing) | `dev-view/ut.md` |
| `go-e2e` | `public/test-config.md` (triggers test-config setup if missing), `agent-view/plan.md` | `dev-view/e2e.md` |
| `go-review` | `agent-view/plan.md`, `agent-view/research.md`, `dev-view/review.md`, `dev-view/ut.md`, `dev-view/e2e.md`, `public/glossary.md`, `public/adr/` | `dev-view/review.md`, `dev-view/review.html` |
| `go-fix` | `dev-view/review.md`, `agent-view/plan.md`, `agent-view/checklist.md` | Updates `dev-view/review.md`, `dev-view/review.html`, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |
| `to-pr` | `agent-view/plan.md`, `dev-view/review.md`, `dev-view/ut.md`, `dev-view/e2e.md`, `public/glossary.md` | `dev-view/pr.md` |
| `to-test-doc` | `agent-view/plan.md`, `agent-view/research.md`, `agent-view/attachments/`, `public/glossary.md` | `dev-view/testing-guide.md` and/or `dev-view/testing-guide.html` |
| `to-handoff` | `agent-view/research.md`, `agent-view/plan.md`, `public/glossary.md` | `dev-view/handoff.md` |
| `to-charsiu` | Last message in chat | Chat only unless the user explicitly asks to save |

## Rules

- Honor an explicit user request to print in the terminal only; otherwise always save to the skill's path under `~/.just-do-it/{project}/{branch}/` and report the saved file path.
- Check write permission before saving outside writable roots. Plan approval grants no filesystem permission.
- Keep documents outside the repository and plugin cache unless the user explicitly chooses a repository path. Update existing files in place—never create `_2.md` copies.
- Task `agent-view/CHANGELOG.md` format (conventional changelog): `# Changelog`, `## [<branch or ticket>] (<YYYY-MM-DD>)`, grouped under `### Features`, `### Bug Fixes`, `### Refactors`, etc., with `* <summary> (<short-sha>)`. Update on every commit or amend (replacing amended SHAs).
