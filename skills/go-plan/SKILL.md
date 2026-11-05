---
name: go-plan
description: 'Think through one ticket with the user, then plan it as a plan and checklist for approval, returned in the reply, with no code changes and no files written. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope

- Run in the main thread; talk to the user directly.
- Write no production code, tests, or files. Return the plan and checklist in the reply; the caller saves them. Report as the caller specifies.
- Two phases: grill, then write. User only wants gaps found: stop after the grill.

## Inputs

- Requirements come only from supplied or explicitly retrieved context. Store a supplied ticket link; the key alone says nothing.
- Ticket URL or explicit lookup: run `go-triage` first. Its brief is context, not approved scope.
- Follow `AGENTS.md`, `CLAUDE.md`, and project-local skills. Read the project references per [setup.md](references/setup.md) and the code the ticket likely touches.

## 1. Grill

Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, numbered, most important first.
  - A question that depends on an open one waits.
- Per question: a recommended answer and one line on why it matters. Word it so "yes" accepts.
- Find facts yourself in code, docs, and ticket. Ask only decisions.
- Look for: missing or conflicting requirements, unclear criteria, edge and error cases, roles, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - The commit format, when the project has none (see Commit format).
  - A checkable `Goal`.
  - Glossary term clashes and ADR-worthy decisions per [domain-docs.md](references/domain-docs.md).
  - Boundaries, probed with a concrete edge-case scenario.
- Done when the frontier is empty and the user confirms shared understanding. Then ask them to say plan, unless they already did.

## Commit format

- Use the project's format (`AGENTS.md`, `CLAUDE.md`, rules, project-local skills), else the caller's.
- Neither: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Return the answer under `Decisions` as a `Commit format` line (one line plus an example) for the caller to save.

## 2. Write

1. Read [plan-format.md](references/plan-format.md). Return the plan, then the checklist per [checklist-format.md](references/checklist-format.md). Record the grill's decisions under `Decisions`.
2. Bug ticket whose diagnosis would clutter the plan: also return a diagnosis per [diagnose-format.md](references/diagnose-format.md).
3. Check unit and e2e setup per [setup.md](references/setup.md). No setup: `none: no setup` in the `Test` or `E2E` line.
4. Make each step concrete enough for `go-work` to run without new design decisions: affected files, public test seams (approved with the plan), test authoring and run authorization, the one-line commit message, delivery mode.
5. List every file a step deletes under `Deletions`; deletions are the only thing the plan asks approval for.
6. User changes the requirement: revise `Goal`, steps, and `Deletions`, return the whole plan again.
7. New term or hard-to-reverse decision: ask the user; propose it per [domain-docs.md](references/domain-docs.md) only after they confirm.
8. Show the plan and checklist for approval, and stop.

## Done when

- Every acceptance criterion maps to a step with a failing test named (or `none: no setup`).
- Every step has a `Commit` line.
- The `Goal` is confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
