# Antigravity

Map each tier to Antigravity's preferred model family and effort:

| Tier | Model |
| --- | --- |
| `standard` | `hydrogen (medium)` |
| `deep` | `neon (medium)` |

| Spawn & model | Collect results | Cleanup |
| --- | --- | --- |
| `swarm(action="add", workspace=<assigned workspace>, model=<selected model ID>)`. Resolve supported workspace options and model variants from the host. | Workers report to `@coordinator`. When the board tools become available, use `swarm_wait` and follow up by `@name` in `post_message`. | `swarm(action="kill")` after the result is verified |

## Dispatch

- In Swarm, pass the exact user-selected model and effort, or the configured tier's model and effort, using the requested tier. Swarm encodes effort in the selectable model variant. If no applicable variant is available or `workspace="inherit"` is unavailable, report the blocker. Get approval before changing a user-selected model or effort.
- Use `workspace="inherit"` for ticket-checkout roles. For an implementation pipeline, use a supported workspace option that matches the assigned worktree, or run commands from its absolute root when accessible. Omit `fork` for fresh context. Verify the assigned root, branch, and model before accepting work.
- Fetch uses Swarm like the other review roles.
- Use legacy `define_subagent` and `invoke_subagent` only for `to-spec` when tracker MCP access requires it. Use `Workspace="inherit"`, grant the required tracker access, and scope writes to `agent-view/spec.md` and `agent-view/attachments/`. Use the Standard Hydrogen model variant. If the lookup tool cannot select it, report the blocker. If a user's requested model or effort cannot be set on that tool, report the blocker. Follow up with `send_message` and clean up via `manage_subagents(Action="kill")`.
