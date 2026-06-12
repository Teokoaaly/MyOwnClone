from flask import Flask, g

from api.controllers.console.myownclone.stripe_ctrl import (
    DEFAULT_DASHBOARD_CANCEL_PATH,
    DEFAULT_DASHBOARD_SUCCESS_PATH,
    _account_email,
    _safe_redirect_url,
)


def test_safe_redirect_normalizes_old_dashboard_paths(monkeypatch):
    monkeypatch.setenv("MYOWNCLONE_SITE_URL", "http://localhost:3000")
    app = Flask(__name__)

    with app.test_request_context("/"):
        assert _safe_redirect_url("/dashboard/resumen", DEFAULT_DASHBOARD_SUCCESS_PATH) == "http://localhost:3000/resumen"
        assert _safe_redirect_url("/dashboard/facturacion", DEFAULT_DASHBOARD_CANCEL_PATH) == "http://localhost:3000/facturacion"


def test_safe_redirect_rejects_foreign_absolute_urls(monkeypatch):
    monkeypatch.setenv("MYOWNCLONE_SITE_URL", "http://localhost:3000")
    app = Flask(__name__)

    with app.test_request_context("/"):
        assert _safe_redirect_url("https://evil.example/steal", DEFAULT_DASHBOARD_SUCCESS_PATH) == "http://localhost:3000/resumen"


def test_account_email_uses_forwarded_proxy_identity():
    app = Flask(__name__)

    with app.test_request_context("/"):
        g.account_email = "admin@example.com"
        assert _account_email("user-id") == "admin@example.com"
