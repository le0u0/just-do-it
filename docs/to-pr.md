# to-pr

Writes the pull request title and body for the current branch. You call it; the model and the manager never do.

## DO IT

- Reads the branch diff against its base and what you tell it, plus `GLOSSARY.md` when present.
- Writes a one-line title in the project's commit format.
- Writes the body as Summary (diagram, tree, pseudocode or diff), Evidence (before and after) and Merge Danger (door and blast radius).
- Saves `pr.md` in `~/.just-do-it/{project}/{branch}/`, updating in place.
- Pushes and opens the PR only when you ask. It never force-pushes and never invents a result: no evidence reads `not run`.

## USE IT

| Situation | Use |
| --- | --- |
| Branch is done, you need the PR text | `to-pr` |
| Also open the PR | ask `to-pr` to open it |
| Check the code first | `go-review` |

- It needs no `plan.md` or `review.md`.

## WORK IT

- The title is one line in the project's commit format.
- Summary uses the smallest view that makes the point.
- Evidence shows before and after, or `not run`.
- Merge Danger names a one-way or two-way door.
- `pr.md` exists at the branch folder path.
- Without an open request, nothing is pushed.

## FIT IT

```text
go-review -> go-fix -> go-review -> to-pr
```

- You run it after the review is approved, outside the manager flow.
- With no host CLI, it gives the new-PR URL and says the PR is not opened.
- Follows Matt Pocock's `pr`, from the `show-me` skill by Dex Horthy.
