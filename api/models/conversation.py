from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import DateTime, ForeignKey, String, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column

from api.base import TypeBase
from api.libs.uuid_utils import uuidv7


class Conversation(TypeBase):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(Text, primary_key=True, insert_default=lambda: str(uuidv7()), default=lambda: str(uuidv7()))
    clone_id: Mapped[str] = mapped_column(Text, ForeignKey("clone_configs.id", ondelete="CASCADE"), nullable=False)
    visitor_id: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    mode: Mapped[str] = mapped_column(String(30), nullable=False, server_default=text("'pedagogy'"), default="pedagogy")
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


class Message(TypeBase):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(Text, primary_key=True, insert_default=lambda: str(uuidv7()), default=lambda: str(uuidv7()))
    conversation_id: Mapped[str] = mapped_column(Text, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sources: Mapped[Optional[list[dict]]] = mapped_column(sa.JSON, nullable=True)
    feedback: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )


__all__ = ["Conversation", "Message"]
