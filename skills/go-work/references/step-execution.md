# Execute One Step

## Start gate

1. The branch must contain the ticket key, such as `PROJ-123`, unless the user approved an exception or the project has no ticket convention. Otherwise warn and stop.
2. The step must be in approved scope in `agent-view/plan.md` with every `Blocked by` step done in `agent-view/checklist.md`. Stop on overlapping unrelated work; ask when the plan is unclear.
   - For standalone work on an approved plan, [sync the checklist](../../go-plan/references/checklist-format.md#approval) if it still shows pending approval.
3. Check the assigned root, branch and starting SHA against the checkout before editing or testing. For a worker worktree, verify it belongs to the ticket repository. Use the assigned starting SHA for the step diff and the original ticket storage for the plan and prerequisite evidence.
   - Invalidate stale evidence; keep the user's changes.
   - Ask only when drift makes scope ambiguous.
   - Per-step commits: recorded commits must stay ancestors of `HEAD`.

## Step gate

- Complete the assigned step through workflow step 4 of `SKILL.md`. When behavior tests are available and authorized, run the failing spec before editing the behavior and rerun it after the fix. Worktree workers pass the assigned checkout and original ticket storage to test skills and use evidence-only mode. Return red and green evidence, or the named setup check and outcome.
- A failing spec stays in the step's scope: leave bootstrap, configuration, and unrelated specs alone.
- An existing spec that the step's change breaks is in scope: fix the code, and rerun that spec before reporting `Done`.

### Per-step commits

- Plan approval covers each step, its commit, and the `Deletions`.
- When scoped verification passes, commit each approved category and return the ordered SHAs and evidence. Standalone `go-work` records delivery in `agent-view/checklist.md` and `agent-view/CHANGELOG.md`. The coordinator records worktree steps only after integration.
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

- Use the step's verification as commit evidence.
- Use the plan's exact one-line `Commit` message for each approved category unless the user's latest instruction says otherwise.
- Scope changed: propose a new one-line message and get approval first.
- No plan message: `agent-view/commit-format.md` or the project's commit format, else `<type>: <description>`.
- Inspect production and test changes together. Scope each commit to its approved category. In an isolated worktree, stage only that category's files or hunks, inspect the staged diff, then commit. In a shared checkout, use a path-scoped commit only when every change in those paths belongs to that category. Preserve unrelated staging.
- Verify each commit's SHA and diff. A worker returns the SHAs for integration. Standalone execution records them in the checklist and changelog. Never push.
