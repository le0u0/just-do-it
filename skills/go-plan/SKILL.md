---
name: go-plan
description: 'Think through one ticket with the user, then plan it as a plan and checklist for approval, returned in the reply, with no code changes and no files written. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

Talk to the user directly; run in the main thread, not a subagent. Write no production code, tests, or files: return the plan and checklist in the reply, and the caller saves them. Report as the caller specifies.

Two phases in one context: grill, then write. When the user only wants gaps found, stop after the grill and return no plan.

## Inputs

- Take requirements only from supplied or explicitly retrieved context. Store a supplied ticket link; the key alone says nothing about requirements.
- For a ticket URL or explicit lookup, run `go-triage` first. Its brief is context, not approved scope.
- Follow the repository's `AGENTS.md`, `CLAUDE.md`, and project-local skills. Read the project references per [setup.md](references/setup.md) and the code the ticket likely touches, enough to judge feasibility.

## 1. Grill

Interview the user until nothing is silently assumed. Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled. Ask the whole frontier in one round, numbered, most important first. A question that depends on another open one waits for a later round.
- Give each question a recommended answer and one line on why it matters. Word it so "yes" accepts the recommendation.
- Find facts yourself in the code, docs and ticket; never ask the user for what you can look up. Ask only decisions.
- Look for: missing or conflicting requirements, unclear acceptance criteria, edge and error cases, roles and permissions, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree: the commit format when the project does not specify one (see Commit format), a checkable `Goal`, a glossary term clash, and an ADR-worthy decision per [domain-docs.md](references/domain-docs.md). Probe boundaries with a concrete edge-case scenario.
- Done when the frontier is empty and the user confirms shared understanding. Then ask the user to say plan, unless they already asked for one.

## Commit format

Use the format the project specifies in its `AGENTS.md`, `CLAUDE.md`, rules, or project-local skills, else the one the caller supplies. When neither exists, ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`, and return the answer as a `Commit format` line (one line plus an example) under `Decisions` for the caller to save.

## 2. Write

1. Read [plan-format.md](references/plan-format.md). Return the plan, then the checklist per [checklist-format.md](references/checklist-format.md), in the reply. Record the grill's decisions under `Decisions`. For a bug ticket whose diagnosis would clutter the plan, return a diagnosis too per [diagnose-format.md](references/diagnose-format.md).
2. Check the unit and e2e test setup per [setup.md](references/setup.md), and write `none: no setup` in a `Test` or `E2E` line when the project has no setup for it.
3. Make each step concrete enough for `go-work` to run without new design decisions: affected files, public test seams, test authoring and run authorization, the one-line commit message, and delivery mode. The seams under test are part of the plan, so the user approves them with it.
4. List every file a step deletes under `Deletions`; deletions are the only thing the plan asks approval for. When the user later changes the requirement, revise `Goal`, steps, and `Deletions` and return the whole plan again. A new term or hard-to-reverse decision found while writing goes to the user, and is proposed for the caller to save per [domain-docs.md](references/domain-docs.md) only after they confirm.
5. Show the plan and checklist in the reply for approval, and stop.

Done when every acceptance criterion maps to a step with a failing test named (or `none: no setup`), every step has a `Commit` line, the `Goal` is confirmed and checkable, and `Open` is `None.` or lists the blocking questions.
