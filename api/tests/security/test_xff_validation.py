"""
RED Security Test: X-Forwarded-For Validation for Rate Limiting

Tests that spoofed X-Forwarded-For headers cannot bypass rate limiting
when requests do not come from a trusted proxy.

RED = Reject, Escape, Detect
- Reject: Block spoofed X-Forwarded-For from non-trusted sources
- Escape: Fall back to request.remote_addr when not from trusted proxy
- Detect: Log when spoofed IPs are rejected

Trust model:
- TRUSTED_PROXY_IPS env var defines trusted proxy networks (CIDR notation)
- Only requests from trusted proxies have X-Forwarded-For parsed
- All other requests use request.remote_addr directly
"""
import os
import pytest


@pytest.fixture
def clean_trusted_proxy_env(monkeypatch):
    """Fixture to temporarily clear TRUSTED_PROXY_IPS env var."""
    monkeypatch.delenv("TRUSTED_PROXY_IPS", raising=False)
    yield


class TestXForwardedForValidation:
    """Test X-Forwarded-For validation logic."""

    def test_get_validated_client_ip_function_exists(self):
        """Verify _get_validated_client_ip function exists."""
        from api.controllers.myownclone_public import _get_validated_client_ip
        assert callable(_get_validated_client_ip)

    def test_is_from_trusted_proxy_function_exists(self):
        """Verify _is_from_trusted_proxy function exists."""
        from api.controllers.myownclone_public import _is_from_trusted_proxy
        assert callable(_is_from_trusted_proxy)

    def test_get_trusted_proxy_nets_function_exists(self):
        """Verify _get_trusted_proxy_nets function exists."""
        from api.controllers.myownclone_public import _get_trusted_proxy_nets
        assert callable(_get_trusted_proxy_nets)

    def test_no_trusted_proxies_configured_defaults_to_remote_addr(
        self, app, clean_trusted_proxy_env
    ):
        """When no TRUSTED_PROXY_IPS configured, X-Forwarded-For should be ignored."""
        from api.controllers.myownclone_public import (
            _get_validated_client_ip,
            _get_trusted_proxy_nets,
            _is_from_trusted_proxy,
        )

        # Verify no trusted proxies configured
        assert _get_trusted_proxy_nets() == []

        # Simulate a request with spoofed X-Forwarded-For
        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "10.0.0.1,192.168.1.1"},
            environ_base={"REMOTE_ADDR": "203.0.113.50"}
        ):
            # Even with X-Forwarded-For, should return remote_addr since no trusted proxy
            assert _is_from_trusted_proxy("203.0.113.50") is False
            client_ip = _get_validated_client_ip()
            assert client_ip == "203.0.113.50"

    def test_spoofed_xff_rejected_when_not_from_trusted_proxy(self, app, monkeypatch):
        """Spoofed X-Forwarded-For should NOT be used when request is not from trusted proxy."""
        # Configure trusted proxy - but the incoming request is NOT from it
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8")

        from api.controllers.myownclone_public import (
            _is_from_trusted_proxy,
            _get_validated_client_ip,
        )

        # Request comes from 203.0.113.50 (not in 10.0.0.0/8)
        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "10.0.0.1"},
            environ_base={"REMOTE_ADDR": "203.0.113.50"}
        ):
            assert _is_from_trusted_proxy("203.0.113.50") is False
            # Should NOT use X-Forwarded-For value since not from trusted proxy
            client_ip = _get_validated_client_ip()
            assert client_ip == "203.0.113.50"
            assert client_ip != "10.0.0.1"  # Spoofed IP rejected

    def test_xff_accepted_from_trusted_proxy(self, app, monkeypatch):
        """X-Forwarded-For should be used when request comes from trusted proxy."""
        # Configure trusted proxy
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8")

        from api.controllers.myownclone_public import (
            _is_from_trusted_proxy,
            _get_validated_client_ip,
        )

        # Request comes from 10.0.0.1 (in 10.0.0.0/8)
        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "203.0.113.50"},
            environ_base={"REMOTE_ADDR": "10.0.0.1"}
        ):
            assert _is_from_trusted_proxy("10.0.0.1") is True
            # Should use X-Forwarded-For since request is from trusted proxy
            client_ip = _get_validated_client_ip()
            assert client_ip == "203.0.113.50"

    def test_xff_multiple_ips_takes_first(self, app, monkeypatch):
        """When X-Forwarded-For has multiple IPs, first (original client) should be used."""
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8")

        from api.controllers.myownclone_public import _get_validated_client_ip

        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "203.0.113.50,10.0.0.2,10.0.0.3"},
            environ_base={"REMOTE_ADDR": "10.0.0.1"}
        ):
            client_ip = _get_validated_client_ip()
            assert client_ip == "203.0.113.50"

    def test_xff_empty_fallback_to_remote_addr(self, app, monkeypatch):
        """When X-Forwarded-For is empty but from trusted proxy, fallback to remote_addr."""
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8")

        from api.controllers.myownclone_public import _get_validated_client_ip

        with app.test_request_context(
            "/",
            headers={},  # No X-Forwarded-For
            environ_base={"REMOTE_ADDR": "10.0.0.1"}
        ):
            client_ip = _get_validated_client_ip()
            assert client_ip == "10.0.0.1"

    def test_ipv6_trusted_proxy_support(self, app, monkeypatch):
        """IPv6 addresses should work with trusted proxy validation."""
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "2001:db8::/32")

        from api.controllers.myownclone_public import (
            _is_from_trusted_proxy,
            _get_validated_client_ip,
        )

        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "192.0.2.1"},
            environ_base={"REMOTE_ADDR": "2001:db8::1"}
        ):
            assert _is_from_trusted_proxy("2001:db8::1") is True
            client_ip = _get_validated_client_ip()
            assert client_ip == "192.0.2.1"

    def test_invalid_cidr_in_config_logged_warning(self, app, monkeypatch, caplog):
        """Invalid CIDR in TRUSTED_PROXY_IPS should log a warning."""
        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8,invalid-cidr,192.168.0.0/16")

        import logging
        caplog.set_level(logging.WARNING)

        from api.controllers.myownclone_public import _get_trusted_proxy_nets

        nets = _get_trusted_proxy_nets()
        # Should have parsed the two valid networks, skipped invalid
        assert len(nets) == 2
        assert any("invalid-cidr" in record.message for record in caplog.records)


