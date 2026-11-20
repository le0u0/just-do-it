# just-do-it

Independent skills that research, plan, build, test and review a ticket. The process lives here; the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

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

Call any skill directly, or call [`go-flow`](docs/go-flow.md) to chain the full ticket pipeline (`go-setup` → `go-research` → `go-plan` → parallel `go-work` → `go-review` → `go-fix`) or the steps you choose.

Every skill writes its output to your branch storage folder (`agent-view/` and `dev-view/`), initializing it with [`go-setup`](docs/go-setup.md) after confirming the project name with you.

## Skills

| Skill | Job | Tier |
| --- | --- | --- |
| [`go-setup`](docs/go-setup.md) | Confirm project and set up branch storage (`agent-view/`, `dev-view/`, `public/`) | — |
| [`go-research`](docs/go-research.md) | Read ticket or requirements link and map repo paths | fast |
| [`go-plan`](docs/go-plan.md) | Grill goal, decisions, and unknown terms, then write plan and checklist | reasoning |
| [`go-work`](docs/go-work.md) | Implement one step test-first (`dev-tdd`). Independent steps run in parallel in `go-flow` | standard |
| [`go-ut`](docs/go-ut.md) | Write, fix, or run focused unit specs | standard |
| [`go-e2e`](docs/go-e2e.md) | Explore UI, author, run, or debug Playwright E2E specs | standard |
| [`go-review`](docs/go-review.md) | Confirm review goal, run review team, and link test results | Fetch and recheck fast, hunters standard, verifier reasoning |
| [`go-fix`](docs/go-fix.md) | Fix selected review findings and record dispositions | — |
| [`go-flow`](docs/go-flow.md) | Run the full pipeline or a chosen sequence of steps | — |

| Tier | Claude | Codex | Antigravity (preferred family) |
| --- | --- | --- | --- |
| `fast` | `haiku (low)` | `luna (low)` | `flash (low)` |
| `standard` | `sonnet (medium)` | `terra (medium)` | `hydrogen (medium)` |
| `reasoning` | `opus (medium)` | `sol (medium)` | `neon (medium)` |

Model families resolve from the active host's worker options. Antigravity uses Swarm with `workspace="inherit"` and the selected model variant. Legacy dispatch is reserved for tracker research that needs MCP access. See [Antigravity dispatch](skills/go-flow/references/agents.md#antigravity-dispatch).

| Also | Detail |
| --- | --- |
| Announces | Model and effort per subagent; tell it a preference and it uses that |
| Storage | Outputs save to `agent-view/` and `dev-view/` under the project's branch directory; shared glossary, ADRs, and test config live in `public/`. See [Storage](skills/go-setup/references/storage.md) |
| Docs | [Architecture](docs/architecture/ARCHITECTURE.md); one doc per skill in [`docs/`](docs/), such as [`docs/go-review.md`](docs/go-review.md) |

## Method & Utility Skills

| Skill | Job |
| --- | --- |
| [`dev-tdd`](docs/dev-tdd.md) | Test-first loop over `go-ut` and `go-e2e` |
| [`to-pr`](docs/to-pr.md) | PR title and body |
| [`to-test-doc`](docs/to-test-doc.md) | Manual testing guide as Markdown or interactive HTML QA page |
| [`to-handoff`](skills/to-handoff/SKILL.md) | Cross-team issue, requirement, or handoff report (BE, FE, DevOps, etc.) |
| [`to-charsiu`](docs/to-charsiu.md) | Restate the last message in plain language |

## Credits

| Skill | Follows |
| --- | --- |
| `dev-tdd` | Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill |
| `to-pr` | Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill |
| `go-e2e` | lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill) |
