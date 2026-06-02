"""myownclone models — CloneConfig, CloneSilo, CreatorMemory, EmailInbound, MeetingType, Booking, CostTracking, Analytics, Impersonation, Plan.

All models extend Dify's base classes and are scoped to a tenant_id.
"""

from __future__ import annotations

import enum
from datetime import datetime
from typing import Any, TypedDict
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import JSON, DateTime, String, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from models.base import TypeBase
from models.types import LongText, StringUUID


# ─── Enums ───────────────────────────────────────────────────────────────────


class CloneSilo(str, enum.Enum):
    """Silo de conocimiento — determina qué dataset se usa para retrieval."""

    TEACH = "teach"    # Contenido pedagógico / cursos
    SUPPORT = "support"  # Documentación de soporte
    SALES = "sales"    # Catálogo de productos / pricing


class CreatorMemoryType(str, enum.Enum):
    """Tipo de memoria del creador."""

    MEMORY = "memory"       # Información de contexto permanente
    SIGNATURE = "signature"  # Firma de email
    TEMPLATE = "template"    # Plantilla de respuesta


class EmailInboundStatus(str, enum.Enum):
    """Estado de un email recibido."""

    PENDING = "pending"    # Recibido, sin clasificar
    CLASSIFIED = "classified"  # Clasificado, draft generado
    SENT = "sent"          # Respuesta enviada
    DISCARDED = "discarded"  # Descartado por el creador


class BookingStatus(str, enum.Enum):
    """Estado de una reserva."""

    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


# ─── DTOs (paraserialización) ───────────────────────────────────────────────


class CloneSiloTypedDict(TypedDict):
    pass  # str enum serializes directly


class CloneModePromptDict(TypedDict):
    id: str
    mode: str
    system_prompt: str
    is_active: bool


class CloneConfigDict(TypedDict):
    id: str
    tenant_id: str
    name: str
    slug: str
    description: str | None
    avatar_url: str | None
    personality_tone: str | None
    language: str
    active_modes: list[str]
    is_active: bool
    custom_domain: str | None
    created_at: datetime | None
    updated_at: datetime | None


# ─── clone_configs ───────────────────────────────────────────────────────────


