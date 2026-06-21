"""Stub de IngestionPipeline. Implementación real en M10."""
from typing import List
import uuid


class IngestionPipeline:
    """Stub que retorna IDs mock."""

    def ingest_text(self, text: str) -> str:
        return str(uuid.uuid4())

    def ingest_batch(self, texts: List[str]) -> List[str]:
        return [self.ingest_text(t) for t in texts]
