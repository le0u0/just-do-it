---
name: to-pr
description: 'Write the pull request title and body for a finished branch: a visual summary, before and after evidence, and merge danger. Saves pr.md, and opens the PR when asked. Use for "pr", "create a PR", "open a PR", "write the PR", "PR text" or "commit, push, pr".'
disable-model-invocation: true
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

# PR

Write the title and body for the current branch. Open the PR only when asked.

## Input

- The branch diff against its base, and what the user said.
- No plan or review file.
- The project's own terms, from `GLOSSARY.md` when present.

## Steps

1. Write the title as one line in the project's commit format.
2. Write the body with the template below. No preambles; short prose.
3. Save the body as `pr.md` in the branch folder (see Storage).
4. Reply with the title, the body, and the path.
5. Only when asked to open the PR:
   1. Host: `git remote get-url origin`. Base: `git symbolic-ref refs/remotes/origin/HEAD`. Ask when unclear.
   2. Push the branch if it has no remote copy. Never force-push.
   3. Open with the host's CLI, e.g. `gh pr create --base <base> --title <title> --body-file <path>`.
   4. No CLI: give the new-PR URL and say it is not opened:
      - GitHub: `<repo-url>/compare/<base>...<branch>`
      - Bitbucket: `<repo-url>/pull-requests/new?source=<branch>&dest=<base>`
      - GitLab: `<repo-url>/-/merge_requests/new?merge_request[source_branch]=<branch>`
      - Another host: say the URL is unknown.
   5. Report the PR URL.

## Storage

- Branch folder: `~/.just-do-it/{project}/{branch}/`; `{branch}` = `git branch --show-current`, `/` replaced by `-`.
- Find it: glob `~/.just-do-it/*/{branch}`.
- No match: ask which project. Reuse the folder matching ignoring case and separators, else create it (lowercase words joined by hyphens).
- `pr.md` exists: update in place. No numbered or dated copy.

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

- Before and after proof the change works.
- Best: screenshots, for visual changes when the environment allows.
- Next: execution output: the exact test that failed and now passes, as pseudocode, with command and result.
- Never invent a result. Write `not run` where none.

### Merge Danger

- **Door:** two-way when a revert is cheap; one-way when destructive or hard to reverse (data migrations).
- **Blast Radius:** impact if it goes wrong: layout shift, consumer breakage, mobile responsiveness.
