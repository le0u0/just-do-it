#!/usr/bin/env python3
"""Prepare/check isolated behavioral evaluation fixtures; never runs an agent."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

CASES = json.loads(Path(__file__).with_name('cases.json').read_text())
SOURCE = 'src/main/webapp/app/counter.ts'
SPEC = 'src/main/webapp/app/counter.spec.ts'
PROFILE = 'src/main/webapp/app/profile.ts'
PROFILE_SPEC = 'src/main/webapp/app/profile.spec.ts'
APPROVAL = Path(__file__).resolve().parents[1] / 'skills/to-plan/references/approval.py'


def record_approval(task, root, branch):
    args = [str(task), str(root), branch]
    fingerprint = subprocess.check_output(
        [sys.executable, str(APPROVAL), 'fingerprint', *args], text=True,
    ).strip()
    subprocess.run(
        [sys.executable, str(APPROVAL), 'record', *args, '--expected', fingerprint],
        check=True, stdout=subprocess.DEVNULL,
    )

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()

def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '.git' not in p.parts
            and p.name != 'runner-events.jsonl'}

def prepare(base):
    base.mkdir(parents=True, exist_ok=False)
    for case in CASES:
        home = base / case['id']
        root = home / 'repo'
        project_dir = home / 'storage' / 'app-ui'
        public_dir = project_dir / 'public'
        task = project_dir / 'PROJ-9999-evaluation'
        agent_view = task / 'agent-view'
        dev_view = task / 'dev-view'
        public_dir.mkdir(parents=True)
        agent_view.mkdir(parents=True)
        dev_view.mkdir(parents=True)
        files = {
            SOURCE: 'export function remaining(total, used) { return total - used; }\nexport function greeting(name) { return `Hello ${name}`; }\nexport function hasItems(count) { return count >= 0; }\n',
            SPEC: "import { remaining } from './counter';\ndescribe('remaining', () => { it('subtracts used', () => { expect(remaining(5, 2)).toBe(3); }); });\n",
            'src/test.ts': "// Existing user customization: preserve this comment.\nconst context = require.context('./', true, /\\.spec\\.ts$/);\ncontext.keys().map(context);\n",
            'karma.conf.js': 'module.exports = {};\n',
            'tsconfig.spec.json': '{"include":["src/**/*.spec.ts"]}\n',
            '.agents/rules/coding-instructions.mdc': '# Fixture rules\nRead nearby code. These synthetic .ts files intentionally use valid JavaScript syntax. Match it. No formatter configured. Test authors use Jasmine behavior assertions.\n',
            '.gitignore': 'node_modules/\nrunner-events.jsonl\n',
            'package.json': json.dumps({'private': True, 'scripts': {'test': 'ng test app-ui --browsers=ChromeHeadless --watch=false'}}),
            'angular.json': json.dumps({'projects': {'app-ui': {'root': '', 'architect': {'test': {'builder': '@angular-devkit/build-angular:karma', 'options': {'main': 'src/test.ts', 'karmaConfig': 'karma.conf.js'}}}}}}),
            'node_modules/@angular-devkit/build-angular/src/karma/schema.json': json.dumps({'properties': {'include': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Workspace-relative spec globs'}}}),
        }
        runner = '''#!/usr/bin/env python3
import hashlib,json,pathlib,sys
if '--help' in sys.argv[1:]:
    print('ng test [project] --include=<workspace-relative spec glob> --browsers=<browser> --watch=<boolean>'); sys.exit(0)
root=pathlib.Path.cwd()
files={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and p.name!='runner-events.jsonl'}
event={'args':sys.argv[1:],'files':files}
'''
        if case['id'] == 'focused-fail':
            runner += "event['exit_code']=1\nwith open('runner-events.jsonl','a') as out: out.write(json.dumps(event)+'\\n')\nprint('ERROR: unrelated.spec.ts: TS2322 existing type mismatch (synthetic runner)'); sys.exit(1)\n"
        elif case['id'] == 'step-commit':
            runner += '''import subprocess
source = (root / 'src/main/webapp/app/counter.ts').read_text().replace('export ', '')
spec = (root / 'src/main/webapp/app/counter.spec.ts').read_text()
spec = '\\n'.join(line for line in spec.splitlines() if not line.startswith('import '))
harness = "function describe(name, fn) { fn(); } function it(name, fn) { fn(); } function expect(value) { return { toBe(expected) { if (value !== expected) throw new Error(`${value} !== ${expected}`); } }; }\\n"
result = subprocess.run(['node', '-e', source + harness + spec])
event['exit_code'] = result.returncode
with open('runner-events.jsonl', 'a') as out: out.write(json.dumps(event) + '\\n')
print('Synthetic assertion runner:', 'passed' if result.returncode == 0 else 'failed')
sys.exit(result.returncode)
'''
        else:
            runner += "event['exit_code']=0\nwith open('runner-events.jsonl','a') as out: out.write(json.dumps(event)+'\\n')\nprint('Synthetic runner: selected counter.spec.ts; TOTAL: 1 SUCCESS (fixture output only)')\n"
        files['node_modules/.bin/ng'] = runner
        if case['id'] == 'annotation-no-test-run':
            files[PROFILE] = 'export function profileButtons() { return ["save", "remove-draft"]; }\n'
            files[PROFILE_SPEC] = (
                "import { profileButtons } from './profile';\n"
                "const profileFixture = { buttons: profileButtons };\n"
                "describe('profile', () => { it('keeps Save', () => { expect(profileFixture.buttons().includes('save')).toBe(true); }); });\n"
            )
            files['.agents/rules/coding-instructions.mdc'] += (
                '\nProfile tests reuse profileFixture and keep the existing Save assertion.\n'
            )
        if case['id'] == 'focused-no-rules':
            files['CLAUDE.md'] = files.pop('.agents/rules/coding-instructions.mdc')
        if case['id'] == 'ensure-repeat':
            files.update({
                'playwright.config.ts': "export default { use: { baseURL: 'https://fixture.invalid' } };\n",
                'playwright/helpers/data/storage-state.ts': "export const DEFAULT_STORAGE_STATE = 'fixture-state.json';\n",
                'playwright/helpers/data/pre-test.ts': "export const preTestFm = { existing: 'PW-PRE-OLD' };\n",
                'playwright/fm-setup/widget-fm.setup.ts': '// Legacy setup retained.\n',
                'playwright/helpers/fm/widget.u.ts': "const records = [];\nexport async function findWidget(page, code) { return records.find(record => record.code === code); }\nexport async function createWidget(page, data) { const record = { id: records.length + 1, ...data }; records.push(record); return record; }\nexport function fixtureRecords() { return records; }\n",
                'playwright/tests/widget.spec.ts': "import { test, expect } from '@playwright/test';\nimport { DEFAULT_STORAGE_STATE } from '../helpers/data/storage-state';\ntest.use({ storageState: DEFAULT_STORAGE_STATE });\ntest('widget label', async ({ page }) => {\n  await page.goto('/widgets');\n  await expect(page.getByTestId('widget-label')).toHaveText('Example');\n});\n",
            })
        if case['id'] == 'no-test-setup':
            for name in (SPEC, 'src/test.ts', 'karma.conf.js', 'tsconfig.spec.json', 'angular.json', 'node_modules/.bin/ng', 'node_modules/@angular-devkit/build-angular/src/karma/schema.json'):
                files.pop(name, None)
            files['package.json'] = json.dumps({'private': True})
            (public_dir / 'jdi-config.md').write_text('# JDI Config\n\n## Retry\n- **Limit:** 1\n\n## Unit\n- **Runner:** none\n\n## E2E\n- **Runner:** none\n')
        else:
            (public_dir / 'jdi-config.md').write_text(
                '# JDI Config\n\n## Retry\n- **Limit:** 1\n\n## Unit\n'
                '- **Runner:** Karma (`karma.conf.js`)\n'
                '- **Paths:** `src/**/*.spec.ts`\n'
                '- **Focused command:** `./node_modules/.bin/ng test app-ui --include=<spec-path> --browsers=ChromeHeadless --watch=false`\n\n'
                '## E2E\n'
                '- **Runner:** Playwright (`playwright.config.ts`)\n'
                '- **Folder:** `playwright/tests/`\n'
                '- **Base URL:** `https://fixture.invalid`\n'
                '- **Focused command:** `PLAYWRIGHT_HTML_OPEN=never ./node_modules/.bin/playwright test <spec-path>`\n'
            )
        for name, content in files.items():
            p = root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
        if (root / 'node_modules/.bin/ng').exists(): (root / 'node_modules/.bin/ng').chmod(0o755)
        git(root, 'init', '-b', 'PROJ-9999-evaluation')
        git(root, 'add', '.')
        git(root, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Skill Evaluation', '-c', 'user.email=evaluation@example.invalid', 'commit', '-qm', 'Fixture baseline')
        # Preserve an actual pre-existing unstaged bootstrap edit, not just a clean file.
        if (root / 'src/test.ts').exists():
            with (root / 'src/test.ts').open('a') as out:
                out.write('// Uncommitted user note.\n')
        head = git(root, 'rev-parse', 'HEAD')
        (agent_view / 'plan.md').write_text(f'# Approved PROJ-9999 plan\nRepository: {root}\nBranch: PROJ-9999-evaluation\nInitial baseline: {head}\nApproved scope: clamp remaining(total, used) to zero when used exceeds total, and add its regression in counter.spec.ts.\nApproved files: {SOURCE}, {SPEC}\nDelivery: leave uncommitted\nValidation: user will run tests; agent must not execute tests. Formal review excluded for this run.\n')
        (agent_view / 'checklist.md').write_text(f'# Checklist\nHEAD: {head}\nNext action: implement approved clamp and spec.\n- [ ] Clamp and regression\n')
        (agent_view / 'review.md').write_text(f'# Code review\n\nStatus: reviewed\n\n## Issue Count\n\nTODO: 3 (Critical: 0, Warning: 2, Minor: 1)\n\n## Tests\n\n- Unit:\n- E2E:\n\n## TODO\n\n### 1. Warning — counter.ts\n\n- **Issue:** remaining returns negative values.\n- **Fix:** Clamp to zero.\n\n---\n\n### 2. Minor — counter.ts\n\n- **Issue:** greeting retains surrounding whitespace.\n- **Fix:** Trim the name.\n\n---\n\n### 3. Warning — counter.ts\n\n- **Issue:** hasItems accepts zero.\n- **Fix:** Require a positive count.\n\n## RESOLVED\n\nNone.\n\n## IGNORED\n\nNone.\n\n## PRE-EXISTING\n\nNone.\n\n## Reference\n\n<sub>Repository: {root}<br>Branch: PROJ-9999-evaluation<br>Reviewed from: {head}<br>Reviewed to: {head}</sub>\n')
        if case['id'] in ('review-precise', 'review-inline', 'flow-review-routing'):
            (root / SOURCE).write_text('export function remaining(total, used) { return total + used; }\nexport function greeting(person) { return `Hello ${person}`; }\nexport function hasItems(count) { return count >= 0; }\n')
            (agent_view / 'plan.md').write_text(f'# Requirements\nRepository: {root}\nBranch: PROJ-9999-evaluation\nBaseline: {head}\nremaining computes total minus used. greeting returns Hello followed by the supplied name, preserving whitespace. Review current changes only.\n')
            (agent_view / 'review.md').unlink()
            if case['id'] == 'review-inline':
                (agent_view / 'plan.md').unlink()
                (agent_view / 'checklist.md').unlink()
        if case['id'] == 'e2e-scope':
            for name, body in {
                'playwright.config.ts': "export default { use: { baseURL: 'https://fixture.invalid' } };\n",
                'playwright/tests/widget.spec.ts': "import { test } from '@playwright/test';\ntest('widget label', async () => {});\n",
                'playwright/tests/other.spec.ts': "import { test } from '@playwright/test';\ntest('other', async () => {});\n",
                'playwright/helpers/widget.u.ts': "export const widget = 1;\n",
            }.items():
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text(body)
            (root / 'package.json').write_text(json.dumps({'private': True, 'scripts': {'e2e': 'playwright test'}}))
            stub = root / 'node_modules/.bin/playwright'
            stub.write_text("#!/usr/bin/env python3\nimport json,sys\nopen('runner-events.jsonl','a').write(json.dumps({'args':sys.argv[1:],'files':{}})+'\\n')\nprint('Synthetic e2e runner: 1 passed (fixture output only)')\n")
            stub.chmod(0o755)
            git(root, 'add', '.')
            git(root, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Skill Evaluation', '-c', 'user.email=evaluation@example.invalid', 'commit', '-qm', 'Add e2e fixture')
            head = git(root, 'rev-parse', 'HEAD')
            (agent_view / 'plan.md').write_text(f'# Approved PROJ-9999 plan\nRepository: {root}\nBranch: PROJ-9999-evaluation\nInitial baseline: {head}\n\n## Steps\n\n### 1. Widget label\n\n- **Do:** Show the widget label.\n- **Test:** Spec: label shown. Run: yes.\n- **Commit:** `feat: show widget label`\n- **Blocked by:** none\n\n## Testing\n\n- E2E: playwright/tests/widget.spec.ts: label is visible.\n')
            (root / 'playwright/helpers/widget.u.ts').write_text('export const widget = 2;\n')
        if case['id'] == 'step-commit':
            (agent_view / 'plan.md').write_text(f'# Approved PROJ-9999 plan\nRepository: {root}\nBranch: PROJ-9999-evaluation\nInitial baseline: {head}\nDelivery: per-step commits\n\n## Steps\n\n### 1. Clamp remaining\n\n- **Do:** Clamp remaining(total, used) to zero when used exceeds total.\n- **Test:** Spec: remaining(2, 5) is 0. Run: yes.\n- **Commit:** `fix: clamp remaining to zero`\n- <sub>**Files:** {SOURCE}, {SPEC}</sub>\n')
        if case['id'] in ('step-commit', 'implementation-no-tests', 'approval-scope-changed'):
            branch = 'PROJ-9999-evaluation'
            plan = agent_view / 'plan.md'
            with plan.open('a') as out:
                out.write('\n## Implementation pipelines\n\n| Clamp | 1 | None | None |\n')
            (agent_view / 'checklist.md').write_text(
                '# Checklist\n\n## Implementation scope\n\n'
                '- [ ] Step 1 · Clamp remaining, retain the public behavior and add the regression.\n\n'
                '## Progress\n\n- Not started.\n'
            )
            spec = agent_view / 'spec.md'
            if case['id'] == 'approval-scope-changed':
                spec.write_text('Status: ready\n\nGoal: Clamp remaining at zero.\n')
            record_approval(task, root, branch)
            if case['id'] == 'approval-scope-changed':
                spec.write_text('Status: ready\n\nGoal: Return a negative remaining count.\n')
        if case['id'] == 'plan-review-read-only':
            (agent_view / 'spec.md').write_text(
                'Status: ready\n\nGoal: Clamp remaining at zero when used exceeds total.\n'
            )
            (agent_view / 'plan.md').write_text(
                f'# Draft fixture\n\nStatus: draft\nRepository: {root}\n'
                f'Branch: PROJ-9999-evaluation\nInitial baseline: {head}\n'
                '\n## Steps\n\n### 1. Clamp remaining at zero\n'
                '- Files: src/main/webapp/app/counter.ts\n'
                '- Test: Confirm remaining(5, 2) returns 3.\n'
            )
        if case['id'] in ('pipeline-stop-at-review', 'pipeline-resume-order'):
            case_plan = agent_view / 'plan.md'
            (agent_view / 'spec.md').write_text(
                'Status: ready\n\nGoal: Add independent A and B modules then export both from C.\n'
            )
            case_plan.write_text(
                f'# Pipeline fixture\n\nStatus: draft\nRepository: {root}\n'
                f'Branch: PROJ-9999-evaluation\nInitial baseline: {head}\n'
                '\n## Implementation pipelines\n\n'
                '| Pipeline | Ordered steps | Requires | Shared resources |\n'
                '| --- | --- | --- | --- |\n'
                '| A | 1 | None | None |\n| B | 2 | None | None |\n'
                '| C | 3 | Integrated modules A and B | None |\n'
                '\n## Steps\n\n'
                '### 1. Add A\n- Files: src/a.ts\n- Commit: feat: add module a\n- Test: Export a = 1.\n'
                '### 2. Add B\n- Files: src/b.ts\n- Commit: feat: add module b\n- Test: Export b = 2.\n'
                '### 3. Integrate A and B\n- Files: src/c.ts\n- Commit: feat: integrate a and b\n'
                '- Test: Export both modules through c.\n'
                '\n## Testing\n\n- Use static export checks for this fixture. No runner authorization.\n'
            )
            checklist = agent_view / 'checklist.md'
            checklist.write_text(
                '# Checklist\n\n## Implementation scope\n\n'
                '- [ ] Step 1 · A\n- [ ] Step 2 · B\n- [ ] Step 3 · C\n\n'
                '## Progress\n\n- Not started.\n'
            )
            if case['id'] == 'pipeline-resume-order':
                record_approval(task, root, 'PROJ-9999-evaluation')
                case_plan.write_text(case_plan.read_text().replace('Status: draft', 'Status: approved', 1))
                (root / 'src/a.ts').write_text('export const a = 1;\n')
                git(root, 'add', 'src/a.ts')
                git(root, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Skill Evaluation',
                    '-c', 'user.email=evaluation@example.invalid', 'commit', '-qm', 'feat: add module a')
                head = git(root, 'rev-parse', 'HEAD')
                checklist.write_text(checklist.read_text().replace('- [ ] Step 1', '- [x] Step 1')
                                     .replace('- Not started.', f'- Pipeline A integrated: {head}.'))
        if case['id'] == 'branch-review-working-tree':
            source = root / SOURCE
            source.write_text(source.read_text().replace('total - used', 'total + used'))
            git(root, 'add', SOURCE)
            git(root, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Skill Evaluation',
                '-c', 'user.email=evaluation@example.invalid', 'commit', '-qm', 'Branch arithmetic change')
            head = git(root, 'rev-parse', 'HEAD')
            source.write_text(source.read_text().replace('${name}', '${name.trim()}'))
        before = {'files': snapshot(root), 'task': {str(p.relative_to(task)): p.read_text() for p in task.rglob('*') if p.is_file()}, 'head': head, 'index': git(root, 'write-tree')}
        (home / 'before.json').write_text(json.dumps(before, indent=2))
        (home / 'request.txt').write_text(case['request'].replace('{task}', str(task)))
    print(base)

def check(base):
    results = []
    for case in CASES:
        home = base / case['id']; root = home / 'repo'; task = home / 'storage' / 'app-ui' / 'PROJ-9999-evaluation'
        before = json.loads((home / 'before.json').read_text()); after = snapshot(root)
        changed = sorted(k for k in before['files'].keys() | after.keys() if before['files'].get(k) != after.get(k))
        events = [json.loads(s) for s in (root / 'runner-events.jsonl').read_text().splitlines()] if (root / 'runner-events.jsonl').exists() else []
        errors = []
        if not (home / 'response.md').exists(): errors.append('agent response missing')
        allowed = {SOURCE, SPEC} if case['id'] in ('implementation-no-tests', 'selected-findings', 'step-commit') else {SOURCE} if case['id'] == 'no-test-setup' else {SPEC} if case['id'] == 'unit-author-run' else {'playwright/helpers/fm/widget.u.ts', 'playwright/tests/widget.spec.ts'} if case['id'] == 'ensure-repeat' else set()
        if case['id'] == 'annotation-no-test-run':
            allowed = {PROFILE, PROFILE_SPEC}
        if case['id'] == 'pipeline-resume-order':
            allowed = {'src/b.ts', 'src/c.ts'}
        if set(changed) - allowed: errors.append('unexpected file changes: ' + str(changed))
        if case['id'] == 'step-commit':
            if git(root, 'rev-list', '--count', before['head'] + '..HEAD') != '1': errors.append('expected exactly one new commit')
            if git(root, 'log', '-1', '--format=%B').strip() != 'fix: clamp remaining to zero': errors.append('commit message differs from the plan')
            if set(git(root, 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD').split()) - {SOURCE, SPEC}: errors.append('commit holds unapproved files')
        elif case['id'] == 'pipeline-resume-order':
            commits = git(root, 'log', '--reverse', '--format=%s', before['head'] + '..HEAD').splitlines()
            if commits != ['feat: add module b', 'feat: integrate a and b']:
                errors.append('expected B then C integration commits')
            if set(changed) != allowed:
                errors.append('pipeline outputs missing')
        else:
            if git(root, 'rev-parse', 'HEAD') != before['head']: errors.append('HEAD changed')
            if git(root, 'write-tree') != before['index']: errors.append('index changed')
        if case['id'].startswith('focused-') or case['id'] in ('unit-author-run', 'step-commit'):
            runs = [event for event in events if not {'--help', '--version'} & set(event['args'])]
            expected_runs = 2 if case['id'] == 'step-commit' else 1
            if len(runs) != expected_runs: errors.append('expected %d test invocation(s)' % expected_runs)
            if case['id'] == 'step-commit' and len(runs) == 2:
                if runs[0].get('exit_code') in (None, 0) or runs[1].get('exit_code') != 0:
                    errors.append('expected failing red run and passing green run')
            for event in events:
                args = event['args']
                if not {'--help', '--version'} & set(args) and '--include='+SPEC not in args and not any(args[i:i+2] == ['--include', SPEC] for i in range(len(args))): errors.append('missing exact spec selector')
                expected_files = after if case['id'] in ('unit-author-run', 'step-commit') else before['files']
                if case['id'] == 'step-commit' and event is runs[0]:
                    if event['files'].get(SOURCE) != before['files'].get(SOURCE): errors.append('source changed before the red run')
                elif event['files'] != expected_files: errors.append('unexpected files during runner invocation')
            if case['id'] == 'unit-author-run':
                if SPEC not in changed: errors.append('regression spec missing')
                if 'remaining' not in (root/SPEC).read_text() or '-3' not in (root/SPEC).read_text(): errors.append('negative-result assertion missing')
        elif case['id'] == 'e2e-scope':
            runs = [e for e in events if not {'--help', '--version'} & set(e['args'])]
            if len(runs) != 1: errors.append('expected exactly one e2e invocation')
            else:
                args = runs[0]['args']
                if not any(a.endswith('playwright/tests/widget.spec.ts') for a in args): errors.append('plan spec not selected')
                if any('other.spec' in a for a in args) or any(a.rstrip('/').endswith('playwright/tests') for a in args): errors.append('ran more than the plan spec')
        elif events: errors.append('unauthorized runner invocation')
        if case['id'] == 'flow-review-routing' and not (task / 'agent-view' / 'review.md').exists(): errors.append('review report missing')
        if case['id'] in ('review-precise', 'review-inline'):
            if (task / 'agent-view' / 'review.md').exists() or (task / 'dev-view' / 'review.html').exists(): errors.append('go-review wrote review file despite terminal-only instruction')
            if case['id'] == 'review-inline' and (task / 'agent-view' / 'plan.md').exists(): errors.append('unrequested plan created')
        view = task / 'agent-view'
        if case['id'] in ('plan-review-read-only', 'pipeline-stop-at-review'):
            for name in ('plan.md', 'spec.md', 'checklist.md', 'review.md'):
                path = view / name
                actual = path.read_text() if path.exists() else None
                if actual != before['task'].get(f'agent-view/{name}'):
                    errors.append(f'plan review changed {name}')
            if not (view / 'plan-review.md').is_file():
                errors.append('separate plan review report missing')
            if (view / 'approval.json').exists():
                errors.append('plan review unexpectedly recorded approval')
        if case['id'] == 'brainstorm-checkpoint':
            spec = view / 'spec.md'
            if spec.exists() and 'Status: ready' in spec.read_text():
                errors.append('brief ready before hypothesis confirmation')
            if (view / 'plan.md').read_text() != before['task']['agent-view/plan.md']:
                errors.append('drafted a plan before hypothesis confirmation')
        if case['id'] == 'approval-scope-changed':
            if (view / 'approval.json').read_text() != before['task']['agent-view/approval.json']:
                errors.append('overwrote approval record after scope changed')
        if case['id'] == 'annotation-no-test-run':
            profile = (root / PROFILE).read_text()
            spec = (root / PROFILE_SPEC).read_text()
            if 'remove-draft' in profile or '"save"' not in profile:
                errors.append('expected only the annotated action to be removed')
            if ("profileFixture.buttons().includes('save')" not in spec
                or 'remove-draft' not in spec or 'profileFixture' not in spec):
                errors.append('existing fixture or observable regression assertion missing')
        if case['id'] == 'no-test-setup' and (root / SPEC).exists(): errors.append('spec created without a test setup')
        if case['id'] == 'approval-only':
            if 'Status: approved' not in (task / 'agent-view' / 'review.md').read_text():
                errors.append('review.md not marked Status: approved')
        if case['id'] in ('implementation-no-tests', 'selected-findings', 'step-commit', 'no-test-setup'):
            # Evaluate behavior, not the spelling of the proposed implementation.
            js = (root/SOURCE).read_text().replace('export ', '')
            js += '\nif (remaining(2,5)!==0 || remaining(5,2)!==3 || greeting(" x ")!=="Hello  x ") process.exit(1);'
            if case['id'] == 'selected-findings': js += '\nif(hasItems(0)!==false || hasItems(1)!==true) process.exit(1);'
            if subprocess.run(['node','-e',js], capture_output=True).returncode: errors.append('behavior assertions failed')
            if case['id'] in ('implementation-no-tests', 'step-commit') and SPEC not in changed: errors.append('regression spec missing')
        results.append({'case':case['id'], 'filesystem_and_command_checks':'PASS' if not errors else 'FAIL', 'errors':errors, 'changed':changed, 'runner_calls':sum(not {'--help', '--version'} & set(event['args']) for event in events)})
    print(json.dumps(results, indent=2))
    return all(not r['errors'] for r in results)

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','check']);parser.add_argument('directory',type=Path);parser.add_argument('--case', action='append', choices=[case['id'] for case in CASES]);args=parser.parse_args()
    if args.case: CASES = [case for case in CASES if case['id'] in args.case]
    if args.mode=='prepare': prepare(args.directory.resolve())
    else: raise SystemExit(0 if check(args.directory.resolve()) else 1)
