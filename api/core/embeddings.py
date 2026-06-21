"""Stub de EmbeddingService. Implementación real en M8."""
from typing import List
import hashlib


class EmbeddingService:
    """Stub que retorna vectores deterministas (hash → vector 1536d)."""

    DIMENSION = 1536

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        return [self._hash_to_vector(t) for t in texts]

    @staticmethod
    def _hash_to_vector(text: str) -> List[float]:
        h = hashlib.sha256(text.encode()).digest()
        return [
            (b / 255.0) - 0.5
            for b in (h * 60)[:EmbeddingService.DIMENSION]
        ]
