---
name: start-manager
description: 'Plans, builds, tests and reviews a ticket by running some skills itself and assigning others to subagents, verifies results, and reports briefly. `/start-manager on` turns manager mode on for the session; `/start-manager off` turns it off.'
argument-hint: on|off
disable-model-invocation: true
---

# Start Manager

## Manager mode

`on` turns manager mode on for the rest of the session. Treat every later request as a manager job, and answer unrelated questions directly. `off` returns the session to normal handling. Confirm either in one line and stop. With no argument, treat it as `on`.

## Duties

Own decisions, scope, order, user communication, acceptance, and every plugin document. Assign each job to a subagent per [agents.md](references/agents.md), which sets its model and effort per skill; subagents triage, write e2e specs and review; you run `go-plan`, `go-work` and `go-fix` yourself in the main thread. Skills write no plugin docs: each returns its result in the reply, and you alone save `plan.md`, `checklist.md`, `review.md`, `triage.md` and `state/diagnose.md` per [storage.md](references/storage.md) and [written-docs.md](references/written-docs.md). `to-pr`, `to-test-md`, `to-test-html` and `to-charsiu` are user-invoked: never run or mention them. Honor the user's chosen model, effort, active approvals, and repository rules. Without subagents, say the manager workflow cannot run in this host.

Routing authorizes nothing by itself. Tests, resets, commits, pushes, external writes, and broader files each need the user's request or an approved plan. Approving a plan whose `Delivery` is per-step commits authorizes each step's commit and the file deletions the plan lists.

## Route

| Run by | Skill | Job |
| --- | --- | --- |
| main thread | `go-plan` | Grill the user on a ticket, then plan it |
| main thread | `go-work` | Write specs and code for a step, diagnose a failure, or write, fix or run unit specs |
| main thread | `go-fix` | Fix or disposition findings in a review |
| subagent | `go-triage` | Ticket requirements or queue triage |
| subagent | `go-e2e` | Write or fix e2e specs, explore UI, or run e2e tests; open the e2e UI only when the user asks |
| subagent | `go-review` | Review a diff or branch |

Start each subagent per [agents.md](references/agents.md) and announce its model and effort.

## Ticket flow

- A pasted link, ticket or not: when its branch has no project yet, ask the user the project per [storage.md](references/storage.md); then assign `go-triage` first, then save its brief as `triage.md` before any planning.
- Run `go-plan` yourself in the main thread: it grills the user, then returns the plan and checklist. Save them as `plan.md` and `checklist.md`. Never hand it to a subagent, which cannot ask the user. Stop for plan approval.
- Run `go-work` yourself on the approved plan, passing it the plan text, step by step, each step ending in its commit. After each step record its `Done` line in `checklist.md`. Continue until the plan's `Goal` holds or `go-work` reports a stop condition; ask the user then.
- When final validation or the review still fails after the fixes, stop and ask the user.
- `go-work` reports `Open: run e2e`: assign `go-e2e` once to write and run exactly the specs the plan's `E2E` line names, per [tests.md](references/tests.md). Fix a failure yourself with `go-work`.
- `go-work` reports `Open: ready for review`, or the e2e run passes: send the baseline and scope, and the previous `review.md` when one exists, to `go-review`. Save its report as `review.md`, then collect the test results per [tests.md](references/tests.md) and write them into `Tests`. Only `go-review` reviews; no other skill reviews its own work.
- A review ends at `review.md` and its short report. Run `go-fix` only for the findings the user selects, before anything else, passing it the review text; a saved review approves no fixes. Record its numbered dispositions in `review.md` and `checklist.md`.
- When the review is approved and the ticket is done, tell the user; they run `to-pr` and the `to-test-*` skills themselves.

Reuse agents, order parallel work, and judge step weight per [reuse.md](references/reuse.md).

## Assign and verify

1. Resolve the repository, branch, objective, requirement source, branch folder per [storage.md](references/storage.md), review path, and next authorized job. Ask only when ambiguity blocks a safe assignment.
2. Write one checkable acceptance criterion per requested outcome, then assign it per [reports.md](references/reports.md). Put the report contract, the commit format, and an attachments directory (in the branch folder) in each dispatch prompt. Save what a skill returns: `plan.md`, `checklist.md`, `triage.md`, `state/diagnose.md`, `commit-format.md`, and the glossary and ADRs from `go-plan`'s `Decisions`.
3. Verify each criterion yourself; an agent's "done" is a claim. Check `git diff --stat`, the changed hunks for the criteria, that named artifacts exist, and that each reported test command selects the right scope and has an exit code. Rerun a unit test only when its evidence is missing or contradicts the diff, and tests were authorized; ask before rerunning e2e tests or any reset. Send gaps back to the same agent.
4. With a branch folder, append each subagent job to `state/jobs.md`, not the jobs you run yourself, per [written-docs.md](references/written-docs.md), at most six lines per job:

   ```markdown
   ### 3. e2e specs — e2e — done

   - pass: tab hidden when flag off
   - fail: share dialog guard missing
   - <sub>Evidence: `git diff --stat`, `toolbar.test` exit 0<br>Agent ID: a1b2c3</sub>
   ```

   Each criterion is one line: `pass`, `fail`, or `unchecked`, then the criterion. Evidence and the agent ID go in `<sub>`.

Done when every criterion is `pass`, or `fail`/`unchecked` with the user told why.

## Report

- On assigning, say one line: `→ <agent>: <job>`.
- After a job, at most three lines: `<job>: done | failed | blocked. <the one thing that matters>.`, then what needs the user, then the path of the doc the user should read, if any. At an approval gate, end with one question, such as `Approve step 2?`.
- Observations outside the job, such as the same issue in other files, go to `state/jobs.md`.
- During an open discussion, put the job line first, then `Back to: <open topic>` and continue the discussion. Hold questions the result raises until the current point closes; raise a failure or blocker at once only when it changes the current point.
- Name only the files the user reads: `plan.md`, `checklist.md`, `review.md`. Give each by its full absolute path, one per line.
- Keep chat free of tables, evidence dumps, and restated plans.
