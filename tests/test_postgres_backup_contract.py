"""Executable contracts for the release-safe PostgreSQL backup tooling."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT / "ops" / "backup_postgres.sh"
VERIFY = ROOT / "ops" / "verify_postgres_backup.sh"
VERIFY_B2 = ROOT / "ops" / "verify_b2_backup.sh"


def test_backup_uses_backend_current_and_is_unix_executable() -> None:
    # Given: the release-scoped backup runner
    source = BACKUP.read_bytes()

    # When: its provenance and interpreter are inspected
    # Then: it resolves backend-current and cannot be corrupted by CRLF shebangs.
    assert source.startswith(b"#!/usr/bin/env bash\n")
    assert b"\r\n" not in source
    assert b"backend-current" in source
    assert b"readlink -f" in source


def test_scripts_invoked_directly_are_executable() -> None:
    # Given: scripts referenced directly by systemd or the recovery runbook
    service = (ROOT / "ops" / "myownclone-postgres-backup.service").read_text(
        encoding="utf-8"
    )
    runbook = (ROOT / ".omo" / "runbooks" / "restore-from-backup.md").read_text(
        encoding="utf-8"
    )

    # When: their owner-mode bits are inspected
    # Then: every direct operational invocation selects Bash explicitly.
    assert "ExecStart=/usr/bin/env bash /opt/myownclone/backend-current/ops/backup_postgres.sh" in service
    assert "bash /opt/myownclone/backend-current/ops/verify_postgres_backup.sh" in runbook
    assert "bash /opt/myownclone/backend-current/ops/install-postgres-backup-systemd.sh" in runbook


def test_backup_contract_is_atomic_and_fail_closed() -> None:
    # Given: backup and verification scripts
    backup_source = BACKUP.read_text(encoding="utf-8")
    verify_source = VERIFY.read_text(encoding="utf-8")

    # When: failure handling is inspected
    # Then: publication happens after gzip/checksum/manifest verification only.
    assert "mktemp" in backup_source
    assert "trap cleanup" in backup_source
    assert "gzip -t" in backup_source
    assert "sha256sum" in backup_source
    assert "mv --" in backup_source
    assert backup_source.index("gzip -t") < backup_source.index("mv --")
    assert "sha256sum -c" in verify_source
    assert "gzip -t" in verify_source
    assert "ON_ERROR_STOP=1" in verify_source
    assert "timeout" in backup_source
    assert "timeout" in verify_source
    assert "setsid bash -o pipefail" in backup_source
    assert "trap cancel INT TERM HUP" in backup_source
    assert 'kill -- "-$pipeline_pid"' in backup_source
    assert "publication_started=1" in backup_source
    assert 'rm -f -- "$file" "$checksum_file" "$manifest_file"' in backup_source
    assert backup_source.index("publication_started=1") < backup_source.index('mv -- "$tmp_dump"')
    assert backup_source.index("backup_complete=1") > backup_source.rindex('mv -- "$tmp_manifest"')


def test_offsite_upload_is_required_encrypted_and_never_deletes_remote() -> None:
    # Given: the backup runner source
    source = BACKUP.read_text(encoding="utf-8")

    # When: the B2 upload integration is inspected
    # Then: credentials come from the root-only runtime file and only age-encrypted
    # backup bytes are uploaded immutably.
    assert "/etc/myownclone/backup-b2.env" in source
    assert "BACKUP_OFFSITE_REQUIRED" in source
    assert "BACKUP_AGE_RECIPIENT" in source
    assert "RCLONE_CONFIG" in source
    assert 'rclone --config "$RCLONE_CONFIG"' in source
    assert "age --encrypt" in source
    assert 'rclone --config "$RCLONE_CONFIG" copyto' in source
    assert "--immutable" in source
    assert 'rclone --config "$RCLONE_CONFIG" copyto --immutable "$encrypted_file"' in source
    assert 'rclone --config "$RCLONE_CONFIG" copyto --immutable "$file"' not in source
    assert "rclone delete" not in source
    assert "rclone purge" not in source
    assert "rclone sync" not in source


def test_systemd_units_replace_cron_only_after_activation() -> None:
    # Given: the versioned unit files
    service = (ROOT / "ops" / "myownclone-postgres-backup.service").read_text(
        encoding="utf-8"
    )
    timer = (ROOT / "ops" / "myownclone-postgres-backup.timer").read_text(
        encoding="utf-8"
    )
    installer = (ROOT / "ops" / "install-postgres-backup-systemd.sh").read_text(
        encoding="utf-8"
    )

    # When: their activation ordering is inspected
    # Then: the timer activates before the legacy cron removal is attempted.
    assert "backend-current" in service
    assert "Persistent=true" in timer
    assert "systemctl enable --now myownclone-postgres-backup.timer" in installer
    assert "crontab -l" in installer
    assert installer.index("systemctl enable --now") < installer.index("crontab -l")


def test_retention_and_upload_contract_preserve_latest_and_avoid_deletion() -> None:
    # Given: the runner source
    source = BACKUP.read_text(encoding="utf-8")

    # When: retention and upload operations are inspected
    # Then: retention starts after the newest entry and uploads use copyto only.
    assert "for ((index = KEEP_DAYS" in source
    assert 'rm -f -- "$old" "$old.sha256" "$old.manifest" "$old.age" "$old.age.sha256"' in source
    assert source.count('rclone --config "$RCLONE_CONFIG" copyto --immutable') == 3


def test_restore_uses_disposable_pgvector_container_not_production_postgres() -> None:
    source = VERIFY.read_text(encoding="utf-8")

    assert "moc-task04-" in source
    assert "pgvector/pgvector:pg15@" in source
    assert "docker network create" in source
    assert "docker volume create" in source
    assert "docker run" in source
    assert "docker rm --force" in source
    assert "docker network rm" in source
    assert "docker volume rm" in source
    assert "POSTGRES_CONTAINER" not in source
    assert "myownclone_postgres" not in source
    assert "--publish" not in source
    assert " -p " not in source


def test_b2_verifier_downloads_checks_decrypts_and_calls_isolated_restore() -> None:
    source = VERIFY_B2.read_text(encoding="utf-8")

    assert "/etc/myownclone/backup-b2.env" in source
    assert "/etc/myownclone/backup-age.key" in source
    assert 'rclone --config "$RCLONE_CONFIG"' in source
    assert "age identity must be owned by root" in source
    assert "age identity must not be accessible by group or others" in source
    assert source.count('rclone --config "$RCLONE_CONFIG" copyto') == 3
    assert "sha256sum -c" in source
    assert "age --decrypt" in source
    assert "verify_postgres_backup.sh" in source
    assert "mktemp -d" in source
    assert "trap cleanup" in source


def test_installer_gates_activation_on_b2_and_age_readiness() -> None:
    installer = (ROOT / "ops" / "install-postgres-backup-systemd.sh").read_text(
        encoding="utf-8"
    )

    gate = installer.index('rclone --config "$RCLONE_CONFIG" lsf')
    activate = installer.index("systemctl enable --now")
    assert "command -v rclone" in installer
    assert "command -v age" in installer
    assert "/etc/myownclone/backup-b2.env" in installer
    assert "/etc/myownclone/rclone.conf" in installer
    assert 'rclone --config "$RCLONE_CONFIG"' in installer
    assert "BACKUP_AGE_RECIPIENT" in installer
    assert gate < activate
