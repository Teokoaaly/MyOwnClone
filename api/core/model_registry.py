"""DB-backed model resolution with short-lived cache and legacy fallback."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Any, Callable

from sqlalchemy import select

from api.extensions import db
from api.libs.crypto import SecretCipher
from api.models.ai_models import AIModel, AIModelAssignment, AITask, TASK_CAPABILITY


@dataclass(slots=True)
class ResolvedModelConfig:
    """Normalized resolved model configuration for one tenant/task."""

    task: AITask
    provider: str
    model_id: str
    tenant_id: str | None
    source: str
    assignment_id: str | None = None
    ai_model_id: str | None = None
    display_name: str | None = None
    api_key: str | None = None
    api_key_encrypted: str | None = None
    base_url: str | None = None
    capabilities: tuple[str, ...] = ()
    override_params: dict[str, Any] = field(default_factory=dict)
    temperature_default: float | None = None
    max_tokens_default: int | None = None
    max_input_tokens: int | None = None
    embedding_dimensions: int | None = None
    priority: int = 100


@dataclass(slots=True)
class _CacheEntry:
    value: ResolvedModelConfig
    expires_at: float


class ModelRegistryError(RuntimeError):
    """Raised when a model cannot be resolved from DB or legacy fallback."""


class ModelRegistry:
    """Resolve the active model for a tenant/task with cache and fallback."""

    def __init__(
        self,
        *,
        ttl_seconds: int = 60,
        time_fn: Callable[[], float] | None = None,
    ) -> None:
        self.ttl_seconds = ttl_seconds
        self._time_fn = time_fn or time.monotonic
        self._cache: dict[tuple[str | None, str], _CacheEntry] = {}

    def resolve(self, *, tenant_id: str | None, task: AITask) -> ResolvedModelConfig:
        key = self._cache_key(tenant_id, task)
        now = self._time_fn()
        cached = self._cache.get(key)
        if cached and cached.expires_at > now:
            return cached.value

        try:
            resolved = self._resolve_from_db(tenant_id=tenant_id, task=task)
        except Exception:
            if cached:
                return cached.value
            resolved = self._resolve_from_legacy_env(task=task, tenant_id=tenant_id)
            if resolved is None:
                raise
        else:
            if resolved is None:
                resolved = self._resolve_from_legacy_env(task=task, tenant_id=tenant_id)

        if resolved is None:
            raise ModelRegistryError(
                f"No active AI model configured for tenant={tenant_id!r} task={task.value!r}."
            )

        self._cache[key] = _CacheEntry(
            value=resolved,
            expires_at=now + self.ttl_seconds,
        )
        return resolved

    def get_model_for_task(
        self,
        *,
        tenant_id: str | None,
        task: AITask,
    ) -> ResolvedModelConfig:
        return self.resolve(tenant_id=tenant_id, task=task)

    def invalidate(self, *, tenant_id: str | None = None, task: AITask | None = None) -> None:
        if tenant_id is None and task is None:
            self._cache.clear()
            return

        to_delete: list[tuple[str | None, str]] = []
        for cache_key in self._cache:
            cache_tenant_id, cache_task = cache_key
            if tenant_id is not None and cache_tenant_id != tenant_id:
                continue
            if task is not None and cache_task != task.value:
                continue
            to_delete.append(cache_key)
        for cache_key in to_delete:
            self._cache.pop(cache_key, None)

    def _cache_key(self, tenant_id: str | None, task: AITask) -> tuple[str | None, str]:
        return (tenant_id, task.value)

    def _resolve_from_db(
        self,
        *,
        tenant_id: str | None,
        task: AITask,
    ) -> ResolvedModelConfig | None:
        for scoped_tenant_id in self._scope_order(tenant_id):
            row = self._select_assignment_row(tenant_id=scoped_tenant_id, task=task)
            if row is None:
                continue
            assignment, model = row
            return self._build_resolved_from_db(
                tenant_id=tenant_id,
                task=task,
                assignment=assignment,
                model=model,
            )
        return None

    def _scope_order(self, tenant_id: str | None) -> tuple[str | None, ...]:
        if tenant_id:
            return (tenant_id, None)
        return (None,)

    def _select_assignment_row(
        self,
        *,
        tenant_id: str | None,
        task: AITask,
    ) -> tuple[AIModelAssignment, AIModel] | None:
        stmt = (
            select(AIModelAssignment, AIModel)
            .join(AIModel, AIModel.id == AIModelAssignment.model_id)
            .where(
                AIModelAssignment.task == task.value,
                AIModelAssignment.is_active.is_(True),
                AIModel.is_active.is_(True),
            )
            .order_by(AIModel.priority.asc(), AIModelAssignment.created_at.asc())
        )
        if tenant_id is None:
            stmt = stmt.where(AIModelAssignment.tenant_id.is_(None))
        else:
            stmt = stmt.where(AIModelAssignment.tenant_id == tenant_id)

        row = db.session.execute(stmt).first()
        if row is None:
            return None
        assignment, model = row
        required_capability = TASK_CAPABILITY[task].value
        if model.capabilities and required_capability not in model.capabilities:
            return None
        return assignment, model

    def _build_resolved_from_db(
        self,
        *,
        tenant_id: str | None,
        task: AITask,
        assignment: AIModelAssignment,
        model: AIModel,
    ) -> ResolvedModelConfig:
        return ResolvedModelConfig(
            task=task,
            provider=model.provider,
            model_id=model.model_id,
            tenant_id=tenant_id,
            source="database",
            assignment_id=assignment.id,
            ai_model_id=model.id,
            display_name=model.name,
            api_key=SecretCipher.decrypt(model.api_key_encrypted) if model.api_key_encrypted and not model.api_key_encrypted.startswith("local:") else None,
            api_key_encrypted=model.api_key_encrypted,
            base_url=model.base_url,
            capabilities=tuple(model.capabilities or ()),
            override_params=dict(assignment.override_params or {}),
            temperature_default=model.temperature_default,
            max_tokens_default=model.max_tokens_default,
            max_input_tokens=model.max_input_tokens,
            embedding_dimensions=model.embedding_dimensions,
            priority=model.priority,
        )

    def _resolve_from_legacy_env(
        self,
        *,
        task: AITask,
        tenant_id: str | None,
    ) -> ResolvedModelConfig | None:
        provider = self._detect_legacy_provider_for_task(task=task)
        if provider is None:
            return None

        if provider == "openai":
            model_id, dimensions = self._openai_legacy_model_for_task(task=task)
            return ResolvedModelConfig(
                task=task,
                provider="openai",
                model_id=model_id,
                tenant_id=tenant_id,
                source="legacy_env",
                api_key=os.environ["OPENAI_API_KEY"],
                base_url=self._openai_base_url(),
                embedding_dimensions=dimensions,
            )
        if provider == "anthropic":
            return ResolvedModelConfig(
                task=task,
                provider="anthropic",
                model_id=self._env("ANTHROPIC_MODEL", "claude-3-haiku-20240307"),
                tenant_id=tenant_id,
                source="legacy_env",
                api_key=os.environ["ANTHROPIC_API_KEY"],
            )
        if provider == "minimax":
            model_id, dimensions = self._minimax_legacy_model_for_task(task=task)
            return ResolvedModelConfig(
                task=task,
                provider="minimax",
                model_id=model_id,
                tenant_id=tenant_id,
                source="legacy_env",
                api_key=os.environ["MINIMAX_API_KEY"],
                base_url="https://api.minimax.io/v1",
                embedding_dimensions=dimensions,
            )
        if provider == "together":
            model_id, dimensions = self._together_legacy_model_for_task(task=task)
            return ResolvedModelConfig(
                task=task,
                provider="together",
                model_id=model_id,
                tenant_id=tenant_id,
                source="legacy_env",
                api_key=os.environ["TOGETHER_API_KEY"],
                base_url="https://api.together.xyz/v1",
                embedding_dimensions=dimensions,
            )
        if provider == "local_whisper":
            # Local faster-whisper: no API key, no base URL. The
            # ``model_id`` selects which whisper size to load (default
            # ``tiny``) and can be overridden via LOCAL_WHISPER_MODEL.
            model_id = (
                os.environ.get("LOCAL_WHISPER_MODEL", "").strip()
                or "tiny"
            )
            return ResolvedModelConfig(
                task=task,
                provider="local_whisper",
                model_id=model_id,
                tenant_id=tenant_id,
                source="legacy_env",
                api_key=None,
                base_url=None,
            )
        return None

    def _detect_legacy_provider_for_task(self, *, task: AITask) -> str | None:
        if task is AITask.STT:
            if os.getenv("OPENAI_API_KEY"):
                return "openai"
            # No external key? Fall back to the local faster-whisper
            # runtime so STT keeps working out of the box on hosts
            # that don't have a paid STT provider configured.
            return "local_whisper"
        if task is AITask.EMBEDDING:
            if os.getenv("OPENAI_API_KEY"):
                return "openai"
            if os.getenv("TOGETHER_API_KEY"):
                return "together"
            if os.getenv("MINIMAX_API_KEY"):
                return "minimax"
            return None

        if os.getenv("OPENAI_API_KEY"):
            return "openai"
        if os.getenv("ANTHROPIC_API_KEY"):
            return "anthropic"
        if os.getenv("MINIMAX_API_KEY"):
            return "minimax"
        if os.getenv("TOGETHER_API_KEY"):
            return "together"
        return None

    def _openai_legacy_model_for_task(self, *, task: AITask) -> tuple[str, int | None]:
        if task is AITask.EMBEDDING:
            return ("text-embedding-3-small", 1536)
        if task is AITask.STT:
            return ("whisper-1", None)
        return (self._env("OPENAI_MODEL", "gpt-4o-mini"), None)

    def _together_legacy_model_for_task(self, *, task: AITask) -> tuple[str, int | None]:
        if task is AITask.EMBEDDING:
            return ("togethercomputer/m2-bert-80M-8k-retrieval", 1536)
        return (self._env("TOGETHER_MODEL", "meta-llama/Llama-3-8B-Instruct-Turbo"), None)

    def _minimax_legacy_model_for_task(self, *, task: AITask) -> tuple[str, int | None]:
        if task is AITask.EMBEDDING:
            return ("embo-01", 1536)
        return (self._env("MINIMAX_MODEL", "minimax-m2.7"), None)

    def _env(self, name: str, default: str) -> str:
        return os.getenv(name, "").strip() or default

    def dump_status(self, *, tenant_id: str | None = None) -> dict:
        """Return registry state for the admin monitoring panel."""
        now = self._time_fn()
        items = []
        for task in AITask:
            key = self._cache_key(tenant_id, task)
            cached = self._cache.get(key)
            if cached and cached.expires_at > now:
                entry = cached.value
                items.append({
                    "task": task.value,
                    "provider": entry.provider,
                    "model_id": entry.model_id,
                    "display_name": entry.display_name,
                    "source": entry.source,
                    "cache_hit": True,
                    "cache_ttl_remaining_s": int(cached.expires_at - now),
                })
            else:
                try:
                    resolved = self.resolve(tenant_id=tenant_id, task=task)
                    items.append({
                        "task": task.value,
                        "provider": resolved.provider,
                        "model_id": resolved.model_id,
                        "display_name": resolved.display_name,
                        "source": resolved.source,
                        "cache_hit": False,
                        "cache_ttl_remaining_s": self.ttl_seconds,
                    })
                except ModelRegistryError:
                    items.append({
                        "task": task.value,
                        "provider": None,
                        "model_id": None,
                        "display_name": None,
                        "source": "unresolved",
                        "cache_hit": False,
                        "cache_ttl_remaining_s": 0,
                    })
        return {
            "ttl_seconds": self.ttl_seconds,
            "cache_size": len(self._cache),
            "tasks": items,
        }

    def _openai_base_url(self) -> str | None:
        return (
            os.getenv("OPENAI_BASE_URL", "").strip()
            or os.getenv("OPENAI_API_BASE", "").strip()
            or None
        )
