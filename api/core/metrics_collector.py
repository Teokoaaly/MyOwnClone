"""MetricsCollector: real-time model metrics with Redis sliding windows.

Tracks per-model latency, success rate, and quality score.
Uses Redis sorted sets with timestamps as scores for sliding-window queries.

Key naming:
- metrics:{model_id}:latencies (sorted set, score=timestamp, value=latency_ms)
- metrics:{model_id}:successes (sorted set, score=timestamp, value=1)
- metrics:{model_id}:failures (sorted set, score=timestamp, value=1)
- metrics:{model_id}:quality (sorted set, score=timestamp, value=score)

TTL: 5 minutes per entry (auto-expire via Redis EXPIRE on the sorted set).
"""
from __future__ import annotations
import time
import os
from typing import Optional, Protocol
from dataclasses import dataclass


# Default TTL for sliding window entries (5 minutes)
DEFAULT_TTL_SECONDS = 300
DEFAULT_WINDOW_SECONDS = 300  # 5 min for default aggregations


class _RedisLike(Protocol):
    """Minimal Redis interface we depend on (sorted sets + expire)."""
    def zadd(self, name: str, mapping: dict) -> int: ...
    def zremrangebyscore(self, name: str, min: float, max: float) -> int: ...
    def zcard(self, name: str) -> int: ...
    def zrange(self, name: str, start: int, end: int, withscores: bool = False) -> list: ...
    def expire(self, name: str, seconds: int) -> bool: ...
    def delete(self, *names: str) -> int: ...


class InMemoryRedis:
    """In-memory drop-in replacement for Redis (for tests + offline dev).
    
    Implements only the methods MetricsCollector needs.
    """
    def __init__(self):
        self._data: dict[str, list[tuple[float, float]]] = {}
    
    def zadd(self, name: str, mapping: dict) -> int:
        if name not in self._data:
            self._data[name] = []
        # mapping is {member: score} per Redis ZADD semantics
        for member, score in mapping.items():
            self._data[name].append((float(score), member))
        # Sort by score (timestamp)
        self._data[name].sort()
        return len(mapping)
    
    def zremrangebyscore(self, name: str, min: str, max: str) -> int:
        """Remove elements with scores between min and max (inclusive).
        
        Supports Redis-style exclusive bounds: "(score" means exclusive.
        Supports -inf and +inf for unbounded ranges.
        """
        if name not in self._data:
            return 0
        before = len(self._data[name])
        
        def parse_bound(bound) -> tuple[float, bool]:
            """Parse a bound, returning (value, inclusive)."""
            if isinstance(bound, (int, float)):
                return (float(bound), True)
            if bound == "-inf":
                return (float("-inf"), True)
            if bound == "+inf":
                return (float("inf"), True)
            if bound.startswith("("):
                return (float(bound[1:]), False)
            return (float(bound), True)
        
        min_val, min_inclusive = parse_bound(min)
        max_val, max_inclusive = parse_bound(max)
        
        def should_remove(s: float) -> bool:
            # Check min bound
            if min_val == float("-inf"):
                min_ok = True
            elif min_inclusive:
                min_ok = min_val <= s
            else:
                min_ok = min_val < s
            
            # Check max bound
            if max_val == float("inf"):
                max_ok = True
            elif max_inclusive:
                max_ok = s <= max_val
            else:
                max_ok = s < max_val
            
            return min_ok and max_ok
        
        self._data[name] = [(s, v) for s, v in self._data[name] if not should_remove(s)]
        return before - len(self._data[name])
    
    def zcard(self, name: str) -> int:
        return len(self._data.get(name, []))
    
    def zrange(self, name: str, start: int, end: int, withscores: bool = False) -> list:
        if name not in self._data:
            return []
        data = self._data[name]
        # end=-1 means "to the end" in Redis
        if end == -1:
            end = len(data)
        else:
            end = end + 1  # Redis is inclusive
        sliced = data[start:end]
        if withscores:
            return [(v, s) for s, v in sliced]
        return [v for s, v in sliced]
    
    def expire(self, name: str, seconds: int) -> bool:
        # No-op for in-memory (we don't track TTL)
        return True
    
    def delete(self, *names: str) -> int:
        count = 0
        for n in names:
            if n in self._data:
                del self._data[n]
                count += 1
        return count


def _get_default_redis() -> _RedisLike:
    """Get the default Redis client (or InMemoryRedis if not available)."""
    try:
        from api.extensions.ext_redis import redis_client
        if redis_client is not None:
            return redis_client
    except Exception:
        pass
    return InMemoryRedis()


@dataclass
class ModelMetrics:
    """Snapshot of metrics for a single model over the sliding window."""
    model_id: str
    p50_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    success_rate: float  # 0.0 - 1.0
    sample_count: int
    avg_quality: Optional[float] = None


def _percentile(sorted_values: list[float], p: float) -> float:
    """Compute the p-th percentile (0.0-1.0) from a sorted list."""
    if not sorted_values:
        return 0.0
    if len(sorted_values) == 1:
        return sorted_values[0]
    k = (len(sorted_values) - 1) * p
    f = int(k)
    c = f + 1 if f + 1 < len(sorted_values) else f
    return sorted_values[f] + (k - f) * (sorted_values[c] - sorted_values[f])


