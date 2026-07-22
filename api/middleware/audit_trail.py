"""Audit trail middleware — logs admin actions to database.

P1.2 (auditoria 2026-07-13, C-16): the runtime ``_ensure_table`` DDL
call was removed. The ``audit_log`` table is now created via the
Alembic migration ``2026_07_14_0002_add_audit_log_table``. This
eliminates the cold-start race between workers and brings DDL into
the migration lineage so drift is detectable.

The decorator ``audit_action`` is the only public entry point for
state-changing endpoints; see ``api/controllers/console/myownclone/admin_platform.py``
for example usage.
"""
import logging
from datetime import datetime, timezone
from functools import wraps

from flask import g, request

from api.extensions.ext_database import db

logger = logging.getLogger(__name__)


class AuditLog(db.Model):
    """Audit log entry for admin actions."""
    __tablename__ = "audit_log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        server_default=db.func.current_timestamp(),
    )
    user_id = db.Column(db.String(36), nullable=True)
    tenant_id = db.Column(db.String(36), nullable=True)
    action = db.Column(db.String(100), nullable=False)
    resource_type = db.Column(db.String(50), nullable=True)
    resource_id = db.Column(db.String(36), nullable=True)
    details = db.Column(db.JSON, nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)


def log_audit_action(
    action: str,
    resource_type: str | None = None,
    resource_id: str | None = None,
    details: dict | None = None,
):
    """Log an audit action to the database.

    P1.2: the table is created by Alembic migration; this function
    only inserts. Failures are logged and never break the request.
    """
    try:
        user_id = getattr(g, "account_id", None)
        tenant_id = getattr(g, "tenant_id", None)

        entry = AuditLog(
            user_id=str(user_id) if user_id else None,
            tenant_id=str(tenant_id) if tenant_id else None,
            action=action,
            resource_type=resource_type,
            resource_id=str(resource_id) if resource_id else None,
            details=details,
            ip_address=request.remote_addr,
            user_agent=str(request.user_agent)[:255] if request.user_agent else None,
        )
        db.session.add(entry)
        db.session.commit()
    except Exception:
        logger.exception("Failed to write audit log for action: %s", action)
        db.session.rollback()


def audit_action(action: str, resource_type: str | None = None):
    """Decorator that logs an audit action after a successful (2xx) request.

    Usage::

        @console_ns.route(...)
        class MyEndpoint(Resource):
            @audit_action("tenant.create", resource_type="tenant")
            def post(self):
                ...
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            result = f(*args, **kwargs)

            # Only log successful mutations
            status_code = 200
            if isinstance(result, tuple) and len(result) >= 2:
                status_code = result[1] if isinstance(result[1], int) else 200

            if status_code < 300 and request.method in ("POST", "PUT", "PATCH", "DELETE"):
                resource_id = (
                    kwargs.get("id")
                    or kwargs.get("tenant_id")
                    or kwargs.get("clone_id")
                    or None
                )
                body = result[0] if isinstance(result, tuple) else result
                if resource_id is None and isinstance(body, dict):
                    resource_id = body.get("tenant_id") or body.get("id")
                    tenant = body.get("tenant")
                    if resource_id is None and isinstance(tenant, dict):
                        resource_id = tenant.get("id")
                log_audit_action(
                    action=action,
                    resource_type=resource_type,
                    resource_id=resource_id,
                    details={"method": request.method, "path": request.path},
                )

            return result

        return decorated_function

    return decorator
