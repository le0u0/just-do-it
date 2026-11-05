---
name: to-test-md
description: 'Write the manual testing guide for a finished ticket as Markdown, for a reader who knows nothing about the code. Use for "write the testing guide", "test steps" or "QA guide".'
disable-model-invocation: true
---

# Testing Guide

Write the manual testing guide as Markdown. Run `to-test-html` afterwards for the HTML page.

## Input

- `plan.md` in the branch folder (see Storage). Missing: ask the user for it, or for the requirements and the diff.
- The diff from the plan's initial baseline, to find what changed for users.
- The ticket key and link, from the plan's `Requirement source`.

## Steps

1. Read `plan.md` and the diff. Use the screen names users see, with no file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md): setup, groups, tests.
3. Save it as `testing-guide-{short-description}.md` in the branch folder. Update in place when it exists.
4. List under `Open` for the user:
   - Behaviours in the diff or plan that no test covers.
   - Tests that cannot be done by hand, such as fetch failure or timing.
5. Add or drop no test without the user's answer.
6. Reply with the path, and `Open`.

## Storage

- Branch folder: `~/.just-do-it/{project}/{branch}/`. `{branch}` is `git branch --show-current` with each `/` replaced by `-`.
- Find it by globbing `~/.just-do-it/*/{branch}`. No match: ask the user which project.
- Read `state/triage.md` there for the `Linked:` line.

## Done when

- Every acceptance criterion in `plan.md` is covered by a test.
- Every step is 15 words or fewer.
