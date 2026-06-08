"""MyOwnClone authentication primitives — JWT-based."""
import os
from functools import wraps
from flask import g, request
from typing import Callable, Any

from api.libs.jwt_utils import _verify_token


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
        # Service-to-service token (X-Admin-Token) — bypasses JWT verification
        admin_token = request.headers.get('X-Admin-Token', '')
        if admin_token:
            expected = os.getenv('PLATFORM_ADMIN_TOKEN', '')
            if expected and admin_token == expected:
                g.account_id = 'platform-admin'
                g.tenant_id = 'platform'
                g.account_role = 'platform_admin'
                g.account_email = 'admin@myownclone.platform'
                return f(*args, **kwargs)
            # Unknown admin token falls through to Bearer path

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


__all__ = ['current_account_with_tenant', 'login_required']
