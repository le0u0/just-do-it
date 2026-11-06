# Agent Handling

## Parallel work

- Order jobs by their inputs. Parallelize only read-only work or edits to disjoint files.

## Token budget

- If one command verifies it, verify it yourself; reruns and reads stay in the manager.

## Reuse

- Record each agent's name and ID in `state/jobs.md`; send later work to the same ID with SendMessage.
- Resume the same agent for `go-e2e`: writing and rerunning e2e specs.
- `go-review` re-review: run it again with the previous `review.md`; save its full report over `review.md`. Its agents start fresh each round.
- Start fresh only when no agent for that skill exists on the ticket; one agent per skill, never one per step.
- A resumed agent cannot change model or effort; settle both at the start.
- SendMessage fails: start a fresh agent, point it at the plan, `checklist.md`, `state/jobs.md`.
