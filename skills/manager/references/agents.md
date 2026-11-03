# Agents

A role is a label the manager gives a job. It has no file: the manager starts a general-purpose subagent, names the skill in the prompt, and sets `model` and `effort` on the call. A subagent does its job with that skill and starts no agents. `plan`, `develop`, `resolve-review`, `pr` and `testing-guide` are not roles: the manager runs them in the main thread.

| Role | Skills | Model | Effort |
| --- | --- | --- | --- |
| `helper` | `triage-ticket` | haiku | low |
| `e2e-tester` | `write-e2e`, `run-e2e` | sonnet | medium |
| `reviewer` | `review` | opus | medium |

The manager writes and runs unit specs per `develop`, in its own steps and for a review or the user's request; `e2e-tester` runs e2e specs once, before review. The others run no tests.

A skill's `metadata.tier` and `effort` apply when it is called alone; inside the manager, this table decides.

## Announce

Before each start, say the model, version and effort in the one-line assignment, such as `→ e2e-tester: write specs (sonnet 5.5, medium)`. When the user states a preference for a model or effort, use it for that job and later jobs of the same role. There are no variants to ask about.

## Start

- Start `general-purpose` with `model` and `effort` from the table. Never start a fork: a fork copies the whole chat.
- The prompt holds the skill to call, such as `just-do-it:develop`, the file paths, the acceptance criterion and the authorization, per [reports.md](reports.md). Never paste or summarise the conversation with the user.
- A resumed agent keeps its model and effort, so settle both before starting.
- A small job you can finish with one command or read, such as a one-line fix, runs in the main thread with no subagent.

## Hand-off between skills

When a skill needs a skill its role lacks, such as `develop` needing an e2e run from `run-e2e`, return the request to the manager as `Open`. Called directly without the manager, run that skill yourself.
