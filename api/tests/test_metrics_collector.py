"""Tests for MetricsCollector using in-memory Redis."""
from __future__ import annotations
import time
import pytest

from api.core.metrics_collector import (
    MetricsCollector, InMemoryRedis, ModelMetrics, get_metrics_collector, reset_metrics_collector,
)


@pytest.fixture
def clock():
    """Controllable clock for deterministic tests."""
    fake_now = [1000.0]
    def now():
        return fake_now[0]
    def advance(seconds):
        fake_now[0] += seconds
    return now, advance


@pytest.fixture
def collector(clock):
    now, _ = clock
    redis = InMemoryRedis()
    return MetricsCollector(redis_client=redis, window_seconds=60, clock=now), redis


# ---------- InMemoryRedis basics ----------

def test_in_memory_redis_zadd_zcard():
    r = InMemoryRedis()
    r.zadd("k1", {"a": 100.0})
    r.zadd("k1", {"b": 200.0})
    assert r.zcard("k1") == 2


def test_in_memory_redis_zremrangebyscore():
    r = InMemoryRedis()
    r.zadd("k1", {"a": 50.0})
    r.zadd("k1", {"b": 150.0})
    r.zadd("k1", {"c": 250.0})
    removed = r.zremrangebyscore("k1", 0, 100)
    assert removed == 1
    assert r.zcard("k1") == 2


def test_in_memory_redis_zrange_with_scores():
    r = InMemoryRedis()
    r.zadd("k1", {"a": 10.0})
    r.zadd("k1", {"b": 20.0})
    r.zadd("k1", {"c": 30.0})
    with_scores = r.zrange("k1", 0, -1, withscores=True)
    assert with_scores == [("a", 10.0), ("b", 20.0), ("c", 30.0)]


# ---------- record methods ----------

def test_record_latency_stores_value(collector):
    c, _ = collector
    c.record_latency("m1", 100)
    assert c.get_p50_latency_ms("m1") == 100


def test_record_latency_with_multiple_samples(collector):
    c, _ = collector
    for lat in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        c.record_latency("m1", lat)
    assert c.get_p50_latency_ms("m1") == 55
    assert c.get_p95_latency_ms("m1") == 95.5
    assert c.get_p99_latency_ms("m1") == 99.1


def test_record_success_and_failure_track_separately(collector):
    c, _ = collector
    c.record_success("m1")
    c.record_success("m1")
    c.record_failure("m1")
    assert c.get_success_rate("m1") == pytest.approx(2/3)


def test_success_rate_with_no_data_returns_one(collector):
    c, _ = collector
    assert c.get_success_rate("unknown") == 1.0


def test_record_quality_and_avg(collector):
    c, _ = collector
    c.record_quality("m1", 0.8)
    c.record_quality("m1", 0.6)
    c.record_quality("m1", 1.0)
    assert c.get_avg_quality("m1") == pytest.approx(0.8)


def test_avg_quality_returns_none_when_no_data(collector):
    c, _ = collector
    assert c.get_avg_quality("unknown") is None


# ---------- Sliding window behavior ----------

def test_sliding_window_evicts_old_entries(collector, clock):
    c, _ = collector
    now, advance = clock
    # Record 3 latencies at t=0
    c.record_latency("m1", 100)
    c.record_latency("m1", 200)
    c.record_latency("m1", 300)
    # Advance past window (60s)
    advance(61)
    # New latency at t=61
    c.record_latency("m1", 50)
    # Old ones should be evicted on next read
    p50 = c.get_p50_latency_ms("m1")
    assert p50 == 50  # only the new one remains


def test_sliding_window_does_not_evict_recent(collector, clock):
    c, _ = collector
    now, advance = clock
    c.record_latency("m1", 100)
    advance(30)  # half the window
    c.record_latency("m1", 200)
    # Both should still be there
    p50 = c.get_p50_latency_ms("m1")
    assert p50 == 150  # average of two


# ---------- get_metrics snapshot ----------

def test_get_metrics_returns_full_snapshot(collector):
    c, _ = collector
    for lat in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        c.record_latency("m1", lat)
    c.record_success("m1")
    c.record_success("m1")
    c.record_failure("m1")
    c.record_quality("m1", 0.8)
    
    metrics = c.get_metrics("m1")
    assert isinstance(metrics, ModelMetrics)
    assert metrics.model_id == "m1"
    assert metrics.p50_latency_ms == 55
    assert metrics.sample_count == 10
    assert metrics.success_rate == pytest.approx(2/3)
    assert metrics.avg_quality == 0.8


# ---------- Singleton ----------

def test_singleton_returns_same_instance():
    reset_metrics_collector()
    c1 = get_metrics_collector()
    c2 = get_metrics_collector()
    assert c1 is c2
    reset_metrics_collector()