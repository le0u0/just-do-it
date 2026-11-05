# start-manager

Turns the session into a manager that runs the whole ticket flow. You call it with `/start-manager on`; the model never starts it.

## DO IT

- Runs `go-plan`, `go-work` and `go-fix` itself in the main thread.
- Sends `go-triage`, `go-e2e` and `go-review` to subagents, and announces each model and effort.
- Saves every plugin doc the skills return: `plan.md`, `checklist.md`, `review.md`, `triage.md`, `state/diagnose.md`, `state/jobs.md`.
- Checks each result itself: diff, artifacts, and test exit codes.
- Never runs or mentions `to-pr`, `to-test-md`, `to-test-html` or `to-charsiu`.
- Never commits, pushes or resets unless you or an approved plan said so.

## USE IT

| Situation | Use |
| --- | --- |
| A ticket from triage to review | `start-manager` |
| One job, such as a plan or a review | that `go-*` skill directly |
| Finished ticket needs a PR or guide | `to-pr`, `to-test-md` yourself |

- `/start-manager off` returns the session to normal.
- Without subagents it says the workflow cannot run.

## WORK IT

- It asks the project once, then triages before planning.
- It stops for plan approval, and only fixes findings you select.
- Replies stay at three lines: job, what needs you, doc path.
- `state/jobs.md` holds each subagent job with evidence and agent ID.
- It ends the ticket by telling you to run the `to-*` skills.

## FIT IT

```text
go-triage -> go-plan -> go-work -> go-e2e -> go-review -> go-fix -> go-review
```

- It saves the output of every step to `~/.just-do-it/{project}/{branch}/`.
- It reuses one subagent per skill for the ticket.
- After approval, you run `to-pr`, `to-test-md`, `to-test-html`.
