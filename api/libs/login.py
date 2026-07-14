"""MyOwnClone authentication primitives — JWT-based."""
import logging
import os
from functools import wraps
from flask import g, request
from typing import Callable, Any

from api.libs.jwt_utils import _verify_token
from api.libs.security_checks import _is_production

logger = logging.getLogger(__name__)

# Roles privilegiados que NUNCA se aceptan solo por header X-User-Role en el
# path X-API-Key (service-to-service). Requieren confirmacion contra DB para
# prevenir escalada de privilegios si SERVICE_API_KEY se filtra.
# (auditoria 2026-07-13 / P0.1 / defecto C-02)
_PRIVILEGED_ROLES = frozenset({"platform_admin", "superadmin", "root"})


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


def _confirm_privileged_role(account_id: str, claimed_role: str) -> str:
    """P0.1 (C-02): confirm a privileged role against the DB before honoring it.

    In the service-to-service path (X-API-Key), the backend used to trust the
    ``X-User-Role`` header verbatim. If ``SERVICE_API_KEY`` ever leaks, any
    caller could impersonate a platform_admin by setting that header.

    Now: if the forwarded role claims to be privileged
    (``platform_admin``/``superadmin``/``root``), we confirm against the
    ``accounts`` table that the account actually holds that role. On any
    mismatch, lookup failure, or DB unavailability, the role is downgraded to
    a non-privileged default so the request can still proceed as a normal
    user (defense in depth — fail closed on privilege, fail open on access).

    Returns the (possibly downgraded) role string to set on ``g``.
    """
    if claimed_role not in _PRIVILEGED_ROLES:
        return claimed_role

    try:
        from api.extensions.ext_database import db
        from api.models.account import Account
        from sqlalchemy import select

        row = db.session.execute(
            select(Account.role, Account.is_platform_admin).where(
                Account.id == account_id
            )
        ).first()
        if row is None:
            logger.warning(
                "Privileged role %r claimed for unknown account %s; downgrading.",
                claimed_role, account_id,
            )
            return "user"
        db_role, is_platform_admin = row
        # Accept only if the DB agrees the account is platform_admin.
        if is_platform_admin is True or (db_role or "").lower() in _PRIVILEGED_ROLES:
            return claimed_role
        logger.warning(
            "Account %s claimed privileged role %r but DB role=%r is_platform_admin=%r; downgrading.",
            account_id, claimed_role, db_role, is_platform_admin,
        )
        return db_role or "user"
    except Exception as exc:
        # Never grant privilege on DB error. Downgrade and log loudly.
        logger.warning(
            "Could not confirm privileged role %r for account %s (%s); downgrading.",
            claimed_role, account_id, exc,
        )
        return "user"


def login_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        # First try: JWT Bearer token (standard auth)
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            payload = _verify_token(token)
            if payload is not None:
                g.account_id = payload.get('sub')
                g.tenant_id = payload.get('tenant_id')
                g.account_role = payload.get('role')
                g.account_email = payload.get('email')
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
            forwarded_tenant_id = request.headers.get('X-Tenant-Id', '').strip()
            forwarded_role = request.headers.get('X-User-Role', '').strip()
            forwarded_email = request.headers.get('X-User-Email', '').strip()

            if not forwarded_user_id or not forwarded_role:
                return {'error': 'Unauthorized — missing forwarded identity'}, 401

            # P0.1 (C-02): no confiar en X-User-Role para roles privilegiados
            # sin confirmacion DB (defensa si SERVICE_API_KEY se filtra).
            confirmed_role = _confirm_privileged_role(forwarded_user_id, forwarded_role)

            g.account_id = forwarded_user_id
            g.tenant_id = forwarded_tenant_id if _is_uuid_like(forwarded_tenant_id) else None
            g.account_role = confirmed_role
            g.account_email = forwarded_email or ''
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
