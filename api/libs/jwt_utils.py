"""Shared JWT helpers — zero controller/lib dependencies to avoid circular imports.

This module is the single source of truth for JWT secret-key resolution
and token verification.  Both ``api.controllers.console.auth`` and
``api.libs.login`` import from here, never the other way around.
"""

import os
import jwt


def _get_secret_key() -> str:
    """Return the JWT signing secret. Fails fast in production if unset."""
    # P0.1 (H-01): usar el criterio estricto y unificado de _is_production()
    # en vez del literal "production". Antes, FLASK_ENV=staging caia al path
    # dev (random per-process key), divergiendo de security_checks.
    from api.libs.security_checks import _is_production

    secret = os.environ.get("JWT_SECRET_KEY", "")
    if not secret or secret == "dev-secret-change-me":
        if _is_production():
            raise RuntimeError(
                "SECURITY ERROR: JWT_SECRET_KEY must be set to a strong value in production. "
                "Generate one with: python -c 'import secrets; print(secrets.token_urlsafe(64))'"
            )
        # Dev/test: log a warning and use a random per-process key
        import secrets
        return secrets.token_urlsafe(64)
    if len(secret) < 32:
        raise RuntimeError(
            "SECURITY ERROR: JWT_SECRET_KEY must be at least 32 characters. "
            f"Current length: {len(secret)}. Generate a stronger one with: "
            "python -c 'import secrets; print(secrets.token_urlsafe(64))'"
        )
    return secret


def _verify_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, _get_secret_key(), algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


__all__ = ["_get_secret_key", "_verify_token"]
