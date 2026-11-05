# Guide Format

The reader tests by hand and knows nothing about the code. Say what to do and expect, once. `to-test-html` renders the HTML page from this Markdown.

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

- Title: feature name. Lead line: ticket key as a link; no ticket, a short feature description.
- `Related: KEY (role) · KEY`: one line after the lead, each a link on the ticket's site, from `Linked:` in `state/triage.md`. None: omit.

## Setup

- List account and data labels (AC_1, PR_A).
- Add an account only for another organisation or role. Rights are changed by hand in the project's settings.

## Groups

- Group by purpose: heading plus a one-line reason.
- Order:
  1. What must exist first.
  2. Simple to complex.
  3. Variations.
  4. Permissions.
  5. Where values show up.
  6. Anything needing a different account.
- Final group `Not affected`: what must stay unchanged.

## Tests

- `Test N: descriptive title`, numbered across the guide. Parts: optional note, numbered steps, one `Expect:` line.
- Start at the first screen that differs from the previous test.
- Create test data inside the steps; no shared data up front.
- Name a default as a default ("unchecked by default"). Put what is checked after an action in the same `Expect` line.

## Steps

- One action, 15 words or fewer.
- Never say to log in or switch account when Setup or the title names it.

## Wording

- Use on-screen words: menu, button, field names.
- Other languages: grep the project's translation files; none found: keep code labels (AC_1) and menu paths in English.
- A customer-configurable name gets a best-fit term and goes to `Open`.
