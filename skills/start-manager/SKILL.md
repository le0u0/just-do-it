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
- Assign each job to a subagent per [agents.md](references/agents.md), which sets model and effort per skill.
  - Subagents: triage, e2e specs, review.
  - Main thread (you): `go-plan`, `go-work`, `go-fix`.
- Skills write no plugin docs; each returns its result in the reply.
  - You alone save `plan.md`, `checklist.md`, `review.md`, `triage.md`, `state/diagnose.md`, per [storage.md](references/storage.md) and [written-docs.md](references/written-docs.md).
- `to-pr`, `to-test-md`, `to-test-html`, `to-charsiu` are user-invoked: never run or mention them.
- Honor the user's chosen model, effort, active approvals, repository rules.
- Without subagents, say the manager workflow cannot run in this host.

## Authorization

- Routing authorizes nothing by itself.
- Tests, resets, commits, pushes, external writes, broader files each need the user's request or an approved plan.
- Approving a plan whose `Delivery` is per-step commits authorizes each step's commit and the file deletions the plan lists.

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

1. Pasted link, ticket or not:
   - Branch has no project yet: ask the user the project per [storage.md](references/storage.md).
   - Assign `go-triage` first; save its brief as `triage.md` before any planning.
2. Run `go-plan` yourself in the main thread.
   - It grills the user, then returns the plan and checklist. Save as `plan.md` and `checklist.md`.
   - Never hand it to a subagent: it cannot ask the user.
   - Stop for plan approval.
3. Run `go-work` yourself on the approved plan, passing the plan text, step by step, each step ending in its commit.
   - After each step, record its `Done` line in `checklist.md`.
   - Continue until the plan's `Goal` holds or `go-work` reports a stop condition; ask the user then.
4. Final validation or review still fails after the fixes: stop and ask the user.
5. `go-work` reports `Open: run e2e`:
   - Assign `go-e2e` once to write and run exactly the specs the plan's `E2E` line names, per [tests.md](references/tests.md).
   - Fix a failure yourself with `go-work`.
6. `go-work` reports `Open: ready for review`, or the e2e run passes:
   - Send baseline, scope, and the previous `review.md` (when one exists) to `go-review`.
   - Save its report as `review.md`.
   - Collect test results per [tests.md](references/tests.md); write them into `Tests`.
   - Only `go-review` reviews; no other skill reviews its own work.
7. A review ends at `review.md` and its short report.
   - Run `go-fix` only for findings the user selects, before anything else, passing the review text. A saved review approves no fixes.
   - Record its numbered dispositions in `review.md` and `checklist.md`.
8. Review approved and ticket done: tell the user; they run `to-pr` and the `to-test-*` skills themselves.

- Reuse agents, order parallel work, judge step weight per [reuse.md](references/reuse.md).

## Assign and verify

1. Resolve repository, branch, objective, requirement source, branch folder per [storage.md](references/storage.md), review path, next authorized job. Ask only when ambiguity blocks a safe assignment.
2. Write one checkable acceptance criterion per requested outcome; assign it per [reports.md](references/reports.md).
   - Put in each dispatch prompt: the report contract, the commit format, an attachments directory (in the branch folder).
   - Save what a skill returns: `plan.md`, `checklist.md`, `triage.md`, `state/diagnose.md`, `commit-format.md`, and the glossary and ADRs from `go-plan`'s `Decisions`.
3. Verify each criterion yourself; an agent's "done" is a claim.
   - Check `git diff --stat`, changed hunks for the criteria, that named artifacts exist, that each reported test command selects the right scope and has an exit code.
   - Rerun a unit test only when its evidence is missing or contradicts the diff, and tests were authorized.
   - Ask before rerunning e2e tests or any reset.
   - Send gaps back to the same agent.
4. With a branch folder, append each subagent job to `state/jobs.md` (not jobs you run yourself), per [written-docs.md](references/written-docs.md), at most six lines per job:

   ```markdown
   ### 3. e2e specs — e2e — done

   - pass: tab hidden when flag off
   - fail: share dialog guard missing
   - <sub>Evidence: `git diff --stat`, `toolbar.test` exit 0<br>Agent ID: a1b2c3</sub>
   ```

   - Each criterion: one line, `pass`, `fail`, or `unchecked`, then the criterion.
   - Evidence and agent ID go in `<sub>`.

Done when every criterion is `pass`, or `fail`/`unchecked` with the user told why.

## Report

- On assigning, one line: `→ <agent>: <job>`.
- After a job, at most three lines:
  1. `<job>: done | failed | blocked. <the one thing that matters>.`
  2. What needs the user.
  3. Path of the doc the user should read, if any.
- At an approval gate, end with one question, such as `Approve step 2?`.
- Observations outside the job (same issue in other files) go to `state/jobs.md`.
- During an open discussion: job line first, then `Back to: <open topic>`; continue the discussion.
  - Hold questions the result raises until the current point closes.
  - Raise a failure or blocker at once only when it changes the current point.
- Name only files the user reads: `plan.md`, `checklist.md`, `review.md`. Full absolute path, one per line.
- Keep chat free of tables, evidence dumps, restated plans.
