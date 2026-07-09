"""Prompt management models — versioned system prompts for clones."""

from __future__ import annotations

import enum
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship

from api.extensions.ext_database import db


class Prompt(db.Model):
    """A named prompt template, optionally tied to a clone."""

    __tablename__ = "prompts"

    id = Column(String(36), primary_key=True, default=lambda: __import__("uuid").uuid4().hex)
    name = Column(String(120), nullable=False)
    clone_id = Column(String(36), ForeignKey("clone_configs.id"), nullable=True, index=True)
    task = Column(String(32), nullable=False, default="chat", index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    versions = relationship("PromptVersion", backref="prompt", lazy="dynamic")


class PromptVersion(db.Model):
    """A specific version of a prompt."""

    __tablename__ = "prompt_versions"

    id = Column(String(36), primary_key=True, default=lambda: __import__("uuid").uuid4().hex)
    prompt_id = Column(String(36), ForeignKey("prompts.id"), nullable=False, index=True)
    version = Column(Integer, nullable=False, default=1)
    content = Column(Text, nullable=False)
    variables = Column(JSON, nullable=True)
    is_active = Column(Boolean, default=False, index=True)
    created_by = Column(String(36), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
