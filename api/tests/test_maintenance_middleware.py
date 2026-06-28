"""Test for maintenance middleware."""
from unittest.mock import patch

import pytest
from flask import Flask

from api.middleware.maintenance import init_maintenance_middleware
from api.i18n import init_i18n


@pytest.fixture
def app():
    app = Flask(__name__)
    init_i18n(app)
    init_maintenance_middleware(app)

    @app.route("/auth/login", methods=["POST"])
    def login():
        return "ok", 200

    @app.route("/admin/test", methods=["GET", "POST"])
    def admin_test():
        return "ok", 200

    @app.route("/maintenance/status")
    def status():
        return {"active": False}, 200

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_login_passes_when_maintenance_active(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=True), \
         patch("api.middleware.maintenance._is_admin", return_value=False):
        r = client.post("/auth/login")
        assert r.status_code == 200


def test_admin_get_passes_during_maintenance(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=True), \
         patch("api.middleware.maintenance._is_admin", return_value=True):
        r = client.get("/admin/test")
        assert r.status_code == 200


def test_admin_post_passes_during_maintenance(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=True), \
         patch("api.middleware.maintenance._is_admin", return_value=True):
        r = client.post("/admin/test")
        assert r.status_code == 200


def test_non_admin_get_blocked_during_maintenance(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=True), \
         patch("api.middleware.maintenance._is_admin", return_value=False):
        r = client.get("/admin/test")
        assert r.status_code == 503


def test_non_admin_post_blocked_during_maintenance(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=True), \
         patch("api.middleware.maintenance._is_admin", return_value=False):
        r = client.post("/admin/test")
        assert r.status_code == 503


def test_all_passes_when_maintenance_inactive(client):
    with patch("api.middleware.maintenance.is_maintenance_active", return_value=False):
        r = client.get("/admin/test")
        assert r.status_code == 200
        r = client.post("/admin/test")
        assert r.status_code == 200
