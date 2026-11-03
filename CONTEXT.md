# Just Do It

Shared terms for this plugin.

## Roles

| Term | Meaning |
| --- | --- |
| Manager | `manager`, the main thread. Assigns triage, e2e and review jobs to a role's subagent, runs `plan`, `develop`, `resolve-review`, `pr` and `testing-guide` itself, verifies each result, and decides the next step. |
| Role | A role such as `e2e-tester` or `reviewer`. A subagent the manager starts with that role's model and effort, holding the skills of the job. Only roles carry role names. |
| Skill | An action, such as `write-e2e`. Called directly or used by a subagent. |
| Tier | A skill's `metadata.tier` (light, standard or advanced), mapped to haiku, sonnet and opus. The manager sets `model` and `effort` per role; the table is in `agents.md`. |

## Skill structure

| Term | Meaning |
| --- | --- |
| Reference | A file in a skill's `references/`, read only for one branch of its workflow, linked directly from `SKILL.md`. |
| Project references | Rules, project-local skills, and comparable code in the repository being changed. Every skill reads them; none copies them. |
| Project-local skill | A skill inside the repository, such as in `.agents/skills/` or `.claude/skills/`. Followed over this plugin's defaults where they conflict. |

## Tickets and tasks

| Term | Meaning |
| --- | --- |
| Ticket | A task ID such as `PROJ-123`. Requirements come from supplied or retrieved context, never the key alone. |
| Project folder | `~/.just-do-it/{project}/`, one per product or codebase, holding `docs/` and its branch folders. |
| Branch folder | `~/.just-do-it/{project}/{branch}/`, with `plan.md`, `checklist.md`, `commit-format.md`, `review.md`, `pr.md`, a testing guide, and `attachments/`. Plugin files live in its `state/` subfolder. |
| Step | A reviewable milestone in an approved plan. Work stays uncommitted unless the user approves a commit. |
| Test-driven slice | One behavior: one failing test through a public seam, then the minimum code to pass it. |
| Temporary contract | A feature-local stand-in used until a real dependency exists, with a ticket-linked `FIXME` and removal condition. |

## Code

| Term | Meaning |
| --- | --- |
| Test selector contract | A stable selector defined by `write-e2e` and implemented in production by `develop`. |

## Review

| Term | Meaning |
| --- | --- |
| Self-check | A skill checking its own work before finishing. Not a review. |
| Formal review | `review`'s single pass of the project's review skill (else standards and requirements) and review checks. |
| Review baseline | Where the review starts: a user-supplied baseline, else the saved `Reviewed to` SHA, else the parent branch. Never assumed to be the default branch. |
