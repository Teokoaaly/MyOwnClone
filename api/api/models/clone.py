import enum
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from libs.datetime_utils import naive_utc_now
from libs.uuid_utils import uuidv7

from ..base import DefaultFieldsDCMixin, TypeBase
from ..types import LongText


class CloneSilo(enum.StrEnum):
    TEACH = "teach"
    SUPPORT = "support"
    SALES = "sales"


class CloneConfig(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "clone_configs"

    tenant_id: Mapped[str] = mapped_column(String(36), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    personality_tone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    language: Mapped[str] = mapped_column(String(10), server_default=text("'es'"), default="es")
    custom_domain: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, default=None)
    active_modes: Mapped[Optional[str]] = mapped_column(sa.ARRAY(String(20)), nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("true"), default=True)


class CloneModePrompt(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "clone_mode_prompts"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    mode: Mapped[str] = mapped_column(String(20), nullable=False)
    system_prompt: Mapped[str] = mapped_column(LongText, nullable=False)
    is_active: Mapped[bool] = mapped_column(sa.Boolean, server_default=text("true"), default=True)


class CreatorMemoryType(enum.StrEnum):
    MEMORY = "memory"
    SIGNATURE = "signature"
    TEMPLATE = "template"


class CreatorMemory(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "creator_memory"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(LongText, nullable=False)
    trigger_condition: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    priority: Mapped[int] = mapped_column(sa.Integer, server_default=text("0"), default=0)
