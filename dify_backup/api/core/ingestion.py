"""Clonify RAG ingestion pipeline — adds silo/context metadata on top of Dify's ingestion.

Wraps Dify's document ingestion to:
1. Tag documents with silo + context_id metadata
2. Route documents to the correct silo-specific dataset
3. Support speaker diarization metadata (for future use)
"""

import logging
from typing import Any, Optional

from core.myownclone.silos import CloneSilo, dataset_name_for_silo

logger = logging.getLogger(__name__)


class IngestionMetadata:
    def __init__(
        self,
        clone_id: str,
        silo: CloneSilo,
        context_id: Optional[str] = None,
        speaker: Optional[str] = None,
    ):
        self.clone_id = clone_id
        self.silo = silo
        self.context_id = context_id
        self.speaker = speaker

    def to_doc_metadata(self) -> dict[str, Any]:
        meta: dict[str, Any] = {
            "clone_id": self.clone_id,
            "silo": self.silo.value,
        }
        if self.context_id:
            meta["context_id"] = self.context_id
        if self.speaker:
            meta["speaker"] = self.speaker
            meta["source_type"] = "creator" if self.speaker == "creator" else "external"
        return meta

    def to_dataset_name(self) -> str:
        return dataset_name_for_silo(self.clone_id, self.silo)
