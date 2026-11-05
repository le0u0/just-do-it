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

- The user reads the files above `state/`; the plugin keeps everything else in `state/`.
- The manager saves every doc a `go-*` skill returns.
- The user-invoked `to-*` skills write `pr.md` and the testing guide themselves, in the same branch folder.
- Write only the files listed here.
  - Missing: create it. Existing: update it in place.
  - A new version, rerun, or changed plan edits the same file; never add a numbered or dated copy.

## Project folder

- One folder per product or codebase, named in lowercase words joined by hyphens, such as `acme-billing`.
- Spaces, underscores, capitals in the user's wording all become that form, so every spelling reaches one folder.

1. Find a branch's project by globbing `~/.just-do-it/*/{branch}`.
2. No match: ask the user which project the work is for.
   - List `~/.just-do-it/` first; reuse the folder whose name matches the answer ignoring case and separators.
   - Otherwise create it.

- The manager asks when a link or a review starts the work.

## Branch folder

- Name: current git branch (`git branch --show-current`), each `/` replaced by `-`.
- Inside the project folder, one folder holds everything for that branch: plan, checklist, review, PR text, testing guide, commit format, `state/`, `attachments/`.
- No branch to name (a link researched before work starts): use a short kebab-case description; keep working in it until a branch exists.
- Find it by that name. None: create it. A user-supplied path wins.
