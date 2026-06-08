"""Retrieval methods enum stub."""
from enum import Enum

class RetrievalMethod(str, Enum):
    SEMANTIC_SEARCH = "semantic_search"
    SEMANTIC = "semantic"
    KEYWORD = "keyword"
    HYBRID = "hybrid"
    MMR = "mmr"

__all__ = ['RetrievalMethod']
