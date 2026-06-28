"""Test for maintenance flag helper."""
from unittest.mock import patch

from api.core.maintenance import is_maintenance_active


def test_is_maintenance_active_returns_false_when_no_row():
    with patch("api.core.maintenance.db.session") as mock_session:
        mock_session.execute.return_value.scalar_one_or_none.return_value = None
        assert is_maintenance_active() is False


def test_is_maintenance_active_returns_true_when_flag_true():
    with patch("api.core.maintenance.db.session") as mock_session:
        mock_session.execute.return_value.scalar_one_or_none.return_value = "true"
        assert is_maintenance_active() is True


def test_is_maintenance_active_returns_false_when_flag_false():
    with patch("api.core.maintenance.db.session") as mock_session:
        mock_session.execute.return_value.scalar_one_or_none.return_value = "false"
        assert is_maintenance_active() is False


def test_is_maintenance_active_fails_open_on_db_error():
    with patch("api.core.maintenance.db.session") as mock_session:
        mock_session.execute.side_effect = Exception("DB down")
        assert is_maintenance_active() is False