class CloneConfig(TypeBase):
    """Configuración principal de un clon.

    Un clon pertenece a un tenant y tiene un slug único.
    Define personalidad, idioma, modos activos y dominio personalizado.
    """

    __tablename__ = "clone_configs"

    tenant_id: Mapped[str] = mapped_column(StringUUID, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(LongText, nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    personality_tone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    language: Mapped[str] = mapped_column(String(10), nullable=False, server_default="es")
    active_modes: Mapped[list[str] | None] = mapped_column(
        ARRAY(String(20)), server_default="'{}'", nullable=True
    )
    is_active: Mapped[bool] = mapped_column(server_default="true", nullable=False)
    custom_domain: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Relaciones
    mode_prompts: Mapped[list["CloneModePrompt"]] = sa.orm.relationship(
        "CloneModePrompt", back_populates="clone_config", cascade="all, delete-orphan"
    )
    creator_memories: Mapped[list["CreatorMemory"]] = sa.orm.relationship(
        "CreatorMemory", back_populates="clone_config", cascade="all, delete-orphan"
    )
    emails: Mapped[list["EmailInbound"]] = sa.orm.relationship(
        "EmailInbound", back_populates="clone_config", cascade="all, delete-orphan"
    )
    meeting_types: Mapped[list["MeetingType_"]] = sa.orm.relationship(
        "MeetingType_", back_populates="clone_config", cascade="all, delete-orphan"
    )
    products: Mapped[list["Product"]] = sa.orm.relationship(
        "Product", back_populates="clone_config", cascade="all, delete-orphan"
    )
    analytics_questions: Mapped[list["AnalyticsQuestion"]] = sa.orm.relationship(
        "AnalyticsQuestion", back_populates="clone_config", cascade="all, delete-orphan"
    )
    analytics_gaps: Mapped[list["AnalyticsGap"]] = sa.orm.relationship(
        "AnalyticsGap", back_populates="clone_config", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<CloneConfig {self.slug} ({self.name})>"


# ─── clone_mode_prompts ──────────────────────────────────────────────────────


class CloneModePrompt(TypeBase):
    """Prompt del sistema para un modo específico (teach/support/sales).

    Cada clon tiene un prompt activo por modo. El prompt define cómo
    el clon responde en ese contexto.
    """

    __tablename__ = "clone_mode_prompts"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    mode: Mapped[str] = mapped_column(String(20), nullable=False)  # teach/support/sales
    system_prompt: Mapped[str] = mapped_column(LongText, nullable=False)
    is_active: Mapped[bool] = mapped_column(server_default="true", nullable=False)

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="mode_prompts"
    )

    __table_args__ = (
        sa.Index("idx_mode_prompts_clone", "clone_id", "mode"),
    )

    def __repr__(self) -> str:
        return f"<CloneModePrompt {self.clone_id}/{self.mode}>"


# ─── creator_memory ──────────────────────────────────────────────────────────


class CreatorMemory(TypeBase):
    """Memoria, firma o plantilla del creador.

    Se inyecta en el prompt del clon paradar contexto personal.
    - memory: información de contexto permanente
    - signature: firma de email
    - template: plantilla de respuesta
    """

    __tablename__ = "creator_memory"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    type: Mapped[str] = mapped_column(String(20), nullable=False)  # memory/signature/template
    content: Mapped[str] = mapped_column(LongText, nullable=False)
    trigger_condition: Mapped[str | None] = mapped_column(LongText, nullable=True)
    priority: Mapped[int] = mapped_column(server_default="0", nullable=False)

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="creator_memories"
    )

    __table_args__ = (
        sa.Index("idx_creator_memory_clone_type", "clone_id", "type"),
    )

    def __repr__(self) -> str:
        return f"<CreatorMemory {self.clone_id}/{self.type}>"


# ─── email_inbound ────────────────────────────────────────────────────────────


class EmailInbound(TypeBase):
    """Email recibido vía SendGrid Inbound Parse webhook.

    Se clasifica con IA y se genera un draft de respuesta automáticamente.
    """

    __tablename__ = "email_inbound"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    from_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    from_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    subject: Mapped[str | None] = mapped_column(String(500), nullable=True)
    body_text: Mapped[str | None] = mapped_column(LongText, nullable=True)
    body_html: Mapped[str | None] = mapped_column(LongText, nullable=True)
    draft_reply: Mapped[str | None] = mapped_column(LongText, nullable=True)
    status: Mapped[str] = mapped_column(String(20), server_default="'pending'", nullable=False)
    labels: Mapped[list[str] | None] = mapped_column(
        ARRAY(String(50)), server_default="'{}'", nullable=True
    )
    classification: Mapped[str | None] = mapped_column(String(50), nullable=True)
    thread_id: Mapped[str | None] = mapped_column(String(500), nullable=True)
    received_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    responded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="emails"
    )

    __table_args__ = (
        sa.Index("idx_email_inbound_clone_status", "clone_id", "status"),
    )

    def __repr__(self) -> str:
        return f"<EmailInbound {self.id} {self.status}>"


# ─── email_templates ─────────────────────────────────────────────────────────


class EmailTemplate(TypeBase):
    """Plantilla de email con trigger keywords.

    Se usa para respuestas automáticas basadas en palabras clave.
    """

    __tablename__ = "email_templates"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    subject: Mapped[str | None] = mapped_column(String(500), nullable=True)
    body: Mapped[str | None] = mapped_column(LongText, nullable=True)
    trigger_keywords: Mapped[list[str] | None] = mapped_column(
        ARRAY(String(100)), server_default="'{}'", nullable=True
    )

    def __repr__(self) -> str:
        return f"<EmailTemplate {self.name}>"


# ─── meeting_types ───────────────────────────────────────────────────────────


