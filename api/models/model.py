"""Stub models for Dify compatibility layer.

In standalone MyOwnClone mode, the Dify base platform tables (App, Conversation,
Message) do not exist. These stubs prevent ImportError while the analytics
controller degrades gracefully to zeros for those metrics.

TODO: Replace App/Conversation/Message with native MyOwnClone conversation
tracking once the conversations table is queried directly.
"""
from __future__ import annotations

from typing import Optional


class _UnmappedStub:
    """Base for stub classes that are NOT SQLAlchemy-mapped.

    These exist only to prevent ImportError. Any select() call against
    these classes will raise RuntimeError to signal unimplemented behavior.
    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)


class App(_UnmappedStub):
    """Dify App model — not available in standalone mode."""
    id: str
    tenant_id: str


class Conversation(_UnmappedStub):
    """Dify Conversation model — not available in standalone mode."""
    id: str
    app_id: str
    is_deleted: bool = False


class Message(_UnmappedStub):
    """Dify Message model — not available in standalone mode."""
    id: str
    app_id: str


__all__ = ["App", "Conversation", "Message"]
