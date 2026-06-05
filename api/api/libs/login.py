"""MyOwnClone authentication primitives — JWT-based.

Two accepted credential sources for `login_required`:

  1. `Authorization: Bearer <jwt>` — standard user JWT, verified with the
     shared HS256 secret.
  2. `X-Admin-Token: <token>` matching `PLATFORM_ADMIN_TOKEN` — a service
     token used by the Next.js admin proxy after it has verified the
     NextAuth session. The token maps to a synthetic `platform_admin`
     account so all downstream role checks still work.
"""
import logging
import os
from functools import wraps
from flask import g, request
from typing import Callable, Any

from api.controllers.console.auth import _verify_token

logger = logging.getLogger(__name__)


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


def _check_service_token() -> bool:
    """Return True if the request presents a valid platform admin service token."""
    expected = os.environ.get('PLATFORM_ADMIN_TOKEN', '')
    if not expected:
        return False
    presented = request.headers.get('X-Admin-Token', '')
    if not presented:
        return False
    # Constant-time comparison to avoid timing side channels.
    import hmac
    return hmac.compare_digest(presented, expected)


def login_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        # 1) Service token — service-to-service auth from the Next proxy.
        if _check_service_token():
            g.account_id = 'service:platform_admin'
            g.tenant_id = 'platform'
            g.account_role = 'platform_admin'
            g.account_email = 'service@platform.local'
            return f(*args, **kwargs)

        # 2) Standard user JWT.
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


__all__ = ['current_account_with_tenant', 'login_required', '_check_service_token']
