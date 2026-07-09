"""Onboarding models — track tour progress per user."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, String, UniqueConstraint, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.extensions.ext_database import db
from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7


class OnboardingStep(db.Model):
    """Tracks completion of individual tour steps per user."""

    __tablename__ = "onboarding_steps"
    __table_args__ = (
        UniqueConstraint("account_id", "tour_id", "step_key", name="uq_onboarding_step"),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuidv7())
    )
    account_id: Mapped[str] = mapped_column(
        String(36), nullable=False, index=True
    )
    tour_id: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )
    step_key: Mapped[str] = mapped_column(String(50), nullable=False)
    completed_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=naive_utc_now
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=naive_utc_now, server_default=func.current_timestamp()
    )


class OnboardingEvent(db.Model):
    """Analytics events for onboarding funnel tracking."""

    __tablename__ = "onboarding_events"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuidv7())
    )
    account_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    event: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    tour_id: Mapped[str | None] = mapped_column(String(50), nullable=True)
    step_key: Mapped[str | None] = mapped_column(String(50), nullable=True)
    properties: Mapped[dict | None] = mapped_column(db.JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=naive_utc_now, server_default=func.current_timestamp()
    )
