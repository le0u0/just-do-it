# Agents

## Who runs what

- Main thread: `go-plan`, `go-work`, `go-fix`.
- General-purpose subagent: `go-triage`, `go-e2e`, `go-review`. The prompt names the skill; `model` and `effort` are set on the call. It starts no agents.
- No skill writes plugin docs; the manager saves what it returns.

| Skill | Model | Effort |
| --- | --- | --- |
| `go-triage` | haiku | low |
| `go-e2e` | sonnet | medium |
| `go-review` | opus | medium |

- The manager writes and runs unit specs per `go-work`; `go-e2e` runs e2e once, before review. Other subagents run no tests.

## Announce

- Before each start, say model, version, effort in the assignment line: `→ e2e: write specs (sonnet 5.5, medium)`.
- A user preference for model or effort applies to that and later jobs of the same skill.

## Start

- `general-purpose` with `model` and `effort` from the table. Never a fork: it copies the whole chat.
- Prompt: skill to call (such as `just-do-it:go-review`), file paths, acceptance criterion, authorization, per [reports.md](reports.md). Never paste the conversation.
- A resumed agent keeps its model and effort; settle both first.
- A one-command job, such as a one-line fix, runs in the main thread.

## Hand-off between skills

- A skill needing one it cannot run (`go-work` needing `go-e2e`): return `Open` to the manager.
- Called directly without the manager: run that skill yourself.
