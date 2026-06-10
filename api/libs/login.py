"""MyOwnClone authentication primitives — JWT-based."""
import hmac
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


def _is_uuid_like(value: str | None) -> bool:
    if not value:
        return False
    normalized = value.replace("-", "")
    if len(normalized) != 32:
        return False
    return all(ch in "0123456789abcdefABCDEF" for ch in normalized)


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
        valid_keys = [
            os.environ.get('SERVICE_API_KEY', ''),
            os.environ.get('DEPLOY_SECRET', ''),
        ]
        # In development only, fall back to a hardcoded key so local hacking
        # works without a freshly generated secret.
        if os.environ.get('FLASK_ENV', 'production') != 'production':
            valid_keys.append('dev-api-key-for-proxy')
        if api_key and api_key in valid_keys:
            forwarded_user_id = request.headers.get('X-User-Id', '').strip()
            forwarded_tenant_id = request.headers.get('X-Tenant-Id', '').strip()
            forwarded_role = request.headers.get('X-User-Role', '').strip()
            forwarded_email = request.headers.get('X-User-Email', '').strip()

            g.account_id = forwarded_user_id or 'proxy-service'
            g.tenant_id = forwarded_tenant_id if _is_uuid_like(forwarded_tenant_id) else 'proxy-service'
            g.account_role = forwarded_role or 'admin'
            g.account_email = forwarded_email or 'proxy@myownclone.local'
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
