"""Retrieval: semantic search via Weaviate + tenant filtering.

Two modes:
1. retrieve_from_silo: search Weaviate by query embedding, filter by tenant
2. retrieve_from_silo_with_rerank: search + Cohere rerank (M14)
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

from api.core.embeddings import EmbeddingService
from api.core.token_budget import DimensionGuard
from api.extensions import db


logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    found: bool
    contents: list[str] = field(default_factory=list)
    scores: list[float] = field(default_factory=list)
    chunk_ids: list[str] = field(default_factory=list)
    metadata_list: list[dict] = field(default_factory=list)


def retrieve_from_silo(
    tenant_id: str,
    query: str,
    *,
    top_k: int = 5,
    weaviate_client=None,
    weaviate_class: str = "Chunk",
    embedding_service: Optional[EmbeddingService] = None,
    expected_embedding_dim: int = 1536,
) -> RetrievalResult:
    """Semantic search via Weaviate, filtered by tenant_id.

    Args:
        tenant_id: tenant to scope the search to
        query: search query text
        top_k: number of results to return
        weaviate_client: Weaviate client (injected for testing; if None, falls back to mock)
        weaviate_class: Weaviate class to query (default "Chunk")
        embedding_service: EmbeddingService to embed the query (default: new instance)
        expected_embedding_dim: dimension to validate against the store

    Returns RetrievalResult with up to top_k results, sorted by score desc.
    """
    if not query or not query.strip():
        return RetrievalResult(found=False)

    embedding_service = embedding_service or EmbeddingService()

    # Validate dimensions (skip if no client)
    if weaviate_client is not None:
        try:
            guard = DimensionGuard(expected_dim=expected_embedding_dim)
            guard.check_weaviate(weaviate_client, weaviate_class)
        except Exception as exc:
            logger.warning("Dimension guard failed: %s (continuing)", exc)

    # Embed the query
    try:
        query_vectors = embedding_service.embed_texts(tenant_id, [query])
        if not query_vectors:
            return RetrievalResult(found=False)
        query_vector = query_vectors[0]
    except Exception as exc:
        logger.error("Failed to embed query: %s", exc)
        return RetrievalResult(found=False)

    # Real Weaviate search
    if weaviate_client is not None:
        try:
            from weaviate.classes.query import MetadataQuery

            collection = weaviate_client.collections.get(weaviate_class)

            # Build tenant filter
            try:
                from weaviate.classes.filters import Filter

                tenant_filter = Filter.by_property("tenant_id").equal(tenant_id)
            except ImportError:
                # Older weaviate-client versions may use different filter API
                tenant_filter = None

            response = collection.query.near_vector(
                near_vector=query_vector,
                limit=top_k,
                return_metadata=MetadataQuery(distance=True),
                filters=tenant_filter,
            )

            # Parse response
            contents = []
            scores = []
            chunk_ids = []
            metadata_list = []
            for obj in response.objects:
                contents.append(obj.properties.get("text", ""))
                scores.append(1.0 - obj.metadata.distance)  # convert distance to similarity
                chunk_ids.append(str(obj.uuid))
                metadata_list.append(dict(obj.properties))

            return RetrievalResult(
                found=len(contents) > 0,
                contents=contents,
                scores=scores,
                chunk_ids=chunk_ids,
                metadata_list=metadata_list,
            )
        except Exception as exc:
            logger.error("Weaviate search failed: %s", exc)
            return RetrievalResult(found=False)

    # No Weaviate client — return empty (caller can decide to fall back)
    logger.debug("No Weaviate client available; returning empty RetrievalResult")
    return RetrievalResult(found=False)