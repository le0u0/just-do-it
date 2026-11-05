# just-do-it

A manager that plans, builds, tests and reviews a ticket with subagents. It works in any project: the process lives here, the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

## Install

```text
/plugin marketplace add le0u0/le0u0.ai
/plugin install just-do-it@le0u0.ai
```

## Use

```text
/just-do-it:start-manager on
```

Describe the work. The manager assigns jobs to subagents, runs the rest itself, checks the result, and reports in a few lines. Run `/just-do-it:start-manager off` to end it. Every skill also works on its own: `go-*` skills return their result in the reply and write no files, so `/go-plan` prints the plan and `/go-work` just implements.

## Subagents

The manager starts a subagent per job, naming the skill and setting the model and effort per skill. It announces both each time; tell it a preference and it uses that.

| Skill | Model |
| --- | --- |
| `go-review` | opus medium |
| `go-e2e` | sonnet medium |
| `go-triage` | haiku low |

The manager runs `go-plan`, `go-work` and `go-fix` itself, in the main thread, so it can ask you questions directly, and saves every document the skills return.

## Skills you call

| Skill | Job |
| --- | --- |
| `dev-tdd` | Test-first loop over `go-ut` and `go-e2e` |
| `to-pr` | PR title and body |
| `to-test-md` | Manual testing guide as Markdown |
| `to-test-html` | QA page built from that guide |
| `to-charsiu` | Restate the last message in plain language |

`to-*` skills never run on their own; you call them.

Plugin docs are saved in `~/.just-do-it/{project}/{branch}/`. More in [architecture](docs/architecture/ARCHITECTURE.md).

## Credits

- `dev-tdd` follows Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill.
- `to-pr` follows Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill.
- `go-e2e` borrows from lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill).
