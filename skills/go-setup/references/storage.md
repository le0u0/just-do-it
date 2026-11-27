# Storage

Task and project documents live outside the repository under `~/.just-do-it/{project}/` (or a user-supplied root directory).

## Directory tree

```text
~/.just-do-it/
  {project}/
    public/                             # shared across branches of {project}
      standards.md                      # user-confirmed practices, created on demand
      glossary.md                       # domain terms, created/updated on demand
      adr/                              # NNN-short-title.md, created/updated on demand
      jdi-config.md                    # UT & E2E runner/path/command, created when handling tests
    {branch}/                           # branch- plus UTF-8 hexadecimal branch name
      agent-view/                       # compact Markdown consumed by agents
        spec.md                     # to-spec
        attachments/{ticket}/           # to-spec cached ticket attachments
        plan.md                         # to-plan
        approval.json                   # exact plan/scope approval before work
        checklist.md                    # to-plan, updated by go-work and go-fix
        commit-format.md                # to-plan
        diagnose.md                     # to-plan, go-work
        CHANGELOG.md                    # go-work, go-fix
        ut.md                           # go-ut test run report
        e2e.md                          # go-e2e test run report
        plan-review.md                  # go-review plan
        review.md                       # go-review (references agent-view/ut.md and agent-view/e2e.md)
      dev-view/                         # human-facing outputs (HTML by default, except pr.md & handoff.md)
        spec.html                   # to-spec (visual brief + inline attachment images)
        plan.html                       # to-plan (visual plan + statechart + attachment images)
        plan-review.html                # human-readable plan review
        review.html                     # go-review (interactive findings + UT/E2E pass/fail badge)
        testing-guide.html              # to-test-doc (default HTML; or testing-guide.md when user prefers .md)
        pr.md                           # to-pr (always .md)
        handoff.md                      # to-handoff (always .md)
```

## Skill ownership

Every skill resolves `~/.just-do-it/{project}/{branch}/` before reading or writing task files, using the repository and exact branch identity and legacy compatibility rules in [`go-setup`](../SKILL.md). Never infer the project from a branch directory name alone.

An implementation worktree worker receives the original ticket's resolved storage path. Use it for inputs and return evidence to the coordinator. The worktree branch is not a separate ticket.

| Skill | Reads from storage (when present) | Writes to storage |
| --- | --- | --- |
| `go-setup` | `~/.just-do-it/{project}/public/jdi-config.md` and existing branch artifacts | Creates `public/`, `agent-view/`, `dev-view/`; writes `public/jdi-config.md` when test setup is requested |
| `to-spec` | `public/glossary.md` | `agent-view/spec.md`, `agent-view/attachments/{ticket}/`, `dev-view/spec.html` |
| `to-plan` | `agent-view/spec.md`, `agent-view/attachments/`, `public/glossary.md`, `public/adr/`, `public/jdi-config.md` | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/commit-format.md`, `agent-view/diagnose.md`, `dev-view/plan.html`, plus on-demand updates to `public/standards.md`, `public/glossary.md` and `public/adr/` |
| `go-work` | `agent-view/approval.json` for planned work, `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/spec.md`, `agent-view/attachments/`, `agent-view/commit-format.md`, `public/glossary.md`, `public/adr/` | Updates `agent-view/checklist.md`, `agent-view/CHANGELOG.md`, `agent-view/diagnose.md`, plus on-demand updates to `public/glossary.md` and `public/adr/` |
| `go-ut` | `public/jdi-config.md` (triggers configuration setup if missing) | `agent-view/ut.md` |
| `go-e2e` | `public/jdi-config.md` (triggers configuration setup if missing), `agent-view/plan.md` | `agent-view/e2e.md` |
| `go-review plan` | `agent-view/plan.md`, matching spec/checklist and applicable project guidance | `agent-view/plan-review.md` and `dev-view/plan-review.html` |
| `go-review code` | `agent-view/plan.md`, `agent-view/spec.md`, `agent-view/review.md`, `agent-view/ut.md`, `agent-view/e2e.md`, `public/glossary.md`, `public/adr/` | `agent-view/review.md` (referencing `ut.md` and `e2e.md`), `dev-view/review.html` |
| `go-fix` | `agent-view/review.md`, `agent-view/plan.md`, `agent-view/checklist.md` | Updates `agent-view/review.md`, `dev-view/review.html`, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |
| `to-pr` | `agent-view/plan.md`, `agent-view/review.md`, `agent-view/ut.md`, `agent-view/e2e.md`, `public/glossary.md` | `dev-view/pr.md` (always `.md`) |
| `to-test-doc` | `agent-view/plan.md`, `agent-view/spec.md`, `agent-view/attachments/`, `public/glossary.md` | `dev-view/testing-guide.html` by default (or `dev-view/testing-guide.md` when user prefers `.md`) |
| `to-handoff` | `agent-view/spec.md`, `agent-view/plan.md`, `public/glossary.md` | `dev-view/handoff.md` (always `.md`) |
| `to-charsiu` | Last message in chat | Chat only unless the user explicitly asks to save |

## Rules

- `dev-view/` defaults to `.html` (`spec.html`, `plan.html`, `plan-review.html`, `review.html`, `testing-guide.html`) unless the user explicitly asks for `.md` or terminal-only output. `dev-view/pr.md` and `dev-view/handoff.md` are always `.md`.
- Check write permission before saving outside writable roots. Plan approval grants no filesystem permission.
- Keep documents outside the repository and plugin cache unless the user explicitly chooses a repository path. Update existing files in place—never create `_2.md` or `_2.html` copies.
- Task `agent-view/CHANGELOG.md` format (following [release-please](https://github.com/googleapis/release-please) SemVer style): start at `0.1.0` for the branch's first commit and bump per commit (`fix:` / `refactor:` → patch `0.1.1`; `feat:` → minor `0.2.0`; `feat!:` / breaking → major `1.0.0`; `git commit --amend` updates the current version entry in place):
  `# Changelog`, `## [<version>] (<YYYY-MM-DD>)`, grouped under `### Features`, `### Bug Fixes`, `### Code Refactoring`, etc., with `* <summary> (<short-sha>)`.
