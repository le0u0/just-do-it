# Agent Handling

## Parallel work

Split cross-agent requests into jobs ordered by their inputs. Parallelize only read-only work or edits to disjoint files.

## Spec volume

`developer` writes the specs of its steps. When one job needs more than 10 specs, split the work by spec file into groups of at most 10 and start one extra `developer` per group, in parallel, each on disjoint files: 100 specs, 10 developers. Hand each group only its files and the path of `state/context.md`. Then the developers each run their own specs.

## Token budget

Every agent costs tokens, and a started agent can pull in far more context than its job needs. Keep the harness small:

- Start a general-purpose agent per [agents.md](agents.md); never as a fork of the main thread, which copies its whole context.
- Hand off per [reports.md](reports.md): paths and criteria, nothing pasted.
- Reuse the ticket's agent over starting a new one. Extra `developer`s only for spec volume.
- Every agent follows the context cache in [project-references.md](project-references.md), so a later agent reads `state/context.md` instead of searching again.
- Before starting an agent, ask whether you can verify it yourself with one command. Rerun checks and reads stay in the manager.

## Reuse

Agents stay alive for the ticket. Record each agent's name and ID from its start result in `state/jobs.md`, and send all later work to the same ID with SendMessage, so it keeps its context. Resume the same agent for:

- `developer`: the plan, follow-ups, gaps you found, review fixes. A failure goes to the developer that did the work.
- `e2e-tester`: writing and rerunning e2e specs.
- `reviewer`: re-review of the same branch, which updates `review.md` in place.

Start a fresh agent only when no agent of that role exists on this ticket, never one per plan step. A resumed agent cannot change its model or effort, so settle both at the start, per [agents.md](agents.md).

A ticket holds one agent per role; send each step to it.

When SendMessage to a recorded ID fails, start a fresh agent and point it at the plan, `checklist.md`, and `state/jobs.md`.
