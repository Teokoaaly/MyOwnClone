"""Regression tests for P2 (H-02): rate-limit memory leak + XFF spoofing.

Covers:
- ``_client_ip`` falls back to ``remote_addr`` when no TRUSTED_PROXIES is set
  (so a client setting X-Forwarded-For does NOT get bucketed differently).
- ``_client_ip`` honors X-Forwarded-For ONLY when the immediate peer is in
  TRUSTED_PROXIES.
- ``_prune_memory_fallback`` removes IPs whose entire window has expired,
  bounding the memory footprint of ``_memory_fallback``.
"""
from __future__ import annotations

from unittest.mock import patch

import pytest


def test_client_ip_falls_back_to_remote_when_no_trusted_proxies():
    from api.controllers.console import auth as auth_mod
    with patch.object(auth_mod, "_TRUSTED_PROXIES", []):
        # Even with X-Forwarded-For set by client, we use remote_addr.
        req = type("R", (), {"remote_addr": "10.0.0.1", "headers": {"X-Forwarded-For": "1.2.3.4"}})()
        assert auth_mod._client_ip(req) == "10.0.0.1"


def test_client_ip_honors_xff_only_when_peer_is_trusted():
    from api.controllers.console import auth as auth_mod
    import ipaddress
    trusted = [ipaddress.ip_network("10.0.0.0/8")]
    # Peer in trusted range + XFF present -> use XFF first hop.
    with patch.object(auth_mod, "_TRUSTED_PROXIES", trusted):
        req = type("R", (), {"remote_addr": "10.0.0.5", "headers": {"X-Forwarded-For": "1.2.3.4, 10.0.0.5"}})()
        assert auth_mod._client_ip(req) == "1.2.3.4"
    # Peer NOT in trusted range + XFF present -> ignore XFF, use remote.
    with patch.object(auth_mod, "_TRUSTED_PROXIES", trusted):
        req = type("R", (), {"remote_addr": "8.8.8.8", "headers": {"X-Forwarded-For": "1.2.3.4"}})()
        assert auth_mod._client_ip(req) == "8.8.8.8"


def test_prune_memory_fallback_evicts_stale_ips():
    from api.controllers.console import auth as auth_mod

    # Reset module state for the test.
    auth_mod._memory_fallback.clear()
    auth_mod._last_memory_prune = 0.0

    now = 1_000_000.0
    # Add a stale IP (all timestamps outside the window) and a fresh one.
    auth_mod._memory_fallback["stale-ip"] = [now - 9999.0]
    auth_mod._memory_fallback["fresh-ip"] = [now - 10.0]

    # Force the prune to run by backdating the last-prune stamp.
    auth_mod._prune_memory_fallback(now)

    assert "stale-ip" not in auth_mod._memory_fallback, (
        "H-02: stale IPs must be evicted to prevent memory leak under IP spray"
    )
    assert "fresh-ip" in auth_mod._memory_fallback


def test_prune_is_throttled(monkeypatch):
    """The prune runs at most every 60s to avoid overhead per request."""
    from api.controllers.console import auth as auth_mod
    auth_mod._memory_fallback.clear()
    auth_mod._last_memory_prune = 0.0
    auth_mod._memory_fallback["stale"] = [0.0]
    # First call: should prune (now=1000 > 60 since last=0).
    auth_mod._prune_memory_fallback(1000.0)
    assert "stale" not in auth_mod._memory_fallback
    # Re-add and call again before the 60s window.
    auth_mod._memory_fallback["stale2"] = [1000.0 - 9999.0]
    auth_mod._prune_memory_fallback(1010.0)  # 10s after the previous prune
    # Still present because prune was throttled.
    assert "stale2" in auth_mod._memory_fallback
    # Now past the throttle window.
    auth_mod._prune_memory_fallback(1200.0)
    assert "stale2" not in auth_mod._memory_fallback
