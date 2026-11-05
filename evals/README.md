# Evals

Behavioral cases for the skills: file changes and executed commands, not just frontmatter and links.

## Run

1. Prepare disposable fixtures outside any real checkout (git repos, synthetic test runner, nothing installed):

   ```bash
   python3 evals/fixture.py prepare /private/tmp/just-do-it-evals-UNIQUE
   ```

2. Per case in `cases.json`, give a fresh agent only the skill path (from `skills/`, not an installed cache), the generated `request.txt` and the `repo` directory. It saves its final answer as `response.md` beside `repo`. Withhold `checks`, `before.json` and the fixture script.
3. Check files and commands:

   ```bash
   python3 evals/fixture.py check /private/tmp/just-do-it-evals-UNIQUE
   ```

4. Read traces and responses against each case's `checks`. For manager cases, confirm each handoff and no extra subagents.
5. Repeat without the skill as a baseline. A case passing both ways may be redundant: shorten it unless it guards safety, approval or scope.

Run a subset with `--case CASE_ID` (repeatable) on `prepare` and `check`.

## Limits

- The runner is synthetic. It logs arguments and file hashes per call, so it catches config or spec edits that narrow a run.
- It cannot validate real tests, browsers or ticket tools.
- A failing focused command stays a reported failure.
