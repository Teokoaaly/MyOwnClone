"""Maintenance mode middleware."""
import logging

from flask import g, jsonify, request

from api.core.maintenance import is_maintenance_active

logger = logging.getLogger(__name__)


def _is_admin() -> bool:
    """Check if the current request user is platform_admin."""
    try:
        user = getattr(g, "current_user", None) or getattr(g, "user", None)
        if user is None:
            return False
        role = getattr(user, "role", None)
        return role == "platform_admin"
    except Exception:
        logger.exception("Failed to determine if user is admin; defaulting to False")
        return False


def init_maintenance_middleware(app) -> None:
    @app.before_request
    def enforce_maintenance():
        if not is_maintenance_active():
            return

        if request.path.endswith("/auth/login"):
            return
        if "/maintenance/status" in request.path:
            return

        if _is_admin():
            return

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
