"""Fail-fast validation of critical configuration before the app boots."""
from __future__ import annotations

import os
import sys
from typing import Iterable

_INSECURE_DEFAULTS: dict[str, set[str]] = {
    "JWT_SECRET_KEY": {"dev-secret-change-me", "", "changeme"},
    "IMPERSONATION_TOKEN_PEPPER": {"dev-pepper-rotate-in-prod", "", "changeme"},
}

_REQUIRED_IN_PROD: Iterable[str] = (
    "JWT_SECRET_KEY",
    "IMPERSONATION_TOKEN_PEPPER",
    "ALLOWED_ORIGINS",
    "REDIS_PASSWORD",
)

def _is_production() -> bool:
    env = os.getenv("FLASK_ENV", "production").lower()
    return env not in {"development", "dev", "test", "testing"}

def assert_production_secrets() -> None:
    """Raise SystemExit if running in production with insecure defaults."""
    if not _is_production():
        return

    errors: list[str] = []

    for var in _REQUIRED_IN_PROD:
        if not os.getenv(var):
            errors.append(f"{var} is required in production but is not set.")

    if not os.getenv("DATABASE_URL"):
        for var in ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"):
            if not os.getenv(var):
                errors.append(
                    f"{var} is required in production when DATABASE_URL is not set."
                )

    for var, bad_values in _INSECURE_DEFAULTS.items():
        value = os.getenv(var, "")
        if value in bad_values:
            errors.append(
                f"{var} is using an insecure development default. "
                f"Rotate it before deploying to production."
            )

    for var, bad_values in {
        "DB_PASSWORD": {"", "postgres", "changeit", "dev_password_123"},
        "REDIS_PASSWORD": {"", "changeit", "dev_password_123"},
    }.items():
        value = os.getenv(var, "")
        if value in bad_values and not (var == "DB_PASSWORD" and os.getenv("DATABASE_URL")):
            errors.append(f"{var} is missing or uses an insecure default.")

    if errors:
        sys.stderr.write("\n[FATAL] Insecure configuration detected:\n")
        for err in errors:
            sys.stderr.write(f"  - {err}\n")
        sys.stderr.write(
            "\nSet FLASK_ENV=development to bypass this check locally.\n\n"
        )
        raise SystemExit(1)
