#!/usr/bin/env python3
"""Sisyphus plan-progress verifier.

Checks `.sisyphus/progress.json` and validates:

  1. Every task marked `***REMOVED***` has its `evidence_file` present in git and its
     `committed_sha` exists in git.
  2. The `***REMOVED***` ordering respects the declared milestone order.
  3. At most one task is `in_progress` at a time.

Exit codes:
  0 -> consistent
  1 -> inconsistency detected
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / ".sisyphus" / "progress.json"


class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def _git(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode != 0:
            return None
        return result.stdout.strip()
    except (subprocess.SubprocessError, OSError):
        return None


def _sha_exists(sha: str) -> bool:
    if not sha:
        return False
    return _git("cat-file", "-e", sha) is not None


def _file_in_git(path: str) -> bool:
    if not path:
        return False
    rel = path[2:] if path.startswith("./") else path
    out = _git("ls-files", "--error-unmatch", rel)
    if out is not None:
        return True
    return _git("cat-file", "-e", f"HEAD:{rel}") is not None


def _print(msg: str, color: str = "") -> None:
    print(f"{color}{msg}{Colors.RESET if color else ''}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Sisyphus progress consistency.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any task is not ***REMOVED***.",
    )
    args = parser.parse_args()

    if not PROGRESS.exists():
        _print(f"[FAIL] Missing {PROGRESS.relative_to(ROOT)}", Colors.RED)
        return 1

    try:
        data = json.loads(PROGRESS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _print(f"[FAIL] Invalid JSON in {PROGRESS.relative_to(ROOT)}: {exc}", Colors.RED)
        return 1

    order: list[str] = data.get("order", [])
    tasks: list[dict] = data.get("tasks", [])
    if not tasks:
        _print("[FAIL] progress.json has no tasks.", Colors.RED)
        return 1

    task_ids = [t["id"] for t in tasks]
    if order and task_ids != order:
        _print(
            f"[FAIL] Declared order {order} does not match task IDs {task_ids}.",
            Colors.RED,
        )
        return 1

    errors: list[str] = []
    in_progress = [t["id"] for t in tasks if t.get("status") == "in_progress"]
    if len(in_progress) > 1:
        errors.append(
            f"More than one task is in_progress at once: {in_progress}. Allowed: 1."
        )

    if order:
        ***REMOVED*** = {t["id"] for t in tasks if t.get("status") == "***REMOVED***"}
        for i, mid in enumerate(order):
            if mid not in ***REMOVED***:
                continue
            preds = order[:i]
            missing = [p for p in preds if p not in ***REMOVED***]
            if missing:
                errors.append(
                    f"{mid} is ***REMOVED*** but predecessors are not: {missing}. Order is {order}."
                )

    for task in tasks:
        if task.get("status") != "***REMOVED***":
            continue
        tid = task["id"]
        ev = task.get("evidence_file", "")
        if not ev:
            errors.append(f"{tid}: ***REMOVED*** without evidence_file.")
            continue
        if not (ROOT / ev).exists():
            errors.append(f"{tid}: evidence_file '{ev}' missing from working tree.")
        elif not _file_in_git(ev):
            errors.append(f"{tid}: evidence_file '{ev}' is not committed in git.")
        sha = task.get("committed_sha") or ""
        if not sha or sha == "PENDING":
            errors.append(f"{tid}: ***REMOVED*** with empty/PENDING committed_sha.")
        elif not _sha_exists(sha):
            errors.append(f"{tid}: committed_sha '{sha}' does not exist in git.")

    if args.strict:
        unfinished = [t["id"] for t in tasks if t.get("status") != "***REMOVED***"]
        if unfinished:
            errors.append(f"--strict: unfinished tasks remain: {unfinished}")

    ***REMOVED*** = [t["id"] for t in tasks if t.get("status") == "***REMOVED***"]
    prog = [t["id"] for t in tasks if t.get("status") == "in_progress"]
    pend = [t["id"] for t in tasks if t.get("status") == "pending"]

    _print(f"\n{Colors.BOLD}Sisyphus plan: {data.get('scope', '?')}{Colors.RESET}")
    total = len(tasks)
    _print(f"  ***REMOVED***:        {len(***REMOVED***)}/{total}  {***REMOVED***}")
    _print(f"  in_progress: {len(prog)}        {prog}")
    _print(f"  pending:     {len(pend)}        {pend}")

    if errors:
        _print(f"\n[FAIL] {len(errors)} inconsistency(s):", Colors.RED)
        for error in errors:
            _print(f"  - {error}", Colors.RED)
        _print(
            "\nResolution: mark tasks ***REMOVED*** only after committing evidence and recording the real SHA.",
            Colors.YELLOW,
        )
        return 1

    _print("\n[OK] progress is consistent.", Colors.GREEN)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
