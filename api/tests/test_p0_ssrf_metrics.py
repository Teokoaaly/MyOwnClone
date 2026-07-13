"""Regression tests for P0.5: SSRF allowlist + /metrics auth (auditoria 2026-07-13).

Covers:
- C-10: ``_is_safe_url`` blocks internal/cloud-metadata URLs before fetch.
- C-13: ``/metrics`` requires auth in production; returns 401/404 without creds.
"""
from __future__ import annotations

import pytest

from api.core.ingestion import UnsafeURLError, _is_safe_url
from api.core.metrics import _metrics_authorized, _metrics_has_creds_configured


# ── C-10: SSRF allowlist ────────────────────────────────────────────────

class TestSSRFAllowlist:
    def test_blocks_loopback_ipv4(self):
        with pytest.raises(UnsafeURLError, match="blocked"):
            _is_safe_url("http://127.0.0.1:5001/admin")

    def test_blocks_loopback_hostname(self):
        with pytest.raises(UnsafeURLError, match="blocked"):
            _is_safe_url("http://localhost/admin")

    def test_blocks_link_local_metadata(self):
        # AWS/Azure/DO metadata endpoint.
        with pytest.raises(UnsafeURLError, match="metadata"):
            _is_safe_url("http://169.254.169.254/latest/meta-data/")

    def test_blocks_private_network_10(self):
        with pytest.raises(UnsafeURLError, match="blocked"):
            _is_safe_url("http://10.0.0.1/internal")

    def test_blocks_private_network_192(self):
        with pytest.raises(UnsafeURLError, match="blocked"):
            _is_safe_url("http://192.168.1.1/router")

    def test_blocks_gcp_metadata_host(self):
        with pytest.raises(UnsafeURLError, match="metadata"):
            _is_safe_url("http://metadata.google.internal/computeMetadata/")

    def test_blocks_file_scheme(self):
        with pytest.raises(UnsafeURLError, match="scheme"):
            _is_safe_url("file:///etc/passwd")

    def test_blocks_gopher_scheme(self):
        with pytest.raises(UnsafeURLError, match="scheme"):
            _is_safe_url("gopher://x")

    def test_blocks_missing_scheme(self):
        with pytest.raises(UnsafeURLError, match="scheme"):
            _is_safe_url("//example.com/path")

    def test_blocks_empty(self):
        with pytest.raises(UnsafeURLError, match="empty"):
            _is_safe_url("")

    def test_allows_public_hostname(self):
        # example.com resolves to public IANA reserved addresses; must NOT
        # raise (it is a reserved documentation domain but publicly routable
        # at the IP level for resolution purposes).
        try:
            _is_safe_url("https://example.com/index.html")
        except UnsafeURLError as exc:
            # If the test runner has no network, resolution fails — that is
            # also a rejection, but via "unable to resolve", not "blocked".
            assert "blocked" not in str(exc).lower() or "resolves" in str(exc).lower()

    def test_allows_public_ipv4(self):
        # 8.8.8.8 is a public anycast address; must be allowed.
        _is_safe_url("https://8.8.8.8/dns")


# ── C-13: /metrics auth ─────────────────────────────────────────────────

class TestMetricsAuth:
    def test_metrics_open_in_dev_without_creds(self, app, monkeypatch):
        # dev env, no creds configured.
        monkeypatch.delenv("METRICS_USER", raising=False)
        monkeypatch.delenv("METRICS_PASSWORD", raising=False)
        monkeypatch.delenv("METRICS_TOKEN", raising=False)
        monkeypatch.setenv("FLASK_ENV", "development")
        assert _metrics_has_creds_configured() is False

        class FakeReq:
            headers = {}
        assert _metrics_authorized(FakeReq()) is True

    def test_metrics_rejects_in_production_without_creds(self, monkeypatch):
        # production, no creds -> deny by default.
        monkeypatch.delenv("METRICS_USER", raising=False)
        monkeypatch.delenv("METRICS_PASSWORD", raising=False)
        monkeypatch.delenv("METRICS_TOKEN", raising=False)
        monkeypatch.setenv("FLASK_ENV", "production")

        class FakeReq:
            headers = {}
        assert _metrics_authorized(FakeReq()) is False

    def test_metrics_accepts_valid_basic_auth(self, monkeypatch):
        import base64
        monkeypatch.setenv("METRICS_USER", "scraper")
        monkeypatch.setenv("METRICS_PASSWORD", "s3cret")
        monkeypatch.setenv("FLASK_ENV", "production")

        creds = base64.b64encode(b"scraper:s3cret").decode()
        class FakeReq:
            headers = {"Authorization": f"Basic {creds}"}
        assert _metrics_authorized(FakeReq()) is True

    def test_metrics_rejects_wrong_basic_auth(self, monkeypatch):
        import base64
        monkeypatch.setenv("METRICS_USER", "scraper")
        monkeypatch.setenv("METRICS_PASSWORD", "s3cret")
        monkeypatch.setenv("FLASK_ENV", "production")

        creds = base64.b64encode(b"scraper:wrong").decode()
        class FakeReq:
            headers = {"Authorization": f"Basic {creds}"}
        assert _metrics_authorized(FakeReq()) is False

    def test_metrics_accepts_valid_bearer_token(self, monkeypatch):
        monkeypatch.delenv("METRICS_USER", raising=False)
        monkeypatch.delenv("METRICS_PASSWORD", raising=False)
        monkeypatch.setenv("METRICS_TOKEN", "tok-123")
        monkeypatch.setenv("FLASK_ENV", "production")

        class FakeReq:
            headers = {"Authorization": "Bearer tok-123"}
        assert _metrics_authorized(FakeReq()) is True

    def test_metrics_rejects_missing_auth_header(self, monkeypatch):
        monkeypatch.setenv("METRICS_TOKEN", "tok-123")
        monkeypatch.setenv("FLASK_ENV", "production")

        class FakeReq:
            headers = {}
        assert _metrics_authorized(FakeReq()) is False

    def test_metrics_endpoint_returns_401_in_prod_with_creds(self, app, monkeypatch):
        monkeypatch.setenv("METRICS_USER", "scraper")
        monkeypatch.setenv("METRICS_PASSWORD", "s3cret")
        monkeypatch.setenv("FLASK_ENV", "production")
        response = app.test_client().get("/metrics")
        assert response.status_code == 401
        assert "WWW-Authenticate" in response.headers

    def test_metrics_endpoint_serves_with_basic_auth(self, app, monkeypatch):
        import base64
        monkeypatch.setenv("METRICS_USER", "scraper")
        monkeypatch.setenv("METRICS_PASSWORD", "s3cret")
        monkeypatch.setenv("FLASK_ENV", "production")
        creds = base64.b64encode(b"scraper:s3cret").decode()
        response = app.test_client().get(
            "/metrics",
            headers={"Authorization": f"Basic {creds}"},
        )
        assert response.status_code == 200
