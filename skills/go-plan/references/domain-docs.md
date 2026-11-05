# Domain Docs

Domain notes are a glossary and ADRs.

## Rules

- Read what the caller supplies and the repository's own `GLOSSARY.md` and `docs/adr/`.
- Write no files. After the user confirms in the conversation, return a new or changed term as a glossary row, or an accepted decision as an ADR; the caller saves it.

## While asking

- Ticket word conflicts with a glossary term: ask which meaning.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary

```markdown
| Term | Meaning | Avoid |
| --- | --- | --- |
| Export button | Toolbar button that downloads the current view. | Download link |
```

- One sentence per meaning, no implementation details.

## ADR

- Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off.
- Once accepted, return a title and one to three sentences: context, decision, why.
