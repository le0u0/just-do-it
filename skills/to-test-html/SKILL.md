---
name: to-test-html
description: 'Build the single-file HTML QA page from a Markdown testing guide. Use for "QA page", "html testing guide" or "build the test page".'
disable-model-invocation: true
---

# Testing Guide HTML

Render the guide into one HTML page the tester ticks through. Never hand-edited.

## Input

- Use the supplied Markdown guide, a guide in the current session, or `testing-guide-{short-description}.md` in the resolved task directory.
- Guide missing: stop, tell the user to run `to-test-md` first, write nothing.
- Start the translation worker whether `justaway` is on or off. If that worker cannot start, report blocked and write no HTML.

## Steps

1. Resolve save or terminal output per [Output delivery](../justaway/references/storage.md#output-delivery). For a save, find any existing output first so test IDs can be preserved. Convert the guide to English data JSON per [data-shape.md](references/data-shape.md).
2. Translate per `Translate` in the same file: one `fast` subagent adds `zh` to every text.
3. Fill [qa-template.html](references/qa-template.html) per the same file and follow [html-page.md](references/html-page.md).
4. Verify per [verify.md](references/verify.md). Use an isolated temporary preview for terminal delivery.
5. Save as `testing-guide-{short-description}.html` in the selected task directory and report the path, or print the HTML in the terminal. If the host cannot display the bundled page in full, provide a copy-ready stdout command using the installed template and complete generated substitutions. State what was verified.

## Rules

- Change the `.md` first, then rerun. The `.html` is the only output.

## Done when

- The generated page opens with no console error. Deliver through the selected output.
- Each `verify.md` check is `pass`, `fail` or `not verified`.
