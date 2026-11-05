# go-triage

Read a ticket, a queue or a pasted link and return a short requirements brief. The manager runs it as a subagent; you can also call it directly.

## DO IT

- Takes a ticket URL or key, queue filters, or any pasted link.
- Fetches summary, description, status and comments from the tracker, and each linked ticket one level deep.
- Caches attachments, then reads every image and text file. Videos are listed by name and you are asked to describe them.
- Returns a brief in the reply: requirements, acceptance criteria, open questions, code pointers and a source reference.
- With a checkout, maps likely affected components with file evidence, labeled as an estimate.
- Is read-only. It changes no ticket field, posts no comment, approves nothing, and writes no files.

## USE IT

| Situation | Use |
| --- | --- |
| "Triage PROJ-123", "what does this ticket need", "go through my queue", a pasted URL | `go-triage` |
| You want the ticket turned into a plan | `go-plan` |
| The manager gets a pasted link | It runs `go-triage` first, so the research exists before any planning |

## WORK IT

- Each fetched ticket lists requirements, acceptance criteria and open questions, each with a source.
- Every attachment is either read or listed.
- Requirements stay apart from comments, proposals and conflicts.
- A later link returns the whole updated brief, not a fragment.
- No credentials or personal data appear in the brief.

## FIT IT

```text
go-triage -> go-plan
```

- `go-plan` takes the brief as context, not as approved scope.
- `justaway` saves the returned brief as `triage.md`.
