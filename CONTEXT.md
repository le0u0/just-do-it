# Just Do It

Shared terms for this plugin.

## Skills and Flow

| Term | Meaning |
| --- | --- |
| Skill | An independent action, such as `go-review`. `go-*` do work and write directly to `~/.just-do-it/{project}/{branch}/`; `dev-*` drive a method; `to-*` produce developer/QA deliverables or restatements. |
| Flow (`go-flow`) | Stateless pipeline skill that chains `go-setup` → `to-spec` → `to-plan` → plan review when required → approval → `go-work` pipelines → verification → code review → `go-fix`, or a user-selected subset of steps. |
| Setup (`go-setup`) | Resolves `~/.just-do-it/{project}/{branch}/` (`agent-view/`, `dev-view/`, and `public/`). Triggered automatically by any skill when the branch folder is missing; always confirms `{project}` with the user. Also confirms `public/jdi-config.md` on demand when a skill needs to handle tests. |

## Skill structure

| Term | Meaning |
| --- | --- |
| Reference | A file in a skill's `references/`, linked from `SKILL.md`, read for one branch of its workflow. Shared storage and public-doc rules live in `skills/go-setup/references/`. Host dispatch lives in `references/`: `agents.md` plus one file per host under `references/hosts/`. |
| Project references | Rules, project-local skills and comparable code in the repository. Read, never copied. |
| Project-local skill | A skill the active host loads from the repository. Wins over this plugin's defaults. |

## Storage and views

| Term | Meaning |
| --- | --- |
| Ticket | A task ID such as `PROJ-123`. Requirements come from supplied or retrieved context, never the key alone. |
| Project folder | `~/.just-do-it/{project}/`: confirmed with the user by `go-setup`. Holds `public/` and branch folders. |
| `public/` | `~/.just-do-it/{project}/public/`: shared across branches of `{project}`. Holds on-demand `standards.md`, `glossary.md` (unknown domain terms asked and saved), `adr/` (`NNN-short-title.md` for hard-to-reverse decisions), and `jdi-config.md` (confirmed UT/E2E runner, paths, and commands when handling tests). |
| Branch folder | `~/.just-do-it/{project}/{branch}/` (encoded exact Git branch; see storage resolver): split into `agent-view/` and `dev-view/`. |
| `agent-view/` | Working markdown artifacts consumed across agent steps: `spec.md`, `attachments/{ticket}/`, `plan.md`, `approval.json`, `checklist.md`, `plan-review.md`, `commit-format.md`, `diagnose.md`, `CHANGELOG.md`, `ut.md`, `e2e.md`, and `review.md` (which references `ut.md` and `e2e.md`). |
| `dev-view/` | Developer and QA deliverables (`.html` by default unless `.md` is requested, except `pr.md` and `handoff.md` which are always `.md`): `spec.html` (with inline attachment images), `plan.html` (visual plan + statechart + attachment images for user approval), `plan-review.html`, `review.html` (interactive findings + UT/E2E pass/fail status), `testing-guide.html`, `pr.md`, `handoff.md`. |
| Pipeline | Approved, ordered steps with one owner and declared prerequisites. Single runs inline; multiple pipelines can use isolated workers. |
| Step | A reviewable milestone in an approved plan. Uncommitted unless the plan or user approves a commit. |
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
| Plan review | Fresh read-only reviewer checks a specific draft and supporting evidence before approval. |
| Formal code review | `go-review`'s hunters and verifier applying the project's review skill (else standards and confirmed goal/plan) and review checks, writing `agent-view/review.md` and `dev-view/review.html`. |
| Fetch | `go-review`'s Standard worker that gathers baseline, diff, checkout snapshot, and rule evidence. |
| Tier | Standard uses two hunters and one verifier. Deep adds a security hunter. Select from the reviewed diff and risky paths. |
| Round | Counts full reviews of the same target. A fourth full review requires explicit authorization. |
| Pre-existing | A real bug the change did not introduce or expose. Listed under `PRE-EXISTING`, not counted, not sent to `go-fix` unless the user asks. |
| Review baseline | Start for a full review: confirmed baseline, previously saved `Reviewed from`, or evidenced Git parent. An eligible direct re-review compares from the prior `Reviewed to` commit. |
