from __future__ import annotations

from pathlib import Path


def test_python_auth_does_not_select_drizzle_only_email_verified() -> None:
    api_root = Path(__file__).resolve().parents[1]
    auth_source = (api_root / "controllers" / "console" / "auth.py").read_text(
        encoding="utf-8"
    )
    migration_sources = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (api_root / "migrations" / "versions").glob("*.py")
    )

    assert "email_verified" not in auth_source
    assert "email_verified" not in migration_sources


def test_drizzle_repairs_the_nullable_email_verified_column_idempotently() -> None:
    repository_root = Path(__file__).resolve().parents[2]
    migration = (
        repository_root
        / "MyOwnClone"
        / "drizzle"
        / "0005_repair_users_email_verified.sql"
    )
    journal = migration.parent / "meta" / "_journal.json"
    schema = (
        repository_root
        / "MyOwnClone"
        / "src"
        / "lib"
        / "db"
        / "schema"
        / "users.ts"
    )

    migration_source = migration.read_text(encoding="utf-8")
    assert "table_name = 'users'" in migration_source
    assert 'ADD COLUMN IF NOT EXISTS "email_verified" timestamp' in migration_source
    assert '"tag": "0005_repair_users_email_verified"' in journal.read_text(
        encoding="utf-8"
    )
    assert 'emailVerified: timestamp("email_verified"),' in schema.read_text(
        encoding="utf-8"
    )
