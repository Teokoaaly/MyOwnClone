"""System-wide settings table for runtime configuration."""
from datetime import datetime

from api.extensions.ext_database import db


class SystemSetting(db.Model):
    """Generic key-value store for system-level runtime flags.

    Examples: maintenance_mode (true/false), feature flags, etc.
    """

    __tablename__ = "system_settings"

    key = db.Column(db.String(64), primary_key=True)
    value = db.Column(db.Text, nullable=True)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    def __repr__(self) -> str:
        return f"<SystemSetting {self.key}={self.value!r}>"
