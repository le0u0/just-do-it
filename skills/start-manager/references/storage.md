# Storage

Every file this plugin writes lives under `~/.just-do-it/`, so any repository can reach it. The repository receives only the source and test changes the job requires.

```text
~/.just-do-it/
  {project}/
    docs/                          # glossary.md and adr/, shared by every branch
    {branch}/
      commit-format.md
      plan.md
      checklist.md
      review.md
      pr.md
      testing-guide-{short-description}.md   # written by to-test-md; to-test-html writes the .html beside it
      attachments/{ticket}/        # cached ticket files
      state/
        jobs.md
        triage.md                  # every researched ticket or link
        diagnose.md                # optional
        context.md                 # rule files and comparable specs, searched once
        logs
```

## Rules

- The user reads files above `state/`; the plugin keeps the rest in `state/`.
- The manager saves every doc a `go-*` skill returns; user-invoked `to-*` skills write `pr.md` and the testing guide themselves, in the same branch folder.
- Write only files listed here: create when missing, update in place otherwise. Never a numbered or dated copy.

## Project folder

- One per product or codebase, lowercase words joined by hyphens (`acme-billing`); any spelling of a name reaches one folder.

1. Find a branch's project: glob `~/.just-do-it/*/{branch}`.
2. No match: ask the user which project. Reuse the folder matching the answer ignoring case and separators, else create it.

- The manager asks when a link or review starts the work.

## Branch folder

- Name: `git branch --show-current` with each `/` replaced by `-`.
- It holds everything for the branch: plan, checklist, review, PR text, testing guide, commit format, `state/`, `attachments/`.
- No branch yet (link researched first): short kebab-case description, kept until a branch exists.
- Find by name; none: create. A user-supplied path wins.
