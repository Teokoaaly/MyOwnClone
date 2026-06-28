"""Maintenance mode helper functions."""
import logging

from sqlalchemy import select, text

from api.extensions.ext_database import db
from api.models.system_settings import SystemSetting

logger = logging.getLogger(__name__)


def is_maintenance_active() -> bool:
    """Read maintenance flag from DB. Fail-open on DB error."""
    try:
        row = db.session.execute(
            select(SystemSetting.value).where(SystemSetting.key == "maintenance_mode")
        ).scalar_one_or_none()
        return row == "true"
    except Exception:
        logger.exception("Failed to read maintenance_mode flag; failing open")
        return False


def set_maintenance_active(active: bool) -> None:
    """Set maintenance flag. Used by admin toggle endpoint."""
    value = "true" if active else "false"
    db.session.execute(
        text("UPDATE system_settings SET value = :v WHERE key = 'maintenance_mode'"),
        {"v": value},
    )
    db.session.commit()
