"""Tier enforcement middleware — applies plan limits per tenant."""

import logging
from functools import wraps

from flask import g, jsonify

from api.extensions.ext_database import db
from api.models.account import Tenant
from api.models.clone import CloneConfig
from api.models.knowledge import Source

logger = logging.getLogger(__name__)

TIER_LIMITS = {
    "free": {
        "max_clones": 2,
        "max_sources": 3,
        "max_conversations_per_day": 100,
    },
    "starter": {
        "max_clones": 5,
        "max_sources": 20,
        "max_conversations_per_day": 500,
    },
    "pro": {
        "max_clones": 10,
        "max_sources": 50,
        "max_conversations_per_day": 2000,
    },
    "business": {
        "max_clones": 30,
        "max_sources": 200,
        "max_conversations_per_day": 10000,
    },
    "enterprise": {
        "max_clones": -1,  # unlimited
        "max_sources": -1,
        "max_conversations_per_day": -1,
    },
}

DEFAULT_LIMITS = TIER_LIMITS["free"]


def get_tier_limits(tenant) -> dict:
    """Get limits for a tenant's current plan."""
    plan = getattr(tenant, "plan", "free") or "free"
    return TIER_LIMITS.get(plan.lower(), DEFAULT_LIMITS)


def check_tenant_limit(tenant, resource: str) -> tuple[bool, int | None]:
    """Check if tenant is within limit for a resource.

    Returns (allowed, current_count).
    """
    limits = get_tier_limits(tenant)
    max_allowed = limits.get(resource, -1)

    if max_allowed == -1:
        return True, 0  # unlimited

    if resource == "max_clones":
        count = db.session.query(CloneConfig).filter_by(
            tenant_id=tenant.id
        ).count()
    elif resource == "max_sources":
        count = db.session.query(Source).join(CloneConfig).filter(
            CloneConfig.tenant_id == tenant.id
        ).count()
    else:
        return True, 0

    return count < max_allowed, count


def require_within_limit(resource: str):
    """Decorator that blocks requests if tenant exceeds tier limit."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from api.libs.login import current_account_with_tenant

            try:
                account, tenant_id = current_account_with_tenant()
            except Exception:
                return f(*args, **kwargs)

            if not tenant_id:
                return f(*args, **kwargs)

            tenant = db.session.query(Tenant).filter_by(id=tenant_id).first()
            if not tenant:
                return f(*args, **kwargs)

            allowed, count = check_tenant_limit(tenant, resource)
            if not allowed:
                limits = get_tier_limits(tenant)
                return {
                    "error": "tier_limit_exceeded",
                    "resource": resource,
                    "current": count,
                    "limit": limits.get(resource),
                    "plan": getattr(tenant, "plan", "free"),
                    "upgrade_url": "/planes",
                }, 403

            return f(*args, **kwargs)

        return decorated_function

    return decorator
