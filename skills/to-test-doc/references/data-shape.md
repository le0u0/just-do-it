# Data Shape

The template holds a sample guide between two markers: `const DATA=/*DATA*/{...}/*END*/;`. Replace the JSON between `/*DATA*/` and `/*END*/` with the guide as JSON. The sample lets the template preview as is. Change nothing else in the template, except to add a language (see Substitute).

## JSON

```json
{
  "ticket": "PROJ-123",
  "link": "https://example.atlassian.net/browse/PROJ-123",
  "slug": "testing-guide",
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
          "id": "case-1",
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
- `slug`: `"testing-guide"` (or short identifier for the branch).
- `languages`: keys shown, first is default. The template ships `en` and `zh`. Omit for English only (hides the switch).
- Every text is an object with one key per language. A missing key falls back to the first.
- `note` is optional. Tests number across the whole guide.
- `id`: unique stable ID for each test, matching `[a-z0-9-]+`. Generate a fresh UUID for each new test. Keep the same ID when wording or position changes; never reuse a removed test's ID for another test. IDs preserve saved results.

## Convert the guide

1. `# PROJ-123: feature name` gives `ticket` and `title`. The `[PROJ-123](link)` line gives `link`.
2. `## Before you start` bullets give `setup`, one `text` each. No such section: `"setup": []`, and the page shows none.
3. Each later `##` heading gives `name`; its one-line paragraph gives `why`.
4. Each `### Test N:` gives `title`; optional paragraph `note`; numbered steps `steps`; `You should see:` line `expect`.
5. Keep the guide's wording. Write English only; `Translate` adds the other languages.

## Translate

The guide's languages are always `en` and `zh` (Traditional Chinese). The main session writes `en`; a `fast` subagent writes `zh`.

1. Spawn one `fast` subagent (per [host mapping](../../go-flow/references/agents.md#host-mapping)). Give it the repository path and the list of English texts (every `title`, `setup`, `name`, `why`, `note`, step and `expect`), each with a key.
2. It first greps the repository's translation files (i18n, locales, `zh*.json`) for each menu, button and field name, and uses the repo's own Chinese term. No match: it then greps `~/.just-do-it/{project}/public/glossary.md` and the branch folder (`agent-view/research.md`, `agent-view/plan.md`, `agent-view/attachments/`) for the term. Still no match: it translates plainly and marks the key `guess`.
3. It returns `{key: zh}` only, plus the `guess` keys. Add them as `zh`; report the `guess` keys under `Open`.

## Substitute

1. Serialize with `JSON.stringify`.
2. Escape every `<` as `\u003c`, so `</script>` and `<!--` cannot occur.
3. Replace the text between `/*DATA*/` and `/*END*/` in [qa-template.html](qa-template.html) once, and replace `<!--PDF_BUNDLE-->` with the raw contents of `../assets/pdf-bundle.html` via script/command (never read `assets/pdf-bundle.html` into agent context).
4. Add a language only when the project has one the template lacks: add it to `ALL_LANGS` and `UI`, with every key of the existing entries.

## Preserve results

- When updating an existing `dev-view/testing-guide.html`, read its DATA first. Match tests by meaning, reuse each matching `id`, and assign new unique IDs to new or materially changed tests. If a match is uncertain, ask before carrying results over.
- For an older guide without IDs, assign IDs to matching tests and add `legacy` to the new DATA: `sig` is the old guide's hash of `JSON.stringify(oldData.groups)` using the template's `sig` algorithm; `ids` is the old test order, with each matching new ID or `null` for a removed test. Example: `"legacy": {"sig": "abc123", "ids": ["case-1", null]}`. The page migrates the old saved results only from that exact hash.
- Keep `legacy` on later updates until the old guide no longer needs migration. Do not change `ticket` or `slug` for the same guide.
