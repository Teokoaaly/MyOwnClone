"""Redis-only rate limiting with circuit breaker for fail-closed behavior.

This module provides rate limiting that ONLY uses Redis. If Redis is unavailable
or the circuit breaker is open, requests are rejected with 503 (fail-closed).

Key schema (from security_types.py):
    - Public: ratelimit:{ip}:{endpoint}
    - Authenticated: ratelimit:{tenant_id}:{endpoint}
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from enum import Enum

import redis

from api.core.security_types import (
    RATE_LIMIT_KEY_PREFIX,
    RateLimitKey,
    RateLimitKeyType,
)

logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Circuit breaker states."""

    CLOSED = "closed"  # Normal operation, Redis requests allowed
    OPEN = "open"  # Redis failing, reject requests
    HALF_OPEN = "half_open"  # Testing if Redis recovered


@dataclass(frozen=True)
class RateLimitConfig:
    """Configuration for a rate limit rule."""

    limit: int
    window_seconds: int


# Circuit breaker configuration
_CIRCUIT_BREAKER_FAILURE_THRESHOLD = 3  # Failures before opening circuit
_CIRCUIT_BREAKER_RESET_TIMEOUT = 30  # Seconds before trying half-open
_CIRCUIT_FAILURE_TIMEOUT = 1.0  # Socket timeout for Redis operations

# Global state
_circuit_state = CircuitState.CLOSED
_circuit_failure_count = 0
_circuit_last_failure_time: float | None = None
_redis_client: redis.Redis | None = None
_redis_initialized = False


def _get_client() -> redis.Redis | None:
    """Get or create Redis client with circuit breaker protection.

    Returns:
        Redis client if available and circuit is closed/half-open, None otherwise.

    Note:
        Unlike other Redis helpers, this returns None when the circuit is open
        to enforce fail-closed behavior (calling code should reject the request).
    """
    global _circuit_state, _circuit_failure_count, _circuit_last_failure_time, _redis_client, _redis_initialized

    # Check circuit breaker state
    current_time = time.time()

    if _circuit_state == CircuitState.OPEN:
        # Check if we should transition to half-open
        if _circuit_last_failure_time and (current_time - _circuit_last_failure_time) >= _CIRCUIT_BREAKER_RESET_TIMEOUT:
            logger.info("Rate limiter: circuit breaker transitioning to HALF_OPEN (testing Redis)")
            _circuit_state = CircuitState.HALF_OPEN
      ***REMOVED***:
            # Circuit is open, refuse to attempt Redis
            return None

    # If already initialized, return existing client
    if _redis_initialized:
        return _redis_client

    host = __get_env("REDIS_HOST", "")
    password = __get_env("REDIS_PASSWORD", "")
    port = int(__get_env("REDIS_PORT", "6379"))

    if not host:
        logger.error("Rate limiter: REDIS_HOST not configured - cannot enforce rate limits (fail-closed)")
        _redis_initialized = True
        _circuit_state = CircuitState.OPEN
        return None

    try:
        client = redis.Redis(
            host=host,
            port=port,
            password=password or None,
            socket_connect_timeout=_CIRCUIT_FAILURE_TIMEOUT,
            socket_timeout=_CIRCUIT_FAILURE_TIMEOUT,
        )
        # Test connection
        client.ping()
        _redis_client = client
        _redis_initialized = True
        _circuit_state = CircuitState.CLOSED
        _circuit_failure_count = 0
        logger.info("Rate limiter: connected to Redis at %s:%s", host, port)
        return client
    except redis.RedisError as exc:
        logger.error("Rate limiter: initial Redis connection failed (%s) - circuit OPEN", exc)
        _record_circuit_failure()
        _redis_initialized = True
        return None


def __get_env(key: str, default: str) -> str:
    """Get environment variable or default."""
    import os
    return os.environ.get(key, default)


