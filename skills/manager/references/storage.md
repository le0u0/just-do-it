# Storage

Every file this plugin writes lives under `~/.agent-workflow/`, so any repository can reach it. The repository receives only the source and test changes the job requires.

```text
~/.agent-workflow/
  {project}/
    docs/                          # glossary.md and adr/, shared by every branch
    {branch}/
      commit-format.md
      plan.md
      checklist.md
      review.md
      pr.md
      testing-guide-{short-description}.md
      attachments/{ticket}/        # cached ticket files
      state/
        jobs.md
        think.md
        triage.md                  # every researched ticket or link
        diagnose.md                # optional
        context.md                 # rule files and comparable specs, searched once
        logs
```

The user reads the files above `state/`. The plugin keeps everything else in `state/`.

Write only the files listed here. Create a file when it is missing; when it exists, update it in place. A new version, a rerun, or a changed plan edits the same file and never adds a numbered or dated copy.

## Project folder

One folder per product or codebase the user works on, named in lowercase words joined by hyphens, such as `acme-billing`. Spaces, underscores and capitals in the user's wording all become that one form, so every spelling of a name reaches one folder.

1. Find a branch's project by globbing `~/.agent-workflow/*/{branch}`.
2. With no match, ask the user which project the work is for. Listing `~/.agent-workflow/` first, reuse the folder whose name matches the answer ignoring case and separators; otherwise create it.

`planner` and `senior-planner` ask in `think` or `plan`, whichever comes first. The manager asks when a link or a review starts the work.

## Branch folder

Name it after the current git branch (`git branch --show-current`), with each `/` replaced by `-`. Inside the project folder, one folder holds everything for that branch: plan, checklist, review, PR text, testing guide, commit format, `state/` and `attachments/`. With no branch to name (a link researched before work starts), use a short kebab-case description and keep working in it until a branch exists.

Find it by that name. None: create it. A user-supplied path wins.
