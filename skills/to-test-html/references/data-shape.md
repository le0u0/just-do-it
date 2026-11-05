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
  "setup": [{ "id": "AC_1", "text": { "en": "...", "zh": "..." } }],
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
2. `## Setup` bullets `- AC_1: text` give `setup`.
3. Each `## Group:` heading gives `name`; its one-line paragraph gives `why`.
4. Each `### Test N:` gives `title`; optional paragraph `note`; numbered steps `steps`; `Expect:` line `expect`.
5. Keep the guide's wording. Translate extra languages with the project's translation files.

## Substitute

1. Serialize with `JSON.stringify`.
2. Escape every `<` as `\u003c`, so `</script>` and `<!--` cannot occur.
3. Replace the text between `/*DATA*/` and `/*END*/` once.
4. Add a language only when the project has one the template lacks: add it to `ALL_LANGS` and `UI`, with every key of the existing entries.