def _record_circuit_failure() -> None:
    """Record a Redis failure and update circuit breaker state."""
    global _circuit_state, _circuit_failure_count, _circuit_last_failure_time

    _circuit_failure_count += 1
    _circuit_last_failure_time = time.time()

    if _circuit_failure_count >= _CIRCUIT_BREAKER_FAILURE_THRESHOLD:
        if _circuit_state != CircuitState.OPEN:
            logger.warning(
                "Rate limiter: circuit breaker OPEN after %d failures",
                _circuit_failure_count,
            )
        _circuit_state = CircuitState.OPEN


def _record_circuit_success() -> None:
    """Record a successful Redis operation and close circuit if half-open."""
    global _circuit_state, _circuit_failure_count

    if _circuit_state == CircuitState.HALF_OPEN:
        logger.info("Rate limiter: circuit breaker CLOSED (Redis recovered)")
    _circuit_state = CircuitState.CLOSED
    _circuit_failure_count = 0


def check_rate_limit(
    identifier: str,
    endpoint: str,
    key_type: RateLimitKeyType,
    config: RateLimitConfig,
) -> tuple[bool, int | None, int | None]:
    """Check and consume a rate limit slot using Redis.

    This function is FAIL-CLOSED: if Redis is unavailable or the circuit
    breaker is open, it returns (False, None, None) indicating the request
    should be rejected.

    Args:
        identifier: IP address (public) or tenant_id (authenticated)
        endpoint: The API endpoint being rate limited
        key_type: Whether this is a public or authenticated request
        config: Rate limit configuration (limit and window)

    Returns:
        Tuple of (allowed, remaining, reset_time):
        - allowed: True if request is within rate limit, False if exceeded
        - remaining: Number of requests remaining in window (None if Redis down)
        - reset_time: Seconds until rate limit window resets (None if Redis down)

    When Redis is unavailable, returns (False, None, None) to enforce
    fail-closed behavior (request is rejected).
    """
    client = _get_client()

    if client is None:
        # Circuit breaker open or Redis unavailable - fail closed
        logger.warning(
            "Rate limiter: Redis unavailable, rejecting request (fail-closed) "
            "identifier=%s endpoint=%s",
            identifier,
            endpoint,
        )
        return False, None, None

    key = RateLimitKey(
        identifier=identifier,
        endpoint=endpoint,
        key_type=key_type,
    )
    redis_key = key.to_redis_key()

    try:
        now = time.time()
        window_start = now - config.window_seconds

        # Use Redis pipeline for atomic operations
        pipe = client.pipeline()
        pipe.zremrangebyscore(redis_key, 0, window_start)  # Remove old entries
        pipe.zcard(redis_key)  # Count current entries
        pipe.zadd(redis_key, {str(now): now})  # Add this request
        pipe.expire(redis_key, config.window_seconds)
        results = pipe.execute()

        current_count = results[1]  # zcard result before adding this request
        remaining = max(0, config.limit - current_count - 1)
        reset_time = config.window_seconds

        if current_count >= config.limit:
            # Rate limit exceeded
            _record_circuit_success()
            return False, 0, reset_time

        _record_circuit_success()
        return True, remaining, reset_time

    except redis.RedisError as exc:
        logger.error("Rate limiter: Redis operation failed (%s) - fail-closed", exc)
        _record_circuit_failure()
        # Fail closed - reject the request
        return False, None, None


def is_redis_available() -> bool:
    """Check if Redis is available for rate limiting.

    This is useful for health checks and monitoring.

    Returns:
        True if Redis is available, False otherwise.
    """
    return _get_client() is not None


def get_circuit_state() -> CircuitState:
    """Get the current circuit breaker state."""
    return _circuit_state


def reset_circuit_for_testing() -> None:
    """Reset circuit breaker state for testing purposes.

    WARNING: This should only be used in tests, not in production.
    """
    global _circuit_state, _circuit_failure_count, _circuit_last_failure_time, _redis_initialized, _redis_client

    _circuit_state = CircuitState.CLOSED
    _circuit_failure_count = 0
    _circuit_last_failure_time = None
    _redis_initialized = False
    _redis_client = None
