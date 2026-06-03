import enum
from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from libs.datetime_utils import naive_utc_now
from libs.uuid_utils import uuidv7

from ..base import DefaultFieldsDCMixin, TypeBase
from ..types import LongText


class EmailInboundStatus(enum.StrEnum):
    PENDING = "pending"
    SENT = "sent"
    DISCARDED = "discarded"
    SPAM = "spam"


class EmailInbound(TypeBase):
    __tablename__ = "email_inbound"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        insert_default=lambda: str(uuidv7()),
        default_factory=lambda: str(uuidv7()),
        init=False,
    )
    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    from_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    from_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    subject: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    body_text: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    body_html: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    draft_reply: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    status: Mapped[str] = mapped_column(String(20), server_default=text("'pending'"), default="pending")
    labels: Mapped[Optional[str]] = mapped_column(sa.ARRAY(String(50)), nullable=True, default=None)
    classification: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default=None)
    thread_id: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)
    received_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        insert_default=naive_utc_now,
        default_factory=naive_utc_now,
        init=False,
        server_default=func.current_timestamp(),
    )
    responded_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, default=None)


class EmailTemplate(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "email_templates"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    subject: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    body: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    trigger_keywords: Mapped[Optional[str]] = mapped_column(sa.ARRAY(String(100)), nullable=True)
