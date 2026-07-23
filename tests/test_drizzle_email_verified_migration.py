from __future__ import annotations

import subprocess
from collections.abc import Iterator
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "MyOwnClone" / "drizzle" / "0005_repair_users_email_verified.sql"


def _docker(*args: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", *args],
        check=True,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=60,
    )


@pytest.fixture
def postgres_container() -> Iterator[str]:
    try:
        availability = subprocess.run(
            ["docker", "info"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except subprocess.TimeoutExpired:
        pytest.skip("Docker daemon did not become available within 10 seconds")
    if availability.returncode != 0:
        pytest.skip("Docker daemon is unavailable for Postgres migration integration tests")

    container = _docker(
        "run",
        "--detach",
        "--rm",
        "--env",
        "POSTGRES_PASSWORD=postgres",
        "--env",
        "POSTGRES_DB=luna03",
        "postgres:16-alpine",
    ).stdout.strip()
    try:
        _docker(
            "exec",
            container,
            "sh",
            "-ec",
            "until pg_isready -U postgres -d luna03; do sleep 1; done",
        )
        yield container
    finally:
        _docker("rm", "--force", "--volumes", container)


def _psql(container: str, sql: str) -> str:
    return _docker(
        "exec",
        "--interactive",
        container,
        "psql",
        "--username=postgres",
        "--dbname=luna03",
        "--tuples-only",
        "--no-align",
        "--set=ON_ERROR_STOP=1",
        "--command",
        sql,
    ).stdout.strip()


def test_email_verified_migration_is_a_noop_on_an_empty_database(
    postgres_container: str,
) -> None:
    # Given: an empty Postgres database.
    migration = MIGRATION.read_text(encoding="utf-8")

    # When: the custom Drizzle migration executes.
    _psql(postgres_container, migration)

    # Then: it succeeds without creating an unrelated users table.
    assert _psql(postgres_container, "SELECT to_regclass('public.users');") == ""


def test_email_verified_migration_preserves_existing_identity_password_and_tenant_rows(
    postgres_container: str,
) -> None:
    # Given: a compatible database whose users table predates email_verified.
    _psql(
        postgres_container,
        """
        CREATE TABLE tenants (id text PRIMARY KEY, slug text NOT NULL);
        CREATE TABLE users (
          id text PRIMARY KEY,
          tenant_id text NOT NULL REFERENCES tenants(id),
          email text NOT NULL,
          password_hash text NOT NULL
        );
        INSERT INTO tenants (id, slug) VALUES ('tenant-1', 'acme');
        INSERT INTO users (id, tenant_id, email, password_hash)
        VALUES ('user-1', 'tenant-1', 'owner@acme.test', 'preserved-password-hash');
        """,
    )
    migration = MIGRATION.read_text(encoding="utf-8")

    # When: the custom Drizzle migration runs twice.
    _psql(postgres_container, migration)
    _psql(postgres_container, migration)

    # Then: the nullable column exists and the seed identity, password, and tenant remain intact.
    assert _psql(
        postgres_container,
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'users'
          AND column_name = 'email_verified';
        """,
    ) == "email_verified"
    assert _psql(
        postgres_container,
        "SELECT id || '|' || tenant_id || '|' || email || '|' || password_hash FROM users;",
    ) == "user-1|tenant-1|owner@acme.test|preserved-password-hash"
