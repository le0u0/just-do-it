# Storage

A task directory holds plugin documents outside the checkout. Use the user's path when supplied. The conventional location is `~/.just-do-it/{project}/{branch}/`.

## Output delivery

Applies to the final user-facing outputs of `go-research`, `go-plan`, `go-review`, `to-pr`, `to-test-md`, and `to-test-html`. A worker returns its result privately to its caller. An internal result used only as input to another skill needs no delivery decision.

1. Honor an explicit choice to save or print. Otherwise, in `justaway`, save to the resolved task directory. Outside `justaway`, or when its task directory cannot be resolved, ask whether to save or print in the terminal. If saving needs a destination, ask for a directory or project name in that question.
2. Save: check permission first, then create or update the named file and report its path plus any required summary, approval question, or verification status. For research, transfer temporary attachments per [attachments.md](../../go-research/references/attachments.md#location) before cleanup. Keep the full result in the file. A draft plan and checklist must exist before asking for plan approval.
3. Print: deliver the complete result in the terminal and make no persistent task files for that run. In `justaway`, keep the brief, plan, checklist, review and other state in the coordinator's context and pass the needed text to workers. Ask for plan approval after displaying the plan and checklist.
4. If a save is blocked, report the unsaved path and ask for a writable destination or permission to print. Hold the unsaved result. Resume delivery and any dependent approval once the user chooses.

An output choice for the task applies to subsequent managed outputs until the user changes it. Temporary working files may support preview, tests, or attachment inspection. Keep them isolated and clean them up when no longer needed.

## Rules

- Check write permission before saving. Use the host's approval flow outside writable roots. Plan approval grants no filesystem permission.
- Pass the resolved task directory to workers that need it. Supply specific paths or text in their handoff. Workers leave user-facing documents to the coordinator.
- Keep reports outside the repository and plugin cache unless the user explicitly selects a repository path. Update existing documents in place.
- Write plan-derived diagnosis, commit format, checklist progress, and job history only for tasks using storage. Write shared project documents only when their project directory is known and the user approved the underlying decision. Otherwise retain needed decisions in the plan or session.

```text
~/.just-do-it/
  {project}/
    docs/                             # glossary.md, adr/, e2e-path.md
    {branch}/
      commit-format.md
      plan.md
      checklist.md
      review.md
      pr-{base}.md
      testing-guide-{short-description}.md
      testing-guide-{short-description}.html
      attachments/{ticket}/
      state/
        jobs.md
        triage.md                     # go-research brief
        diagnose.md
```

## Resolve the task directory

1. Use a user-supplied directory or the directory already resolved for the task.
2. Otherwise use `git branch --show-current`, replacing each `/` with `-`. Look for a unique `~/.just-do-it/*/{branch}` match. A known project can use its conventional branch path directly.
3. No match, several matches, or detached HEAD: use the Output delivery question when a save needs a destination. Reuse the matching project regardless of case and separators. For a new project use lowercase kebab case. If no branch exists, use a short kebab-case task name or the supplied directory.
