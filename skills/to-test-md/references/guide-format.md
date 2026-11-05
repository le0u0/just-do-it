# Guide Format

The reader tests by hand, knows nothing about the code, has no source. Say what to do and what to expect, once. `to-test-html` renders the HTML page from this Markdown.

```markdown
# PROJ-123: feature name

[PROJ-123](link) QA Test

## Setup

- AC_1: account that can <what it must be able to do>.
- ORG_1: organisation with <state it must be in>.

## Group: <purpose>

<one line: why this group, and why in this order>

### Test 1: <what it shows>

<optional note>

1. <screen>: <action>.
2. <screen>: <action>.

Expect: <result>.
```

## Title and related

- Title: the feature name. Lead line: the ticket key as a link. No ticket: a short feature description.
- Related tickets: one line after the lead, `Related: KEY (role) · KEY`.
  - Each is a link on the ticket's site.
  - Source: the `Linked:` line of `triage.md` in `state/`.
  - None: omit the line.

## Setup

- List account and data labels (AC_1, PR_A).
- Add another account only when a test needs another organisation or role.
- Rights are changed by hand in the project's settings screen: never one account per right.

## Groups

- Group tests by purpose: a heading and a one-line reason.
- Order:
  1. What must exist first.
  2. Simple to complex.
  3. Variations.
  4. Permissions.
  5. Where values show up.
  6. Anything needing a different account.
- Last group `Not affected`: what must stay unchanged. List only what the change affects elsewhere.

## Tests

- `Test N: descriptive title`, numbered across the whole guide.
- Parts: optional note, numbered steps, one `Expect:` line.
- A test starts at the first screen that differs from the previous test.
- Create test data inside the steps (a new record, a saved item with hand-chosen values). No shared data set up front.
- Name a default as a default ("unchecked by default").
- Say what is checked after an action in the same `Expect` line.

## Steps

- One action per step, 15 words or fewer.
- Never say to log in or switch account when Setup or the title already names it.

## Wording

- Use the words on screen: menu, button, field names.
- Other languages: use the project's translation files for each label (grep them).
- Translation unknown: keep code labels (AC_1) and menu paths in English.
- A customer-configurable name gets a best-fit term and goes to `Open` for review.
