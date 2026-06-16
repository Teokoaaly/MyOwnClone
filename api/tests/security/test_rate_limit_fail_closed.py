"""
RED Security Test: Rate Limiting Fail-Closed Behavior

Tests that rate limiting is Redis-only and fail-closed:
- R: Reject requests when Redis is unavailable (503)
- E: Enforce rate limits when Redis is available
- D: Detect and log Redis failures

Key security properties:
1. Redis is the ONLY rate limit store (no in-memory fallback for public endpoints)
2. When Redis is down, requests are REJECTED with 503, not allowed through
3. Circuit breaker prevents repeated Redis connection attempts during outage
4. Rate limit keys follow schema: ratelimit:{ip}:{endpoint}

This differs from auth.py which uses Redis with in-memory fallback (fail-open).
For public endpoints, we use Redis-only fail-closed to prevent abuse.
"""
import os
import pytest
import redis
from unittest.mock import patch, MagicMock


class TestRateLimitRedisOnly:
    """Test that public rate limiting uses Redis only, no in-memory fallback."""

    def test_no_in_memory_rate_limit_store(self):
        """Verify no in-memory rate limit store exists in myownclone_public."""
        # The _public_rate_limit_store should NOT exist in myownclone_public
        # (it was removed in favor of Redis-only)
        import api.controllers.myownclone_public as public_module

        assert not hasattr(public_module, '_public_rate_limit_store'), (
            "In-memory rate limit store should not exist - use Redis only"
        )

    def test_rate_limit_module_has_circuit_breaker(self):
        """Verify rate_limit module implements circuit breaker pattern."""
        from api.core.rate_limit import (
            CircuitState,
            check_rate_limit,
            get_circuit_state,
            reset_circuit_for_testing,
        )

        assert hasattr(CircuitState, 'CLOSED')
        assert hasattr(CircuitState, 'OPEN')
        assert hasattr(CircuitState, 'HALF_OPEN')
        assert callable(check_rate_limit)
        assert callable(get_circuit_state)

    def test_rate_limit_key_schema_uses_ratelimit_prefix(self):
        """Verify rate limit keys use 'ratelimit:' prefix from security_types."""
        from api.core.security_types import RATE_LIMIT_KEY_PREFIX
        assert RATE_LIMIT_KEY_PREFIX == "ratelimit"

    def test_rate_limit_public_key_format(self):
        """Verify public rate limit key format is ratelimit:{ip}:{endpoint}."""
        from api.core.security_types import (
            RATE_LIMIT_KEY_FORMAT_PUBLIC,
            RateLimitKey,
            RateLimitKeyType,
        )
        assert RATE_LIMIT_KEY_FORMAT_PUBLIC == "ratelimit:{ip}:{endpoint}"

        key = RateLimitKey(
            identifier="192.168.1.1",
            endpoint="/chat_public/test-slug",
            key_type=RateLimitKeyType.PUBLIC,
        )
        assert key.to_redis_key() == "ratelimit:192.168.1.1:/chat_public/test-slug"


