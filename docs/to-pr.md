# to-pr

Writes the pull request title and body for the current branch and saves `dev-view/pr.md`. Opens the PR when asked.

## DO IT

```mermaid
flowchart LR
    IN([branch diff vs base,<br/>plan.md, review.md, glossary.md]) --> T[one-line title]
    T --> B[body: Summary,<br/>Evidence, Merge Danger]
    B --> S[save dev-view/pr.md]
    S -->|you ask| P([push, open PR])
```

| Step | Does |
| --- | --- |
| Reads | Branch diff against its base, `agent-view/plan.md`, `dev-view/review.md`, `dev-view/ut.md`, `dev-view/e2e.md`, and `public/glossary.md` when present |
| Title | One-line title in the project's commit format |
| Body | Summary (diagram, tree, pseudocode or diff), Evidence (before and after) and Merge Danger (door and blast radius) |
| Writes to storage | `~/.just-do-it/{project}/{branch}/dev-view/pr.md` |

[Skill](../skills/to-pr/SKILL.md) · [Storage](../skills/go-setup/references/storage.md)
