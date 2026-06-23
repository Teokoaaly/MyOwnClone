"""Silo-aware retrieval wrapper.

Retrieval service for MyOwnClone that adds silo selection to the base retrieval service.

Flow:
    1. Resolve silo → dataset_id
    2. Delegate retrieval to the underlying retrieval service
    3. Post-filter results by context_id if specified
    4. Return SiloRetrievalResult with structured output
"""

import logging
import math
import re
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import select

from api.core.rag.datasource.retrieval_service import RetrievalService
from api.core.rag.retrieval.retrieval_methods import RetrievalMethod
from api.core.myownclone.silos import CloneSilo, filter_segments_by_context, get_dataset_id_for_silo
from api.models.knowledge import Chunk, Source

logger = logging.getLogger(__name__)


@dataclass
class SiloRetrievalResult:
    segments: list[Any] = field(default_factory=list)
    silo: CloneSilo = CloneSilo.TEACH
    context_id: str | None = None
    total_found: int = 0
  ***REMOVED***ltered_out: int = 0

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


@dataclass
class LexicalSegment:
    content: str
    metadata: dict[str, Any]


_STOPWORDS = {
    "a", "al", "algo", "ante", "como", "con", "de", "del", "el", "en", "es",
    "esta", "este", "esto", "la", "las", "lo", "los", "me", "mi", "para",
    "por", "que", "se", "si", "sobre", "su", "sus", "the", "to", "and",
    "or", "of", "in", "is", "it", "for", "from", "about",
}

_EMBEDDING_DIMENSIONS = 1536


def _terms(text: str) -> set[str]:
    return {
        term
        for term in re.findall(r"[\wáéíóúüñÁÉÍÓÚÜÑ]{3,}", text.lower())
        if term not in _STOPWORDS
    }


def _hash_term(term: str) -> int:
    value = 2166136261
    for char in term:
        value ^= ord(char)
        value = (value * 16777619) & 0xFFFFFFFF
    return value


def _lexical_embedding(text: str) -> list[float]:
    vector = [0.0] * _EMBEDDING_DIMENSIONS
    for term in _terms(text):
        hashed = _hash_term(term)
        index = hashed % _EMBEDDING_DIMENSIONS
        sign = 1.0 if hashed % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]


def _cosine_similarity(left: list[float], right: list[float] | None) -> float:
    if not left or not right:
        return 0.0
    size = min(len(left), len(right))
    if size == 0:
        return 0.0
    return max(0.0, sum(left[i] * float(right[i]) for i in range(size)))


def _lexical_score(query_terms: set[str], content: str) -> float:
    if not query_terms:
        return 0.0
    content_terms = _terms(content)
    if not content_terms:
        return 0.0

    overlap = query_terms.intersection(content_terms)
    if not overlap:
        return 0.0

    coverage = len(overlap) / len(query_terms)
    density = len(overlap) / max(len(content_terms), 1)
    return min(1.0, 0.25 + coverage * 0.65 + density * 0.1)


def _retrieve_from_local_chunks(
    session: Any,
    clone_id: str,
    query: str,
    silo: CloneSilo,
    context_id: str | None,
    top_k: int,
    score_threshold: float,
) -> SiloRetrievalResult:
    query_terms = _terms(query)
    if not query_terms:
        return SiloRetrievalResult(silo=silo, context_id=context_id)
    query_embedding = _lexical_embedding(query)

    try:
        rows = session.execute(
            select(Chunk, Source)
            .join(Source, Source.id == Chunk.source_id)
            .where(
                Source.clone_id == clone_id,
                Source.status == "ready",
            )
        ).all()
    except Exception:
        logger.exception("Local chunk retrieval failed for clone=%s silo=%s", clone_id, silo.value)
        return SiloRetrievalResult(silo=silo, context_id=context_id)

    scored: list[LexicalSegment] = []
    scanned = 0
    min_score = score_threshold
    for chunk, source in rows:
        source_meta = source.source_metadata or {}
        chunk_meta = chunk.chunk_metadata or {}
        if source_meta.get("silo", "teach") != silo.value:
            continue
        if context_id and chunk_meta.get("context_id") != context_id:
            continue

        # Defect #6: count chunks that passed silo/context filtering and were
        # actually scored, so we can emit a diagnostic when content existed but
        # nothing cleared the relevance bar.
        scanned += 1
        term_score = _lexical_score(query_terms, chunk.content)
        vector_score = _cosine_similarity(query_embedding, getattr(chunk, "embedding", None))
        score = max(term_score, vector_score)
        if score < min_score:
            continue

        scored.append(
            LexicalSegment(
                content=chunk.content,
                metadata={
                    "score": score,
                    "segment_id": chunk.id,
                    "source_id": source.id,
                    "source_title": source.title,
                    "retrieval": "local_hybrid_v1",
                    "term_score": term_score,
                    "vector_score": vector_score,
                },
            )
        )

    if scanned and not scored:
        logger.info(
            "Retrieval below threshold: clone=%s silo=%s threshold=%.2f scanned=%d query_terms=%s",
            clone_id,
            silo.value,
            score_threshold,
            scanned,
            sorted(query_terms),
        )

    scored.sort(key=lambda segment: segment.metadata.get("score", 0.0), reverse=True)
    segments = scored[:top_k]
    return SiloRetrievalResult(
        segments=segments,
        silo=silo,
        context_id=context_id,
        total_found=len(segments),
    )


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
    local_result = _retrieve_from_local_chunks(
        session=session,
        clone_id=clone_id,
        query=query,
        silo=silo,
        context_id=context_id,
        top_k=top_k,
        score_threshold=score_threshold,
    )
    if local_result.found:
        return local_result

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
  ***REMOVED***ltered = 0

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
      ***REMOVED***ltered = total - len(documents)

    return SiloRetrievalResult(
        segments=documents,
        silo=silo,
        context_id=context_id,
        total_found=len(documents),
      ***REMOVED***ltered_out=filtered,
    )
