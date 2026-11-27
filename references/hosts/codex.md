# Codex

Map each tier to Codex's model and effort:

| Tier | Model |
| --- | --- |
| `standard` | `terra (medium)` |
| `deep` | `sol (medium)` |

| Spawn & model | Collect results | Cleanup |
| --- | --- | --- |
| `spawn_agent` with fresh context, `model` and supported effort; or `collaboration.spawn_agent(fork_turns="none", model, reasoning_effort)` | `wait` / `send_input`; or `collaboration.wait_agent` / `collaboration.followup_task` (plain `send_message` does not wake idle workers) | `close_agent` when exposed; otherwise the host's documented completion/cleanup |

Inspect the available native subagent schema and use the fresh-context parameter it exposes. Resolve the selectable model in the named tier. Report when that model, its effort, or fresh context is unavailable. A user-requested model and effort replaces the tier when supported.
