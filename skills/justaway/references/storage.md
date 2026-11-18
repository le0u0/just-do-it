# Storage

Plugin documents default to `~/.just-do-it/`. The repository receives only the source and test changes the job requires. A user-supplied task directory wins.

```text
~/.just-do-it/
  {project}/
    docs/                          # glossary.md, adr/, and e2e-path.md (shared by every branch)
    {branch}/
      commit-format.md
      plan.md
      checklist.md
      review.md
      pr-{base}.md
      testing-guide-{short-description}.md   # written by to-test-md; to-test-html writes the .html beside it
      backend-{short-description}.md         # written by ask-be
      attachments/{ticket}/        # cached ticket files
      state/
        jobs.md
        triage.md                  # every researched ticket or link
        diagnose.md                # optional
        logs
```

## Rules

- Resolve the directory and write permission before saving. Outside the sandbox's writable roots, use the host's approval flow; an approved plan does not grant filesystem access.
- Approval unavailable or denied: report the blocked path and return the unsaved content. Do not claim it was saved, ask for plan approval, or advance a manager step that requires the file. Continue only after access or an explicit writable task directory is supplied.
- Keep an explicit task directory for the whole job and pass it to subagents and `to-*` skills. Never silently move documents into the repository or plugin cache.
- The user reads files above `state/`; the plugin keeps the rest in `state/`.
- The manager saves every doc a `go-*` skill returns; `to-*` skills and `ask-be` write their documents in the same branch folder.
- Write only files listed here: create when missing, update in place otherwise. Never a numbered or dated copy.

## Project folder

- One per product or codebase, lowercase words joined by hyphens (`acme-billing`); any spelling of a name reaches one folder.

1. Find a branch's project: glob `~/.just-do-it/*/{branch}`.
2. No match, several matches, or no branch name (detached HEAD): ask the user which project. Reuse the folder matching the answer ignoring case and separators, else create it.

- The manager asks when a link or review starts the work.

## Branch folder

- Name: `git branch --show-current` with each `/` replaced by `-`.
- It holds everything for the branch: plan, checklist, review, PR text, testing guide, commit format, `state/`, `attachments/`.
- No branch yet (link researched first): short kebab-case description, kept until a branch exists.
- Find by name; none: create. A user-supplied path wins.
