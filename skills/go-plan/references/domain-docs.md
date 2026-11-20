# Domain Docs (`public/glossary.md` and `public/adr/`)

Domain notes live in `~/.just-do-it/{project}/public/glossary.md` and `~/.just-do-it/{project}/public/adr/` per [public-docs.md](../../go-setup/references/public-docs.md).

## Rules

- Read `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), plus the repository's own `GLOSSARY.md` and `docs/adr/`.
- **Never guess** unknown domain terminology, product terms, internal abbreviations, or business concepts. Always ask the user.
- Once the user confirms a term or decision, write or update `~/.just-do-it/{project}/public/glossary.md` or `~/.just-do-it/{project}/public/adr/NNN-short-title.md` (creating the file on demand if it does not exist yet).

## While asking

- Unknown domain term or product concept: ask what it means and where it lives in the UI or code.
- Ticket word conflicts with an existing glossary term: ask which meaning applies.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary (`~/.just-do-it/{project}/public/glossary.md`)

```markdown
# Glossary

| Term | Meaning | Context / Location | Avoid |
| --- | --- | --- | --- |
| Export button | Toolbar button that downloads the current view. | `src/toolbar.ts` | Download link |
```

- One sentence per meaning; include UI/code context when helpful.

## ADR (`~/.just-do-it/{project}/public/adr/NNN-short-title.md`)

- Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off.
- Once accepted by the user, save `public/adr/NNN-short-title.md` with title, `Context`, `Decision`, and `Why` (one line each).
