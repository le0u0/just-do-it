# Domain Docs

Domain notes are a glossary and ADRs.

## Rules

- Read what the caller supplies and the repository's own `GLOSSARY.md` and `docs/adr/`, if present. Leave them unedited.
- This skill writes no files: return a confirmed term or ADR in the reply, the caller saves it.
- Return a new or changed term as a glossary row, and an accepted decision as an ADR, only after the user confirms in the conversation.

## While asking

- Ticket word conflicts with a glossary term: ask which meaning is intended.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary

One table:

```markdown
| Term | Meaning | Avoid |
| --- | --- | --- |
| Export button | Toolbar button that downloads the current view. | Download link |
```

- Return a row only after the user confirms the term and its meaning.
- One sentence per meaning, no implementation details.

## ADR

- Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off.
- After the user accepts, return a title, then one to three sentences: context, decision, why.
