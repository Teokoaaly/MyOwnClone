"""Test for maintenance controller module structure.

The maintenance controller is registered via Flask-RESTX.
These tests verify the module exports the expected classes.
"""
import api.controllers.console.myownclone.maintenance as m


def test_module_exports_status_class():
    """Module exports MaintenanceStatusApi class."""
    assert hasattr(m, "MaintenanceStatusApi")


def test_module_exports_toggle_class():
    """Module exports MaintenanceToggleApi class."""
    assert hasattr(m, "MaintenanceToggleApi")


def test_status_class_has_get_method():
    """MaintenanceStatusApi has a get method."""
    assert hasattr(m.MaintenanceStatusApi, "get")
    assert callable(m.MaintenanceStatusApi.get)


def test_toggle_class_has_post_method():
    """MaintenanceToggleApi has a post method."""
    assert hasattr(m.MaintenanceToggleApi, "post")
    assert callable(m.MaintenanceToggleApi.post)
