# Agents

The caller that launches a worker chooses its model and effort. `go-review` and `to-test-html` own their workers in either mode.

| Manager job | Tier | Lifecycle |
| --- | --- | --- |
| `go-research` | `fast` | Reuse for new or refreshed requirement sources |
| `go-plan` | `reasoning` | One worker for the grill, plan, and revisions |
| `go-work` | `standard` | One worker per implementation step, reused only for that step's retries |
| `go-e2e` | `standard` | One worker for exploration, authoring, runs and reruns |

## Announce

Before launch, state worker, job, resolved model and effort. Omit effort when the tool has no effort parameter or selectable effort variant. User overrides win when supported.

## Start

1. Inspect the active host tool and model catalog. Request fresh context and pass the selectable model ID with the role's effort when supported. Follow the Antigravity model rules below. On other hosts, if a preferred family is absent, use the closest selectable model for that tier and announce the actual choice. Ask before replacing a model the user explicitly requested.
2. Launch in the coordinator's existing checkout. Send its absolute repository root and current branch with the skill name, absolute `SKILL.md` path, inputs, acceptance criteria, and authorization. Workers verify the root and branch before editing or running tests. Pass no full chat transcript.
3. Use the host's follow-up tool to resume the same worker when needed. A resumed worker keeps its original model and effort.
4. Release completed step workers after verification and close other workers when their job ends or slots are needed. If a reusable worker is gone, restore it from the current inputs and decisions.
5. Keep delegated work in the current checkout and branch. Workers return their in-place edits. Only the coordinator stages and commits approved changes on that branch. If the host requires a separate branch, worktree, or merge for a worker, report the dispatch blocker.

## Host mapping

Map each tier to the active host's model and effort:

| Tier | Claude | Codex | Antigravity (preferred family) |
| --- | --- | --- | --- |
| `fast` | `haiku (low)` | `luna (low)` | `flash (low)` |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `reasoning` | `opus (medium)` | `sol (medium)` | `neon (medium)` |

| Host | Spawn & model | Wait / reuse | Cleanup |
| --- | --- | --- | --- |
| Claude | `general-purpose` in the current checkout (`model`, `effort` if supported). Omit worktree isolation. | `SendMessage` by ID | — |
| Codex | `spawn_agent` with fresh context, `model` and supported effort; or `collaboration.spawn_agent(fork_turns="none", model, reasoning_effort)` | `wait` / `send_input`; or `collaboration.wait_agent` / `collaboration.followup_task` (plain `send_message` does not wake idle workers) | `close_agent` when exposed; otherwise the host's documented completion/cleanup |
| Antigravity | `swarm(action="add", workspace="inherit", model=<selected model ID>)`. Resolve the model and effort variant from `swarm(action="models", all=true)` when supported. | Workers report to `@coordinator`. When the board tools become available, use `swarm_wait` and follow up by `@name` in `post_message`. | `swarm(action="kill")` after the result and in-place edits are verified |

### Antigravity dispatch

- In Swarm, pass the exact user-selected model and effort, or the configured tier's model and effort. Swarm encodes effort in the selectable model variant. If the variant or `workspace="inherit"` is unavailable, report the blocker. Get approval before changing the model or effort.
- Use `workspace="inherit"` explicitly for every Swarm worker. It shares the checkout. Omit `fork` to start with fresh conversation context. Send the worker's brief and references to any relevant Swarm board posts. Workers verify the repository root and branch before editing. Verify the worker's workspace and model in Swarm status. Keep edits in place on that branch.
- Use legacy `define_subagent` and `invoke_subagent` only for `go-research` when tracker MCP access requires it. Use `Workspace="inherit"`, grant the required tracker access, and scope writes to attachment caching. The legacy research default is `flash_lite`. If a user's requested model or effort cannot be set on that tool, report the blocker. Follow up with `send_message` and clean up via `manage_subagents(Action="kill")`.
