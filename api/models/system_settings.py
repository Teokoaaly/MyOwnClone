"""System-wide settings table for runtime configuration."""
from datetime import datetime, timezone

from api.extensions.ext_database import db


def _naive_utc_now():
    """P2.4: replacement for datetime.utcnow (deprecated in Py 3.12+)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class SystemSetting(db.Model):
    """Generic key-value store for system-level runtime flags.

    Examples: maintenance_mode (true/false), feature flags, etc.
    """

    __tablename__ = "system_settings"

    key = db.Column(db.String(64), primary_key=True)
    value = db.Column(db.Text, nullable=True)
    updated_at = db.Column(
        db.DateTime,
        default=_naive_utc_now,
        onupdate=_naive_utc_now,
    )

    def __repr__(self) -> str:
        return f"<SystemSetting {self.key}={self.value!r}>"
