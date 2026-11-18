# Agents

The caller that launches an agent chooses its model and effort. `go-review` and `to-test-html` own their workers whether manager mode is on or off.

## Who runs what

- Main thread: `go-plan`, `go-work`, `go-fix`, `go-review`. `go-review` starts its own agents with the models its skill sets.
- General-purpose subagent: `go-triage`, `go-e2e`. The prompt names the skill; the host's model and effort (if supported) from `Host mapping` are set on the call. It starts no agents. Use `go-triage` (`Fetch` mode, `fast` tier) for any read-only fetch, git diff/compare, baseline check, code search, or folder scan — both for the main thread and for other subagents (pass the fetched facts in their handoff).

| Skill | Tier |
| --- | --- |
| `go-triage` | `fast` |
| `go-e2e` | `standard` |

- The manager writes and runs unit specs per `go-work`; `go-e2e` runs e2e once, before review. Other subagents run no tests.

## Announce

- Before each start, emit the assignment line with resolved model and effort (if supported): `→ <agent> (<model>, <effort>): <job>` (or `→ <agent> (<model>): <job>` when effort is unsupported).
- A user preference for model or effort applies to that and later jobs of the same skill.

## Start

- Spawn via the host's subagent tool per [Host mapping](#host-mapping). Never a fork: it copies the whole chat.
- Inspect the exposed tool schema and request fresh context. A required agent unavailable or launch failed: report blocked and stop; never execute its role in the main thread. Full-chat forks do not satisfy this requirement.
- Prompt: skill name and absolute `SKILL.md` path, file paths, acceptance criterion, authorization, per [reports.md](reports.md). Resolve the skill from the active host's catalog; read its file when the host has no skill-call tool. Never paste the conversation.
- A resumed agent keeps its model and effort; settle both first.
- Resolve each mapped model family from the active host's catalog at dispatch, preferring its current/default release in that family. Pass the selectable model ID, not an invented alias. User overrides win; unavailable model or effort blocks dispatch until resolved.
- Wait for results; use the host's follow-up tool to start another turn on an idle worker.
- A one-command job, such as a one-line fix, runs in the main thread.
- Release finished workers before dependent jobs. Batch parallel roles when slots are limited; preserve every role.
- Reuse `go-triage` and `go-e2e` workers across the whole ticket/session (one worker per skill — e.g. `triage`, `e2e` — never kill after one job or split into `e2e-write` / `e2e-run`). Only kill when the ticket is done or capacity requires releasing slots. A closed worker is replaced with a fresh one reading the handoff paths.
- Subagents inherit sandbox and tool permissions. Report blocked actions to the caller; instructions do not grant filesystem access.

## Host mapping

Map each tier to the active host's model and effort:

| Tier | Claude | Codex | Antigravity (`swarm`) |
| --- | --- | --- | --- |
| `fast` | `haiku (low)` | `luna (low)` | `flash_lite` (`invoke_subagent`) |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `reasoning` | `opus (medium)` | `sol (medium)` | `argon (medium)` |

| Host | Spawn & model | Wait / reuse | Cleanup |
| --- | --- | --- | --- |
| Claude | `general-purpose` (`model`, `effort` if supported) | `SendMessage` by ID | — |
| Codex | `spawn_agent` with fresh context, `model` and supported effort; or `collaboration.spawn_agent(fork_turns="none", model, reasoning_effort)` | `wait` / `send_input`; or `collaboration.wait_agent` / `collaboration.followup_task` (plain `send_message` does not wake idle workers) | `close_agent` when exposed; otherwise the host's documented completion/cleanup |
| Antigravity | Always use one reusable `invoke_subagent` worker with `Model: flash_lite` for `go-triage` (never `swarm`, never kill between jobs): `define_subagent(Name="go-triage", EnableMCPTools=true, EnableWriteTools=true)` with strict read-only prompt so one worker handles both MCP tickets and read-only `git`/`scan` commands (or `TypeName: research` if no MCP is needed). For `go-e2e` / `go-review` workers, `swarm(action="add")` (`model` from `swarm(action="models", all=true)`; effort in `model`). | Reactive wakeup on reply; follow up via `send_message` (`invoke_subagent`) or `@<name>` (`swarm`) | Only at ticket end (or slot pressure): `manage_subagents(Action="kill")` / `swarm(action="kill")` |
