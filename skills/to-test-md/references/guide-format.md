# Guide Format

The reader tests by hand, knows nothing about the code, and has no source. Say what to do and what to expect, once. The guide is a Markdown file in the shape below. `to-test-html` renders the HTML page from it.

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

## Rules

- Title: the feature name. The lead line is the ticket key as a link to the ticket. With no ticket, use a short feature description.
- Related tickets: one line after the lead, `Related: KEY (role) · KEY`, each a link on the same site as the ticket, taken from the `Linked:` line of `triage.md` in `state/`. Omit the line when there are none.
- Setup lists account and data labels (AC_1, PR_A). Add another account only when a test needs another organisation or role. Rights are changed by hand in the project's own settings screen, so one account per right is never needed.
- Group tests by purpose, each group with a heading and a one-line reason. Order: what must exist first, then simple to complex, then variations, then permissions, then where values show up, then anything needing a different account.
- Every test is `Test N: descriptive title`, numbered across the whole guide, with an optional note, numbered steps, and one `Expect:` line.
- One action per step, 15 words or fewer. A step never says to log in or switch account when Setup or the title already names it. A test starts at the first screen that differs from the test before it.
- Create test data inside the steps (a new record, a saved item with values chosen by hand). Define no shared data set up front.
- Name a default as a default ("unchecked by default"). Say what is checked after an action in the same `Expect` line.
- Use the words on the screen: menu, button, and field names. In each other language, use the project's own translation files for each label (grep them). Keep code labels (AC_1) and menu paths in English where the translation is unknown. A name a customer can configure gets a best-fit term and goes to `Open` for the user's review.
- List only what the change affects. Put what must stay unchanged in a final group `Not affected`.
