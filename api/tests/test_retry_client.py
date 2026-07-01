"""Tests for RetryClient (retry + circuit breaker)."""
from __future__ import annotations
import pytest
from unittest.mock import MagicMock

from api.core.retry_client import (
    RetryClient, CircuitBreakerOpenError, get_retry_client, reset_retry_client,
    STATE_CLOSED, STATE_OPEN, STATE_HALF_OPEN,
)
from api.core.providers.base import ProviderError


# --- Retry behavior ---

def test_retry_succeeds_on_first_attempt():
    sleeps = []
    client = RetryClient(sleep=sleeps.append)
    func = MagicMock(return_value="ok")
    result = client.call(func, key="k1")
    assert result == "ok"
    assert func.call_count == 1
    assert sleeps == []


def test_retry_succeeds_on_second_attempt():
    sleeps = []
    client = RetryClient(sleep=sleeps.append, initial_backoff=0.01)
    func = MagicMock(side_effect=[
        ProviderError("rate limit", retriable=True),
        "ok",
    ])
    result = client.call(func, key="k2")
    assert result == "ok"
    assert func.call_count == 2
    assert len(sleeps) == 1


def test_retry_exhausted_raises_last_error():
    sleeps = []
    client = RetryClient(max_retries=2, sleep=sleeps.append, initial_backoff=0.01)
    func = MagicMock(side_effect=ProviderError("boom", retriable=True))
    with pytest.raises(ProviderError, match="boom"):
        client.call(func, key="k3")
    # 1 initial + 2 retries = 3 calls
    assert func.call_count == 3
    assert len(sleeps) == 2


def test_retry_does_not_retry_non_retriable_error():
    sleeps = []
    client = RetryClient(sleep=sleeps.append, initial_backoff=0.01)
    func = MagicMock(side_effect=ProviderError("bad request", retriable=False))
    with pytest.raises(ProviderError, match="bad request"):
        client.call(func, key="k4")
    assert func.call_count == 1
    assert sleeps == []


def test_retry_passes_through_unexpected_exception_without_retry():
    sleeps = []
    client = RetryClient(sleep=sleeps.append, initial_backoff=0.01)
    func = MagicMock(side_effect=ValueError("nope"))
    with pytest.raises(ValueError, match="nope"):
        client.call(func, key="k5")
    assert func.call_count == 1
    assert sleeps == []


def test_retry_exponential_backoff():
    sleeps = []
    client = RetryClient(
        max_retries=3,
        initial_backoff=0.1,
        backoff_multiplier=2.0,
        max_backoff=10.0,
        sleep=sleeps.append,
    )
    func = MagicMock(side_effect=ProviderError("x", retriable=True))
    with pytest.raises(ProviderError):
        client.call(func, key="k6")
    assert sleeps == [0.1, 0.2, 0.4]


def test_retry_caps_backoff_at_max():
    sleeps = []
    client = RetryClient(
        max_retries=3,
        initial_backoff=0.5,
        backoff_multiplier=10.0,
        max_backoff=2.0,
        sleep=sleeps.append,
    )
    func = MagicMock(side_effect=ProviderError("x", retriable=True))
    with pytest.raises(ProviderError):
        client.call(func, key="k7")
    # 0.5, 2.0 (capped), 2.0 (capped)
    assert sleeps == [0.5, 2.0, 2.0]


# --- Circuit breaker ---

def test_circuit_breaker_starts_closed():
    client = RetryClient(failure_threshold=3)
    state = client.get_breaker_state("key1")
    assert state["state"] == STATE_CLOSED
    assert state["failure_count"] == 0


def test_circuit_breaker_opens_after_threshold():
    sleeps = []
    client = RetryClient(
        failure_threshold=3,
        max_retries=0,  # don't retry, just record failure
        sleep=sleeps.append,
    )
    func = MagicMock(side_effect=ProviderError("x", retriable=True))
    for _ in range(3):
        with pytest.raises(ProviderError):
            client.call(func, key="breaker1")
    state = client.get_breaker_state("breaker1")
    assert state["state"] == STATE_OPEN
    assert state["failure_count"] == 3


def test_circuit_breaker_open_rejects_calls():
    sleeps = []
    client = RetryClient(
        failure_threshold=2,
        max_retries=0,
        reset_timeout=60.0,  # long so we stay open
        sleep=sleeps.append,
    )
    func = MagicMock(side_effect=ProviderError("x", retriable=True))
    # Trip the breaker
    for _ in range(2):
        with pytest.raises(ProviderError):
            client.call(func, key="breaker2")
    # Now subsequent calls should be rejected without invoking func
    call_count_before = func.call_count
    with pytest.raises(CircuitBreakerOpenError):
        client.call(func, key="breaker2")
    assert func.call_count == call_count_before  # func NOT called again


