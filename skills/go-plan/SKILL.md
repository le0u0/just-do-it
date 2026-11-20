---
name: go-plan
description: 'Grill one ticket, then write agent-view/plan.md and agent-view/checklist.md for approval. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope & Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
- In `go-flow`, work in one reasoning subagent: return each question round to the caller, then resume with the user's answers. Direct use asks the user in the current thread.
- Write no production code or tests. Write planning outputs to `agent-view/plan.md` and `agent-view/checklist.md` (plus `agent-view/commit-format.md` when confirmed and `agent-view/diagnose.md` when needed), then ask for plan approval.
- Two phases: grill, then write. Complete `Grill` before `Write`, unless the user asks to skip grilling. User only wants gaps found: stop after the grill.

## Inputs

- Requirements come only from supplied context, `agent-view/research.md`, or explicitly retrieved sources. Cite supplied ticket links; a key alone says nothing.
- Read `agent-view/research.md` and `agent-view/attachments/` when present in the branch folder. For a direct ticket URL or explicit lookup with no `agent-view/research.md`, run `go-research` first.
- Read the project references per [setup.md](references/setup.md) (including `~/.just-do-it/{project}/public/glossary.md`, `public/adr/`, and `public/test-config.md` when present), existing reusable project components, and the code the ticket likely touches.

## 1. Grill

Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, numbered, most important first.
  - A question that depends on an open one waits.
- Per question: a recommended answer and one line on why it matters. Word it so "yes" accepts.
  - Put the question and the recommendation on separate lines, never in one sentence.
- Find facts yourself in code, docs, and ticket. Ask only decisions and unknown domain terms.
- Look for: missing or conflicting requirements, unclear criteria, edge and error cases, roles, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - A checkable `Goal` confirmed with the user.
  - Unknown terminology, product section names ("Section B", "Section C", "patient history"), or glossary clashes per [domain-docs.md](references/domain-docs.md) and [public-docs.md](../go-setup/references/public-docs.md): **never guess unknown domain terms—ask the user, then save confirmed terms to `public/glossary.md` and accepted hard-to-reverse decisions to `public/adr/`**.
  - The commit format, when the project and `agent-view/commit-format.md` have none (see Commit format).
  - Boundaries, probed with a concrete edge-case scenario.
  - E2E scenario when E2E setup exists and UI or user flows change: read the E2E folder path from `public/test-config.md` or locate it directly. List the folder first without reading spec files, then suggest concrete scenario(s) and confirm with the user before writing the plan.
- Done when the frontier is empty and the user confirms shared understanding and the `Goal`. Then write `agent-view/plan.md` and `agent-view/checklist.md`. For a grill-only request, stop after the final round.

## Commit format

- Use the project's format (`AGENTS.md`, `CLAUDE.md`, rules, project-local skills), else `agent-view/commit-format.md`.
- Neither: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Save the confirmed format to `agent-view/commit-format.md` (one line plus an example) and record it under `Decisions`.

## 2. Write

1. Read [plan-format.md](references/plan-format.md) and [checklist-format.md](references/checklist-format.md). Write `agent-view/plan.md` and `agent-view/checklist.md`. Record the grill's decisions under `Decisions`.
2. Bug ticket whose diagnosis would clutter the plan: also write `agent-view/diagnose.md` per [diagnose-format.md](references/diagnose-format.md).
3. Check unit and E2E setup per [setup.md](references/setup.md). Record `none: no setup` when there is no setup and adding it is outside scope.
4. Make each step concrete enough for `go-work` to run without new design decisions: owned source and test files, reusable components or `agent-view/attachments/` where relevant, dependencies including shared state, public test seams, test authorization, one-line commit message, and delivery mode. Group related changes into cohesive steps.
5. List every file a step deletes under `Deletions`; plan approval covers the listed scope and its deletions.
6. User changes the requirement: revise `Goal`, steps, and `Deletions`, and update `agent-view/plan.md` and `agent-view/checklist.md` in place.
7. Update `public/glossary.md` for any newly confirmed domain terms and write `public/adr/NNN-short-title.md` for any confirmed ADR decisions per [domain-docs.md](references/domain-docs.md).
8. Report the saved `agent-view/plan.md` and `agent-view/checklist.md` paths with a concise summary (`Goal`, steps, test scope, deletions), then ask for plan approval.

## Done when

- Every behavior acceptance criterion maps to a step with a failing test named (or `none: no setup`). Each shared setup step has a focused verification check.
- Every step has a `Commit` line.
- The `Goal` is confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
- `agent-view/plan.md` and `agent-view/checklist.md` (plus any updates to `public/glossary.md` or `public/adr/`) are written.