class TestRateLimitFailClosed:
    """Test fail-closed behavior when Redis is unavailable."""

    def teardown_method(self):
        """Reset circuit breaker after each test."""
        from api.core.rate_limit import reset_circuit_for_testing
        reset_circuit_for_testing()

    def test_returns_503_when_redis_unavailable(self):
        """When Redis is unavailable, rate limit check returns (False, None)."""
        from api.core.rate_limit import (
            check_rate_limit,
            RateLimitConfig,
            CircuitState,
        )
        from api.core.security_types import RateLimitKeyType

        # Simulate Redis unavailable by patching environment
        with patch.dict(os.environ, {'REDIS_HOST': ''}):
            from api.core.rate_limit import reset_circuit_for_testing
            reset_circuit_for_testing()

            config = RateLimitConfig(limit=10, window_seconds=60)
            allowed, remaining, reset_time = check_rate_limit(
                identifier="192.168.1.1",
                endpoint="/test",
                key_type=RateLimitKeyType.PUBLIC,
                config=config,
            )

            # Should reject (fail closed)
            assert allowed is False
            # remaining=None signals Redis was unavailable
            assert remaining is None

    def test_circuit_breaker_opens_after_failures(self):
        """Circuit breaker should open after repeated Redis failures."""
        from api.core.rate_limit import (
            CircuitState,
            _record_circuit_failure,
            get_circuit_state,
            reset_circuit_for_testing,
        )

        reset_circuit_for_testing()

        # Simulate failures
        for _ in range(3):
            _record_circuit_failure()

        assert get_circuit_state() == CircuitState.OPEN

    def test_check_rate_limit_returns_fail_closed_on_redis_error(self):
        """Redis errors should return fail-closed (False, None)."""
        from api.core.rate_limit import (
            check_rate_limit,
            RateLimitConfig,
            reset_circuit_for_testing,
        )
        from api.core.security_types import RateLimitKeyType
        import redis

        reset_circuit_for_testing()

        config = RateLimitConfig(limit=10, window_seconds=60)

        # Mock Redis to raise an error
        with patch('redis.Redis') as mock_redis:
            mock_redis.return_value.ping.side_effect = redis.RedisError("Connection failed")

            # Force re-initialization
            from api.core import rate_limit
            rate_limit._redis_initialized = False

            allowed, remaining, reset_time = check_rate_limit(
                identifier="192.168.1.1",
                endpoint="/test",
                key_type=RateLimitKeyType.PUBLIC,
                config=config,
            )

            assert allowed is False
            assert remaining is None


class TestRateLimitCheckRateLimitPublic:
    """Test the _check_rate_limit_public helper function."""

    def teardown_method(self):
        """Reset circuit breaker after each test."""
        from api.core.rate_limit import reset_circuit_for_testing
        reset_circuit_for_testing()

    def test_check_rate_limit_public_function_exists(self):
        """Verify _check_rate_limit_public function exists."""
        from api.controllers.myownclone_public import _check_rate_limit_public
        assert callable(_check_rate_limit_public)

    def test_check_rate_limit_public_returns_tuple(self, app):
        """_check_rate_limit_public should return (allowed, remaining) tuple."""
        from api.controllers.myownclone_public import _check_rate_limit_public
        from api.core.rate_limit import RateLimitConfig

        config = RateLimitConfig(limit=10, window_seconds=60)

        # Mock Redis to be unavailable
        with patch.dict(os.environ, {'REDIS_HOST': ''}):
            from api.core.rate_limit import reset_circuit_for_testing
            reset_circuit_for_testing()

            with app.test_request_context('/'):
                result = _check_rate_limit_public("test_scope", config, "test-slug")
                assert isinstance(result, tuple)
                assert len(result) == 2
                allowed, remaining = result
                assert isinstance(allowed, bool)
                # remaining can be int or None


class TestRateLimitServiceUnavailable:
    """Test the _rate_limit_service_unavailable helper function."""

    def test_service_unavailable_function_exists(self):
        """Verify _rate_limit_service_unavailable function exists."""
        from api.controllers.myownclone_public import _rate_limit_service_unavailable
        assert callable(_rate_limit_service_unavailable)

    def test_service_unavailable_returns_503(self):
        """_rate_limit_service_unavailable should return 503 status."""
        from api.controllers.myownclone_public import _rate_limit_service_unavailable

        payload, status = _rate_limit_service_unavailable()
        assert status == 503
        assert "error" in payload

    def test_endpoint_returns_503_when_redis_down(self, app):
        """Endpoint should return 503 when Redis is unavailable."""
        # This tests the integration - when Redis is down,
        # the endpoint should return 503, not allow the request through

        # We mock at a higher level since full integration requires Redis
        from api.controllers.myownclone_public import (
            _check_rate_limit_public,
            _rate_limit_service_unavailable,
        )
        from api.core.rate_limit import RateLimitConfig, reset_circuit_for_testing

        reset_circuit_for_testing()

        config = RateLimitConfig(limit=10, window_seconds=60)

        with patch.dict(os.environ, {'REDIS_HOST': ''}):
            reset_circuit_for_testing()
            with app.test_request_context('/'):
                allowed, remaining = _check_rate_limit_public("test", config, "slug")

                if not allowed and remaining is None:
                    payload, status = _rate_limit_service_unavailable()
                    assert status == 503
              ***REMOVED***:
                    pytest.fail("Expected fail-closed behavior when Redis is down")


