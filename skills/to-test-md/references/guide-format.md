# Guide Format

The reader is support staff, not technical, and tests by hand. Plain words only. Say what to do and what they should see, once.

```markdown
# PROJ-123: feature name

[PROJ-123](link) QA Test

## Before you start

- Account: can <what it must be able to do>.
- Organisation: <state it must be in>.

## <purpose>

<one line: why this group, and why in this order>

### Test 1: <what it shows>

<optional note>

1. <screen>: <action>.
2. <screen>: <action>.

You should see: <result>.
```

## Title and related

- Title: feature name. Lead line: ticket key as a link when its URL is known; otherwise the plain key. No ticket: a short feature description.
- `Related: KEY (role) · KEY`: one line after the lead, each a link on the ticket's site, from `Linked:` in `state/triage.md`. None: omit.

## Before you start

- Nothing to name (no special account or organisation): omit the whole section.
- At most 3 lines, as short noun phrases. More means the item belongs in a test.
- Accounts and organisations only. A device is not a starting item: say it in the test note or step 1.
- Add an account only for another organisation or role. Rights are changed by hand in the project's settings.
- Data used by one test: create it in that test's steps. Used by 2 or more tests: one `Data:` line in plain words.
- No codes like `AC_1`. Two or more accounts: tell them apart by role ("Account that can edit", "Account that can only view").

## Groups

- Group by purpose: heading plus a one-line reason.
- Order:
  1. What must exist first.
  2. Simple to complex.
  3. Variations.
  4. Permissions.
  5. Where values show up.
  6. Anything needing a different account.
- Final group `Should not change`: what must stay unchanged.

## Tests

- `Test N: descriptive title`, numbered across the guide. Parts: optional note, numbered steps, one `You should see:` line.
- Start at the first screen that differs from the previous test.
- Size: 3 to 8 steps. More than 8: split at a natural break. Fewer than 3 and the same start screen as a neighbour: merge into one test; put each check in the `You should see` line, one short sentence each.
- Create test data inside the steps.
- Name a default as a default ("unchecked by default"). Put what is checked after an action in the same `You should see` line.

## Steps

- One action, 15 words or fewer.
- Name the account once, in `Before you start` or the title; steps skip log-in and switching.

## Wording

- Use on-screen words: menu, button, field names.
- No sizes (`px`), code terms or UI-engineering words (`canvas`, `cursor`, `pinned`, `layout`). Say what the eye sees: "a thin bar", "the pointer becomes a hand".
- One idea per sentence, 15 words or fewer.
- Other languages: grep the project's translation files; none found: keep menu paths in English.
- A customer-configurable name gets a best-fit term and goes to `Open`.
