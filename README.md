# just-do-it

A manager that plans, builds, tests and reviews a ticket with specialist agents. It works in any project: the process lives here, the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

## Install

```text
/plugin marketplace add le0u0/le0u0.ai
/plugin install just-do-it@le0u0.ai
```

## Use

```text
/just-do-it:manager on
```

Describe the work. The manager assigns each job to an agent, checks the result, and reports in a few lines. Run `/just-do-it:manager off` to end it. Every skill also works on its own.

## Roles

The manager starts a subagent per job, naming the skill and setting the model and effort. It announces both each time; tell it a preference and it uses that.

| Role | Skills | Model |
| --- | --- | --- |
| `developer` | `develop`, `resolve-review`, `pr`, `testing-guide` | sonnet medium |
| `reviewer` | `review` | opus medium |
| `e2e-tester` | `write-e2e`, `run-e2e` | sonnet medium |
| `helper` | `triage-ticket` | haiku low |

The manager runs `plan` itself, in the main thread, so it can ask you questions directly.

Plugin docs are saved in `~/.just-do-it/{project}/{branch}/`. More in [architecture](docs/architecture/ARCHITECTURE.md).

## Credits

- `develop` follows Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill.
- `pr` follows Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill.
- `write-e2e` borrows from lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill).
