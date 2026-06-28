"""Test for maintenance controller module structure."""
import inspect


def test_module_exports_status_class():
    """Module exports MaintenanceStatusApi class."""
    from api.controllers.console.myownclone.maintenance import MaintenanceStatusApi
    assert inspect.isclass(MaintenanceStatusApi)


def test_module_exports_toggle_class():
    """Module exports MaintenanceToggleApi class."""
    from api.controllers.console.myownclone.maintenance import MaintenanceToggleApi
    assert inspect.isclass(MaintenanceToggleApi)


def test_status_class_has_get_method():
    """MaintenanceStatusApi has a get method."""
    from api.controllers.console.myownclone.maintenance import MaintenanceStatusApi
    assert hasattr(MaintenanceStatusApi, "get")
    assert callable(MaintenanceStatusApi.get)


def test_toggle_class_has_post_method():
    """MaintenanceToggleApi has a post method."""
    from api.controllers.console.myownclone.maintenance import MaintenanceToggleApi
    assert hasattr(MaintenanceToggleApi, "post")
    assert callable(MaintenanceToggleApi.post)
