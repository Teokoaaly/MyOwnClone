"""Stub de retrieval. Implementación real en M10 con RAG pipeline."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class RetrievalResult:
    found: bool
    contents: List[str] = field(default_factory=list)
    scores: List[float] = field(default_factory=list)


def retrieve_from_silo(*args, **kwargs) -> RetrievalResult:
    return RetrievalResult(found=False)
