# Execute One Step

## Start gate

1. The branch must contain the ticket key, such as `PROJ-123`, unless the user approved an exception or the project has no ticket convention. Otherwise warn and stop.
2. The step must be in approved scope, and every step it is `Blocked by` must be done. Stop when unrelated work overlaps it; ask when the plan is unclear.
3. Compare the saved repository, branch, baseline, HEAD, and task diff in `checklist.md` with the checkout. Invalidate stale evidence, keep the user's changes as they are, and ask only when drift makes scope ambiguous. In per-step commit mode, recorded commits must remain ancestors of `HEAD`.

## Step gate

Run workflow step 3 of `SKILL.md` for the whole step, until the step's specs pass.

With `Delivery` per-step commits, approving the plan approves each step, its commit, and the deletions in its `Deletions`. When the step's unit specs pass, mark the step done in `checklist.md`, commit per the commit gate, and start the next step without asking. Keep working until the plan's `Goal` holds. On a failing spec, diagnose and try a different fix; never repeat a fix that already failed. Stop and ask the user only when:

- three different fixes for the same failure have failed;
- a step needs a file deletion the plan's `Deletions` does not list, or a change outside the plan;
- the plan is unclear.

On a stop, report the failure and what was tried.

With `Delivery` uncommitted, stop at one approval gate per step and show the specs, the diff, and the passing output. Plan approval never approves a step then, unless the user pre-approved it, such as "all steps are approved".

A failing spec stays within the step's scope: leave bootstrap, configuration, and unrelated specs alone.

When a dependency such as a backend contract is unavailable, get approval for a feature-local temporary contract, leave generated code unchanged, and add one ticket-linked `FIXME` with its removal condition.

## Formatting and handoff

Format each changed file with the project's file-scoped command. When the staged-file workflow would change the index in leave-uncommitted mode, use a file-scoped equivalent or report formatting as pending. Preserve unrelated changes and the user's staging.

Record changed files, evidence, and next action in `checklist.md`. At the gate, print its `## Implementation` section with the current item marked.

## Commit gate

Applies when `Delivery` is per-step commits, or the user asks. Commit each finished step with its plan `Commit` message, exactly, as one line with no body or trailer. No other approval is needed. When the step's scope changed, propose a new one-line message and get approval first. Without a plan message, use the project's commit format, else `<type>: <description>`. Stage only the step's files or hunks; stop if unrelated staged changes would enter. Record the SHA. Never push.
