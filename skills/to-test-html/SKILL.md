---
name: to-test-html
description: 'Build the single-file HTML QA page from an existing testing guide Markdown. Use for "QA page", "html testing guide" or "build the test page".'
disable-model-invocation: true
---

# Testing Guide HTML

Render the guide into one HTML page the tester ticks through. Never hand-edited.

## Input

- `testing-guide-{short-description}.md` in `~/.just-do-it/{project}/{branch}/` (`{branch}` = `git branch --show-current`, `/` replaced by `-`; glob `~/.just-do-it/*/{branch}`).
- Guide missing: stop, tell the user to run `to-test-md` first, write nothing.

## Steps

1. Convert the guide to data JSON per [data-shape.md](references/data-shape.md).
2. Fill [qa-template.html](references/qa-template.html) per the same file. Save as `testing-guide-{short-description}.html` beside the guide, updating in place.
3. Build the page per [html-page.md](references/html-page.md).
4. Verify per [verify.md](references/verify.md).
5. Reply with the path, what you verified, what you could not.

## Rules

- Change the `.md` first, then rerun. Output is the `.html` only: no data or generator file.

## Done when

- The `.html` sits beside the guide and opens with no console error.
- Each `verify.md` check is `pass`, `fail` or `not verified`.
