---
name: to-test-md
description: 'Write the manual testing guide for a finished ticket as Markdown, for a reader who knows nothing about the code. Use for "write the testing guide", "test steps" or "QA guide".'
disable-model-invocation: true
---

# Testing Guide

Write the guide as Markdown.

## Input

- `plan.md` in the branch folder. Missing: ask for it, or for requirements and diff.
- The diff from the plan's initial baseline.
- Ticket key and link, from the plan's `Requirement source`.

## Steps

1. Read `plan.md` and the diff. Use screen names users see: no file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md).
3. Save as `testing-guide-{short-description}.md` in the branch folder, updating in place.
4. Reply with the path and `Open`:
   - Behaviours in the diff or plan that no test covers.
   - Tests that cannot be done by hand, such as fetch failure or timing.
5. Change the test list only on the user's answer.

## Storage

- Branch folder: glob `~/.just-do-it/*/{branch}` (`{branch}` = `git branch --show-current`, `/` replaced by `-`). No match: ask which project.
- `state/triage.md` there has the `Linked:` line.

## Done when

- Every acceptance criterion in `plan.md` has a test.
- Every step is 15 words or fewer.
