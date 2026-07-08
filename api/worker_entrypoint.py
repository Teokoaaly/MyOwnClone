"""Worker entrypoint for RQ.

T3.5: Usa nuestro helper _get_redis_client() que configura mTLS correctamente.
"""
import os
import sys

# Configure path
sys.path.insert(0, "/app")

from rq import Worker, Queue
from api.core.queue import _get_redis_client

if __name__ == "__main__":
    queue_name = sys.argv[1] if len(sys.argv) > 1 else "ingestion"
    REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379")

    conn = _get_redis_client()
    print(f"[worker_entrypoint] PING: {conn.ping()}", flush=True)
    queue = Queue(queue_name, connection=conn)
    worker = Worker([queue], connection=conn)
    print(f"[worker_entrypoint] Listening queue={queue_name}", flush=True)
    worker.work(with_scheduler=True)
