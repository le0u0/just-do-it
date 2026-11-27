# Cursor

Map each tier to Cursor's model and effort:

| Tier | Model |
| --- | --- |
| `standard` | `grok (high)` |
| `deep` | `grok (xhigh)` |

| Spawn & model | Collect results | Cleanup |
| --- | --- | --- |
| Task tool, `generalPurpose`, fresh context. `model` is the current Grok catalog ID at `effort=high` or `effort=xhigh`. Assigned root in the prompt. | Foreground Task result. Resume an implementation worker by its returned agent ID. | — |

## Dispatch

- Launch a foreground subagent with the Task tool. Set `subagent_type` to `generalPurpose` when the tool asks for a type. Omit `resume` so the worker starts fresh. Keep one implementation worker by passing its returned agent ID on later steps of that pipeline. Do not resume review or Brainstorm workers.
- Pass `model` as the current catalog ID for the tier. Do not pass `inherit` and do not pin a version. Standard is Grok at `effort=high`. Deep is Grok at `effort=xhigh`. A user-requested model and effort replaces the tier when it is selectable.
- If that model, its effort, or fresh context cannot be set, report the blocker. Ask before substituting.
- Put the assigned absolute root and branch in the prompt. For an implementation pipeline, request an isolated subagent worktree. The worker verifies that root and branch before edits or tests.
- Wait for the foreground result before dependent work. No separate cleanup call.
