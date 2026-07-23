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
