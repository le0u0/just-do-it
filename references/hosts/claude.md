# Claude

Map each tier to Claude's model and effort:

| Tier | Model |
| --- | --- |
| `standard` | `sonnet (medium)` |
| `deep` | `opus (medium)` |

| Spawn & model | Collect results | Cleanup |
| --- | --- | --- |
| `general-purpose` (`model`, `effort` if supported), with the assigned root in the prompt | `SendMessage` by ID | — |

Resolve the selectable model in the named tier from the host catalog. Report when that model, its effort, or fresh context is unavailable. A user-requested model and effort replaces the tier when supported.
