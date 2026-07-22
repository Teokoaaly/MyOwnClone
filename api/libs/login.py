"""MyOwnClone authentication primitives — JWT-based."""
from __future__ import annotations

import hmac
import logging
import os
from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable

from flask import g, request
from sqlalchemy.exc import SQLAlchemyError

from api.libs.jwt_utils import _verify_token
from api.libs.security_checks import _is_production

logger = logging.getLogger(__name__)

@dataclass(frozen=True, slots=True)
class AuthenticatedIdentity:
    account_id: str
    tenant_id: str
    role: str
    email: str


class _AccountProxy:
    def __getattr__(self, name: str) -> Any:
        return getattr(g, 'account_' + name, None)

    def __iter__(self):
        account = getattr(g, 'account_id', None)
        tenant_id = getattr(g, 'tenant_id', None)
        yield account
        yield tenant_id

    def __repr__(self):
        aid = getattr(g, 'account_id', None)
        return f'<_AccountProxy account={aid}>'


_current_account_with_tenant = _AccountProxy()


def current_account_with_tenant():
    return _current_account_with_tenant


def _is_uuid_like(value: str | None) -> bool:
    if not value:
        return False
    normalized = value.replace("-", "")
    if len(normalized) != 32:
        return False
    return all(ch in "0123456789abcdefABCDEF" for ch in normalized)


def _allow_dev_service_key() -> bool:
    """SECURITY (P0.1 / H-01): dev key only allowed when explicitly enabled
    AND outside production.

    Usa el mismo criterio estricto que ``security_checks._is_production()``:
    cualquier FLASK_ENV que no sea {development, dev, test, testing} cuenta
    como produccion (incluye staging). Antes habia divergencia de politica:
    ``staging`` activaba la dev-key aqui pero security_checks lo trataba
    como produccion.
    """
    return (
        not _is_production()
        and os.environ.get("ALLOW_DEV_SERVICE_KEY", "false").lower() == "true"
    )


def _load_authoritative_identity(account_id: str | None) -> AuthenticatedIdentity | None:
    normalized_id = str(account_id or "").strip()
    if not _is_uuid_like(normalized_id):
        return None
    try:
        from api.extensions.ext_database import db
        from api.models.account import Account
        account = db.session.get(Account, normalized_id)
    except SQLAlchemyError:
        logger.exception("Could not resolve authenticated account %s", normalized_id)
        return None

    if account is None or str(account.status).lower() != "active":
        return None

    role = "platform_admin" if account.is_platform_admin else str(account.role or "member")
    return AuthenticatedIdentity(
        account_id=str(account.id),
        tenant_id=str(account.tenant_id),
        role=role,
        email=str(account.email),
    )


def _apply_identity(identity: AuthenticatedIdentity) -> None:
    g.account_id = identity.account_id
    g.tenant_id = identity.tenant_id
    g.account_role = identity.role
    g.account_email = identity.email


def login_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        # First try: JWT Bearer token (standard auth)
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            payload = _verify_token(token)
            if payload is not None:
                identity = _load_authoritative_identity(payload.get('sub'))
                if identity is None:
                    return {'error': 'Unauthorized — account not active'}, 401
                _apply_identity(identity)
                return f(*args, **kwargs)

        # Second try: X-API-Key header (service-to-service via Next.js proxy)
        api_key = request.headers.get('X-API-Key', '')
        valid_keys = []
        configured_service_key = os.environ.get('SERVICE_API_KEY', '').strip()
        if configured_service_key:
            valid_keys.append(configured_service_key)
        if _allow_dev_service_key():
            valid_keys.append('dev-api-key-for-proxy')

        if api_key and any(_check_service_token(api_key, key) for key in valid_keys):
            forwarded_user_id = request.headers.get('X-User-Id', '').strip()
            if not forwarded_user_id:
                return {'error': 'Unauthorized — missing forwarded identity'}, 401
            identity = _load_authoritative_identity(forwarded_user_id)
            if identity is None:
                return {'error': 'Unauthorized — account not active'}, 401
            _apply_identity(identity)
            return f(*args, **kwargs)

        return {'error': 'Unauthorized — missing or invalid authentication'}, 401
    return decorated


def _check_service_token(provided: str, expected: str) -> bool:
    """Timing-safe service token comparison using hmac.compare_digest.

    Use this instead of == for comparing tokens from headers
    (e.g. X-Admin-Token, service API keys) to prevent timing attacks.

    Args:
        provided: The token received from the request header.
        expected: The expected token from environment/config.

    Returns:
        True if the tokens match, False otherwise.
    """
    if not provided or not expected:
        return False
    return hmac.compare_digest(provided.encode("utf-8"), expected.encode("utf-8"))


__all__ = ['current_account_with_tenant', 'login_required', '_check_service_token']
