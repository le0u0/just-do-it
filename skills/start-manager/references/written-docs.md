# Written Docs

Applies to every markdown file an agent writes, such as `plan.md`, `triage.md`, `diagnose.md`, `checklist.md`, `jobs.md`, `review.md`.

## Files

- Write only the docs [storage.md](storage.md) lists.
- Missing: create it. Existing: update it in place.
- A second version gets no new file, such as `plan_2.md`.

## Style

- Every point is one line, at most 15 words, unless the doc's own format sets another limit. Split or cut longer ones.
- Fragments. Drop articles, filler, hedging, restated context: "Export button shows when flag off. Hide it." not "The Export button is currently displayed even though the preference is disabled, so it should be hidden."
- Code, identifiers, paths, error strings stay exact.
- Present state only: no history, dates, other findings, how a decision was reached.
- Detail only the next reader needs to act goes in the point; reference detail goes in `<sub>`.
