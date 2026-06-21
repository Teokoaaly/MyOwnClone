"""EmbeddingService: produces text embeddings via the configured provider.

Resolves the active embedding model via ModelRegistry (task="embedding"),
uses the provider adapter to call embed(), and records cost via _record_llm_cost.
"""
from __future__ import annotations
import logging
import time
from typing import Optional

from api.core.cost_recording import _record_llm_cost
from api.core.model_manager import _select_provider, _calculate_cost_cents
from api.core.model_registry import get_registry
from api.core.retry_client import get_retry_client
from api.models.analytics import CostCategory


logger = logging.getLogger(__name__)


class EmbeddingService:
    """Embedding service backed by ModelRegistry + provider adapters.
    
    Usage:
        service = EmbeddingService()
        vectors = service.embed_texts("tenant-1", ["hello", "world"])
    
    Or for batch operations with cost tracking per item:
        service.embed_texts("tenant-1", ["a", "b", "c"], batch_size=10)
    """
    
    DEFAULT_BATCH_SIZE = 100
    
    def __init__(self, batch_size: int = DEFAULT_BATCH_SIZE):
        self.batch_size = batch_size
    
    def embed_texts(
        self,
        tenant_id: str,
        texts: list[str],
        *,
        batch_size: Optional[int] = None,
    ) -> list[list[float]]:
        """Embed a list of texts.
        
        Returns a list of vectors (one per input text), in the same order.
        Cost is recorded per call to _record_llm_cost (single row for the batch).
        """
        if not texts:
            return []
        
        batch_size = batch_size or self.batch_size
        registry = get_registry()
        retry_client = get_retry_client()
        
        # Resolve embedding model
        model = registry.get_model_for_task(tenant_id, "embedding")
        if model is None:
            raise RuntimeError(
                f"No embedding model configured for tenant={tenant_id!r}. "
                f"Configure one via /admin/ia-modelos or run `flask ai-backfill-from-env`."
            )
        
        # Resolve API key
        api_key = (model.config or {}).get("api_key", "")
        if not api_key:
            import os
            api_key = os.environ.get(f"{model.provider.upper()}_API_KEY", "")
        
        adapter = _select_provider(model, api_key)
        breaker_key = f"{model.provider}/{model.name}"
        
        all_vectors: list[list[float]] = []
        total_tokens_in = 0
        start = time.monotonic()
        success = False
        error_message: Optional[str] = None
        
        try:
            # Process in batches
            for i in range(0, len(texts), batch_size):
                batch = texts[i : i + batch_size]
                
                def _do_embed() -> list[list[float]]:
                    return adapter.embed(model.name, batch)
                
                vectors = retry_client.call(_do_embed, key=breaker_key)
                all_vectors.extend(vectors)
                # Estimate tokens_in as ~4 chars per token (rough)
                total_tokens_in += sum(max(1, len(t) // 4) for t in batch)
            
            success = True
            return all_vectors
        except Exception as exc:
            error_message = str(exc)[:500]
            raise
      ***REMOVED***nally:
            latency_ms = int((time.monotonic() - start) * 1000)
            cost_cents = _calculate_cost_cents(
                tokens_in=total_tokens_in,
                tokens_out=0,  # embeddings have no output tokens
                cost_per_1k_input_cents=getattr(model, "input_cost_per_1k", None),
                cost_per_1k_output_cents=None,
            )
            try:
                _record_llm_cost(
                    tenant_id=tenant_id,
                    category=CostCategory.CONTENT_INGESTION,
                    operation="embed_texts",
                    model=model.name,
                    tokens_in=total_tokens_in,
                    tokens_out=0,
                    cost_cents=cost_cents,
                    latency_ms=latency_ms,
                    success=success,
                    error_message=error_message,
                )
            except Exception as cost_exc:
                logger.warning("Failed to record embedding cost: %s", cost_exc)
    
    def embed_query(
        self,
        tenant_id: str,
        text: str,
    ) -> list[float]:
        """Convenience: embed a single text, return a single vector."""
        vectors = self.embed_texts(tenant_id, [text])
        return vectors[0] if vectors else []
    
    # ─── Backward-compatibility fallback ─────────────────────────────────────
    
    DIMENSION = 1536
    
    @staticmethod
    def _hash_to_vector(text: str) -> list[float]:
        """Deterministic hash-based vector (used when no model is configured)."""
        import hashlib
        h = hashlib.sha256(text.encode()).digest()
        return [
            (b / 255.0) - 0.5
            for b in (h * 60)[:EmbeddingService.DIMENSION]
        ]


class FallbackEmbeddingService:
    """Test-only embedding service that returns deterministic hash-based vectors.
    
    Use this when no provider is configured (e.g., test environments).
    """
    DIMENSION = 1536
    
    def embed_texts(self, tenant_id, texts, **kwargs):
        return [self._hash_to_vector(t) for t in texts]
    
    def embed_query(self, tenant_id, text):
        return self._hash_to_vector(text)
    
    @staticmethod
    def _hash_to_vector(text: str) -> list[float]:
        import hashlib
        h = hashlib.sha256(text.encode()).digest()
        return [
            (b / 255.0) - 0.5
            for b in (h * 60)[:FallbackEmbeddingService.DIMENSION]
        ]