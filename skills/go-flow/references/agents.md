# Agents

The caller that launches a worker chooses its model and effort. `go-review` and `to-test-doc` also manage their own workers using this mapping.

| Flow job | Tier | Assignment |
| --- | --- | --- |
| `to-spec` | `fast` | Requirement lookup |
| `go-plan` | `reasoning` | Current planning round |
| `go-work` | `standard` | Assigned implementation step or fix |
| `go-e2e` | `standard` | Assigned E2E work |

## Announce

Before launch, state worker, job, resolved model and effort. Omit effort when the tool has no effort parameter or selectable effort variant. User overrides win when supported.

## Start

1. Inspect the active host tool and model catalog. Request fresh context and pass the selectable model ID with the role's effort when supported. If the `fast` model is unavailable, use the `standard` model and its effort. For other unavailable preferred families, use the closest selectable model for that tier. Announce the actual choice. Ask before replacing a model the user explicitly requested. On Antigravity, also follow the dispatch rules below.
2. For implementation steps, use the worktree assigned by [scheduling](scheduling.md#parallel-steps). Other roles use the ticket checkout. Send the assigned absolute root and branch, the resolved storage path of the original ticket branch, skill path, inputs, acceptance criteria, and authorization. Workers verify the assigned root and branch before editing or running tests. Pass no full chat transcript.
3. For a new round, fix, or rerun, start a fresh worker with the applicable artifacts and a short handoff. Include confirmed decisions and unanswered questions for planning, or the assigned checkout, previous results, and retry count for verification and fixes.
4. Collect the result before releasing the worker. Keep implementation worktrees available until their changes are integrated.
5. For a worktree step, use the host's supported workspace selector or pass the assigned root as the working directory for all repository commands. If the worker cannot use or verify that worktree, report the dispatch blocker.

## Host mapping

Map each tier to the active host's model and effort:

| Tier | Claude | Codex | Antigravity (preferred family) |
| --- | --- | --- | --- |
| `fast` | `haiku (low)` | `luna (low)` | `hydrogen (low)` |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `reasoning` | `opus (medium)` | `sol (medium)` | `neon (medium)` |

| Host | Spawn & model | Collect results | Cleanup |
| --- | --- | --- | --- |
| Claude | `general-purpose` (`model`, `effort` if supported), with the assigned root in the prompt | `SendMessage` by ID | — |
| Codex | `spawn_agent` with fresh context, `model` and supported effort; or `collaboration.spawn_agent(fork_turns="none", model, reasoning_effort)` | `wait` / `send_input`; or `collaboration.wait_agent` / `collaboration.followup_task` (plain `send_message` does not wake idle workers) | `close_agent` when exposed; otherwise the host's documented completion/cleanup |
| Antigravity | `swarm(action="add", workspace=<assigned workspace>, model=<selected model ID>)`. Resolve supported workspace options and model variants from the host. | Workers report to `@coordinator`. When the board tools become available, use `swarm_wait` and follow up by `@name` in `post_message`. | `swarm(action="kill")` after the result is verified |

### Antigravity dispatch

- In Swarm, pass the exact user-selected model and effort, or the configured tier's model and effort, using the `fast` to `standard` fallback above when needed. Swarm encodes effort in the selectable model variant. If no applicable variant is available or `workspace="inherit"` is unavailable, report the blocker. Get approval before changing a user-selected model or effort.
- Use `workspace="inherit"` for ticket-checkout roles. For an implementation step, use a supported workspace option that matches the assigned worktree, or run commands from its absolute root when accessible. Omit `fork` for fresh context. Verify the assigned root, branch, and model before accepting work.
- Use legacy `define_subagent` and `invoke_subagent` only for `to-spec` when tracker MCP access requires it. Use `Workspace="inherit"`, grant the required tracker access, and scope writes to `agent-view/spec.md` and `agent-view/attachments/`. The legacy research default is `flash_lite`. If a user's requested model or effort cannot be set on that tool, report the blocker. Follow up with `send_message` and clean up via `manage_subagents(Action="kill")`.
