# agent-workflow

A manager that plans, builds, tests and reviews a ticket with specialist agents. It works in any project: the process lives here, the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

```text
/plugin install agent-workflow@plugins
```

## Use

```text
/agent-workflow:manager on
```

Describe the work. The manager assigns each job to an agent, checks the result, and reports in a few lines. Run `/agent-workflow:manager off` to end it. Every skill also works on its own.

## Agents

| Agent | Skills | Model |
| --- | --- | --- |
| `planner`, `senior-planner` | `think`, `plan` | opus medium, opus high |
| `developer`, `senior-developer` | `develop`, `resolve-review`, `pr`, `testing-guide` | sonnet medium, opus medium |
| `reviewer`, `senior-reviewer` | `review` | opus medium, opus high |
| `e2e-tester` | `write-e2e`, `run-e2e` | sonnet medium |
| `helper` | `triage-ticket` | haiku low |

The manager uses `planner`, `developer`, `reviewer` and `helper` by default, and asks you before using another.

Plugin docs are saved in `~/.agent-workflow/{project}/{branch}/`. More in [architecture](docs/architecture/ARCHITECTURE.md).

## Credits

- `develop` follows Matt Pocock's [tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) skill.
- `pr` follows Matt Pocock's [pr](https://github.com/mattpocock/skills/tree/main/skills/engineering/pr) skill.
- `write-e2e` borrows from lackeyjb's [playwright-skill](https://github.com/lackeyjb/playwright-skill).
