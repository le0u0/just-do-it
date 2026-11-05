---
name: to-test-html
description: 'Build the single-file HTML QA page from an existing testing guide Markdown. Use for "QA page", "html testing guide" or "build the test page".'
disable-model-invocation: true
---

# Testing Guide HTML

Render the testing guide Markdown into one HTML page the tester ticks through. The page is generated, never hand-edited.

## Input

- `testing-guide-{short-description}.md` in the branch folder `~/.just-do-it/{project}/{branch}/`.
- `{branch}` is `git branch --show-current` with each `/` replaced by `-`. Find the folder by globbing `~/.just-do-it/*/{branch}`.
- Guide missing: stop and tell the user to run `to-test-md` first. Write nothing.

## Steps

1. Read the guide. Turn it into the data JSON per [data-shape.md](references/data-shape.md).
2. Fill [qa-page-template.html](references/qa-page-template.html) per the same file, and save the result as `testing-guide-{short-description}.html` beside the guide. Update in place when it exists.
3. Build the page per [html-page.md](references/html-page.md).
4. Verify per [verify.md](references/verify.md).
5. Reply with the path, what you verified, and what you could not verify.

## Rules

- A later change goes into the `.md` first, then rerun this skill.
- Write no data or generator file. The only output is the `.html`.

## Done when

- The `.html` exists beside the guide and opens with no console error.
- Each check in `verify.md` is `pass`, `fail` or `not verified`.
