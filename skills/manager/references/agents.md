# Agents

The manager runs `plan`, `develop`, `resolve-review`, `pr` and `testing-guide` itself, in the main thread. It runs `triage-ticket`, `e2e` and `review` in a general-purpose subagent: the prompt names the skill, and `model` and `effort` are set on the call. A subagent does its job with that skill and starts no agents.

Model comes from the skill's `metadata.tier`; effort is the skill's `effort`.

| `metadata.tier` | Model |
| --- | --- |
| light | haiku |
| standard | sonnet |
| advanced | opus |

The manager writes and runs unit specs per `develop`, in its own steps and for a review or the user's request; `e2e` runs e2e specs once, before review. The other subagents run no tests.

## Announce

Before each start, say the model, version and effort in the one-line assignment, such as `→ e2e: write specs (sonnet 5.5, medium)`. When the user states a preference for a model or effort, use it for that job and later jobs of the same skill. There are no variants to ask about.

## Start

- Start `general-purpose` with `model` and `effort` from the skill. Never start a fork: a fork copies the whole chat.
- The prompt holds the skill to call, such as `just-do-it:review`, the file paths, the acceptance criterion and the authorization, per [reports.md](reports.md). Never paste or summarise the conversation with the user.
- A resumed agent keeps its model and effort, so settle both before starting.
- A small job you can finish with one command or read, such as a one-line fix, runs in the main thread with no subagent.

## Hand-off between skills

When a skill needs a skill it cannot run itself, such as `develop` needing an e2e run from `e2e`, return the request to the manager as `Open`. Called directly without the manager, run that skill yourself.