class MetricsCollector:
    """Records and queries model metrics via Redis sliding windows."""
    
    def __init__(
        self,
        redis_client: Optional[_RedisLike] = None,
        window_seconds: int = DEFAULT_WINDOW_SECONDS,
        ttl_seconds: int = DEFAULT_TTL_SECONDS,
        clock=time.time,
    ):
        self._redis = redis_client or _get_default_redis()
        self.window_seconds = window_seconds
        self.ttl_seconds = ttl_seconds
        self._clock = clock  # injectable for tests
    
    def _key(self, model_id: str, metric: str) -> str:
        return f"metrics:{model_id}:{metric}"
    
    def _now(self) -> float:
        return self._clock()
    
    def _cutoff(self) -> float:
        return self._now() - self.window_seconds
    
    def _trim(self, model_id: str, metric: str) -> None:
        """Remove entries older than the window."""
        key = self._key(model_id, metric)
        cutoff = self._cutoff()
        self._redis.zremrangebyscore(key, "-inf", f"({cutoff}")  # exclusive of cutoff
        # Refresh TTL
        self._redis.expire(key, self.ttl_seconds)
    
    def record_latency(self, model_id: str, latency_ms: int) -> None:
        self._trim(model_id, "latencies")
        self._redis.zadd(
            self._key(model_id, "latencies"),
            {f"{self._now()}:{latency_ms}": self._now()},
        )
    
    def record_success(self, model_id: str) -> None:
        self._trim(model_id, "successes")
        self._redis.zadd(
            self._key(model_id, "successes"),
            {f"{self._now()}:1": self._now()},
        )
    
    def record_failure(self, model_id: str) -> None:
        self._trim(model_id, "failures")
        self._redis.zadd(
            self._key(model_id, "failures"),
            {f"{self._now()}:1": self._now()},
        )
    
    def record_quality(self, model_id: str, score: float) -> None:
        """Record a quality score (0.0-1.0) from user feedback."""
        self._trim(model_id, "quality")
        self._redis.zadd(
            self._key(model_id, "quality"),
            {f"{self._now()}:{score}": self._now()},
        )
    
    def get_p95_latency_ms(self, model_id: str) -> float:
        self._trim(model_id, "latencies")
        values = self._read_metric_values(model_id, "latencies")
        return _percentile(values, 0.95)
    
    def get_p50_latency_ms(self, model_id: str) -> float:
        self._trim(model_id, "latencies")
        values = self._read_metric_values(model_id, "latencies")
        return _percentile(values, 0.50)
    
    def get_p99_latency_ms(self, model_id: str) -> float:
        self._trim(model_id, "latencies")
        values = self._read_metric_values(model_id, "latencies")
        return _percentile(values, 0.99)
    
    def get_success_rate(self, model_id: str) -> float:
        """Return success rate (0.0-1.0) over the sliding window."""
        self._trim(model_id, "successes")
        self._trim(model_id, "failures")
        succ = self._redis.zcard(self._key(model_id, "successes"))
        fail = self._redis.zcard(self._key(model_id, "failures"))
        total = succ + fail
        if total == 0:
            return 1.0  # no data = assume healthy
        return succ / total
    
    def get_avg_quality(self, model_id: str) -> Optional[float]:
        self._trim(model_id, "quality")
        values = self._read_metric_values(model_id, "quality")
        if not values:
            return None
        return sum(values) / len(values)
    
    def get_metrics(self, model_id: str) -> ModelMetrics:
        """Get a full snapshot of metrics for a model."""
        return ModelMetrics(
            model_id=model_id,
            p50_latency_ms=self.get_p50_latency_ms(model_id),
            p95_latency_ms=self.get_p95_latency_ms(model_id),
            p99_latency_ms=self.get_p99_latency_ms(model_id),
            success_rate=self.get_success_rate(model_id),
            sample_count=self._redis.zcard(self._key(model_id, "latencies")),
            avg_quality=self.get_avg_quality(model_id),
        )
    
    def _read_metric_values(self, model_id: str, metric: str) -> list[float]:
        """Read all values from a metric sorted set (skip the timestamp prefix)."""
        key = self._key(model_id, metric)
        # Members are strings like "{timestamp}:{value}"
        members = self._redis.zrange(key, 0, -1)
        values = []
        for m in members:
            if isinstance(m, bytes):
                m = m.decode("utf-8")
            try:
                # Split on the FIRST colon (timestamp may have colons)
                if ":" in m:
                    parts = m.split(":", 1)
                    values.append(float(parts[1]))
                else:
                    values.append(float(m))
            except (ValueError, IndexError):
                continue
        return sorted(values)


# Module-level singleton
_collector: Optional[MetricsCollector] = None


def get_metrics_collector() -> MetricsCollector:
    """Get the process-wide MetricsCollector singleton."""
    global _collector
    if _collector is None:
        _collector = MetricsCollector()
    return _collector


def reset_metrics_collector() -> None:
    """Reset the singleton (for tests)."""
    global _collector
    _collector = None