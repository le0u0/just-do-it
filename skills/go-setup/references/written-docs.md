# Written Docs

Applies to every markdown file an agent writes in `agent-view/`, `dev-view/`, and `public/` (`research.md`, `plan.md`, `checklist.md`, `commit-format.md`, `diagnose.md`, `CHANGELOG.md`, `review.md`, `ut.md`, `e2e.md`, `glossary.md`, `adr/*.md`, `jdi-config.md`). (`CHANGELOG.md` uses the standard `# Changelog` / `### Features` / `* <summary> (<sha>)` format per [storage.md](storage.md).)

- Write only docs [storage.md](storage.md) lists; create when missing, update in place otherwise. No `plan_2.md`.
- One line per point, at most 15 words unless the doc's format says otherwise.
- Fragments; drop articles, filler, hedging, restated context: "Export button shows when flag off. Hide it."
- Code, identifiers, paths, error strings exact.
- Present state only: no history, dates, other findings, decision path.
- Detail the next reader needs to act goes in the point; reference detail in `<sub>`.