class MeetingType_(TypeBase):
    """Tipo de reunión (demo, consulta, onboarding...).

    Cada tipo tiene duración, precio y color para la UI.
    """

    __tablename__ = "meeting_types"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(server_default="30", nullable=False)
    price_cents: Mapped[int] = mapped_column(server_default="0", nullable=False)
    description: Mapped[str | None] = mapped_column(LongText, nullable=True)
    color: Mapped[str] = mapped_column(String(7), server_default="'#6366f1'", nullable=False)
    active: Mapped[bool] = mapped_column(server_default="true", nullable=False)

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="meeting_types"
    )
    bookings: Mapped[list["Booking"]] = sa.orm.relationship(
        "Booking", back_populates="meeting_type", cascade="all, delete-orphan"
    )
    availability_entries: Mapped[list["Availability"]] = sa.orm.relationship(
        "Availability", back_populates="meeting_type", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<MeetingType_ {self.name}>"


# ─── availability ─────────────────────────────────────────────────────────────


class Availability(TypeBase):
    """Ventana de disponibilidad para un tipo de reunión.

    Define días de la semana y franjas horarias disponibles.
    """

    __tablename__ = "availability"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    meeting_type_id: Mapped[str | None] = mapped_column(
        StringUUID, sa.ForeignKey("meeting_types.id", ondelete="CASCADE"), nullable=True
    )
    day_of_week: Mapped[int] = mapped_column(nullable=False)  # 0=Lunes, 6=Domingo
    start_time: Mapped[datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime] = mapped_column(nullable=False)
    buffer_minutes: Mapped[int] = mapped_column(server_default="15", nullable=False)

    # Relaciones
    meeting_type: Mapped["MeetingType_ | None"] = sa.orm.relationship(
        "MeetingType_", back_populates="availability_entries"
    )

    __table_args__ = (
        sa.Index("idx_availability_clone_dow", "clone_id", "day_of_week"),
    )

    def __repr__(self) -> str:
        return f"<Availability day={self.day_of_week}>"


# ─── bookings ─────────────────────────────────────────────────────────────────


class Booking(TypeBase):
    """Reserva de una reunión.

    Creada vía la API pública o el dashboard del creador.
    """

    __tablename__ = "bookings"

    meeting_type_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("meeting_types.id", ondelete="CASCADE"), nullable=False
    )
    visitor_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    visitor_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(20), server_default="'confirmed'", nullable=False)
    meeting_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    recording_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    transcript: Mapped[str | None] = mapped_column(LongText, nullable=True)
    notes: Mapped[str | None] = mapped_column(LongText, nullable=True)

    # Relaciones
    meeting_type: Mapped["MeetingType_"] = sa.orm.relationship(
        "MeetingType_", back_populates="bookings"
    )

    __table_args__ = (
        sa.Index("idx_bookings_meeting_date", "meeting_type_id", "date"),
    )

    def __repr__(self) -> str:
        return f"<Booking {self.id} {self.status}>"


# ─── products ────────────────────────────────────────────────────────────────


class Product(TypeBase):
    """Producto o servicio del catálogo del clon.

    Se usa en modo sales para recomendar productos.
    """

    __tablename__ = "products"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(LongText, nullable=True)
    price_cents: Mapped[int | None] = mapped_column(nullable=True)
    url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    priority: Mapped[int] = mapped_column(server_default="0", nullable=False)
    active: Mapped[bool] = mapped_column(server_default="true", nullable=False)

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="products"
    )

    __table_args__ = (
        sa.Index("idx_products_clone_active", "clone_id", "active"),
    )

    def __repr__(self) -> str:
        return f"<Product {self.name}>"


# ─── cost_tracking ───────────────────────────────────────────────────────────


class CostTracking(TypeBase):
    """Tracking de costes por operación (respuestas clone, ingestion, ops).

    Agregado por tenant y categoría para dashboards de MRR.
    """

    __tablename__ = "cost_tracking"

    tenant_id: Mapped[str] = mapped_column(StringUUID, nullable=False, index=True)
    category: Mapped[str] = mapped_column(String(20), nullable=False)  # clone_response/content_ingestion/platform_ops
    operation: Mapped[str | None] = mapped_column(String(100), nullable=True)
    model: Mapped[str | None] = mapped_column(String(50), nullable=True)
    tokens_in: Mapped[int] = mapped_column(server_default="0", nullable=False)
    tokens_out: Mapped[int] = mapped_column(server_default="0", nullable=False)
    cost_cents: Mapped[int] = mapped_column(server_default="0", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    __table_args__ = (
        sa.Index("idx_cost_tracking_tenant_category_ts", "tenant_id", "category", "created_at"),
    )

    def __repr__(self) -> str:
        return f"<CostTracking {self.category} {self.cost_cents}c>"


# ─── analytics_questions ─────────────────────────────────────────────────────


class AnalyticsQuestion(TypeBase):
    """Preguntas frecuentes capturadas de las conversaciones.

    Se usa para identificar gaps de conocimiento.
    """

    __tablename__ = "analytics_questions"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    question: Mapped[str | None] = mapped_column(LongText, nullable=True)
    count: Mapped[int] = mapped_column(server_default="1", nullable=False)
    last_asked_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="analytics_questions"
    )

    __table_args__ = (
        sa.Index("idx_analytics_q_clone", "clone_id"),
    )

    def __repr__(self) -> str:
        return f"<AnalyticsQuestion {self.id} x{self.count}>"


# ─── analytics_gaps ──────────────────────────────────────────────────────────


