# Project References

Read applicable project [standards and ADRs](../../go-setup/references/public-docs.md#standardsmd) from shared storage. Apply repository rules first and verify cited precedents.

The project owns its rules. Before the review pass, read what applies:

- `AGENTS.md`, `CLAUDE.md`, `REVIEW.md` (what matters most here and what to skip), and the active host's rules (only the ones the caller lists, if any).
- Matching project-local skills for the active host; they win over this skill's defaults.
- `~/.just-do-it/{project}/public/glossary.md` and `public/adr/` (when present), plus repository `GLOSSARY.md` and `docs/adr/`; use terms as written.
- The nearest comparable feature or spec.

Nothing applies: say so, follow nearest comparable code. Cite rules; do not copy them.
