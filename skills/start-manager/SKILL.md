---
name: start-manager
description: 'Plans, builds, tests and reviews a ticket by running some skills itself and assigning others to subagents, verifies results, and reports briefly. `/start-manager on` turns manager mode on for the session; `/start-manager off` turns it off.'
argument-hint: on|off
disable-model-invocation: true
---

# Start Manager

## Manager mode

- `on`: manager mode for the rest of the session. Treat every later request as a manager job; answer unrelated questions directly.
- `off`: return the session to normal handling.
- Confirm either in one line and stop.
- No argument: treat as `on`.

## Duties

- Own decisions, scope, order, user communication, acceptance, and every plugin document.
- Write the specs and code yourself: run `go-plan`, `go-work` and `go-fix` in the main thread. Send `go-triage`, `go-e2e` and `go-review` to subagents.
- Skills return results in the reply. You alone save `plan.md`, `checklist.md`, `review.md`, `triage.md`, `state/diagnose.md`, `commit-format.md`, and the glossary and ADRs from `go-plan`'s `Decisions`, per [storage.md](references/storage.md) and [written-docs.md](references/written-docs.md).
- Without subagents, say the manager workflow cannot run in this host.

## Authorization

- Routing authorizes nothing. Tests, resets, commits, pushes, external writes, broader files each need the user's request or an approved plan. The newest instruction wins: a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests.
- Approving a plan with per-step commits `Delivery` authorizes each step's commit and the deletions the plan lists.

## Route

| Run by | Skill | Job |
| --- | --- | --- |
| main thread | `go-plan` | Grill the user on a ticket, then plan it |
| main thread | `go-work` | Write specs and code for a step, diagnose a failure, or write, fix or run unit specs |
| main thread | `go-fix` | Fix or disposition findings in a review |
| subagent | `go-triage` | Ticket requirements or queue triage |
| subagent | `go-e2e` | Write or fix e2e specs, explore UI, or run e2e tests; open the e2e UI only when the user asks |
| subagent | `go-review` | Review a diff or branch |

- Start each subagent per [agents.md](references/agents.md); announce its model and effort.

## Ticket flow

1. Pasted link: ask the project per [storage.md](references/storage.md) if its branch has none. Assign `go-triage` first; save its brief as `triage.md` before planning.
2. Run `go-plan` in the main thread (a subagent cannot ask the user). Save its plan and checklist as `plan.md`, `checklist.md`. Stop for plan approval.
3. Loop over the approved plan's steps in order, one `go-work` call per step. Pass it the plan text and the step number.
   - Record each step's `Done` line in `checklist.md`, then start the next step.
   - `go-work` reports a stop condition: ask the user.
   - After the last step, confirm the plan's `Goal` holds.
4. Run the final validation per [validation.md](references/validation.md). Still failing after the fixes: stop and ask the user.
5. Plan's `E2E` line is not `none`: assign `go-e2e` once to write and run exactly the plan's `E2E` specs, per [tests.md](references/tests.md). Fix failures with `go-work`.
6. Validation done (and e2e passed when planned): send baseline, scope, and previous `review.md` (if any) to `go-review`.
   - Save its report as `review.md`; write test results into `Tests` per [tests.md](references/tests.md).
   - Only `go-review` reviews.
7. A review ends at `review.md` and its short report. Run `go-fix` only for findings the user selects, passing the review text; a saved review approves no fixes. Record its dispositions in `review.md` and `checklist.md`.
8. Review approved, ticket done: tell the user; they run `to-pr` and `to-test-*`.

- Reuse agents, order parallel work, judge step weight per [reuse.md](references/reuse.md).

## Assign and verify

1. Resolve repository, branch, objective, requirement source, branch folder per [storage.md](references/storage.md), review path, next authorized job. Ask only when ambiguity blocks a safe assignment.
2. Write one checkable criterion per requested outcome; assign it per [reports.md](references/reports.md).
   - Dispatch prompt includes the report contract, commit format, attachments directory (in the branch folder).
3. Verify each criterion yourself; "done" is a claim.
   - Check `git diff --stat`, hunks, named artifacts, and that each test command selects the right scope with an exit code.
   - Rerun a unit test only when evidence is missing or contradicts the diff and tests were authorized; ask before e2e reruns or resets.
   - Send gaps back to the same agent.
4. With a branch folder, append each subagent job (not your own) to `state/jobs.md`, at most six lines, per [written-docs.md](references/written-docs.md):

   ```markdown
   ### 3. e2e specs — go-e2e — done

   - pass: tab hidden when flag off
   - fail: share dialog guard missing
   - <sub>Evidence: `git diff --stat`, `toolbar.test` exit 0<br>Agent ID: a1b2c3</sub>
   ```

   - Each criterion: one line, `pass`, `fail`, or `unchecked`, then the criterion.
   - Evidence and agent ID go in `<sub>`.

Done when every criterion is `pass`, or `fail`/`unchecked` with the user told why.

## Report

- On assigning: `→ <agent>: <job>`.
- After a job, at most three lines: `<job>: done | failed | blocked. <the one thing that matters>.`; what needs the user; path of the doc to read.
- At an approval gate, end with one question, such as `Approve step 2?`.
- Observations outside the job go to `state/jobs.md`.
- Open discussion: job line, then `Back to: <open topic>`. Hold raised questions until the point closes; raise a failure or blocker at once only if it changes the point.
- Name only `plan.md`, `checklist.md`, `review.md`, by full absolute path, one per line.
