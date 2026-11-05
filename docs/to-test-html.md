# to-test-html

Builds a single-file HTML QA page from the testing guide Markdown. You call it; the model and the manager never do.

## DO IT

- Reads `testing-guide-{short-description}.md` in `~/.just-do-it/{project}/{branch}/`.
- Converts it to JSON per `data-shape.md`, and swaps that JSON into `references/qa-template.html`.
- Saves `testing-guide-{short-description}.html` beside the guide, updating in place.
- Verifies the page per `verify.md` and reports `pass`, `fail` or `not verified`.
- Without the guide, stops, writes nothing, and tells you to run `to-test-md` first.
- Never hand-edits the page, and writes no data or generator file.

## USE IT

| Situation | Use |
| --- | --- |
| Guide exists, testers want ticks and export | `to-test-html` |
| No guide yet | `to-test-md` first |
| Guide changed | edit the `.md`, rerun |

## WORK IT

- The `.html` sits beside the guide and opens with no console error.
- Testers can tick steps, mark Pass or Fail, and export results with concerns.
- Progress survives a reload.
- Language and Pass/Fail buttons are segmented controls, and links open in a new tab.
- Each `verify.md` check is reported honestly.

## FIT IT

```text
to-test-md -> to-test-html
```

- The template previews on its own with a sample guide.
- It runs after the review is approved, outside the manager flow.
- `to-pr` is a separate step.
