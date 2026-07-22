from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"
SECRET_SCAN = ROOT / "ops" / "scan_tracked_secrets.sh"


def test_ci_enforces_backend_quality_gates_without_building_frontend() -> None:
    source = WORKFLOW.read_text(encoding="utf-8")

    assert "pytest -q tests api/tests" in source
    assert "flask db heads" in source
    assert "flask db check" in source
    assert "ruff check" in source
    assert "--exit-zero" not in source
    assert "scan_tracked_secrets.sh" in source
    assert "base: 0481c6c4874bb8f35e37af563ad7439848c71f2e" in source
    assert "head: ${{ github.sha }}" in source
    assert "--results=verified,unknown" in source
    assert "test_deploy_backend_rollback.sh" in source
    assert "ALLOWED_ORIGINS: http://localhost:3000" in source
    assert "working-directory: MyOwnClone" not in source
    assert "npm " not in source


@pytest.mark.skipif(os.name == "nt", reason="CI exercises the POSIX scanner")
def test_binary_secret_scan_detects_utf16_literal(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    token = "gh" + "p_" + ("A" * 36)
    (tmp_path / "binary.conf").write_text(token, encoding="utf-16")
    subprocess.run(["git", "-C", str(tmp_path), "add", "binary.conf"], check=True)

    result = subprocess.run(
        ["bash", str(SECRET_SCAN), str(tmp_path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "binary.conf" in result.stdout
    assert token not in result.stdout
