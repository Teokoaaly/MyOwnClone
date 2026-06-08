"""MyOwnClone authentication primitives — JWT-based."""
import hmac
import os
from functools import wraps
from flask import g, request
from typing import Callable, Any


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


def login_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        # Lazy import: avoids circular dependency with api.controllers.console.auth
        from api.controllers.console.auth import _verify_token

        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return {'error': 'Unauthorized — missing Bearer token'}, 401

        token = auth_header[7:]
        payload = _verify_token(token)
        if payload is None:
            return {'error': 'Unauthorized — invalid or expired token'}, 401

        g.account_id = payload.get('sub')
        g.tenant_id = payload.get('tenant_id')
        g.account_role = payload.get('role')
        g.account_email = payload.get('email')

        return f(*args, **kwargs)
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
