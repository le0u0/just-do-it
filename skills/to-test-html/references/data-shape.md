# Data Shape

The template holds one placeholder: `const DATA=/*DATA*/null;`. Replace `/*DATA*/null` with the guide as JSON. Change nothing else in the template, except to add a language (see Substitute).

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

- `ticket`: the key from the guide's lead line, or a short feature name with no ticket. It keys the saved progress and names the export file.
- `link`, `related`: optional. `related` comes from the guide's `Related:` line.
- `slug`: the `{short-description}` of the guide file name.
- `languages`: language keys shown, first one is the default. The template ships `en` and `zh`. Omit for English only, which hides the language switch.
- Every text is an object with one key per entry in `languages`. A missing key falls back to the first language.
- `note` is optional per test. Tests number across the whole guide.

## Convert the guide

1. `# PROJ-123: feature name` gives `ticket` and `title`; the `[PROJ-123](link)` line gives `link`.
2. `## Setup` bullets `- AC_1: text` give `setup`.
3. Each `## Group:` heading gives `name`; its one-line paragraph gives `why`.
4. Each `### Test N:` gives `title`; the optional paragraph is `note`; numbered steps are `steps`; the `Expect:` line is `expect`.
5. Keep the guide's wording. For each extra language, translate with the project's translation files.

## Substitute

1. Serialize with `JSON.stringify`.
2. Escape every `<` as `<`, so `</script>` and `<!--` cannot occur.
3. Replace the text `/*DATA*/null` once.
4. Add a language only when the project has one the template lacks: add it to `ALL_LANGS` and to `UI`, with every key of the existing entries.
