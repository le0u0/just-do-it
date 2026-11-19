---
name: go-plan
description: 'Grill one ticket, then write a plan and checklist for approval. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope

- In `justaway`, work in one reasoning subagent. Return each question round to the coordinator, then resume with the user’s answers. Direct use asks the user in the current thread.
- Write no production code or tests. A delegated worker returns the plan, checklist, and decisions privately. The user-facing thread delivers the output per [Output delivery](../justaway/references/storage.md#output-delivery), then asks for plan approval.
- Two phases: grill, then write. Complete `Grill` before `Write`, unless the user asks to skip grilling. User only wants gaps found: stop after the grill.

## Inputs

- Requirements come only from supplied or explicitly retrieved context. Cite supplied ticket links; a key alone says nothing.
- Reuse the research brief supplied by `justaway`. For a direct ticket URL or explicit lookup with no brief, use `go-research` for internal context. Treat the brief as evidence pending scope approval.
- Read the project references per [setup.md](references/setup.md) and the code the ticket likely touches.

## 1. Grill

Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, numbered, most important first.
  - A question that depends on an open one waits.
- Per question: a recommended answer and one line on why it matters. Word it so "yes" accepts.
  - Put the question and the recommendation on separate lines, never in one sentence.
- Find facts yourself in code, docs, and ticket. Ask only decisions.
- Look for: missing or conflicting requirements, unclear criteria, edge and error cases, roles, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - The commit format, when the project has none (see Commit format).
  - A checkable `Goal`.
  - Glossary term clashes and ADR-worthy decisions per [domain-docs.md](references/domain-docs.md).
  - Boundaries, probed with a concrete edge-case scenario.
  - E2E scenario when E2E setup exists and UI or user flows change: read the E2E folder path from the handoff. If missing, locate it directly and return it under `Decisions`. List the folder first without reading spec files, then suggest concrete scenario(s) and confirm with the user before writing the plan.
- Done when the frontier is empty and the user confirms shared understanding. Then write if asked to plan or assigned the full manager flow. For a grill-only request, stop after the final round.

## Commit format

- Use the project's format (`AGENTS.md`, `CLAUDE.md`, rules, project-local skills), else the caller's.
- Neither: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Return the answer under `Decisions` as a `Commit format` line (one line plus an example) for the caller to save.

## 2. Write

1. Read [plan-format.md](references/plan-format.md). Return the plan, then the checklist per [checklist-format.md](references/checklist-format.md). Record the grill's decisions under `Decisions`.
2. Bug ticket whose diagnosis would clutter the plan: also return a diagnosis per [diagnose-format.md](references/diagnose-format.md).
3. Check unit and e2e setup per [setup.md](references/setup.md). Record `none: no setup` when there is no setup and adding it is outside scope.
4. Make each step concrete enough for `go-work` to run without new design decisions: owned source and test files, dependencies including shared state, public test seams, test authorization, one-line commit message, and delivery mode.
5. List every file a step deletes under `Deletions`; plan approval covers the listed scope and its deletions.
6. User changes the requirement: revise `Goal`, steps, and `Deletions`, return the whole plan again.
7. New term or hard-to-reverse decision: ask the user; propose it per [domain-docs.md](references/domain-docs.md) only after they confirm.
8. Return the plan and checklist with decisions and any diagnosis. For direct use, deliver them before asking for approval.

## Done when

- Every behavior acceptance criterion maps to a step with a failing test named (or `none: no setup`). Each shared setup step has a focused verification check.
- Every step has a `Commit` line.
- The `Goal` is confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
