# Agents

The caller that launches a worker chooses its model and effort. `go-review` and `to-test-doc` also manage their own workers using this mapping.

| Flow job | Tier | Assignment |
| --- | --- | --- |
| `to-spec` | `standard` | Seven Goldfish after Brainstorm confirmation; delegated lookup only when necessary |
| `go-review plan` | `deep` | Fresh plan reviewer; one additional specialist when needed |
| `go-work` | `standard` | Assigned implementation pipeline |
| `go-e2e` | `standard` | Assigned E2E work |

## Announce

Before launch, state worker, job, resolved model and effort. Omit effort when the tool has no effort parameter or selectable effort variant. User overrides win when supported.

## Start

1. Inspect the active host tool and model catalog. Request fresh context and pass the selectable model ID with the role's effort when supported. Resolve the selectable model in the named tier and report when it or fresh context is unavailable. Announce the actual choice. Ask before replacing a model the user explicitly requested. On Antigravity, also follow the dispatch rules below.
2. For delegated implementation, use the pipeline worktree assigned by [scheduling](scheduling.md#approved-pipelines). Other roles use the ticket checkout. Send the assigned absolute root and branch, the resolved storage path of the original ticket branch, skill path, inputs, acceptance criteria, and authorization. Workers verify the assigned root and branch before editing or running tests. Pass no full chat transcript.
3. Start fresh context for independent review or Brainstorm roles. For verification or fixes, give the assigned checkout, previous results and retry count. Keep an implementation worker across all steps of its assigned pipeline.
4. Collect the result before releasing the worker. Keep implementation worktrees available until their changes are integrated.
5. For a pipeline worktree, use the host's supported workspace selector or pass the assigned root as the working directory for all repository commands. If the worker cannot use or verify that worktree, report the dispatch blocker.

## Host mapping

Map each tier to the active host's model and effort:

| Tier | Claude | Codex | Antigravity (preferred family) |
| --- | --- | --- | --- |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `deep` | `opus (medium)` | `sol (medium)` | `neon (medium)` |

| Host | Spawn & model | Collect results | Cleanup |
| --- | --- | --- | --- |
| Claude | `general-purpose` (`model`, `effort` if supported), with the assigned root in the prompt | `SendMessage` by ID | — |
| Codex | `spawn_agent` with fresh context, `model` and supported effort; or `collaboration.spawn_agent(fork_turns="none", model, reasoning_effort)` | `wait` / `send_input`; or `collaboration.wait_agent` / `collaboration.followup_task` (plain `send_message` does not wake idle workers) | `close_agent` when exposed; otherwise the host's documented completion/cleanup |
| Antigravity | `swarm(action="add", workspace=<assigned workspace>, model=<selected model ID>)`. Resolve supported workspace options and model variants from the host. | Workers report to `@coordinator`. When the board tools become available, use `swarm_wait` and follow up by `@name` in `post_message`. | `swarm(action="kill")` after the result is verified |

### Antigravity dispatch

- In Swarm, pass the exact user-selected model and effort, or the configured tier's model and effort, using the requested tier. Swarm encodes effort in the selectable model variant. If no applicable variant is available or `workspace="inherit"` is unavailable, report the blocker. Get approval before changing a user-selected model or effort.
- Use `workspace="inherit"` for ticket-checkout roles. For an implementation pipeline, use a supported workspace option that matches the assigned worktree, or run commands from its absolute root when accessible. Omit `fork` for fresh context. Verify the assigned root, branch, and model before accepting work.
- Use legacy `define_subagent` and `invoke_subagent` only for `to-spec` when tracker MCP access requires it. Use `Workspace="inherit"`, grant the required tracker access, and scope writes to `agent-view/spec.md` and `agent-view/attachments/`. Use the Standard Hydrogen model variant. If the lookup tool cannot select it, report the blocker. If a user's requested model or effort cannot be set on that tool, report the blocker. Follow up with `send_message` and clean up via `manage_subagents(Action="kill")`.
