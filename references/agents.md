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

1. Inspect the active host tool and model catalog. Request fresh context and pass the selectable model ID with the role's effort when supported. Resolve the selectable model in the named tier and report when it or fresh context is unavailable. Announce the actual choice. Ask before replacing a model the user explicitly requested. Then follow only the active host file in [Host mapping](#host-mapping).
2. For delegated implementation, use the pipeline worktree assigned by [scheduling](../skills/go-flow/references/scheduling.md#approved-pipelines). Other roles use the ticket checkout. Send the assigned absolute root and branch, the resolved storage path of the original ticket branch, skill path, inputs, acceptance criteria, and authorization. Workers verify the assigned root and branch before editing or running tests. Pass no full chat transcript.
3. Start fresh context for independent review or Brainstorm roles. For verification or fixes, give the assigned checkout, previous results and retry count. Keep an implementation worker across all steps of its assigned pipeline.
4. Collect the result before releasing the worker. Keep implementation worktrees available until their changes are integrated.
5. For a pipeline worktree, use the host's supported workspace selector or pass the assigned root as the working directory for all repository commands. If the worker cannot use or verify that worktree, report the dispatch blocker.

## Host mapping

Match the tools in this session to one host. Read that file and no other file in `hosts/`.

| Active host | Tools in this session | Read |
| --- | --- | --- |
| Claude | Agent tool with separate `model` and `effort` | [claude.md](hosts/claude.md) |
| Codex | `spawn_agent` or `collaboration.spawn_agent` | [codex.md](hosts/codex.md) |
| Antigravity | `swarm` or `invoke_subagent` | [agy.md](hosts/agy.md) |
| Cursor | Task tool with `subagent_type` | [cursor.md](hosts/cursor.md) |
