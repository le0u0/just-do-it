# Just Do It

Shared terms for this plugin.

## Manager

| Term | Meaning |
| --- | --- |
| Manager | `start-manager`, the main thread. Assigns triage, e2e and review jobs to a subagent, runs `go-plan`, `go-work` and `go-fix` itself, saves every plugin doc, verifies each result, and decides the next step. |
| Skill | An action, such as `go-review`. Called directly or used by a subagent. `go-*` skills do work and return results in the reply; `dev-*` skills drive a method; `start-*` skills start a mode; `to-*` skills are user-invoked and model-blocked. |

## Skill structure

| Term | Meaning |
| --- | --- |
| Reference | A file in a skill's `references/`, read only for one branch of its workflow, linked directly from `SKILL.md`. Only its own skill reads it; skills call each other by name. |
| Project references | Rules, project-local skills, and comparable code in the repository being changed. Every skill reads them; none copies them. |
| Project-local skill | A skill inside the repository, such as in `.agents/skills/` or `.claude/skills/`. Followed over this plugin's defaults where they conflict. |

## Tickets and tasks

| Term | Meaning |
| --- | --- |
| Ticket | A task ID such as `PROJ-123`. Requirements come from supplied or retrieved context, never the key alone. |
| Project folder | `~/.just-do-it/{project}/`, one per product or codebase, holding `docs/` and its branch folders. |
| Branch folder | `~/.just-do-it/{project}/{branch}/`, with `plan.md`, `checklist.md`, `commit-format.md`, `review.md`, `pr.md`, a testing guide (`.md` and `.html`), and `attachments/`. Plugin files live in its `state/` subfolder. The manager saves what `go-*` skills return; `to-*` skills write their own files. |
| Step | A reviewable milestone in an approved plan. Work stays uncommitted unless the user approves a commit. |
| Test-driven slice | One behavior: one failing test through a public seam, then the minimum code to pass it. |
| Temporary contract | A feature-local stand-in used until a real dependency exists, with a ticket-linked `FIXME` and removal condition. |

## Code

| Term | Meaning |
| --- | --- |
| Test selector contract | A stable selector defined by `go-e2e` and implemented in production by `go-work`. |

## Review

| Term | Meaning |
| --- | --- |
| Self-check | A skill checking its own work before finishing. Not a review. |
| Formal review | `go-review`'s single pass of the project's review skill (else standards and requirements) and review checks. |
| Review baseline | Where the review starts: a user-supplied baseline, else the saved `Reviewed to` SHA, else the parent branch. Never assumed to be the default branch. |
