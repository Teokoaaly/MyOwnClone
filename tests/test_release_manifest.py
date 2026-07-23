from __future__ import annotations

import json
from pathlib import Path

import pytest

from ops.release_manifest import ManifestError, build_manifest, load_manifest, verify_manifest


def _manifest(tmp_path: Path, content: bytes = b"healthy\n") -> Path:
    target = tmp_path / "api" / "service.py"
    target.parent.mkdir(parents=True)
    target.write_bytes(content)
    import hashlib

    manifest = tmp_path / "release-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 2,
                "source_commit": "a" * 40,
                "created_at": "2026-07-22T10:00:00Z",
                "alembic_head": "2026_07_23_0001",
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


@pytest.mark.parametrize("source_commit", ["z" * 40, "A" * 40])
def test_load_rejects_non_lowercase_hex_commit(
    tmp_path: Path, source_commit: str
) -> None:
    manifest = _manifest(tmp_path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["source_commit"] = source_commit
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ManifestError, match="source_commit"):
        load_manifest(manifest)


@pytest.mark.parametrize("digest", ["z" * 64, "A" * 64])
def test_load_rejects_non_lowercase_hex_digest(tmp_path: Path, digest: str) -> None:
    manifest = _manifest(tmp_path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["files"]["api/service.py"] = digest
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ManifestError, match="invalid manifest entry"):
        load_manifest(manifest)


def test_verify_rejects_extra_release_file(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    extra = tmp_path / "api" / "unmanifested.py"
    extra.write_text("unexpected\n", encoding="utf-8")
    assert verify_manifest(tmp_path, manifest, check_head=False) == [
        "unexpected: api/unmanifested.py"
    ]


def test_build_manifest_records_time_and_single_alembic_head() -> None:
    root = Path(__file__).resolve().parents[1]

    manifest = build_manifest(
        root,
        "a" * 40,
        created_at="2026-07-22T10:00:00Z",
    )

    assert manifest["schema_version"] == 2
    assert manifest["created_at"] == "2026-07-22T10:00:00Z"
    assert manifest["alembic_head"] == "2026_07_23_0001"
