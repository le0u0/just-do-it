# Domain Docs

Domain notes are a glossary and ADRs. Read those the caller supplies and the repository's own `GLOSSARY.md` and `docs/adr/`, if present, and leave them unedited. This skill writes no files: it returns a confirmed term or ADR in the reply, and the caller saves it.

## When docs change

Only after the user confirms in the conversation: return a new or changed term as a glossary row, and an accepted decision as an ADR, for the caller to save.

## While asking

- Ticket word conflicts with a glossary term: ask which meaning is intended.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary

`glossary.md` is one table:

```markdown
| Term | Meaning | Avoid |
| --- | --- | --- |
| Export button | Toolbar button that downloads the current view. | Download link |
```

Return a row only after the user confirms the term and its meaning. Keep one sentence per meaning and no implementation details.

## ADR

Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off. After the user accepts, return the ADR: a title, then one to three sentences of context, decision, and why.
