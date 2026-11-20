# Execute One Step

## Start gate

1. The branch must contain the ticket key, such as `PROJ-123`, unless the user approved an exception or the project has no ticket convention. Otherwise warn and stop.
2. The step must be in approved scope in `agent-view/plan.md` with every `Blocked by` step done in `agent-view/checklist.md`. Stop on overlapping unrelated work; ask when the plan is unclear.
3. Compare repository root, branch, baseline, `HEAD`, and task diff from the caller with the checkout. A delegated worker must match the given root and branch before editing or running tests. With parallel workers, check your owned paths and treat other assigned paths as separate work.
   - Invalidate stale evidence; keep the user's changes.
   - Ask only when drift makes scope ambiguous.
   - Per-step commits: recorded commits must stay ancestors of `HEAD`.

## Step gate

- Complete the assigned step through workflow step 4 of `SKILL.md`. When behavior tests are available and authorized, run the failing spec before editing the behavior and rerun it after the fix (use `go-ut` in evidence-only mode for coordinator-assigned steps and its usual report otherwise; `go-e2e` writes `agent-view/e2e.md`). Return red and green evidence. For setup only, return the named check and outcome so dependent steps can unlock.
- A failing spec stays in the step's scope: leave bootstrap, configuration, and unrelated specs alone.
- An existing spec that the step's change breaks is in scope: fix the code, and rerun that spec before reporting `Done`.

### Per-step commits

- Plan approval covers each step, its commit, and the `Deletions`.
- When the step's scoped verification passes, report `Done` (at most 20 words) with its verification evidence. Standalone `go-work` commits per the commit gate and updates `agent-view/checklist.md` and `agent-view/CHANGELOG.md`. In a parallel `go-flow` wave, return the diff and evidence to the flow caller to serialize commits.
- On a failing spec, diagnose and try a different fix; never repeat a failed one.
- Stop and ask only when:
  - three different fixes for one failure have failed;
  - a step needs an unlisted deletion or a change outside the plan;
  - the plan or a domain term is unclear.
- On a stop, report the failure and what was tried as `Open`.

### Uncommitted delivery

- One approval gate per step: show the diff and verification evidence, including specs for a behavior step.
- Plan approval never approves a step, unless pre-approved, such as "all steps are approved".

### Missing dependency

- Such as a backend contract: get approval for a feature-local temporary contract, leave generated code unchanged, add one ticket-linked `FIXME` with its removal condition.

## Formatting and handoff

- Format each changed file with the project's file-scoped command. When the staged-file workflow would change the index in leave-uncommitted mode, use a file-scoped equivalent or report formatting as pending.
- Preserve unrelated changes and the user's staging.
- Report changed files, evidence, and the commit SHA. At the gate, show this step.

## Commit gate

Applies for per-step commits, or when the user asks.

- Use the step's existing verification as commit evidence.
- Use `agent-view/plan.md`'s `Commit` message exactly: one line, no body or trailer unless the user's newest instruction says otherwise. No other approval needed.
- Scope changed: propose a new one-line message and get approval first.
- No plan message: `agent-view/commit-format.md` or the project's commit format, else `<type>: <description>`.
- Stage only the step's files or hunks; stop if unrelated staged changes would enter.
- Before committing, inspect the step's production and spec changes. Use an explicit path-scoped commit (for Git, `git commit --only -m <message> -- <paths>`), adding new paths first if needed. This commits the entire working-tree version of each path, regardless of staged hunks: stop before committing if any path also contains unrelated changes. Verify that the commit contains only the step's changes.
- Record the SHA in `agent-view/checklist.md` and update `agent-view/CHANGELOG.md` under its type heading (`### Features`, `### Bug Fixes`, etc.). Never push.
