"""Retry, failover, and circuit-breaker logic for provider invocation."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable, Iterable

from api.core.providers import ModelInvocationError


@dataclass(slots=True)
class RetryCandidate:
    provider_name: str
    model_id: str
    priority: int
    invoke: Callable[[], Any]


@dataclass(slots=True)
class CircuitStatus:
    state: str = "closed"
    consecutive_failures: int = 0
    opened_at: float | None = None


class RetryClient:
    """Execute provider calls with bounded retries, failover, and breaker state."""

    def __init__(
        self,
        *,
        max_attempts_per_candidate: int = 3,
        base_backoff_seconds: float = 0.25,
        circuit_open_after_failures: int = 3,
        half_open_after_seconds: float = 30.0,
        sleep_fn: Callable[[float], None] | None = None,
        time_fn: Callable[[], float] | None = None,
    ) -> None:
        self.max_attempts_per_candidate = max_attempts_per_candidate
        self.base_backoff_seconds = base_backoff_seconds
        self.circuit_open_after_failures = circuit_open_after_failures
        self.half_open_after_seconds = half_open_after_seconds
        self._sleep_fn = sleep_fn or time.sleep
        self._time_fn = time_fn or time.monotonic
        self._circuits: dict[tuple[str, str], CircuitStatus] = {}

    def invoke(self, candidates: Iterable[RetryCandidate]) -> Any:
        ordered = sorted(candidates, key=lambda candidate: candidate.priority)
        if not ordered:
            raise ModelInvocationError("RetryClient requires at least one candidate.")

        last_error: Exception | None = None
        attempted_any = False

        for candidate in ordered:
            circuit = self._circuit_for(candidate)
            if self._is_open(circuit):
                if self._ready_for_half_open(circuit):
                    circuit.state = "half_open"
              ***REMOVED***:
                    continue

            attempted_any = True
            for attempt in range(1, self.max_attempts_per_candidate + 1):
                try:
                    result = candidate.invoke()
                except Exception as exc:
                    last_error = exc
                    self._record_failure(circuit)
                    if circuit.state == "open":
                        break
                    if attempt < self.max_attempts_per_candidate:
                        self._sleep_fn(self._backoff_for(attempt))
                    continue

                self._record_success(circuit)
                return result

        if not attempted_any:
            raise ModelInvocationError("All candidate circuits are open; no invocation attempted.")

        message = "All retry candidates failed."
        if last_error is not None:
            raise ModelInvocationError(f"{message} Last error: {last_error}") from last_error
        raise ModelInvocationError(message)

    def _circuit_for(self, candidate: RetryCandidate) -> CircuitStatus:
        key = (candidate.provider_name, candidate.model_id)
        if key not in self._circuits:
            self._circuits[key] = CircuitStatus()
        return self._circuits[key]

    def _is_open(self, circuit: CircuitStatus) -> bool:
        return circuit.state == "open"

    def _ready_for_half_open(self, circuit: CircuitStatus) -> bool:
        return (
            circuit.opened_at is not None
            and (self._time_fn() - circuit.opened_at) >= self.half_open_after_seconds
        )

    def _record_failure(self, circuit: CircuitStatus) -> None:
        circuit.consecutive_failures += 1
        if circuit.state == "half_open" or circuit.consecutive_failures >= self.circuit_open_after_failures:
            circuit.state = "open"
            circuit.opened_at = self._time_fn()

    def _record_success(self, circuit: CircuitStatus) -> None:
        circuit.state = "closed"
        circuit.consecutive_failures = 0
        circuit.opened_at = None

    def _backoff_for(self, attempt: int) -> float:
        return self.base_backoff_seconds * (2 ** (attempt - 1))
