# go-plan

Think through one ticket with you, then return a plan and checklist for approval. The manager runs it in the main thread; you can also call it directly.

## DO IT

- Takes a ticket (link or pasted requirements), plus `AGENTS.md`, `CLAUDE.md` and project-local skills.
- Grills you in rounds: each round asks every open decision whose prerequisites are settled, numbered, each with a recommended answer.
- Returns the plan (Goal, acceptance criteria, testing, decisions, steps, deletions) and the checklist in the reply.
- Writes no code, tests or files. The caller saves the plan.
- Stops after the grill when you only want gaps found.

## USE IT

| Situation | Use |
| --- | --- |
| "Plan PROJ-123", "what is unclear here", "break this into steps" | `go-plan` |
| You only want requirements read from a ticket | `go-triage` |
| The plan is approved and you want it built | `go-work` |
| The manager has a ticket | It runs `go-triage` first, then `go-plan` itself, because only the main thread can ask you questions |

## WORK IT

- It asks questions in numbered rounds, each with a recommended answer, and doesn't ask what the code already answers.
- A ticket link triggers `go-triage` first.
- The session ends only when you say the picture is shared and then say plan.
- Every acceptance criterion maps to a step with a named failing test.
- Every step has a one-line commit message.

## FIT IT

```text
go-triage -> go-plan -> go-work
```

- `go-triage` supplies the requirements brief before the grill.
- `go-work` builds from the approved plan.
- `start-manager` saves the returned plan and checklist as `plan.md` and `checklist.md`.
