from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Final

SCHEMA_VERSION: Final = 1
INCLUDED_PREFIXES: Final = ("api/", "ops/", ".github/workflows/")
EXCLUDED_NAMES: Final = {
    "backend.env.production",
    "frontend.env.production",
    "release-manifest.json",
}


class ManifestError(ValueError):
    pass


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise ManifestError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()


def _tracked_release_files(root: Path) -> list[str]:
    output = _git(root, "ls-files", "-z", "--", *INCLUDED_PREFIXES)
    paths = [item for item in output.split("\0") if item]
    return sorted(
        path
        for path in paths
        if Path(path).name not in EXCLUDED_NAMES
        and "__pycache__" not in Path(path).parts
        and not Path(path).name.startswith(".env")
    )


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path, source_commit: str) -> dict[str, object]:
    if len(source_commit) != 40 or any(c not in "0123456789abcdef" for c in source_commit):
        raise ManifestError("source_commit must be a full lowercase Git SHA")
    files = {path: _digest(root / path) for path in _tracked_release_files(root)}
    if not files:
        raise ManifestError("no tracked backend release files found")
    return {
        "schema_version": SCHEMA_VERSION,
        "source_commit": source_commit,
        "files": files,
    }


def load_manifest(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"cannot read manifest: {exc}") from exc
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "source_commit",
        "files",
    }:
        raise ManifestError("manifest has an invalid top-level shape")
    if payload["schema_version"] != SCHEMA_VERSION:
        raise ManifestError("unsupported manifest schema")
    source_commit = payload["source_commit"]
    files = payload["files"]
    if not isinstance(source_commit, str) or len(source_commit) != 40:
        raise ManifestError("manifest source_commit is invalid")
    if not isinstance(files, dict) or not files:
        raise ManifestError("manifest files must be a non-empty object")
    for relative, digest in files.items():
        if (
            not isinstance(relative, str)
            or not relative.startswith(INCLUDED_PREFIXES)
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
            or not isinstance(digest, str)
            or len(digest) != 64
        ):
            raise ManifestError(f"invalid manifest entry: {relative!r}")
    return payload


def verify_manifest(root: Path, manifest_path: Path, check_head: bool = True) -> list[str]:
    payload = load_manifest(manifest_path)
    failures: list[str] = []
    if check_head:
        try:
            head = _git(root, "rev-parse", "HEAD")
        except ManifestError as exc:
            failures.append(str(exc))
        else:
            if head != payload["source_commit"]:
                failures.append(f"HEAD mismatch: expected {payload['source_commit']}, got {head}")
    files = payload["files"]
    assert isinstance(files, dict)
    for relative, expected in sorted(files.items()):
        path = root / relative
        if not path.is_file():
            failures.append(f"missing: {relative}")
        elif _digest(path) != expected:
            failures.append(f"digest mismatch: {relative}")
    return failures


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create and verify backend release manifests")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    subparsers = parser.add_subparsers(dest="command", required=True)
    create = subparsers.add_parser("create")
    create.add_argument("--source-commit", required=True)
    create.add_argument("--output", type=Path, required=True)
    verify = subparsers.add_parser("verify")
    verify.add_argument("--manifest", type=Path, required=True)
    verify.add_argument("--no-head-check", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "create":
            payload = build_manifest(root, args.source_commit)
            args.output.write_text(
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            print(f"created {args.output} ({len(payload['files'])} files)")
            return 0
        failures = verify_manifest(root, args.manifest, not args.no_head_check)
    except ManifestError as exc:
        print(f"manifest error: {exc}", file=sys.stderr)
        return 2
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print("PASS: release manifest matches backend tree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