class AnalyticsGap(TypeBase):
    """Gap de conocimiento — pregunta sin respuesta en la base de conocimiento.

    Se detecta cuando el retrieval no encuentra contenido relevante.
    """

    __tablename__ = "analytics_gaps"

    clone_id: Mapped[str] = mapped_column(
        StringUUID, sa.ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False
    )
    question: Mapped[str | None] = mapped_column(LongText, nullable=True)
    count: Mapped[int] = mapped_column(server_default="1", nullable=False)
    suggested_source: Mapped[str | None] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(20), server_default="'open'", nullable=False)  # open/resolved/ignored

    # Relaciones
    clone_config: Mapped["CloneConfig"] = sa.orm.relationship(
        "CloneConfig", back_populates="analytics_gaps"
    )

    __table_args__ = (
        sa.Index("idx_analytics_gaps_clone", "clone_id", "status"),
    )

    def __repr__(self) -> str:
        return f"<AnalyticsGap {self.id} [{self.status}]>"


# ─── impersonation_log ────────────────────────────────────────────────────────


class ImpersonationLog(TypeBase):
    """Log de suplantación de identidad — admins que acceden como tenant.

    Auditoría de acceso: quién, cuándo, por qué.
    """

    __tablename__ = "impersonation_log"

    admin_id: Mapped[str] = mapped_column(StringUUID, nullable=False)
    tenant_id: Mapped[str] = mapped_column(StringUUID, nullable=False, index=True)
    reason: Mapped[str | None] = mapped_column(LongText, nullable=True)
    started_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    ended_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        sa.Index("idx_impersonation_admin", "admin_id"),
    )

    def __repr__(self) -> str:
        return f"<ImpersonationLog {self.admin_id}→{self.tenant_id}>"


# ─── impersonation_tokens ────────────────────────────────────────────────────


class ImpersonationToken(TypeBase):
    """Token de suplantación temporal (30 min).

    Generado al impersonar un tenant desde el admin panel.
    """

    __tablename__ = "impersonation_tokens"

    token: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    admin_id: Mapped[str] = mapped_column(StringUUID, nullable=False)
    tenant_id: Mapped[str] = mapped_column(StringUUID, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    def __repr__(self) -> str:
        return f"<ImpersonationToken {self.token[:8]}...>"

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at


# ─── myownclone_plans ─────────────────────────────────────────────────────────


class Plan(TypeBase):
    """Planes de suscripción (Básico, Pro, Escala, Enterprise).

    Define límites de uso y features activas por tenant.
    """

    __tablename__ = "myownclone_plans"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price_cents: Mapped[int] = mapped_column(nullable=False)
    stripe_price_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    words_training_limit: Mapped[int] = mapped_column(server_default="500000", nullable=False)
    responses_month_limit: Mapped[int] = mapped_column(server_default="2000", nullable=False)
    modes_active: Mapped[int] = mapped_column(server_default="1", nullable=False)
    email_triage: Mapped[bool] = mapped_column(server_default="false", nullable=False)
    booking: Mapped[bool] = mapped_column(server_default="false", nullable=False)
    api_access: Mapped[bool] = mapped_column(server_default="false", nullable=False)
    multi_clone: Mapped[bool] = mapped_column(server_default="false", nullable=False)
    whitelabel: Mapped[bool] = mapped_column(server_default="false", nullable=False)

    def __repr__(self) -> str:
        return f"<Plan {self.name} {self.price_cents}c>"


# ─── Feedback ────────────────────────────────────────────────────────────────


class Feedback(TypeBase):
    """Feedback thumbs up/down en respuestas del clon."""

    __tablename__ = "myownclone_feedback"

    clone_id: Mapped[str] = mapped_column(StringUUID, nullable=False, index=True)
    message_id: Mapped[str] = mapped_column(StringUUID, nullable=False)
    rating: Mapped[str] = mapped_column(String(10), nullable=False)  # up/down
    comment: Mapped[str | None] = mapped_column(LongText, nullable=True)

    def __repr__(self) -> str:
        return f"<Feedback {self.clone_id}/{self.rating}>"


# ─── Exports ─────────────────────────────────────────────────────────────────

__all__ = [
    "Availability",
    "Booking",
    "BookingStatus",
    "CloneConfig",
    "CloneModePrompt",
    "CloneSilo",
    "CloneSiloTypedDict",
    "CloneConfigDict",
    "CloneModePromptDict",
    "CostTracking",
    "CreatorMemory",
    "CreatorMemoryType",
    "EmailInbound",
    "EmailInboundStatus",
    "EmailTemplate",
    "Feedback",
    "ImpersonationLog",
    "ImpersonationToken",
    "MeetingType_",
    "Plan",
    "AnalyticsGap",
    "AnalyticsQuestion",
    "Product",
]