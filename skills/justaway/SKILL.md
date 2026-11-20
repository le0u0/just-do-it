---
name: justaway
description: 'Coordinate ticket research, planning, parallel test-driven implementation, E2E, and review with subagents. `/justaway on` enables manager mode for the session. `/justaway off` disables it.'
argument-hint: on|off
disable-model-invocation: true
---

# Justaway

## Manager mode

- `on` or no argument: enable for the session. Route work requests below. Answer unrelated questions directly.
- `off`: return to normal handling.
- Confirm the mode in one line and stop.

## Coordinator

- Own scope, user questions and approvals, scheduling, verification, delivery, and Git commits for delegated plan steps.
- Read local files, searches, diffs, and runner evidence directly. Each worker does the routine reads its job needs.
- Use the shared [storage and terminal output rules](references/storage.md#output-delivery). Keep worker results private until delivery. Maintain the plan, checklist, and review in session when the user chooses terminal output.
- Announce and start required workers per [agents.md](references/agents.md). A missing worker or failed launch blocks its role until recovered. Keep unrelated ready jobs moving.

## Authorization

- Follow the latest user instruction. Test runs, resets, commits, pushes, external writes, and scope expansion require authorization from the user or approved plan.
- Plan approval covers its listed steps, deletions, scoped verification and `go-fix` for findings in that scope. Per-step delivery also approves each exact commit message.
- An independent review request authorizes the scoped runs in [tests.md](references/tests.md#review-request), subject to user overrides.

## Routes

| Runs | Skill | Job |
| --- | --- | --- |
| Fast worker | `go-research` | Research a ticket, requirements link, or requested queue. Map relevant source and test paths |
| Reasoning worker | `go-plan` | Grill and plan. Relay questions and answers through the coordinator |
| Standard worker per step | `go-work` | Implement or diagnose one step through `dev-tdd`. For standalone unit work, use its `go-ut` route |
| Standard worker | `go-e2e` | Author, debug or run scoped E2E. Open the E2E UI only when requested |
| Coordinator | `go-review` | Run the existing review workflow with its skill-owned team |
| Coordinator | `go-fix` | Fix or disposition review findings |

Explicitly called skills keep their standalone workflow unless routed as a manager job.

## Ticket flow

1. **Research.** For a ticket key or requirements link, assign `go-research` once with the source and checkout. Refresh live requirements when the user brings a ticket link, including a link already researched. Report any fetch/tool failure or timeout immediately—never silently fall back to local git guesses. Deliver the brief per storage rules and give the planner its path or text. Use supplied requirements directly when no lookup is needed.
2. **Grill and plan.** Send the brief, requirements, attachments, known decisions and E2E path if available to one `go-plan` worker. Relay its numbered questions to the user and resume the same worker with confirmed answers. Every round ends in questions or a draft. Get answers to blocking questions before drafting unless the user asks to skip grilling. Deliver the plan and checklist before asking for approval. When saved, give a short summary of the goal, numbered steps, unit tests, E2E scope or reason for skipping, and deletions.
3. **Build.** Mark the plan approved after the user approves it. Schedule ready steps per [Parallel steps](references/reuse.md#parallel-steps). Assign one `go-work` worker per step (passing `triage.md` and relevant attachments), verify each step's evidence, finish its delivery, record progress in the checklist, and update `CHANGELOG.md` before unlocking dependents. Amend unpushed step commits on fixes rather than adding extra fix commits. Use the same worker for its retries. Relay approval gates and stop conditions to the user. Confirm the plan's goal after the last step.
4. **Validate.** Follow [validation.md](references/validation.md). If a fix is needed, assign a `go-work` step. Ask the user when the worker reports a stop condition.
5. **E2E.** When planned, give `go-e2e` the confirmed scenarios and exact spec scope. Use the plan's E2E folder, or locate it directly if missing. Ask for scenario confirmation only if it is still missing. Run per [tests.md](references/tests.md). Assign `go-work` to fix implementation failures.
6. **Review.** Send the baseline, requirements, scope and any previous report to `go-review`. Fill its `Tests` section. Run `go-fix` on in-scope `TODO` findings under the approved plan. Record dispositions in the report and checklist. Re-review changes with the previous report and refresh authorized stale tests. Mark remaining stale tests as `not run: stale after fixes`.
7. **Deliver.** Save or print the final review per storage rules. Share the outcome, any open findings and validation gaps. The user can run `to-pr` and `to-test-*`.

## Independent review

1. Use supplied requirements, a matching research brief, or a plan. If given a new ticket link, research it first and hand the result to `go-review`. If no requirements exist, ask for them or for approval to proceed with the available scope.
2. Run `go-review` and [scoped review validation](references/tests.md#review-request). Deliver the completed report per storage rules. Apply fixes only on request.

## Assign and verify

1. Resolve checkout, branch, objective, inputs, authorized scope, and any task directory.
2. Send paths (including `triage.md` and attachments when relevant), acceptance criteria, test authorization, and the [report contract](references/reports.md). Include named source and test ownership for implementation steps.
3. Verify results directly using changed paths, hunks, artifacts and scoped test evidence. Rerun tests only within authorization, when evidence is missing or contradictory. Ask before an E2E rerun outside the approved flow or a reset. Return gaps to the assigned worker, and report any worker failure or blocker to the user.
4. With storage enabled, append each worker job to `state/jobs.md` per [written-docs.md](references/written-docs.md). Record status and one `pass`, `fail`, or `unchecked` line per criterion plus evidence and worker ID. Keep records within six lines. Without storage, keep the same evidence in session.
5. Keep routine reports brief. Report the job status, material evidence or blockers, and saved output paths. At approval gates, give the user the context needed to decide.
