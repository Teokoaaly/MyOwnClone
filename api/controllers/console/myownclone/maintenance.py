"""Maintenance mode controller endpoints."""
import logging

from flask import g, request
from flask_restx import Resource

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.maintenance import is_maintenance_active, set_maintenance_active
from api.libs.login import login_required

logger = logging.getLogger(__name__)


@console_ns.route("/myownclone/maintenance/status")
class MaintenanceStatusApi(Resource):
    """Public endpoint to check maintenance mode state."""

    def get(self):
        active = is_maintenance_active()
        return {"active": active, "message": ""}, 200


@console_ns.route("/myownclone/maintenance/toggle")
class MaintenanceToggleApi(Resource):
    """Admin endpoint to toggle maintenance mode."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        # Verify admin role
        from api.controllers.console.myownclone.admin_platform import _is_platform_admin
        if not _is_platform_admin(getattr(g, "account_id", "")):
            return {"error": "platform admin only"}, 403

        payload = request.get_json(silent=True) or {}
        active = bool(payload.get("active", False))
        try:
            set_maintenance_active(active)
        except Exception as e:
            logger.exception("Failed to set maintenance flag")
            return {"error": "internal_error"}, 500
        return {"active": active, "message": "ok"}, 200
