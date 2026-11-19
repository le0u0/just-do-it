# just-do-it

A manager that plans, builds, tests and reviews a ticket with subagents. The process lives here; the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

Supports Claude Code, Codex and Antigravity.

## Install

<details>
<summary>Claude Code</summary>

```text
/plugin marketplace add le0u0/le0u0.ai
/plugin install just-do-it@le0u0.ai
```

</details>

<details>
<summary>Codex</summary>

```bash
codex plugin marketplace add le0u0/le0u0.ai
codex plugin add just-do-it@le0u0-ai
```

</details>

<details>
<summary>Antigravity</summary>

```bash
agy plugin install https://github.com/le0u0/just-do-it
```

</details>

## Use

`justaway on` starts manager mode; `justaway off` stops it.

`go-*`, `dev-*` and `to-*` work without manager mode. `go-review` starts its own review team; `to-test-html` starts its translation worker. `justaway` coordinates the full ticket workflow.

| Step | What happens |
| --- | --- |
| Describe the work | The coordinator assigns workers, checks results, and handles approvals and delivery |
| Done | Turn manager mode off |
| One job only | Call a skill directly. Output follows its delivery rules |

## Manager

| Stage | Worker | Tier |
| --- | --- | --- |
| Ticket or requirements link | [`go-research`](docs/go-research.md) | fast |
| Grill and plan | [`go-plan`](docs/go-plan.md) | reasoning |
| Implementation | [`go-work`](docs/go-work.md), one worker per step. Independent TDD steps run in parallel | standard |
| E2E | [`go-e2e`](docs/go-e2e.md) | standard |
| Review | [`go-review`](docs/go-review.md), run by the coordinator with its own team | Fetch and recheck fast, hunters standard, verifier reasoning |

| Tier | Claude | Codex | Antigravity (preferred family) |
| --- | --- | --- | --- |
| `fast` | `haiku (low)` | `luna (low)` | `flash (low)` |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `reasoning` | `opus (medium)` | `sol (medium)` | `neon (medium)` |

Model families resolve from the active host's worker options. Antigravity uses Swarm with `workspace="inherit"` and the selected model variant. Legacy dispatch is reserved for tracker research that needs MCP access. See [Antigravity dispatch](skills/justaway/references/agents.md#antigravity-dispatch).

| Also | Detail |
| --- | --- |
| Announces | Model and effort per subagent; tell it a preference and it uses that |
| Delivers | Research, plan, review, PR, and QA outputs save to a resolved task directory in manager mode. Otherwise choose save or terminal output |
| Docs | [Architecture](docs/architecture/ARCHITECTURE.md); one doc per skill in [`docs/`](docs/), such as [`docs/go-review.md`](docs/go-review.md) |

## Skills you call

| Skill | Job |
| --- | --- |
| `dev-tdd` | Test-first loop over `go-ut` and `go-e2e` |
| `to-pr` | PR title and body |
| `to-test-md` | Manual testing guide as Markdown |
| `to-test-html` | QA page built from that guide |
| `to-charsiu` | Restate the last message in plain language |
| `to-handoff` | Cross-team issue, requirement, or handoff report (BE, FE, DevOps, etc.) |

`to-*` skills never run on their own.

## Credits

| Skill | Follows |
| --- | --- |
| `dev-tdd` | Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill |
| `to-pr` | Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill |
| `go-e2e` | lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill) |
