# Guide Format

The reader tests by hand, knows nothing about the code, and has no source. Say what to do and what to expect, once.

```markdown
# PROJ-123: title

## Setup

- AC_1: account that can <what it must be able to do>.
- CL_1: clinic with <state it must be in>.
- Setting <name> is ON for CL_1.

## Cases

### AC_1 · <what the case shows>

1. <screen>: <action>.
2. <screen>: <action>.

Expect: <result>.

### AC_2 · <edge case>

1. <screen>: <action>.

Expect: <result>.

## Not affected

- <thing that must stay unchanged>.
```

## Rules

- Title starts with the ticket number. With none, use a short feature description, so the guide is easy to find and never duplicated.
- The case title names the account, so a step never says to log in, switch account, or open the clinic. Setup already says which account and clinic each placeholder is.
- A case starts at the first screen that differs from the case before it. Never repeat a path, login, or setting an earlier case or Setup already gave.
- One action per numbered step, at most four steps per case, at most 15 words per line. One `Expect` per case.
- Order cases normal first, then edge cases. An edge case is a case, not a separate section.
- Setup uses placeholders AC_1, AC_2 for accounts and CL_1, CL_2 for clinics, and describes the concept each needs. Give a real account only when it needs a preference only the backend can set.
- Use words from the screen: menu, button, and field names. Never write file paths, component names, code names, or implementation detail.
- List only what the change affects. Put what must stay unchanged under Not affected.
- A diagram only when a flow cannot be said in words; a simple Mermaid flowchart.
- The whole guide fits about 40 lines.
