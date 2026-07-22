from pathlib import Path


SCRIPT = Path("ops/deploy-backend.sh")


def test_rollback_passes_paths_as_quoted_positional_arguments() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert 'bash -s -- \\\n    "$PREV_RELEASE_LINK" "$REMOTE_BACKEND_CURRENT_LINK"' in source
    assert "ln -sfn '${PREV_RELEASE_LINK}'" not in source


def test_deploy_generates_uploads_and_verifies_release_manifest() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "ops/release_manifest.py" in source
    assert "release-manifest.json" in source
    assert " create " in source
    assert " verify " in source
    assert 'diff --quiet -- api ops .github/workflows' in source


def test_backend_deploy_never_switches_frontend_current_or_restarts_frontend() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert 'REMOTE_BACKEND_CURRENT_LINK="${REMOTE_ROOT}/backend-current"' in source
    assert "REMOTE_CURRENT_LINK" not in source
    assert "myownclone-frontend" not in source
    assert "systemctl restart" not in source


def test_backend_deploy_requires_backup_restore_before_activation() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    backup = source.index("backup_postgres.sh")
    restore = source.index("verify_postgres_backup.sh")
    activate = source.index("ln -sfn", restore)
    assert backup < restore < activate


def test_backend_deploy_only_recreates_api_and_worker() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "--no-deps api api_worker" in source
    assert "docker compose" in source


def test_backend_deploy_uses_container_import_path_for_migrations() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    assert "api flask --app api.app_factory db upgrade" in source
    assert "api flask --app api.app_factory db current" in source
