"""Retrieval service stub.

This is a placeholder for the legacy ``RetrievalService`` that backed the
dataset/silo retrieval path. The real implementation is not wired in the
current VPS stack; callers treat ``retrieve()`` as returning a list of
document-like objects exposing ``.metadata``.

Returning an empty list (instead of a dict) keeps ``len(documents)`` and
``for doc in documents`` working in ``api/core/retrieval.py`` without
raising. When a real retrieval backend is connected, replace this stub
with the concrete service.
"""
from typing import Any


class RetrievalService:
    """Stub RetrievalService.

    ``retrieve`` is a ``staticmethod`` so both call shapes work:
    ``RetrievalService.retrieve(...)`` (legacy class-level call in
    ``api/core/retrieval.py``) and ``RetrievalService(**opts).retrieve(...)``.
    """

    def __init__(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    @staticmethod
    def retrieve(*args: Any, **kwargs: Any) -> list:
        # Intentionally empty: no dataset backend is wired in the current stack.
        return []

    def __getattr__(self, name: str):
        return lambda *a, **kw: None


__all__ = ["RetrievalService"]