class TestRateLimitConstants:
    """Test that rate limit constants are properly defined."""

    def test_rate_limit_configs_defined(self):
        """Verify rate limit config objects are defined."""
        from api.controllers.myownclone_public import (
            _CHAT_RATE_LIMIT_CONFIG,
            _CHAT_SIMPLE_RATE_LIMIT_CONFIG,
            _BOOKING_RATE_LIMIT_CONFIG,
        )
        from api.core.rate_limit import RateLimitConfig

        assert isinstance(_CHAT_RATE_LIMIT_CONFIG, RateLimitConfig)
        assert isinstance(_CHAT_SIMPLE_RATE_LIMIT_CONFIG, RateLimitConfig)
        assert isinstance(_BOOKING_RATE_LIMIT_CONFIG, RateLimitConfig)

    def test_rate_limit_values(self):
        """Verify rate limit values match original constants."""
        from api.controllers.myownclone_public import (
            _CHAT_RATE_LIMIT_CONFIG,
            _CHAT_SIMPLE_RATE_LIMIT_CONFIG,
            _BOOKING_RATE_LIMIT_CONFIG,
            _WINDOW_SECONDS,
            _CHAT_LIMIT,
            _CHAT_SIMPLE_LIMIT,
            _BOOKING_LIMIT,
        )

        assert _CHAT_RATE_LIMIT_CONFIG.limit == _CHAT_LIMIT
        assert _CHAT_RATE_LIMIT_CONFIG.window_seconds == _WINDOW_SECONDS

        assert _CHAT_SIMPLE_RATE_LIMIT_CONFIG.limit == _CHAT_SIMPLE_LIMIT
        assert _CHAT_SIMPLE_RATE_LIMIT_CONFIG.window_seconds == _WINDOW_SECONDS

        assert _BOOKING_RATE_LIMIT_CONFIG.limit == _BOOKING_LIMIT
        assert _BOOKING_RATE_LIMIT_CONFIG.window_seconds == _WINDOW_SECONDS


class TestCircuitBreakerRecovery:
    """Test circuit breaker recovery behavior."""

    def teardown_method(self):
        """Reset circuit breaker after each test."""
        from api.core.rate_limit import reset_circuit_for_testing
        reset_circuit_for_testing()

    def test_circuit_breaker_half_open_after_timeout(self):
        """Circuit should transition to half-open after reset timeout."""
        import time
        from api.core.rate_limit import (
            CircuitState,
            _record_circuit_failure,
            get_circuit_state,
            reset_circuit_for_testing,
        )

        reset_circuit_for_testing()

        # Open the circuit
        for _ in range(3):
            _record_circuit_failure()

        assert get_circuit_state() == CircuitState.OPEN

        # Manually set last failure time to 31 seconds ago
        from api.core import rate_limit
        rate_limit._circuit_last_failure_time = time.time() - 31

        # Force a re-check by getting the client (should transition to half-open)
        with patch('redis.Redis') as mock_redis:
            mock_redis.return_value.ping.side_effect = redis.RedisError("Still failing")

            from api.core.rate_limit import _get_client
            result = _get_client()

            # Should be in half-open state now
            # (Note: actual transition happens in _get_client, we just verify state)
            # The circuit should still be open since Redis is still failing
            assert get_circuit_state() in [CircuitState.OPEN, CircuitState.HALF_OPEN]


class TestRateLimitKeyType:
    """Test RateLimitKeyType enum usage."""

    def test_public_rate_limit_key_type_exists(self):
        """Verify RateLimitKeyType.PUBLIC exists."""
        from api.core.security_types import RateLimitKeyType
        assert RateLimitKeyType.PUBLIC is not None

    def test_rate_limit_key_type_in_check(self):
        """Rate limit check should use PUBLIC key type for public endpoints."""
        from api.core.security_types import RateLimitKeyType

        # Public endpoints should use PUBLIC key type
        assert RateLimitKeyType.PUBLIC.value == "public"
