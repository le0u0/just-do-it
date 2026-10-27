# Domain Docs

Domain notes live in `~/.just-do-it/{project}/docs/`, never in a repository, so every branch and agent of a project sees the same definitions.

```text
~/.just-do-it/{project}/docs/glossary.md
~/.just-do-it/{project}/docs/adr/0001-slug.md
```

Read the repository's own `GLOSSARY.md` and `docs/adr/` too, if present, and leave them unedited.

## When docs change

Only `think` and `plan`, and only after the user confirms in the conversation: a new or changed term goes to the glossary, an accepted decision becomes an ADR. Every other skill reads them and never writes; `develop` and `review` use them for naming and to respect past decisions.

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

Add a row only after the user confirms the term and its meaning. Keep one sentence per meaning and no implementation details.

## ADR

Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off. After the user accepts, write the next numbered file in `~/.just-do-it/{project}/docs/adr/`: a title, then one to three sentences of context, decision, and why.
