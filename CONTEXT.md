# Just Do It

Shared terms for this plugin.

## Manager

| Term | Meaning |
| --- | --- |
| Manager | `justaway`, the main thread. Assigns triage, e2e and review to subagents, runs `go-plan`, `go-work` and `go-fix`, saves every plugin doc, verifies results, decides the next step. |
| Skill | An action, such as `go-review`. `go-*` do work and return results in the reply; `dev-*` drive a method; `justaway` starts manager mode; `to-*` are user-invoked and model-blocked. |

## Skill structure

| Term | Meaning |
| --- | --- |
| Reference | A file in a skill's `references/`, linked from `SKILL.md`, read for one branch of its workflow. Only its own skill reads it. |
| Project references | Rules, project-local skills and comparable code in the repository. Read, never copied. |
| Project-local skill | A skill in the repository (`.agents/skills/`, `.claude/skills/`). Wins over this plugin's defaults. |

## Tickets and tasks

| Term | Meaning |
| --- | --- |
| Ticket | A task ID such as `PROJ-123`. Requirements come from supplied or retrieved context, never the key alone. |
| Project folder | `~/.just-do-it/{project}/`: one per product or codebase, with `docs/` and branch folders. |
| Branch folder | `~/.just-do-it/{project}/{branch}/`: `plan.md`, `checklist.md`, `commit-format.md`, `review.md`, `pr.md`, the testing guide (`.md`, `.html`), `attachments/`, and `state/` for plugin files. The manager saves what `go-*` return; `to-*` write their own. |
| Step | A reviewable milestone in an approved plan. Uncommitted unless the user approves a commit. |
| Test-driven slice | One behavior: one failing test through a public seam, then the minimum code to pass it. |
| Temporary contract | A feature-local stand-in until a real dependency exists, with a ticket-linked `FIXME` and removal condition. |

## Code

| Term | Meaning |
| --- | --- |
| Test selector contract | A stable selector defined by `go-e2e`, implemented in production by `go-work`. |

## Review

| Term | Meaning |
| --- | --- |
| Self-check | A skill checking its own work. Not a review. |
| Formal review | `go-review`'s single pass of the project's review skill (else standards and requirements) and review checks. |
| Review baseline | Where review starts: a user-supplied baseline, else the saved `Reviewed to` SHA, else the parent branch. Never the default branch by assumption. |
