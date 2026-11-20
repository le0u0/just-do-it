---
name: to-pr
description: 'Write the pull request title and body for a finished branch: a visual summary, before and after evidence, and merge danger. Saves dev-view/pr.md and opens the PR when asked. Use for "pr", "create a PR", "open a PR", "write the PR", "PR text" or "commit, push, pr".'
disable-model-invocation: true
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

# PR

Write the title and body for the current branch and save to `~/.just-do-it/{project}/{branch}/dev-view/pr.md`.

## Storage & Input

- Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
- Read `agent-view/plan.md`, `agent-view/commit-format.md`, `agent-view/review.md`, `agent-view/ut.md`, and `agent-view/e2e.md` when present in the branch folder.
- The diff of the commits this PR adds, and what the user said.
  - Base: the branch the PR targets. Ask when unclear; `origin/HEAD` is only a guess.
  - Include every commit and change reachable from the intended head that is absent from the selected base. A commit appearing on another branch does not exclude it.
- The project's own terms, from `~/.just-do-it/{project}/public/glossary.md` and repository `GLOSSARY.md` when present.

## Steps

1. Write the title as one line in the project's commit format.
2. Write the body with the template below. No preambles; short prose.
3. Save the body to `~/.just-do-it/{project}/{branch}/dev-view/pr.md` (or print in the terminal only when explicitly requested). Report the title and saved path.
4. Only when asked to open the PR:
   1. Host: `git remote get-url origin`. Use the confirmed base.
   2. Record the intended local commit. Query the selected remote's live head branch. If it is absent or behind, push that commit to the intended branch when authorized. Verify ancestry if needed before pushing. Stop if the remote has commits outside the intended history, the push fails, or verification is unavailable. Never force-push. Check that the live remote head matches the intended commit before opening the PR.
   3. Open with the host's CLI or connector using the verified head. With a saved body, GitHub CLI uses `gh pr create --base <base> --head <head> --title <title> --body-file <path>`. For terminal-only delivery, pass the body through the connector or stdin with `--body-file -`.
   4. If the PR cannot be created, report the blocker and provide the host's compare or new-PR URL when known.
   5. Report the PR URL.

## Body template

```markdown
## Summary

<diagram, diff-sketch, or tree>

## Evidence

- **Before:** <screenshot/output/failing test run>
  **After:** <screenshot/output/passing test run>

## Merge Danger

**Door:** <one-way or two-way>

<optional: description>

**Blast Radius:** <one-word description>

<optional: potential ramifications of merge>
```

### Summary

- Smallest view that makes the point; one, sometimes several.
- Each visual sits next to the short text it supports. Keep only what matters.

Views:

- Logic or algorithm: pseudocode.

  ```text
  on(save)
    if content is unchanged
      return cached result
    write new content
    return fresh result
  ```

- Runtime control flow: call tree.

  ```text
  submitForm
    createSession
      persistPrompt
      launchAgent
    navigateToSession
  ```

- UI structure: component tree, with state and module boundaries that matter.
- File responsibility or broad refactor: shallow file tree, one comment per folder.

- Component interaction or data flow: Mermaid.

  ```mermaid
  sequenceDiagram
      participant User
      participant UI
      participant Daemon
      User->>UI: choose command
      UI->>Daemon: send expanded prompt
      Daemon-->>UI: stream result
  ```

- A change to an existing shape (logic, component, file or call tree): a `diff` of that shape, not of the files.

  ```diff
   on(save)
  -  write content
  +  if content is unchanged
  +    return cached result
  +  write new content
  +  invalidate cache
  ```

- Whole block: when most of it is new, omitted context would hide ownership or order, or the user needs a copyable target shape.

### Evidence

- Before and after proof the change works (using `agent-view/ut.md`, `agent-view/e2e.md`, or screenshots when available).
- Best: screenshots, for visual changes when the environment allows.
- Next: execution output: the exact test that failed and now passes, as pseudocode, with command and result.
- Write `not run` where there is no result.

### Merge Danger

- **Door:** two-way when a revert is cheap; one-way when destructive or hard to reverse (data migrations).
- **Blast Radius:** impact if it goes wrong: layout shift, consumer breakage, mobile responsiveness.