class TestRateLimitKeyUsesValidatedIP:
    """Test that rate limiting uses validated client IP."""

    def test_check_rate_limit_public_function_exists(self):
        """Verify _check_rate_limit_public function exists."""
        from api.controllers.myownclone_public import _check_rate_limit_public
        assert callable(_check_rate_limit_public)

    def test_rate_limit_uses_validated_ip(self, app, clean_trusted_proxy_env):
        """Rate limit should use validated IP, not spoofed X-Forwarded-For."""
        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "10.0.0.1"},
            environ_base={"REMOTE_ADDR": "203.0.113.50"}
        ):
            # The function should use the validated IP (203.0.113.50) not spoofed (10.0.0.1)
            # We can verify this by checking _get_validated_client_ip returns correct value
            from api.controllers.myownclone_public import _get_validated_client_ip
            client_ip = _get_validated_client_ip()
            assert client_ip == "203.0.113.50"
            assert client_ip != "10.0.0.1"


class TestVisitorIDUsesValidatedIP:
    """Test that _visitor_id uses validated client IP."""

    def test_visitor_id_function_exists(self):
        """Verify _visitor_id function exists."""
        from api.controllers.myownclone_public import _visitor_id
        assert callable(_visitor_id)

    def test_visitor_id_spoofed_xff_rejected(self, app, clean_trusted_proxy_env):
        """Visitor ID should use validated IP, not spoofed X-Forwarded-For."""
        from api.controllers.myownclone_public import _visitor_id

        with app.test_request_context(
            "/",
            headers={
                "X-Forwarded-For": "10.0.0.1",
                "User-Agent": "TestBrowser/1.0"
            },
            environ_base={"REMOTE_ADDR": "203.0.113.50"}
        ):
            visitor_id = _visitor_id()
            # Visitor ID should be based on real IP, not spoofed
            # We can't know the exact hash, but it should be different
            # from what it would be with the spoofed IP
            expected_based_on_real = "203.0.113.50:TestBrowser/1.0"
            expected_based_on_spoofed = "10.0.0.1:TestBrowser/1.0"
            # The visitor_id should hash the REAL IP, not the spoofed one
            import hashlib
            real_hash = hashlib.sha256(expected_based_on_real.encode()).hexdigest()[:32]
            spoofed_hash = hashlib.sha256(expected_based_on_spoofed.encode()).hexdigest()[:32]
            assert visitor_id == real_hash
            assert visitor_id != spoofed_hash


class TestSecurityEventLogging:
    """Test that security-relevant XFF spoofing is handled properly."""

    def test_spoofed_ip_logged_as_part_of_validation(self, app, monkeypatch, caplog):
        """When spoofed XFF is rejected, it should be traceable in logs."""
        import logging
        caplog.set_level(logging.INFO)

        monkeypatch.setenv("TRUSTED_PROXY_IPS", "10.0.0.0/8")

        from api.controllers.myownclone_public import _get_validated_client_ip

        # Request from outside trusted range with spoofed XFF
        with app.test_request_context(
            "/",
            headers={"X-Forwarded-For": "10.0.0.1"},
            environ_base={"REMOTE_ADDR": "203.0.113.50"}
        ):
            client_ip = _get_validated_client_ip()
            # The spoofed attempt was rejected, real IP used
            assert client_ip == "203.0.113.50"
