"""Maintenance mode controller endpoints."""
import logging

from flask import request
from flask_restx import Resource

from api.controllers.console import console_ns
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
    def post(self):
        payload = request.get_json(silent=True) or {}
        active = bool(payload.get("active", False))
        try:
            set_maintenance_active(active)
        except Exception as e:
            logger.exception("Failed to set maintenance flag")
            return {"error": "internal_error", "message": str(e)}, 500
        return {"active": active, "message": "ok"}, 200
