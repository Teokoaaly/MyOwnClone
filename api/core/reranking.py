"""RerankingService — Cohere reranking with cost tracking.

Uses the Cohere adapter from api.core.providers.cohere_adapter.
Reads RERANKING_ENABLED env var to enable/disable.
Records cost via _record_llm_cost.
"""
from __future__ import annotations

import os
import logging
from dataclasses import dataclass
from typing import Protocol

from api.core.providers.cohere_adapter import CohereAdapter

logger = logging.getLogger(__name__)


def _reranking_enabled() -> bool:
    """Check if reranking is enabled via env var."""
    return os.environ.get("RERANKING_ENABLED", "").strip().lower() in ("1", "true", "yes")


@dataclass
class RerankResult:
    """A single reranked document result."""
    index: int
    score: float


class RerankingService:
    """Cohere reranking service.

    Usage:
        service = RerankingService()
        results = service.rerank("query", ["doc1", "doc2", "doc3"], top_n=3)
        # results = [RerankResult(index=2, score=0.95), ...]
    """

    DEFAULT_MODEL = "rerank-english-v3.0"

    def __init__(self, api_key: str | None = None):
        """Initialize with optional API key override."""
        self._api_key = api_key
        self._adapter: CohereAdapter | None = None

    def _get_adapter(self) -> CohereAdapter:
        """Lazily create the Cohere adapter."""
        if self._adapter is None:
            key = self._api_key or os.environ.get("COHERE_API_KEY", "")
            if not key:
                raise RuntimeError(
                    "Cohere API key not configured. Set COHERE_API_KEY environment variable."
                )
            self._adapter = CohereAdapter(api_key=key)
        return self._adapter

    def rerank(
        self,
        query: str,
        documents: list[str],
        top_n: int = 3,
        model: str = DEFAULT_MODEL,
        tenant_id: str | None = None,
    ) -> list[RerankResult]:
        """Rerank documents using Cohere rerank-v3.0.

        Args:
            query: The search query.
            documents: List of document texts to rerank.
            top_n: Number of top results to return.
            model: Cohere rerank model to use.
            tenant_id: Optional tenant ID for cost tracking.

        Returns:
            List of RerankResult sorted by score descending.

        Raises:
            RuntimeError: If COHERE_API_KEY is not set and reranking is attempted.
        """
        if not _reranking_enabled():
            logger.debug("Reranking disabled via RERANKING_ENABLED, skipping")
            # Return documents in original order with placeholder scores
            return [
                RerankResult(index=i, score=1.0 / (i + 1))
                for i in range(min(top_n, len(documents)))
            ]

        if not documents:
            return []

        adapter = self._get_adapter()

        try:
            raw_results = adapter.rerank(model, query, documents, top_n=top_n)
            results = [
                RerankResult(index=r["index"], score=r["score"])
                for r in raw_results
            ]
            # Sort by score descending
            results.sort(key=lambda x: x.score, reverse=True)
            return results[:top_n]
      ***REMOVED***nally:
            # Record cost
            self._record_cost(tenant_id=tenant_id, model=model, num_documents=len(documents))

    def _record_cost(
        self,
        tenant_id: str | None,
        model: str,
        num_documents: int,
    ) -> None:
        """Record reranking cost via _record_llm_cost.

        Cohere charges per query + per document. Approximate cost:
        $0.001 per query + $0.00005 per document (as of 2024).
        """
        try:
            from api.core.cost_recording import _record_llm_cost
            from api.models.analytics import CostCategory

            # Approximate cost in cents: $0.001/query = 0.1 cents, $0.00005/doc = 0.005 cents
            cost_cents = max(1, int(0.1 + 0.005 * num_documents))

            _record_llm_cost(
                tenant_id=tenant_id or "platform",
                category=CostCategory.RERANKING,
                operation="rerank",
                model=model,
                tokens_in=num_documents,  # documents as "tokens" proxy
                tokens_out=0,
                cost_cents=cost_cents,
                latency_ms=0,  # Not measured here
                success=True,
                error_message=None,
            )
        except Exception as exc:
            logger.warning("Failed to record reranking cost: %s", exc)


# ─── Singleton instance ─────────────────────────────────────────────────────────

_reranking_service: RerankingService | None = None


def get_reranking_service() -> RerankingService:
    """Get the process-wide RerankingService singleton."""
    global _reranking_service
    if _reranking_service is None:
        _reranking_service = RerankingService()
    return _reranking_service
