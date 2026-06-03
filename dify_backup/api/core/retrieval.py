"""Silo-aware retrieval wrapper.

Wraps Dify's RetrievalService to add silo selection. Does NOT modify Dify core.

Flow:
    1. Resolve silo → dataset_id
    2. Delegate retrieval to Dify's RetrievalService
    3. Post-filter results by context_id if specified
    4. Return SiloRetrievalResult with structured output
"""

import logging
from dataclasses import dataclass, field
from typing import Any

from core.rag.datasource.retrieval_service import RetrievalService
from core.rag.retrieval.retrieval_methods import RetrievalMethod
from core.myownclone.silos import CloneSilo, filter_segments_by_context, get_dataset_id_for_silo

logger = logging.getLogger(__name__)


@dataclass
class SiloRetrievalResult:
    segments: list[Any] = field(default_factory=list)
    silo: CloneSilo = CloneSilo.TEACH
    context_id: str | None = None
    total_found: int = 0
    filtered_out: int = 0

    @property
    def found(self) -> bool:
        return self.total_found > 0

    @property
    def contents(self) -> list[str]:
        return [getattr(seg, "page_content", "") or getattr(seg, "content", "") for seg in self.segments]

    @property
    def scores(self) -> list[float]:
        return [
            (seg.metadata.get("score", 0.0) if hasattr(seg, "metadata") else 0.0)
            for seg in self.segments
        ]

    def to_context_string(self) -> str:
        parts: list[str] = []
        for i, (content, score) in enumerate(zip(self.contents, self.scores)):
            parts.append(f"[Fuente {i+1}] (relevancia: {score:.2f})\n{content}")
        return "\n\n---\n\n".join(parts)


def retrieve_from_silo(
    session: Any,
    tenant_id: str,
    clone_id: str,
    query: str,
    silo: CloneSilo,
    context_id: str | None = None,
    top_k: int = 5,
    score_threshold: float = 0.7,
    retrieval_method: RetrievalMethod = RetrievalMethod.SEMANTIC_SEARCH,
) -> SiloRetrievalResult:
    dataset_id = get_dataset_id_for_silo(session, tenant_id, clone_id, silo)

    if not dataset_id:
        logger.warning(
            "No dataset found for clone=%s silo=%s tenant=%s",
            clone_id,
            silo.value,
            tenant_id,
        )
        return SiloRetrievalResult(silo=silo, context_id=context_id)

    try:
        documents = RetrievalService.retrieve(
            retrieval_method=retrieval_method,
            dataset_id=dataset_id,
            query=query,
            top_k=top_k,
            score_threshold=score_threshold,
        )
    except Exception:
        logger.exception("Retrieval failed for dataset_id=%s", dataset_id)
        return SiloRetrievalResult(silo=silo, context_id=context_id)

    total = len(documents)
    filtered = 0

    if context_id and documents:
        segment_ids = [
            doc.metadata.get("segment_id", "")
            for doc in documents
            if hasattr(doc, "metadata")
        ]
        valid_ids = filter_segments_by_context(
            session,
            segment_ids,
            context_id,
            tenant_id,
        )
        valid_set = set(valid_ids)
        documents = [
            doc for doc in documents
            if getattr(doc, "metadata", {}).get("segment_id", "") in valid_set
        ]
        filtered = total - len(documents)

    return SiloRetrievalResult(
        segments=documents,
        silo=silo,
        context_id=context_id,
        total_found=len(documents),
        filtered_out=filtered,
    )
