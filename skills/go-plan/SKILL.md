---
name: go-plan
description: 'Grill one ticket, then write agent-view/plan.md and agent-view/checklist.md for approval. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope & Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
- In `go-flow`, use confirmed answers and open questions from the caller. Return unanswered questions and the decisions made so far for the next round. Direct use asks the user in the current thread.
- Write no production code or tests. Write planning outputs for agents to `agent-view/plan.md` and `agent-view/checklist.md` (plus `agent-view/commit-format.md` when confirmed and `agent-view/diagnose.md` when needed), and render the human-readable visual plan at `dev-view/plan.html` per [html-render.md](../go-setup/references/html-render.md) (with inline attachment images and visual statechart) so the user can inspect `dev-view/plan.html` and approve.
- Two phases: grill, then write. Complete `Grill` before `Write`, unless the user asks to skip grilling. User only wants gaps found: stop after the grill.

## Inputs

- Requirements come only from supplied context, `agent-view/spec.md`, or explicitly retrieved sources. Cite supplied ticket links; a key alone says nothing.
- Read `agent-view/spec.md` and `agent-view/attachments/` when present. For a ticket key, ticket URL, or explicit lookup, require a complete spec per [to-spec](../to-spec/SKILL.md#workflow). If absent or stale, run `to-spec`. Follow [Blocked spec](../to-spec/SKILL.md#blocked-spec) before reading project code or planning.
- A saved blocked brief for the active ticket triggers the same stop when resuming without a ticket key in the latest message.
- Read the project references per [setup.md](references/setup.md) (including `~/.just-do-it/{project}/public/glossary.md`, `public/adr/`, and `public/jdi-config.md` when present), existing reusable project components, and the code the ticket likely touches.

## 1. Grill

Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, most important first.
  - A question that depends on an open one waits.
- Use the terminal format below. Start each question with a divider, use `1.`, `2.`, and label choices `A.`, `B.`. Keep each question and choice short. Mark the recommended choice `(recommended)`.
- Show only the context needed to choose. Share rationale when the user asks `why <number>`. Use one reply hint per round.

```text
────────────────────────────────────
1. Where should Add Note open?
   A. Patient History (recommended)
   B. Case FM

────────────────────────────────────
2. Fix linked cards too?
   A. Yes (recommended)
   B. No

────────────────────────────────────
Reply 1A, 2A. Type why 2 for the reason.
```

- Find facts yourself in code, docs, and ticket. Ask only decisions and unknown domain terms.
- Look for: missing or conflicting requirements, unclear criteria, edge and error cases, roles, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - The numbered `Goal` scenarios and their `Expected` and `Actual` behavior, confirmed with the user per [plan-format.md](references/plan-format.md#sections).
  - Which existing components, services, or shared primitives to reuse when multiple candidates exist or reuse is unclear (never guess—ask the user).
  - Unknown terminology, product terms, or glossary clashes per [domain-docs.md](references/domain-docs.md) and [public-docs.md](../go-setup/references/public-docs.md): **never guess unknown domain terms—ask the user, then save confirmed terms to `public/glossary.md` and accepted hard-to-reverse decisions to `public/adr/`**.
  - The commit format, when the project and `agent-view/commit-format.md` have none (see Commit format).
  - Boundaries, probed with a concrete edge-case scenario.
  - State transitions & missing-transition checks for stateful UI/workflows per [statechart.md](references/statechart.md).
  - E2E scenario when E2E setup exists and UI or user flows change: read the E2E folder path from `public/jdi-config.md` or locate it directly. List the folder first without reading spec files, then suggest concrete scenario(s) and confirm with the user before writing the plan.
- Done when the frontier is empty and the user confirms shared understanding and the `Goal`. Then write `agent-view/plan.md` and `agent-view/checklist.md`. For a grill-only request, stop after the final round.

## Commit format

- Use the project's format (`AGENTS.md`, `CLAUDE.md`, rules, project-local skills), else `agent-view/commit-format.md`.
- Neither: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Save the confirmed format to `agent-view/commit-format.md` (one line plus an example) and record it under `Decisions`.

## 2. Write

1. Read [plan-format.md](references/plan-format.md), [checklist-format.md](references/checklist-format.md), and (for stateful features) [statechart.md](references/statechart.md). Write `agent-view/plan.md` and `agent-view/checklist.md`. Reference relevant attachments with labeled path tooltips. Record the grill's decisions under `Decisions`.
2. Bug ticket whose diagnosis would clutter the plan: also write `agent-view/diagnose.md` per [diagnose-format.md](references/diagnose-format.md).
3. Check unit and E2E setup per [setup.md](references/setup.md). Record `none: no setup` when there is no setup and adding it is outside scope.
4. Make each step concrete enough for `go-work` to run without new design decisions: owned source and test files, reuse, dependencies and shared state, test seams, authorization, commit groups and messages, and delivery mode. Group the same feature or function in one step.
5. List every file a step deletes under `Deletions`; plan approval covers the listed scope and its deletions.
6. User changes the requirement: revise `Goal`, steps, and `Deletions`, and update `agent-view/plan.md` and `agent-view/checklist.md` in place.
7. Update `public/glossary.md` for any newly confirmed domain terms and write `public/adr/NNN-short-title.md` for any confirmed ADR decisions per [domain-docs.md](references/domain-docs.md).
8. Render `~/.just-do-it/{project}/{branch}/dev-view/plan.html` per [html-render.md](../go-setup/references/html-render.md), including the visual statechart diagram (when stateful) and inline image previews from `../agent-view/attachments/{ticket}/`.
9. Report `dev-view/plan.html` (alongside `agent-view/plan.md` and `agent-view/checklist.md`) so the user can review `dev-view/plan.html` in the browser and approve the plan.

## Done when

- Each `Goal` scenario maps to a step's focused check and an observable assertion, or a documented verification gap. Each shared setup step has a focused check.
- Step titles describe user outcomes. Each `Blocked by` names the needed output, and all checklist step numbers match the plan.
- Every step has a `Commit` line and a `Reuse` line.
- Every `Expected` result is confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
- `agent-view/plan.md`, `agent-view/checklist.md`, and `dev-view/plan.html` (plus any updates to `public/glossary.md` or `public/adr/`) are written.
