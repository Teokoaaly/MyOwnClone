"""Maintenance mode middleware.

When maintenance is active:
- Login and /maintenance/status endpoints always pass
- Admin users (platform_admin role) pass through everything
- Non-admin users get HTTP 503 on all other endpoints
"""
import base64
import json
import logging

from flask import g, jsonify, request

from api.core.maintenance import is_maintenance_active

logger = logging.getLogger(__name__)


def _is_admin() -> bool:
    """Check if the current request user is platform_admin.

    Tries in order:
    1. g.account_role (set by login_required decorator AFTER middleware runs)
    2. X-User-Role header (set by Next.js proxy for service-to-service)
    3. Direct JWT decode from Authorization: Bearer header
    """
    try:
        role = getattr(g, "account_role", None)
        if role:
            return role == "platform_admin"
        header_role = request.headers.get("X-User-Role", "").strip()
        if header_role:
            return header_role == "platform_admin"
        auth_header = request.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
            try:
                parts = token.split(".")
                if len(parts) == 3:
                    payload_b64 = parts[1]
                    payload_b64 += "=" * (-len(payload_b64) % 4)
                    payload = json.loads(base64.urlsafe_b64decode(payload_b64))
                    return payload.get("role") == "platform_admin"
            except Exception:
                pass
        return False
    except Exception:
        logger.exception("Failed to determine if user is admin; defaulting to False")
        return False


def init_maintenance_middleware(app) -> None:
    """Register the before_request hook on the Flask app."""

    @app.before_request
    def enforce_maintenance():
        if not is_maintenance_active():
            return

        # Always allow login endpoints
        if request.path.endswith("/auth/login"):
            return

        # Always allow status endpoint (used by client to poll)
        if "/maintenance/status" in request.path:
            return

        # Admins pass through everything
        if _is_admin():
            return

        # Non-admin: block with 503
        logger.info(
            "Maintenance active; blocking %s %s for non-admin",
            request.method, request.path,
        )
        return (
            jsonify({
                "error": "service_unavailable",
                "message": "Sistema en mantenimiento. Vuelve pronto.",
            }),
            503,
        )
