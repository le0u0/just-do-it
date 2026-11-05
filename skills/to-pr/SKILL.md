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

Write the title and body for the current branch. Open the PR only when the user asks.

## Input

- The branch diff against its base, and what the user told you.
- No plan or review file is needed.
- Use the project's own terms, from `GLOSSARY.md` when present.

## Steps

1. Write the title as one line in the project's commit format.
2. Write the body with the template below. Skip preambles and keep prose short.
3. Save the body as `pr.md` in the branch folder (see Storage).
4. Reply with the title, the body, and the path.
5. Only when the user asked to open or create the PR:
   1. Read the host from `git remote get-url origin` and the base branch from `git symbolic-ref refs/remotes/origin/HEAD`. Ask when either is unclear.
   2. Push the current branch if it has no remote copy. Never force-push.
   3. Open the PR with the host's CLI, such as `gh pr create --base <base> --title <title> --body-file <path>`.
   4. With no CLI, give the new-PR URL and say the PR is not opened:
      - GitHub: `<repo-url>/compare/<base>...<branch>`
      - Bitbucket: `<repo-url>/pull-requests/new?source=<branch>&dest=<base>`
      - GitLab: `<repo-url>/-/merge_requests/new?merge_request[source_branch]=<branch>`
      - Another host: say the URL is unknown.
   5. Report the PR URL.

## Storage

- Branch folder: `~/.just-do-it/{project}/{branch}/`. `{branch}` is `git branch --show-current` with each `/` replaced by `-`.
- Find it by globbing `~/.just-do-it/*/{branch}`.
- No match: ask the user which project, reuse the folder whose name matches ignoring case and separators, else create it.
- Project names are lowercase words joined by hyphens.
- `pr.md` exists: update it in place. Never add a numbered or dated copy.

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

Pick the smallest view that makes the key point clear. Use one, sometimes several, rarely all. Place each visual next to the short text it supports. Keep only the calls, files, props, states, and boundaries that matter.

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

  ```text
  <SessionPage> (apps/example/src/routes/session.tsx)
    useSessionEvents()
    <SessionToolbar>
      <RunSkillButton> (packages/ui)
  ```

- File responsibility or broad refactor: shallow file tree.

  ```text
  src/
  ├── commands/       # parses user actions
  ├── sessions/       # owns session state
  └── transport/      # sends API requests
  ```

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

- A change to an existing shape: a `diff` block of that shape, not of the files.

  ```diff
   on(save)
  -  write content
  +  if content is unchanged
  +    return cached result
  +  write new content
  +  invalidate cache
  ```

  The same works for a component tree (`+    <RunSkillButton />`), a file tree (`+│   └── show-me.ts`), or a call tree (`+    expandSkillMention`).

- Whole block: when most of it is new, when omitted context would hide ownership or order, or when the user needs a copyable target shape.

### Evidence

- Show concrete proof the change works, before and after.
- Best: screenshots, when the environment allows and the change is visual.
- Next: execution output. Show the exact test that failed and now passes, as pseudocode, with the command and result.
- Never invent a result. Write `not run` where there is none.

### Merge Danger

- **Door:** two-way when a revert is cheap. One-way for destructive or hard-to-reverse changes, such as data migrations.
- **Blast Radius:** the scope of impact if it goes wrong, such as layout shift, breakage for consumers, mobile responsiveness.
