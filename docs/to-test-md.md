# to-test-md

Writes the manual testing guide as Markdown for a tester who knows nothing about the code. You call it; the model and the manager never do.

## DO IT

- Reads `plan.md` and the diff from the plan's baseline; the ticket key and link come from the plan's `Requirement source`.
- Writes `testing-guide-{short-description}.md` in `~/.just-do-it/{project}/{branch}/`, updating in place.
- Follows the guide format: setup, groups, numbered tests, one `Expect:` line each.
- Uses screen names, never file paths or component names.
- Returns in `Open`: behaviours no test covers, and tests that cannot be done by hand.
- Never adds or drops a test without your answer.

## USE IT

| Situation | Use |
| --- | --- |
| Finished ticket needs test steps | `to-test-md` |
| You also want a clickable QA page | then `to-test-html` |
| Only the PR text | `to-pr` |

- Without `plan.md`, it asks for it, or for requirements and the diff.

## WORK IT

- Every acceptance criterion in `plan.md` has a test.
- Every step is 15 words or fewer, one action each.
- Tests are grouped by purpose, with a one-line reason.
- The reply gives the path and an `Open` list.
- Re-running edits the same file.

## FIT IT

```text
go-review -> go-fix -> go-review -> to-test-md -> to-test-html
```

- `to-test-html` builds its page from this file.
- It reads `Linked:` tickets from `state/triage.md`, saved by the manager.
- Part of the user-run end of the flow, after `to-pr`.
