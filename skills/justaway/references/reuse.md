# Agent Handling

## Parallel work

- Order jobs by their inputs. Parallelize only read-only work or edits to disjoint files.

## Token budget

- If one command verifies it, verify it yourself; reruns and reads stay in the manager.

## Reuse

- Record each agent's name and ID/roster handle in `state/jobs.md`; send later work to it per [agents.md](agents.md#host-mapping).
- Keep **one** reusable `go-triage` agent and **one** reusable `go-e2e` agent alive for the whole ticket/session (idle/waiting workers cost no tokens). **Do not kill them after a job finishes** — only kill when the ticket/session is done or the host hits slot limits.
- Reuse the same `go-e2e` worker (e.g. `e2e`) for exploring, writing, running, debugging, and rerunning specs — never spawn separate `e2e-write` / `e2e-run` workers.
- Reuse the same `go-triage` worker for all triage and `Fetch` jobs (tickets, diffs, searches, folder scans) via `send_message`.
- `go-review` re-review: run it again with the previous `review.md`; save its full report over `review.md`. Its hunter/verifier agents start fresh each round (and are cleaned up after each review round).
- Start fresh only when no usable agent for that skill exists on the ticket; one agent per skill, never one per step.
- A resumed agent cannot change model or effort; settle both at the start.
- Messaging the existing agent fails (or worker killed): start a fresh agent, point it at the plan, `checklist.md`, `state/jobs.md`.
