# Agents

## Who runs what

- Main thread (manager): `go-plan`, `go-work`, `go-fix`.
- General-purpose subagent: `go-triage`, `go-e2e`, `go-review`.
  - The prompt names the skill; `model` and `effort` are set on the call.
  - A subagent does its job with that skill and starts no agents.
- No skill writes plugin docs: each returns its result in the reply; the manager saves it.

| Skill | Model | Effort |
| --- | --- | --- |
| `go-triage` | haiku | low |
| `go-e2e` | sonnet | medium |
| `go-review` | opus | medium |

## Tests

- The manager writes and runs unit specs per `go-work`: in its own steps, for a review, for the user's request.
- `go-e2e` runs e2e specs once, before review.
- The other subagents run no tests.

## Announce

- Before each start, say model, version, effort in the one-line assignment, such as `→ e2e: write specs (sonnet 5.5, medium)`.
- User states a model or effort preference: use it for that job and later jobs of the same skill.
- There are no variants to ask about.

## Start

- Start `general-purpose` with `model` and `effort` from the table. Never start a fork: a fork copies the whole chat.
- The prompt holds: the skill to call (such as `just-do-it:go-review`), file paths, acceptance criterion, authorization, per [reports.md](reports.md). Never paste or summarise the conversation with the user.
- A resumed agent keeps its model and effort; settle both before starting.
- A small job finishable with one command or read, such as a one-line fix, runs in the main thread with no subagent.

## Hand-off between skills

- A skill needs a skill it cannot run itself, such as `go-work` needing an e2e run from `go-e2e`: return the request to the manager as `Open`.
- Called directly without the manager: run that skill yourself.
