#!/usr/bin/env python3
"""Record or verify the user-approved scope of a just-do-it task."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


def scope_fingerprint(task: Path, repository: Path, branch: str) -> str:
    view = task / "agent-view"
    plan = (view / "plan.md").read_text(encoding="utf-8")
    checklist = (view / "checklist.md").read_text(encoding="utf-8")
    prefix, separator, sections = plan.partition("\n## ")
    prefix = re.sub(r"^Status:.*$", "Status: <approval>", prefix, count=1, flags=re.M)

    headers = list(re.finditer(r"^## ([^\n]+)$", checklist, re.M))
    scope = [i for i, header in enumerate(headers) if header[1] == "Implementation scope"]
    if len(scope) != 1:
        raise ValueError("checklist must contain exactly one Implementation scope section")
    index = scope[0]
    end = headers[index + 1].start() if index + 1 < len(headers) else len(checklist)
    authored_scope = checklist[headers[index].end():end]
    authored_scope = re.sub(r"^- \[[ xX]\]", "- [ ]", authored_scope, flags=re.M)
    spec = view / "spec.md"
    inputs = [
        str(repository.resolve(strict=True)), branch, str(task.resolve(strict=True)),
        spec.read_bytes().hex() if spec.exists() else None,
        prefix + separator + sections, authored_scope,
    ]
    return hashlib.sha256(json.dumps(inputs, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def update_approval(task: Path, repository: Path, branch: str, expected: str) -> None:
    fingerprint = scope_fingerprint(task, repository, branch)
    if fingerprint != expected:
        raise ValueError("scope changed since presentation; request approval of the current draft")
    record = task / "agent-view" / "approval.json"
    data = {
        "fingerprint": fingerprint, "repository": str(repository.resolve(strict=True)),
        "branch": branch, "task": str(task.resolve(strict=True)),
    }
    path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=record.parent, delete=False,
        ) as temporary:
            path = Path(temporary.name)
            json.dump(data, temporary, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
        if scope_fingerprint(task, repository, branch) != expected:
            raise ValueError("scope changed while recording approval")
        os.replace(path, record)
    finally:
        if path is not None:
            path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("fingerprint", "record", "verify"))
    parser.add_argument("task", type=Path)
    parser.add_argument("repository", type=Path)
    parser.add_argument("branch")
    parser.add_argument("--expected", help="fingerprint presented for approval or assigned to the worker")
    args = parser.parse_args()
    try:
        fingerprint = scope_fingerprint(args.task, args.repository, args.branch)
        if args.mode == "record":
            update_approval(args.task, args.repository, args.branch, args.expected)
        elif args.mode == "verify":
            record = json.loads((args.task / "agent-view" / "approval.json").read_text(encoding="utf-8"))
            if record["fingerprint"] != fingerprint or (args.expected and args.expected != fingerprint):
                raise ValueError("approval does not match current task scope")
        print(fingerprint)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
