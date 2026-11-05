# Agent Handling

## Parallel work

- Split cross-agent requests into jobs ordered by their inputs.
- Parallelize only read-only work or edits to disjoint files.

## Token budget

Every agent costs tokens; a started agent can pull in far more context than its job needs. Keep the harness small:

- Start a general-purpose agent per [agents.md](agents.md); never a fork of the main thread, which copies its whole context.
- Hand off per [reports.md](reports.md): paths and criteria, nothing pasted.
- Reuse the ticket's agent over starting a new one.
- Every agent follows the context cache in [project-references.md](project-references.md), so a later agent reads `state/context.md` instead of searching again.
- Before starting an agent, ask whether you can verify it yourself with one command. Rerun checks and reads stay in the manager.

## Reuse

- Agents stay alive for the ticket.
- Record each agent's name and ID from its start result in `state/jobs.md`.
- Send all later work to the same ID with SendMessage, so it keeps its context.
- Resume the same agent for:
  - `go-e2e`: writing and rerunning e2e specs.
  - `go-review`: re-review of the same branch; pass it the previous `review.md`, save its full report over `review.md`.
- Start a fresh agent only when no agent for that skill exists on this ticket, never one per plan step.
- A resumed agent cannot change model or effort; settle both at the start, per [agents.md](agents.md).
- A ticket holds one agent per skill; send each step to it.
- SendMessage to a recorded ID fails: start a fresh agent and point it at the plan, `checklist.md`, `state/jobs.md`.
