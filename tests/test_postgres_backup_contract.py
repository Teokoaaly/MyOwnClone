"""Executable contracts for the release-safe PostgreSQL backup tooling."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT / "ops" / "backup_postgres.sh"
VERIFY = ROOT / "ops" / "verify_postgres_backup.sh"


def test_backup_uses_backend_current_and_is_unix_executable() -> None:
    # Given: the release-scoped backup runner
    source = BACKUP.read_bytes()

    # When: its provenance and interpreter are inspected
    # Then: it resolves backend-current and cannot be corrupted by CRLF shebangs.
    assert source.startswith(b"#!/usr/bin/env bash\n")
    assert b"\r\n" not in source
    assert b"backend-current" in source
    assert b"readlink -f" in source


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


def test_offsite_upload_is_opt_in_root_only_and_never_deletes_remote() -> None:
    # Given: the backup runner source
    source = BACKUP.read_text(encoding="utf-8")

    # When: the B2 upload integration is inspected
    # Then: credentials come from the root-only runtime file and uploads are immutable.
    assert "/etc/myownclone/backup-b2.env" in source
    assert "rclone copyto" in source
    assert "--immutable" in source
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
    assert 'rm -f -- "$old" "$old.sha256" "$old.manifest"' in source
    assert source.count("rclone copyto --immutable") == 3
