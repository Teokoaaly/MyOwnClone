from __future__ import annotations

import pytest

from api.core.providers import ModelInvocationError
from api.core.retry_client import RetryCandidate, RetryClient


def test_retry_client_retries_with_exponential_backoff():
    sleeps: list[float] = []
    attempts = {"count": 0}

    def flaky():
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise RuntimeError("temporary")
        return "ok"

    client = RetryClient(
        max_attempts_per_candidate=3,
        base_backoff_seconds=0.5,
        sleep_fn=sleeps.append,
    )

    result = client.invoke(
        [RetryCandidate(provider_name="openai", model_id="gpt", priority=10, invoke=flaky)]
    )

    assert result == "ok"
    assert sleeps == [0.5, 1.0]


def test_retry_client_failover_respects_priority_order():
    calls: list[str] = []

    def first():
        calls.append("first")
        raise RuntimeError("boom")

    def second():
        calls.append("second")
        return "recovered"

    client = RetryClient(max_attempts_per_candidate=1)
    result = client.invoke(
        [
            RetryCandidate(provider_name="b", model_id="slow", priority=20, invoke=second),
            RetryCandidate(provider_name="a", model_id="fast", priority=10, invoke=first),
        ]
    )

    assert result == "recovered"
    assert calls == ["first", "second"]


def test_retry_client_opens_circuit_after_repeated_failures():
    now = [100.0]
    client = RetryClient(
        max_attempts_per_candidate=1,
        circuit_open_after_failures=2,
        time_fn=lambda: now[0],
    )

    def always_fail():
        raise RuntimeError("down")

    candidate = RetryCandidate(provider_name="openai", model_id="gpt", priority=10, invoke=always_fail)

    with pytest.raises(ModelInvocationError):
        client.invoke([candidate])
    with pytest.raises(ModelInvocationError):
        client.invoke([candidate])

    circuit = client._circuits[("openai", "gpt")]
    assert circuit.state == "open"


def test_retry_client_half_open_recovers_after_timeout():
    now = [100.0]
    state = {"should_fail": True}
    client = RetryClient(
        max_attempts_per_candidate=1,
        circuit_open_after_failures=1,
        half_open_after_seconds=30.0,
        time_fn=lambda: now[0],
    )

    def sometimes():
        if state["should_fail"]:
            raise RuntimeError("down")
        return "ok"

    candidate = RetryCandidate(provider_name="openai", model_id="gpt", priority=10, invoke=sometimes)

    with pytest.raises(ModelInvocationError):
        client.invoke([candidate])

    now[0] = 131.0
    state["should_fail"] = False

    result = client.invoke([candidate])

    assert result == "ok"
    circuit = client._circuits[("openai", "gpt")]
    assert circuit.state == "closed"
    assert circuit.consecutive_failures == 0


def test_retry_client_raises_after_all_candidates_fail():
    client = RetryClient(max_attempts_per_candidate=1)

    def fail_one():
        raise RuntimeError("first boom")

    def fail_two():
        raise RuntimeError("second boom")

    with pytest.raises(ModelInvocationError, match="All retry candidates failed"):
        client.invoke(
            [
                RetryCandidate(provider_name="a", model_id="m1", priority=10, invoke=fail_one),
                RetryCandidate(provider_name="b", model_id="m2", priority=20, invoke=fail_two),
            ]
        )


def test_retry_client_skips_still_open_circuit():
    now = [100.0]
    calls: list[str] = []
    client = RetryClient(
        max_attempts_per_candidate=1,
        circuit_open_after_failures=1,
        half_open_after_seconds=30.0,
        time_fn=lambda: now[0],
    )

    def fail():
        calls.append("fail")
        raise RuntimeError("down")

    def succeed():
        calls.append("success")
        return "ok"

    first = RetryCandidate(provider_name="a", model_id="m1", priority=10, invoke=fail)
    second = RetryCandidate(provider_name="b", model_id="m2", priority=20, invoke=succeed)

    result = client.invoke([first, second])

    assert result == "ok"
    assert calls == ["fail", "success"]
