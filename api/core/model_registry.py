"""ModelRegistry: in-process cache for AI model selection per (tenant, task).

Cache TTL: 60 seconds. Invalidated explicitly on ai_model_assignments changes.
"""
from __future__ import annotations
import time
import threading
from typing import Optional

from sqlalchemy import select, and_, or_
from sqlalchemy.orm import Session

from api.models.ai_models import AIModel, AIModelAssignment, AIModelType
from api.extensions.ext_database import db


CACHE_TTL_SECONDS = 60


class _CacheEntry:
    __slots__ = ("value", "expires_at")

    def __init__(self, value, ttl: float = CACHE_TTL_SECONDS):
        self.value = value
        self.expires_at = time.monotonic() + ttl

    def is_expired(self) -> bool:
        return time.monotonic() > self.expires_at


class ModelRegistry:
    """In-process registry of (tenant_id, task) -> AIModel.

    Thread-safe. Cache TTL: 60s. Invalidated on assignment changes.
    """

    def __init__(self, session_factory=None):
        self._cache: dict[tuple[Optional[str], str], _CacheEntry] = {}
        self._lock = threading.RLock()
        self._session_factory = session_factory or (lambda: db.session)

    def get_model_for_task(
        self,
        tenant_id: Optional[str],
        task: str,
        *,
        session: Optional[Session] = None,
    ) -> Optional[AIModel]:
        """Get the active AIModel for (tenant_id, task).

        Resolution order:
        1. Active tenant-specific assignment (lowest priority wins)
        2. Active global assignment (tenant_id IS NULL) (lowest priority wins)

        Returns None if no assignment exists.
        """
        cache_key = (tenant_id, task)
        with self._lock:
            entry = self._cache.get(cache_key)
            if entry is not None and not entry.is_expired():
                return entry.value

        model = self._fetch_from_db(tenant_id, task, session=session)
        with self._lock:
            self._cache[cache_key] = _CacheEntry(model)
        return model

    def _fetch_from_db(
        self,
        tenant_id: Optional[str],
        task: str,
        *,
        session: Optional[Session] = None,
    ) -> Optional[AIModel]:
        sess = session or self._session_factory()
        # Tenant-specific first, then global
        stmt = (
            select(AIModel)
            .join(AIModelAssignment, AIModelAssignment.model_id == AIModel.id)
            .where(
                and_(
                    AIModelAssignment.task == task,
                    AIModelAssignment.is_active.is_(True),
                    AIModel.is_active.is_(True),
                    or_(
                        AIModelAssignment.tenant_id == tenant_id,
                        AIModelAssignment.tenant_id.is_(None),
                    ),
                )
            )
            .order_by(
                # Tenant-specific first (lower priority number = higher priority)
                AIModelAssignment.tenant_id.is_(None),  # NULL (global) last
                AIModelAssignment.priority.asc(),
            )
            .limit(1)
        )
        return sess.execute(stmt).scalar_one_or_none()

    def invalidate(self, tenant_id: Optional[str] = None, task: Optional[str] = None) -> None:
        """Invalidate cache entries.

        - If both args None: clear all cache
        - If only tenant_id: clear all entries for that tenant
        - If only task: clear all entries for that task
        - If both: clear that specific entry
        """
        with self._lock:
            if tenant_id is None and task is None:
                self._cache.clear()
                return
            keys_to_delete = [
                k for k in self._cache
                if (tenant_id is None or k[0] == tenant_id)
                and (task is None or k[1] == task)
            ]
            for k in keys_to_delete:
                del self._cache[k]

    def cache_size(self) -> int:
        """For tests: number of entries currently cached."""
        with self._lock:
            return len(self._cache)


# Module-level singleton
_registry: Optional[ModelRegistry] = None


def get_registry() -> ModelRegistry:
    """Get the process-wide ModelRegistry singleton."""
    global _registry
    if _registry is None:
        _registry = ModelRegistry()
    return _registry


def reset_registry() -> None:
    """Reset the singleton (for tests)."""
    global _registry
    _registry = None
