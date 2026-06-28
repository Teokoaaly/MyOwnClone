"""Test for SystemSetting model."""
from api.models.system_settings import SystemSetting


def test_system_setting_tablename():
    assert SystemSetting.__tablename__ == "system_settings"


def test_system_setting_columns():
    columns = {c.name: c for c in SystemSetting.__table__.columns}
    assert "key" in columns
    assert "value" in columns
    assert "updated_at" in columns
    assert columns["key"].primary_key is True
