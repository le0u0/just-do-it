# Data Shape

The template holds a sample guide between two markers: `const DATA=/*DATA*/{...}/*END*/;`. Replace the JSON between `/*DATA*/` and `/*END*/` with the guide as JSON. The sample lets the template preview as is. Change nothing else in the template, except to add a language (see Substitute).

## JSON

```json
{
  "ticket": "PROJ-123",
  "link": "https://example.atlassian.net/browse/PROJ-123",
  "slug": "short-description",
  "languages": ["en", "zh"],
  "related": [{ "key": "PROJ-100", "link": "https://...", "role": "blocks" }],
  "title": { "en": "Feature name", "zh": "功能名稱" },
  "setup": [{ "text": { "en": "...", "zh": "..." } }],
  "groups": [
    {
      "name": { "en": "...", "zh": "..." },
      "why": { "en": "...", "zh": "..." },
      "tests": [
        {
          "title": { "en": "...", "zh": "..." },
          "note": { "en": "...", "zh": "..." },
          "steps": [{ "en": "...", "zh": "..." }],
          "expect": { "en": "...", "zh": "..." }
        }
      ]
    }
  ]
}
```

## Fields

- `ticket`: key from the lead line, else a short feature name. Keys saved progress and the export file name.
- `link`, `related`: optional; `related` is the guide's `Related:` line.
- `slug`: `{short-description}` of the guide file name.
- `languages`: keys shown, first is default. The template ships `en` and `zh`. Omit for English only (hides the switch).
- Every text is an object with one key per language. A missing key falls back to the first.
- `note` is optional. Tests number across the whole guide.

## Convert the guide

1. `# PROJ-123: feature name` gives `ticket` and `title`. The `[PROJ-123](link)` line gives `link`.
2. `## Before you start` bullets give `setup`, one `text` each. No such section: `"setup": []`, and the page shows none.
3. Each later `##` heading gives `name`; its one-line paragraph gives `why`.
4. Each `### Test N:` gives `title`; optional paragraph `note`; numbered steps `steps`; `You should see:` line `expect`.
5. Keep the guide's wording. Write English only; `Translate` adds the other languages.

## Translate

The guide's languages are always `en` and `zh` (Traditional Chinese). The main session writes `en`; a subagent writes `zh`, so the main session never spends tokens on it.

1. Spawn one `Agent` with `model: "haiku"`. Give it the repository path and the list of English texts (every `title`, `setup`, `name`, `why`, `note`, step and `expect`), each with a key.
2. It first greps the repository's translation files (i18n, locales, `zh*.json`) for each menu, button and field name, and uses the repo's own Chinese term. No match: it then greps the branch folder (`~/.just-do-it/{project}/{branch}/`, see [storage.md](../../justaway/references/storage.md); present when the manager ran the work) for the term in `triage.md`, `plan.md` and `attachments/`. Still no match: it translates plainly and marks the key `guess`.
3. It returns `{key: zh}` only, plus the `guess` keys. Add them as `zh`; report the `guess` keys under `Open`.

## Substitute

1. Serialize with `JSON.stringify`.
2. Escape every `<` as `\u003c`, so `</script>` and `<!--` cannot occur.
3. Replace the text between `/*DATA*/` and `/*END*/` once.
4. Add a language only when the project has one the template lacks: add it to `ALL_LANGS` and `UI`, with every key of the existing entries.
