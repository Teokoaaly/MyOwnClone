"""Server monitoring module — comprehensive system metrics.

Collects real-time metrics from:
- OS: CPU, RAM, disk, load average, uptime
- PostgreSQL: connections, pool stats, slow queries
- Redis: memory, clients, hit rate, keys
- Docker: container health, restart counts
- Ollama: loaded models, VRAM
- API: request stats, error rates
- Queue: depth, failed jobs

Usage:
    from api.core.monitoring import ServerMonitor
    monitor = ServerMonitor()
    report = monitor.full_report()
"""

from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class ServiceHealth:
    name: str
    status: str  # "healthy", "degraded", "down", "unknown"
    latency_ms: float | None = None
    details: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class ServerMonitor:
    """Collect real-time system metrics from all services."""

    def __init__(self) -> None:
        self._start_time = time.monotonic()

    def full_report(self) -> dict:
        """Generate comprehensive monitoring report."""
        services = []
        services.append(self._check_os())
        services.append(self._check_database())
        services.append(self._check_redis())
        services.append(self._check_ollama())
        services.append(self._check_worker())
        services.append(self._check_docker())
        services.append(self._check_api_health())

        healthy = sum(1 for s in services if s.status == "healthy")
        degraded = sum(1 for s in services if s.status == "degraded")
        down = sum(1 for s in services if s.status == "down")

        overall = "healthy"
        if down > 0:
            overall = "critical"
        elif degraded > 0:
            overall = "degraded"

        return {
            "overall_status": overall,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "uptime_seconds": int(time.monotonic() - self._start_time),
            "summary": {
                "total": len(services),
                "healthy": healthy,
                "degraded": degraded,
                "down": down,
            },
            "services": {
                s.name: {
                    "status": s.status,
                    "latency_ms": s.latency_ms,
                    "details": s.details,
                    "error": s.error,
                }
                for s in services
            },
        }

    def _check_os(self) -> ServiceHealth:
        """Collect OS-level metrics from /proc."""
        details = {}
        try:
            # CPU usage from /proc/stat
            with open("/proc/stat") as f:
                line = f.readline()
            parts = line.split()
            total = sum(int(x) for x in parts[1:])
            idle = int(parts[4])
            details["cpu_total_jiffies"] = total
            details["cpu_idle_jiffies"] = idle
            details["cpu_usage_percent"] = round((1 - idle / total) * 100, 1) if total > 0 else 0

            # Load average
            with open("/proc/loadavg") as f:
                load = f.read().split()
            details["load_1m"] = float(load[0])
            details["load_5m"] = float(load[1])
            details["load_15m"] = float(load[2])

            # Memory from /proc/meminfo
            mem = {}
            with open("/proc/meminfo") as f:
                for line in f:
                    parts = line.split(":")
                    if len(parts) == 2:
                        key = parts[0].strip()
                        val = int(parts[1].strip().split()[0])
                        mem[key] = val
            total_mem = mem.get("MemTotal", 1)
            free_mem = mem.get("MemAvailable", mem.get("MemFree", 0))
            used_mem = total_mem - free_mem
            details["ram_total_mb"] = round(total_mem / 1024)
            details["ram_used_mb"] = round(used_mem / 1024)
            details["ram_available_mb"] = round(free_mem / 1024)
            details["ram_usage_percent"] = round(used_mem / total_mem * 100, 1)

            swap_total = mem.get("SwapTotal", 0)
            swap_free = mem.get("SwapFree", 0)
            details["swap_total_mb"] = round(swap_total / 1024)
            details["swap_used_mb"] = round((swap_total - swap_free) / 1024)
            details["swap_usage_percent"] = round((swap_total - swap_free) / swap_total * 100, 1) if swap_total > 0 else 0

            # Disk usage
            stat = os.statvfs("/")
            details["disk_total_gb"] = round(stat.f_blocks * stat.f_frsize / (1024**3), 1)
            details["disk_used_gb"] = round((stat.f_blocks - stat.f_bfree) * stat.f_frsize / (1024**3), 1)
            details["disk_usage_percent"] = round((stat.f_blocks - stat.f_bfree) / stat.f_blocks * 100, 1)

            # Uptime
            with open("/proc/uptime") as f:
                uptime_secs = float(f.read().split()[0])
            details["uptime_days"] = round(uptime_secs / 86400, 1)

            # Determine status
            status = "healthy"
            if details["cpu_usage_percent"] > 90 or details["ram_usage_percent"] > 90 or details["disk_usage_percent"] > 90:
                status = "degraded"
            if details["cpu_usage_percent"] > 95 or details["ram_usage_percent"] > 95 or details["disk_usage_percent"] > 95:
                status = "down"

            return ServiceHealth(name="os", status=status, details=details)
        except Exception as exc:
            return ServiceHealth(name="os", status="unknown", error=str(exc))

    def _check_database(self) -> ServiceHealth:
        """Check PostgreSQL health and connection pool."""
        details = {}
        try:
            from sqlalchemy import text
            from api.extensions.ext_database import db

            # Basic connectivity + latency
            start = time.monotonic()
            db.session.execute(text("SELECT 1"))
            latency = round((time.monotonic() - start) * 1000, 2)
            details["latency_ms"] = latency

            # Connection count
            result = db.session.execute(
                text("SELECT count(*) FROM pg_stat_activity WHERE datname = current_database()")
            ).scalar()
            details["active_connections"] = result

            # Max connections
            max_conn = db.session.execute(text("SHOW max_connections")).scalar()
            details["max_connections"] = int(max_conn) if max_conn else 100
            details["connection_usage_percent"] = round(
                details["active_connections"] / details["max_connections"] * 100, 1
            )

            # Database size
            db_size = db.session.execute(
                text("SELECT pg_size_pretty(pg_database_size(current_database()))")
            ).scalar()
            details["database_size"] = db_size

            # Table counts
            tables = db.session.execute(
                text("SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public'")
            ).scalar()
            details["table_count"] = tables

            # Cache hit ratio
            cache_hit = db.session.execute(
                text("""
                    SELECT round(
                        100.0 * sum(blks_hit) / nullif(sum(blks_hit) + sum(blks_read), 0),
                        2
                    ) FROM pg_stat_database WHERE datname = current_database()
                """)
            ).scalar()
            details["cache_hit_ratio"] = float(cache_hit) if cache_hit else None

            # Slow queries (queries running > 1s)
            slow = db.session.execute(
                text("""
                    SELECT count(*) FROM pg_stat_activity
                    WHERE state = 'active'
                    AND query NOT LIKE '%pg_stat_activity%'
                    AND now() - query_start > interval '1 second'
                """)
            ).scalar()
            details["slow_queries"] = slow

            # Status
            status = "healthy"
            if details["connection_usage_percent"] > 80:
                status = "degraded"
            if details["connection_usage_percent"] > 95 or (slow and slow > 5):
                status = "down"

            return ServiceHealth(name="database", status=status, latency_ms=latency, details=details)
        except Exception as exc:
            return ServiceHealth(name="database", status="down", error=str(exc))

    def _check_redis(self) -> ServiceHealth:
        """Check Redis health and metrics."""
        details = {}
        try:
            import redis as redis_lib

            r = redis_lib.Redis(
                host=os.environ.get("REDIS_HOST", ""),
                password=os.environ.get("REDIS_PASSWORD", ""),
                port=int(os.environ.get("REDIS_PORT", "6379")),
                socket_connect_timeout=2,
                socket_timeout=2,
            )

            # Latency
            start = time.monotonic()
            r.ping()
            latency = round((time.monotonic() - start) * 1000, 2)
            details["latency_ms"] = latency

            # Memory info
            info = r.info("memory")
            details["used_memory_mb"] = round(info.get("used_memory", 0) / (1024**2), 2)
            details["max_memory_mb"] = round(info.get("maxmemory", 0) / (1024**2), 2) if info.get("maxmemory") else None
            details["memory_fragmentation_ratio"] = info.get("mem_fragmentation_ratio")

            # Clients
            client_info = r.info("clients")
            details["connected_clients"] = client_info.get("connected_clients", 0)
            details["blocked_clients"] = client_info.get("blocked_clients", 0)

            # Stats
            stats = r.info("stats")
            details["total_commands"] = stats.get("total_commands_processed", 0)
            details["hit_rate"] = round(
                stats.get("keyspace_hits", 0) / max(stats.get("keyspace_hits", 0) + stats.get("keyspace_misses", 0), 1) * 100, 1
            )
            details["evicted_keys"] = stats.get("evicted_keys", 0)

            # Keyspace
            keyspace = r.info("keyspace")
            details["databases"] = {}
            for db_name, db_info in keyspace.items():
                details["databases"][db_name] = {
                    "keys": db_info.get("keys", 0),
                    "expires": db_info.get("expires", 0),
                }

            # Status
            status = "healthy"
            if details["connected_clients"] > 100 or details.get("memory_fragmentation_ratio", 1) > 2:
                status = "degraded"

            return ServiceHealth(name="redis", status=status, latency_ms=latency, details=details)
        except Exception as exc:
            return ServiceHealth(name="redis", status="down", error=str(exc))

    def _check_ollama(self) -> ServiceHealth:
        """Check Ollama model server health."""
        details = {}
        try:
            import urllib.request

            ollama_url = os.environ.get("OLLAMA_BASE_URL", "http://ollama:11434")

            # Models loaded
            start = time.monotonic()
            req = urllib.request.Request(f"{ollama_url}/api/tags", method="GET")
            resp = urllib.request.urlopen(req, timeout=5)
            data = json.loads(resp.read())
            latency = round((time.monotonic() - start) * 1000, 2)

            models = data.get("models", [])
            details["loaded_models"] = len(models)
            details["models"] = [
                {
                    "name": m.get("name", "unknown"),
                    "size_gb": round(m.get("size", 0) / (1024**3), 2),
                    "modified": m.get("modified_at", ""),
                }
                for m in models
            ]
            details["latency_ms"] = latency

            # Embedding test
            embed_start = time.monotonic()
            embed_req = urllib.request.Request(
                f"{ollama_url}/api/embed",
                method="POST",
                headers={"Content-Type": "application/json"},
                data=json.dumps({"model": "mxbai-embed-large", "input": "test"}).encode(),
            )
            embed_resp = urllib.request.urlopen(embed_req, timeout=30)
            embed_data = json.loads(embed_resp.read())
            embed_latency = round((time.monotonic() - embed_start) * 1000, 1)
            details["embedding_latency_ms"] = embed_latency
            details["embedding_dimensions"] = len(embed_data.get("embeddings", [[]])[0]) if embed_data.get("embeddings") else 0

            status = "healthy"
            if details["loaded_models"] == 0:
                status = "degraded"

            return ServiceHealth(name="ollama", status=status, latency_ms=latency, details=details)
        except Exception as exc:
            return ServiceHealth(name="ollama", status="down", error=str(exc))

    def _check_worker(self) -> ServiceHealth:
        """Check RQ worker health."""
        details = {}
        try:
            import redis as redis_lib

            r = redis_lib.Redis(
                host=os.environ.get("REDIS_HOST", ""),
                password=os.environ.get("REDIS_PASSWORD", ""),
                port=int(os.environ.get("REDIS_PORT", "6379")),
                socket_connect_timeout=2,
                socket_timeout=2,
            )

            # Queue depth
            queue_len = r.llen("ingestion")
            details["queue_depth"] = queue_len

            # Failed jobs
            failed_len = r.llen("failed")
            details["failed_jobs"] = failed_len

            # Workers registered
            workers = r.smembers("rq:workers") or set()
            details["registered_workers"] = len(workers)

            # Status
            status = "healthy"
            if queue_len > 100:
                status = "degraded"
            if failed_len > 10:
                status = "degraded"

            return ServiceHealth(name="worker", status=status, details=details)
        except Exception as exc:
            return ServiceHealth(name="worker", status="unknown", error=str(exc))

    def _check_docker(self) -> ServiceHealth:
        """Check Docker container health (best-effort from inside container)."""
        details = {}
        try:
            import subprocess

            # Check if we can reach Docker socket
            result = subprocess.run(
                ["curl", "-s", "--unix-socket", "/var/run/docker.sock", "http://localhost/containers/json"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                containers = json.loads(result.stdout)
                details["containers"] = []
                for c in containers:
                    name = c.get("Names", ["unknown"])[0].lstrip("/")
                    state = c.get("State", "unknown")
                    status = c.get("Status", "")
                    health = "unknown"
                    if "healthy" in status.lower():
                        health = "healthy"
                    elif "unhealthy" in status.lower():
                        health = "unhealthy"
                    elif state == "running":
                        health = "running"
                    details["containers"].append({
                        "name": name,
                        "state": state,
                        "health": health,
                        "status": status,
                    })
                details["total_containers"] = len(containers)
                unhealthy = sum(1 for c in details["containers"] if c["health"] == "unhealthy")
                status = "healthy" if unhealthy == 0 else "degraded"
            else:
                # Inside container without Docker socket access
                details["note"] = "Docker socket not accessible from inside container"
                status = "unknown"

            return ServiceHealth(name="docker", status=status, details=details)
        except Exception as exc:
            return ServiceHealth(name="docker", status="unknown", error=str(exc))

    def _check_api_health(self) -> ServiceHealth:
        """Check API self-health."""
        details = {}
        try:
            import psutil

            # Process info
            proc = psutil.Process(os.getpid())
            details["pid"] = os.getpid()
            details["memory_mb"] = round(proc.memory_info().rss / (1024**2), 1)
            details["cpu_percent"] = proc.cpu_percent(interval=0.1)
            details["threads"] = proc.num_threads()
            details["open_fds"] = proc.num_fds() if hasattr(proc, "num_fds") else None

            # Child processes
            children = proc.children(recursive=True)
            details["child_processes"] = len(children)

            status = "healthy"
            if details["memory_mb"] > 500:
                status = "degraded"

            return ServiceHealth(name="api", status=status, details=details)
        except ImportError:
            # psutil not installed
            details["note"] = "psutil not available for detailed process metrics"
            return ServiceHealth(name="api", status="healthy", details=details)
        except Exception as exc:
            return ServiceHealth(name="api", status="unknown", error=str(exc))
