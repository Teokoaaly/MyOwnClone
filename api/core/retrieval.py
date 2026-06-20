"""Silo-aware retrieval wrapper (standard RAG pipeline).

Two retrieval modes, selected by the active EmbeddingService provider:

  - **semantic (default when OPENAI_API_KEY is set)**: uses pgvector cosine
    distance (`embedding <=> query_vector`) over the ivfflat index, blended
    with a light lexical boost for exact-keyword matches (hybrid retrieval).
  - **lexical fallback**: pure FNV-1a hashed vectors compared with cosine
    of the hashed vectors (the legacy `local_hybrid_v1` behaviour).

Flow:
    1. Embed the query via EmbeddingService (OpenAI or lexical).
    2. Filter chunks by clone + silo + context_id.
    3. Rank by cosine similarity, optionally boosted by lexical term overlap.
    4. Apply score_threshold and return top_k.

The local chunks table is the only live knowledge source. The legacy
Dataset/DocumentSegment path (Weaviate stub) is preserved as a no-op
fallback and documented as dormant in MANUAL_TECNICO.md.
"""

import logging
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import select, text

from api.core.embeddings import EmbeddingService, EMBEDDING_DIMENSIONS, _lexical_embedding, _lexical_score, _terms
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


@dataclass
class LexicalSegment:
    content: str
    metadata: dict[str, Any]


def _is_pgvector_available(session: Any) -> bool:
    """Detect whether the chunks.embedding column supports the `<=>` operator.

    Returns False on SQLite (tests) or if pgvector isn't installed, so the
    retrieval falls back to the in-Python lexical path instead of crashing.
    """
    try:
        session.execute(text("SELECT 1 WHERE '[1,2]'::vector IS NOT NULL"))
        return True
    except Exception:
        return False


def _retrieve_semantic(
    session: Any,
    clone_id: str,
    query: str,
    query_embedding: list[float],
    silo: CloneSilo,
    context_id: str | None,
    top_k: int,
    score_threshold: float,
) -> SiloRetrievalResult:
    """Rank chunks by pgvector cosine distance + lexical boost.

    `score = max(cosine_sim, 0.7*cosine_sim + 0.3*term_score)`
    The max keeps pure-semantic hits strong while rewarding keyword overlap.
    """
    query_terms = _terms(query)
    # pgvector cosine distance in [0,2]; similarity = 1 - distance.
    distance_expr = Chunk.embedding.cosine_distance(query_embedding)
    similarity_expr = 1.0 - distance_expr

    try:
        rows = session.execute(
            select(Chunk, Source, similarity_expr.label("similarity"))
            .join(Source, Source.id == Chunk.source_id)
            .where(
                Source.clone_id == clone_id,
                Source.status == "ready",
                Chunk.embedding.isnot(None),
            )
            .order_by(distance_expr)
            .limit(top_k * 4)  # over-fetch, then re-rank with lexical boost
        ).all()
    except Exception:
        logger.exception(
            "Semantic retrieval failed for clone=%s silo=%s; falling back",
            clone_id, silo.value,
        )
        return SiloRetrievalResult(silo=silo, context_id=context_id)

    scored: list[LexicalSegment] = []
    for chunk, source, similarity in rows:
        source_meta = source.source_metadata or {}
        chunk_meta = chunk.chunk_metadata or {}
        if source_meta.get("silo", "teach") != silo.value:
            continue
        if context_id and chunk_meta.get("context_id") != context_id:
            continue

        vector_score = float(similarity) if similarity is not None else 0.0
        term_score = _lexical_score(query_terms, chunk.content or "")
        # Hybrid: keep semantic dominant; let keywords break near-ties upward.
        score = max(vector_score, 0.7 * vector_score + 0.3 * term_score)
        if score < score_threshold:
            continue

        scored.append(
            LexicalSegment(
                content=chunk.content,
                metadata={
                    "score": round(score, 4),
                    "segment_id": chunk.id,
                    "source_id": source.id,
                    "source_title": source.title,
                    "retrieval": "pgvector_hybrid_v2",
                    "vector_score": round(vector_score, 4),
                    "term_score": round(term_score, 4),
                },
            )
        )

    scored.sort(key=lambda s: s.metadata.get("score", 0.0), reverse=True)
    segments = scored[:top_k]
    return SiloRetrievalResult(
        segments=segments,
        silo=silo,
        context_id=context_id,
        total_found=len(segments),
    )


def _retrieve_from_local_chunks(
    session: Any,
    clone_id: str,
    query: str,
    silo: CloneSilo,
    context_id: str | None,
    top_k: int,
    score_threshold: float,
) -> SiloRetrievalResult:
    """Lexical fallback (legacy local_hybrid_v1) for when pgvector/OpenAI is off."""
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
    for chunk, source in rows:
        source_meta = source.source_metadata or {}
        chunk_meta = chunk.chunk_metadata or {}
        if source_meta.get("silo", "teach") != silo.value:
            continue
        if context_id and chunk_meta.get("context_id") != context_id:
            continue

        term_score = _lexical_score(query_terms, chunk.content)
        stored = getattr(chunk, "embedding", None)
        # Cosine against a stored vector of any kind (lexical or real).
        vector_score = _cosine_similarity_legacy(query_embedding, stored)
        score = max(term_score, vector_score)
        if score < score_threshold:
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

    scored.sort(key=lambda segment: segment.metadata.get("score", 0.0), reverse=True)
    segments = scored[:top_k]
    return SiloRetrievalResult(
        segments=segments,
        silo=silo,
        context_id=context_id,
        total_found=len(segments),
    )


def _cosine_similarity_legacy(left: list[float], right: list[float] | None) -> float:
    """In-Python cosine similarity for the lexical fallback path."""
    if not left or not right:
        return 0.0
    size = min(len(left), len(right))
    if size == 0:
        return 0.0
    return max(0.0, sum(left[i] * float(right[i]) for i in range(size)))


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
    """Retrieve the top_k most relevant chunks for a query within a silo.

    Tries semantic retrieval (pgvector + OpenAI embeddings) first, then
    falls back to lexical retrieval (legacy hashed vectors).
    """
    embed_service = EmbeddingService(tenant_id=tenant_id)

    # Semantic path: only when (a) OpenAI/lexical service produced a vector
    # and (b) the DB supports the pgvector <=> operator.
    if embed_service.provider == "openai" and _is_pgvector_available(session):
        query_embedding = embed_service.embed_query(query)
        # Real embeddings need a lower threshold: cosine similarity ~0.25+
        # is already a meaningful match, unlike the inflated hash scores.
        semantic_threshold = min(score_threshold, 0.25)
        result = _retrieve_semantic(
            session=session,
            clone_id=clone_id,
            query=query,
            query_embedding=query_embedding,
            silo=silo,
            context_id=context_id,
            top_k=top_k,
            score_threshold=semantic_threshold,
        )
        if result.found:
            return result
        # If semantic found nothing, try lexical before giving up — a user
        # may have an old clone whose chunks were embedded lexically.
        logger.info(
            "Semantic retrieval empty for clone=%s silo=%s; trying lexical",
            clone_id, silo.value,
        )

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

    # Legacy Dataset/DocumentSegment path (currently stubs, returns nothing).
    dataset_id = get_dataset_id_for_silo(session, tenant_id, clone_id, silo)
    if not dataset_id:
        logger.warning(
            "No dataset found for clone=%s silo=%s tenant=%s",
            clone_id, silo.value, tenant_id,
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
        valid_ids = filter_segments_by_context(session, segment_ids, context_id, tenant_id)
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
