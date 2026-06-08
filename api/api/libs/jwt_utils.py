"""JWT utility helpers — shared by auth controller and login_required decorator.

Centralized to avoid circular imports between api.controllers.console.auth
and api.libs.login. Both modules import from here.
"""
from __future__ import annotations
import os
import jwt

DEFAULT_JWT_SECRET = "dev-secret-change-me"

def _get_secret_key() -> str:
    return os.getenv("JWT_SECRET_KEY", DEFAULT_JWT_SECRET)

def _decode_jwt_payload(token: str) -> dict:
    return jwt.decode(token, _get_secret_key(), algorithms=["HS256"])

def _verify_token(token: str) -> dict | None:
    """Verify a JWT and return the payload, or None if invalid."""
    try:
        return _decode_jwt_payload(token)
    except jwt.PyJWTError:
        return None