import enum
from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import BigInteger, DateTime, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7

from ..base import DefaultFieldsDCMixin, TypeBase
from ..types import LongText


class CostCategory(enum.StrEnum):
    CLONE_RESPONSE = "clone_response"
    CONTENT_INGESTION = "content_ingestion"
    PLATFORM_OPS = "platform_ops"


class CostTracking(TypeBase):
    __tablename__ = "cost_tracking"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    category: Mapped[str] = mapped_column(String(20), nullable=False)
    operation: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    model: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    tokens_in: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    tokens_out: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    cost_cents: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )


class Plan(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "myownclone_plans"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price_cents: Mapped[int] = mapped_column(Integer, nullable=False)
    stripe_price_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    words_training_limit: Mapped[int] = mapped_column(BigInteger, server_default=text("500000"), default=500000)
    responses_month_limit: Mapped[int] = mapped_column(Integer, server_default=text("2000"), default=2000)
    modes_active: Mapped[int] = mapped_column(Integer, server_default=text("1"), default=1)
    email_triage: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("false"), default=False)
    booking: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("false"), default=False)
    api_access: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("false"), default=False)
    multi_clone: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("false"), default=False)
    whitelabel: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("false"), default=False)


class GapStatus(enum.StrEnum):
    OPEN = "open"
    RESOLVED = "resolved"


class AnalyticsQuestion(TypeBase):
    __tablename__ = "analytics_questions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    question: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    count: Mapped[int] = mapped_column(Integer, server_default=text("1"), default=1)
    last_asked_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )


class AnalyticsGap(TypeBase):
    __tablename__ = "analytics_gaps"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    question: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    count: Mapped[int] = mapped_column(Integer, server_default=text("1"), default=1)
    suggested_source: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)
    status: Mapped[str] = mapped_column(String(20), server_default=text("'open'"), default="open")
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )


class ImpersonationLog(TypeBase):
    __tablename__ = "impersonation_log"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    admin_id: Mapped[str] = mapped_column(String(36), nullable=False)
    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class ImpersonationToken(TypeBase):
    __tablename__ = "impersonation_tokens"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    token: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    admin_id: Mapped[str] = mapped_column(String(36), nullable=False)
    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )


class Feedback(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "clone_feedback"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    conversation_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    message_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    rating: Mapped[str] = mapped_column(String(10), nullable=False)  # "up" or "down"
    comment: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