def test_circuit_breaker_isolated_per_key():
    sleeps = []
    client = RetryClient(failure_threshold=2, max_retries=0, sleep=sleeps.append)
    failing = MagicMock(side_effect=ProviderError("x", retriable=True))
    succeeding = MagicMock(return_value="ok")
    for _ in range(2):
        with pytest.raises(ProviderError):
            client.call(failing, key="bad")
    # bad is now open
    with pytest.raises(CircuitBreakerOpenError):
        client.call(failing, key="bad")
    # good is still closed
    assert client.call(succeeding, key="good") == "ok"


def test_circuit_breaker_resets_to_closed_after_success_threshold():
    """After reset_timeout elapses + a probe call succeeds, breaker should close."""
    import time as _t
    sleeps = []
    # Use a controllable clock for the test
    fake_now = [1000.0]
    def fake_sleep(s):
        pass  # don't actually sleep
    def fake_monotonic():
        return fake_now[0]

    client = RetryClient(
        failure_threshold=2,
        max_retries=0,
        reset_timeout=5.0,
        half_open_success_threshold=1,
        sleep=fake_sleep,
    )
    # Override _check_breaker to use fake clock
    import api.core.retry_client as rc
    orig_monotonic = rc.time.monotonic
    rc.time.monotonic = fake_monotonic

    try:
        func_fail = MagicMock(side_effect=ProviderError("x", retriable=True))
        for _ in range(2):
            with pytest.raises(ProviderError):
                client.call(func_fail, key="trip")
        assert client.get_breaker_state("trip")["state"] == STATE_OPEN

        # Advance time past reset_timeout
        fake_now[0] += 6.0
        # Next call should be allowed as half-open probe
        func_ok = MagicMock(return_value="ok")
        result = client.call(func_ok, key="trip")
        assert result == "ok"
        assert client.get_breaker_state("trip")["state"] == STATE_CLOSED
    finally:
        rc.time.monotonic = orig_monotonic


def test_circuit_breaker_reopens_on_failed_probe():
    """If the half-open probe fails, breaker should reopen immediately."""
    import time as _t
    fake_now = [1000.0]
    def fake_sleep(s):
        pass
    def fake_monotonic():
        return fake_now[0]

    client = RetryClient(
        failure_threshold=2,
        max_retries=0,
        reset_timeout=5.0,
        sleep=fake_sleep,
    )
    import api.core.retry_client as rc
    orig_monotonic = rc.time.monotonic
    rc.time.monotonic = fake_monotonic

    try:
        func_fail = MagicMock(side_effect=ProviderError("x", retriable=True))
        for _ in range(2):
            with pytest.raises(ProviderError):
                client.call(func_fail, key="trip2")
        assert client.get_breaker_state("trip2")["state"] == STATE_OPEN

        fake_now[0] += 6.0
        # Probe call also fails
        with pytest.raises(ProviderError):
            client.call(func_fail, key="trip2")
        # Should be back to OPEN
        assert client.get_breaker_state("trip2")["state"] == STATE_OPEN
    finally:
        rc.time.monotonic = orig_monotonic


def test_reset_breaker_admin_override():
    client = RetryClient(failure_threshold=1, max_retries=0)
    func = MagicMock(side_effect=ProviderError("x", retriable=True))
    with pytest.raises(ProviderError):
        client.call(func, key="admin")
    assert client.get_breaker_state("admin")["state"] == STATE_OPEN

    client.reset_breaker("admin")
    assert client.get_breaker_state("admin")["state"] == STATE_CLOSED


def test_success_resets_failure_count():
    sleeps = []
    client = RetryClient(failure_threshold=3, max_retries=0, sleep=sleeps.append)
    fail = MagicMock(side_effect=ProviderError("x", retriable=True))
    succeed = MagicMock(return_value="ok")
    # 1 failure
    with pytest.raises(ProviderError):
        client.call(fail, key="counter")
    assert client.get_breaker_state("counter")["failure_count"] == 1
    # 1 success — resets counter
    assert client.call(succeed, key="counter") == "ok"
    assert client.get_breaker_state("counter")["failure_count"] == 0
    # 2 more failures — would trip at 3, but we reset
    for _ in range(2):
        with pytest.raises(ProviderError):
            client.call(fail, key="counter")
    assert client.get_breaker_state("counter")["state"] == STATE_CLOSED
    assert client.get_breaker_state("counter")["failure_count"] == 2