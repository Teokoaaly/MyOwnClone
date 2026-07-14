from pathlib import Path


SCRIPT = Path("ops/deploy-backend.sh")


def test_rollback_passes_paths_as_quoted_positional_arguments() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert 'bash -s -- \\\n    "$PREV_RELEASE_LINK" "$REMOTE_CURRENT_LINK"' in source
    assert "ln -sfn '${PREV_RELEASE_LINK}' '${REMOTE_CURRENT_LINK}'" not in source


def test_deploy_generates_uploads_and_verifies_release_manifest() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "ops/release_manifest.py" in source
    assert "release-manifest.json" in source
    assert " create " in source
    assert " verify " in source
    assert 'diff --quiet -- api ops .github/workflows' in source
