"""RetryClient: retries with exponential backoff + circuit breaker per provider.

Use:
    client = RetryClient()
    result = client.call(lambda: adapter.chat(model, messages))

Or with full options:
    result = client.call(
        lambda: adapter.chat(model, messages),
        key="openai/gpt-4o-mini",  # circuit breaker scope
        max_retries=3,
        initial_backoff=1.0,
        max_backoff=10.0,
    )
"""
from __future__ import annotations
import time
import threading
from dataclasses import dataclass, field
from typing import Callable, TypeVar, Optional, Any

from api.core.providers.base import ProviderError


T = TypeVar("T")


# Circuit breaker state machine
STATE_CLOSED = "closed"  # normal — calls allowed
STATE_OPEN = "open"      # tripped — calls rejected immediately
STATE_HALF_OPEN = "half_open"  # testing — one probe call allowed


@dataclass
class _BreakerState:
    state: str = STATE_CLOSED
    failure_count: int = 0
    last_failure_at: float = 0.0
    last_state_change: float = field(default_factory=time.monotonic)
    half_open_probe_in_flight: bool = False


class CircuitBreakerOpenError(Exception):
    """Raised when the circuit breaker is open and rejects a call."""
    def __init__(self, key: str, reset_after: float):
        super().__init__(f"Circuit breaker open for {key!r}, resets in {reset_after:.1f}s")
        self.key = key
        self.reset_after = reset_after


class RetryClient:
    """Retry with exponential backoff + per-key circuit breaker.
    
    Thread-safe.
    """
    
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_INITIAL_BACKOFF = 1.0
    DEFAULT_MAX_BACKOFF = 30.0
    DEFAULT_BACKOFF_MULTIPLIER = 2.0
    DEFAULT_FAILURE_THRESHOLD = 5       # consecutive failures to open
    DEFAULT_RESET_TIMEOUT = 60.0         # seconds before half-open probe
    DEFAULT_HALF_OPEN_SUCCESS_THRESHOLD = 2  # consecutive successes to close
    
    def __init__(
        self,
        *,
        max_retries: int = DEFAULT_MAX_RETRIES,
        initial_backoff: float = DEFAULT_INITIAL_BACKOFF,
        max_backoff: float = DEFAULT_MAX_BACKOFF,
        backoff_multiplier: float = DEFAULT_BACKOFF_MULTIPLIER,
        failure_threshold: int = DEFAULT_FAILURE_THRESHOLD,
        reset_timeout: float = DEFAULT_RESET_TIMEOUT,
        half_open_success_threshold: int = DEFAULT_HALF_OPEN_SUCCESS_THRESHOLD,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff
        self.backoff_multiplier = backoff_multiplier
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.half_open_success_threshold = half_open_success_threshold
        self._sleep = sleep  # injectable for tests
        self._breakers: dict[str, _BreakerState] = {}
        self._lock = threading.RLock()
    
    def _get_breaker(self, key: str) -> _BreakerState:
        with self._lock:
            if key not in self._breakers:
                self._breakers[key] = _BreakerState()
            return self._breakers[key]
    
    def _check_breaker(self, key: str) -> None:
        """Raise CircuitBreakerOpenError if breaker rejects this call."""
        b = self._get_breaker(key)
        with self._lock:
            if b.state == STATE_CLOSED:
                return
            if b.state == STATE_OPEN:
                elapsed = time.monotonic() - b.last_state_change
                if elapsed >= self.reset_timeout:
                    # Transition to half-open, allow one probe
                    b.state = STATE_HALF_OPEN
                    b.half_open_probe_in_flight = True
                    b.last_state_change = time.monotonic()
                    return
                raise CircuitBreakerOpenError(key, self.reset_timeout - elapsed)
            if b.state == STATE_HALF_OPEN:
                if b.half_open_probe_in_flight:
                    raise CircuitBreakerOpenError(key, 0.5)
                # Allow this call as a probe
                b.half_open_probe_in_flight = True
                return
    
    def _record_success(self, key: str) -> None:
        b = self._get_breaker(key)
        with self._lock:
            if b.state == STATE_HALF_OPEN:
                b.half_open_probe_in_flight = False
                b.failure_count = 0
                b.state = STATE_CLOSED
                b.last_state_change = time.monotonic()
            elif b.state == STATE_CLOSED:
                b.failure_count = 0
    
    def _record_failure(self, key: str) -> None:
        b = self._get_breaker(key)
        with self._lock:
            if b.state == STATE_HALF_OPEN:
                b.half_open_probe_in_flight = False
                b.state = STATE_OPEN
                b.last_state_change = time.monotonic()
                return
            b.failure_count += 1
            b.last_failure_at = time.monotonic()
            if b.failure_count >= self.failure_threshold:
                b.state = STATE_OPEN
                b.last_state_change = time.monotonic()
    
    def call(
        self,
        func: Callable[[], T],
        *,
        key: str = "default",
        max_retries: Optional[int] = None,
    ) -> T:
        """Call `func()` with retries and circuit breaking.
        
        Only retries on `ProviderError(retriable=True)`. Non-retriable errors
        raise immediately. Circuit breaker is per `key`.
        """
        max_retries = max_retries if max_retries is not None else self.max_retries
        backoff = self.initial_backoff
        last_error: Optional[Exception] = None
        
        for attempt in range(max_retries + 1):
            self._check_breaker(key)
            try:
                result = func()
            except ProviderError as exc:
                last_error = exc
                if not exc.retriable:
                    self._record_failure(key)
                    raise
                if attempt < max_retries:
                    self._sleep(backoff)
                    backoff = min(backoff * self.backoff_multiplier, self.max_backoff)
                    continue
                # Out of retries
                self._record_failure(key)
                raise
            except Exception:
                # Non-provider error (e.g. network) — record and re-raise without retry
                self._record_failure(key)
                raise
          ***REMOVED***:
                self._record_success(key)
                return result
        
        # Should be unreachable
        if last_error is not None:
            raise last_error
        raise RuntimeError("RetryClient.call exited without return or raise")
    
    # --- Inspection helpers (for tests + admin UI) ---
    
    def get_breaker_state(self, key: str) -> dict:
        """Get the current state of a circuit breaker for inspection."""
        b = self._get_breaker(key)
        with self._lock:
            elapsed_since_change = time.monotonic() - b.last_state_change
            reset_in = max(0.0, self.reset_timeout - elapsed_since_change) if b.state == STATE_OPEN else 0.0
            return {
                "key": key,
                "state": b.state,
                "failure_count": b.failure_count,
                "reset_in_seconds": reset_in,
            }
    
    def reset_breaker(self, key: str) -> None:
        """Force-reset a circuit breaker to closed (admin override)."""
        with self._lock:
            self._breakers[key] = _BreakerState()


# Module-level singleton
_client: Optional[RetryClient] = None


def get_retry_client() -> RetryClient:
    """Get the process-wide RetryClient singleton."""
    global _client
    if _client is None:
        _client = RetryClient()
    return _client


def reset_retry_client() -> None:
    """Reset the singleton (for tests)."""
    global _client
    _client = None