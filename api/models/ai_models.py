"""AI Models catalog and task assignments (Sisyphus M1).

Three tables that together drive the configurable-AI-by-task system:

- ``AIModel``: catalogue of LLM / embedding / STT providers with encrypted keys.
- ``AIModelAssignment``: which model serves which task for a tenant (or globally
  when ``tenant_id`` is NULL). Backed by a partial unique index that enforces
  "at most one active assignment per (tenant_id, task)".
- ``AIInvocation``: append-only audit log of every AI call. Inserted by M7's
  refactor of ``model_manager`` so streaming cost tracking can be verified.

Design constraints (see ``HANDOFF_LLM.md`` §5 M1 and the plan in
``.sisyphus/plans/ai-models-configurable.md``):

- UUIDv7 primary keys via ``api.libs.uuid_utils.uuidv7``.
- Timestamps via ``naive_utc_now`` + ``func.current_timestamp()``.
- Enums are ``enum.StrEnum`` (NOT plain ``Enum``).
- ``api_key_encrypted`` is ``Text`` and MUST contain an AES-256-GCM blob
  produced by ``api.libs.crypto.SecretCipher`` (M2). Plaintext keys are
  forbidden by the M2 contract test.
- ``AIModelAssignment.model_id`` uses ``ON DELETE RESTRICT`` so deactivating a
  model is the only safe path (soft-delete via ``is_active=False``).
- The partial unique index on active assignments is created in the Alembic
  migration (``2026_06_21_0002_ai_models_catalog.py``), not as a SQLAlchemy
  ``UniqueConstraint``, because PostgreSQL partial indexes cannot be expressed
  portably in the ORM and the migration is the authoritative source of truth.
"""
from __future__ import annotations

import enum
from datetime import date, datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import (
    JSON,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7

from ..base import TypeBase


class AIProvider(enum.StrEnum):
    """Supported LLM / embedding / STT providers."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    MINIMAX = "minimax"  # placeholder, M4b can fill in
    TOGETHER = "together"
    OPENAI_COMPATIBLE = "openai_compatible"
    LOCAL = "local"


class AICapability(enum.StrEnum):
    """What a model can do. Storing as JSON array of these strings."""

    LLM = "llm"
    EMBEDDING = "embedding"
    STT = "stt"
    TTS = "tts"
    RERANKING = "reranking"


class AITask(enum.StrEnum):
    """The 5 user-facing tasks we route to a model."""

    CHAT = "chat"
    EMBEDDING = "embedding"
    EMAIL_CLASSIFICATION = "email_classification"
    EMAIL_DRAFT = "email_draft"
    STT = "stt"


#: Capability required for each task. Used by M9's API layer to validate that
#: an assigned model is actually capable of serving the task.
TASK_CAPABILITY: dict[AITask, AICapability] = {
    AITask.CHAT: AICapability.LLM,
    AITask.EMBEDDING: AICapability.EMBEDDING,
    AITask.EMAIL_CLASSIFICATION: AICapability.LLM,
    AITask.EMAIL_DRAFT: AICapability.LLM,
    AITask.STT: AICapability.STT,
}


def _new_uuid() -> str:
    """Default factory: UUIDv7 string."""
    return str(uuidv7())


class AIModel(TypeBase):
    """A concrete model deployment (provider + model_id + encrypted key).

    ``api_key_encrypted`` MUST be an AES-256-GCM blob produced by
    ``api.libs.crypto.SecretCipher.encrypt``. Plaintext keys are a contract
    violation; the M2 test suite asserts that no row in production has a key
    that does not start with the GCM marker ``"gAAAA"`` (Fernet would start
    the same way — see M2 for the formal check).
    """

    __tablename__ = "ai_models"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=_new_uuid,
        default=_new_uuid,
    )
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    provider: Mapped[str] = mapped_column(String(20), nullable=False)
    model_id: Mapped[str] = mapped_column(String(120), nullable=False)
    api_key_encrypted: Mapped[str] = mapped_column(Text, nullable=False)
    base_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    capabilities: Mapped[list[str]] = mapped_column(
        JSON, nullable=False, default=list
    )
    input_price_cents_per_mtok: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    output_price_cents_per_mtok: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    priority: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="100", default=100
    )
    temperature_default: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True
    )
    max_tokens_default: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )
    max_input_tokens: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )
    embedding_dimensions: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true", default=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        server_default=func.current_timestamp(),
    )


class AIModelAssignment(TypeBase):
    """Routes one (tenant_id, task) pair to a specific ``AIModel``.

    Soft delete via ``is_active=False``. The DB enforces "at most one active
    assignment per (tenant_id, task)" with a partial unique index created in
    the migration.
    """

    __tablename__ = "ai_model_assignments"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=_new_uuid,
        default=_new_uuid,
    )
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    task: Mapped[str] = mapped_column(String(30), nullable=False)
    # ON DELETE RESTRICT is enforced at the DB level (see migration).
    model_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("ai_models.id", ondelete="RESTRICT"),
        nullable=False,
    )
    override_params: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true", default=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        server_default=func.current_timestamp(),
    )


class AIInvocation(TypeBase):
    """Append-only audit log of every AI call. Inserted by M7.

    Includes enough fields to compute cost on the fly, but M12 introduces a
    materialized rollup ``cost_daily_rollup`` for dashboards.
    """

    __tablename__ = "ai_invocations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=_new_uuid,
        default=_new_uuid,
    )
    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    clone_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    task: Mapped[str] = mapped_column(String(30), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    prompt_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    prompt_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    completion_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    latency_ms: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    success: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true", default=True
    )
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )


class CostDailyRollup(TypeBase):
    """Daily aggregated runtime usage for admin/reporting queries."""

    __tablename__ = "cost_daily_rollup"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=_new_uuid,
        default=_new_uuid,
    )
    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    day: Mapped[date] = mapped_column(sa.Date, nullable=False)
    task: Mapped[str] = mapped_column(String(30), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    invocations: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    prompt_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    completion_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    success_count: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    error_count: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0", default=0
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default=naive_utc_now,
        onupdate=naive_utc_now,
        server_default=func.current_timestamp(),
    )


__all__ = [
    "AIProvider",
    "AICapability",
    "AITask",
    "TASK_CAPABILITY",
    "AIModel",
    "AIModelAssignment",
    "AIInvocation",
    "CostDailyRollup",
]
