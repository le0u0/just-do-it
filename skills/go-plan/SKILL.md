---
name: go-plan
description: 'Think through one ticket with the user, then plan it as a plan and checklist for approval, returned in the reply, with no code changes and no files written. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope

- Talk to the user directly: run in the main thread, not a subagent.
- Write no production code, tests, or files. Return the plan and checklist in the reply; the caller saves them.
- Report as the caller specifies.
- Two phases in one context: grill, then write.
- User only wants gaps found: stop after the grill, return no plan.

## Inputs

- Take requirements only from supplied or explicitly retrieved context.
- Store a supplied ticket link. The key alone says nothing about requirements.
- Ticket URL or explicit lookup: run `go-triage` first. Its brief is context, not approved scope.
- Follow the repository's `AGENTS.md`, `CLAUDE.md`, and project-local skills.
- Read the project references per [setup.md](references/setup.md) and the code the ticket likely touches, enough to judge feasibility.

## 1. Grill

Interview the user until nothing is silently assumed. Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds.
  - The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, numbered, most important first.
  - A question that depends on another open one waits for a later round.
- Per question: a recommended answer and one line on why it matters. Word it so "yes" accepts the recommendation.
- Find facts yourself in the code, docs, and ticket. Ask only decisions.
- Look for:
  - Missing or conflicting requirements, unclear acceptance criteria.
  - Edge and error cases, roles and permissions, test data, dependencies.
  - Design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - The commit format, when the project does not specify one (see Commit format).
  - A checkable `Goal`.
  - A glossary term clash, and an ADR-worthy decision per [domain-docs.md](references/domain-docs.md).
  - Boundaries, probed with a concrete edge-case scenario.
- Done when the frontier is empty and the user confirms shared understanding. Then ask the user to say plan, unless they already asked for one.

## Commit format

- Use the format the project specifies in `AGENTS.md`, `CLAUDE.md`, rules, or project-local skills, else the one the caller supplies.
- Neither exists: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Return the answer as a `Commit format` line (one line plus an example) under `Decisions` for the caller to save.

## 2. Write

1. Read [plan-format.md](references/plan-format.md).
   - Return the plan, then the checklist per [checklist-format.md](references/checklist-format.md).
   - Record the grill's decisions under `Decisions`.
   - Bug ticket whose diagnosis would clutter the plan: also return a diagnosis per [diagnose-format.md](references/diagnose-format.md).
2. Check the unit and e2e test setup per [setup.md](references/setup.md). No setup: write `none: no setup` in the `Test` or `E2E` line.
3. Make each step concrete enough for `go-work` to run without new design decisions:
   - Affected files.
   - Public test seams. The user approves them with the plan.
   - Test authoring and run authorization.
   - The one-line commit message.
   - Delivery mode.
4. List every file a step deletes under `Deletions`. Deletions are the only thing the plan asks approval for.
5. Requirement changed by the user later: revise `Goal`, steps, and `Deletions`, return the whole plan again.
6. New term or hard-to-reverse decision found while writing: go to the user first; propose it for the caller to save per [domain-docs.md](references/domain-docs.md) only after they confirm.
7. Show the plan and checklist in the reply for approval, and stop.

## Done when

- Every acceptance criterion maps to a step with a failing test named (or `none: no setup`).
- Every step has a `Commit` line.
- The `Goal` is confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
