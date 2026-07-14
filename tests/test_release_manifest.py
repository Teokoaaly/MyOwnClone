from __future__ import annotations

import json
from pathlib import Path

import pytest

from ops.release_manifest import ManifestError, load_manifest, verify_manifest


def _manifest(tmp_path: Path, content: bytes = b"healthy\n") -> Path:
    target = tmp_path / "api" / "service.py"
    target.parent.mkdir(parents=True)
    target.write_bytes(content)
    import hashlib

    manifest = tmp_path / "release-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "source_commit": "a" * 40,
                "files": {"api/service.py": hashlib.sha256(content).hexdigest()},
            }
        ),
        encoding="utf-8",
    )
    return manifest


def test_verify_accepts_matching_tree_without_git_head_check(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    assert verify_manifest(tmp_path, manifest, check_head=False) == []


def test_verify_rejects_mutated_file(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    (tmp_path / "api" / "service.py").write_text("tampered\n", encoding="utf-8")
    assert verify_manifest(tmp_path, manifest, check_head=False) == [
        "digest mismatch: api/service.py"
    ]


def test_load_rejects_malformed_manifest(tmp_path: Path) -> None:
    manifest = tmp_path / "release-manifest.json"
    manifest.write_text('{"schema_version": 1}', encoding="utf-8")
    with pytest.raises(ManifestError, match="top-level shape"):
        load_manifest(manifest)


def test_load_rejects_parent_traversal(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["files"] = {"api/../secret": "a" * 64}
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ManifestError, match="invalid manifest entry"):
        load_manifest(manifest)
