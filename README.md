# just-do-it

A manager that plans, builds, tests and reviews a ticket with subagents. The process lives here; the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

## Install

```text
/plugin marketplace add le0u0/le0u0.ai
/plugin install just-do-it@le0u0.ai
```

## Use

```text
/just-do-it:start-manager on
```

- Describe the work. The manager assigns subagents, runs the rest, checks results, reports briefly.
- End with `/just-do-it:start-manager off`.
- Every skill also works alone. `go-*` skills return results in the reply and write no files.

## Manager

- Runs `go-plan`, `go-work` and `go-fix` in the main thread, so it can ask you questions.
- Starts a subagent per other job and announces model and effort. Tell it a preference and it uses that.
- Saves every returned document in `~/.just-do-it/{project}/{branch}/`.
- More in [architecture](docs/architecture/ARCHITECTURE.md).
- Each skill has a doc in [`docs/`](docs/), such as [`docs/go-review.md`](docs/go-review.md): what it does, when to use it, signs it works, and its chain.

| Skill | Model |
| --- | --- |
| `go-review` | opus medium |
| `go-e2e` | sonnet medium |
| `go-triage` | haiku low |

## Skills you call

| Skill | Job |
| --- | --- |
| `dev-tdd` | Test-first loop over `go-ut` and `go-e2e` |
| `to-pr` | PR title and body |
| `to-test-md` | Manual testing guide as Markdown |
| `to-test-html` | QA page built from that guide |
| `to-charsiu` | Restate the last message in plain language |

`to-*` skills never run on their own.

## Credits

- `dev-tdd` follows Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill.
- `to-pr` follows Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill.
- `go-e2e` borrows from lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill).
