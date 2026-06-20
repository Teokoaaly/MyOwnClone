"""Embedding service for MyOwnClone RAG.

Single source of truth for converting text into vectors.

Provider selection (in priority order, controlled by EMBEDDING_PROVIDER):
  - "openai"   → OpenAI text-embedding-3-small (1536 dims, semantic).
                 Falls back to "lexical" if OPENAI_API_KEY is missing.
  - "lexical"  → Local FNV-1a hash embedding (1536 dims, keyword-based).
                 Zero-cost, offline, but NOT semantic.

Both providers return 1536-dim vectors so the `chunks.embedding vector(1536)`
column and the ivfflat index work regardless of provider.

Why a fallback:
  - In development without an OpenAI key, the pipeline must still work.
  - If OpenAI is down or quota-exhausted, retrieval degrades gracefully
    to keyword matching instead of failing every chat.

Cost tracking:
  - OpenAI calls record token usage to the cost_tracking table
    (category = content_ingestion), so admins can see embedding spend.
  - Lexical calls are free and not tracked.

Usage:
    from api.core.embeddings import EmbeddingService
    svc = EmbeddingService()
    vectors = svc.embed_texts(["hello", "world"])
    single = svc.embed_query("how much does it cost?")
"""

from __future__ import annotations

import logging
import math
import os
import re
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)


# Dimensiones fijas: coinciden con el esquema `chunks.embedding vector(1536)`
# y con text-embedding-3-small de OpenAI. NO cambiar sin migrar la columna.
EMBEDDING_DIMENSIONS = 1536

# OpenAI accepts up to 2048 input strings per embeddings request.
_OPENAI_BATCH_SIZE = 512  # conservador para no chocar con límite de tokens por request

# Lista de stopwords compartida con el path léxico (retrieval.py).
_STOPWORDS = {
    "a", "al", "algo", "ante", "como", "con", "de", "del", "el", "en", "es",
    "esta", "este", "esto", "la", "las", "lo", "los", "me", "mi", "para",
    "por", "que", "se", "si", "sobre", "su", "sus", "the", "to", "and",
    "or", "of", "in", "is", "it", "for", "from", "about",
}


@dataclass
class EmbeddingResult:
    """Outcome of an embed_texts call."""
    vectors: list[list[float]]
    provider: str  # "openai" | "lexical"
    tokens_used: int = 0  # solo > 0 para openai
    model: str = ""


def _terms(text: str) -> set[str]:
    return {
        term
        for term in re.findall(r"[\wáéíóúüñÁÉÍÓÚÜÑ]{3,}", text.lower())
        if term not in _STOPWORDS
    }


def _hash_term(term: str) -> int:
    """FNV-1a 32-bit hash. Idéntico al del path léxico original para que los
    vectores léxicos viejos sigan siendo compatibles."""
    value = 2166136261
    for char in term:
        value ^= ord(char)
        value = (value * 16777619) & 0xFFFFFFFF
    return value


def _lexical_embedding(text: str) -> list[float]:
    """Produce a 1536-dim hashed lexical vector (L2-normalized).

    Mismo algoritmo que api/core/retrieval.py:_lexical_embedding y que
    MyOwnClone/src/app/api/clone/sources/route.ts:lexicalEmbedding.
    Se mantiene aquí como la implementación canónica del fallback.
    """
    vector = [0.0] * EMBEDDING_DIMENSIONS
    for term in _terms(text):
        hashed = _hash_term(term)
        index = hashed % EMBEDDING_DIMENSIONS
        sign = 1.0 if hashed % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(v * v for v in vector))
    if norm == 0:
        return vector
    return [v / norm for v in vector]


def _lexical_score(query_terms: set[str], content: str) -> float:
    """Heuristic keyword-overlap score in [0, 1] for the lexical fallback.

    Combines coverage (fraction of query terms present) and density
    (overlap relative to content length). Mirrors the legacy behaviour
    that previously lived in retrieval.py.
    """
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


class EmbeddingService:
    """Embed text into 1536-dim vectors using OpenAI or a local lexical fallback."""

    def __init__(self, *, tenant_id: str | None = None) -> None:
        self.tenant_id = tenant_id
        self._provider = self._resolve_provider()
        self._model = self._resolve_model()

    # ── Public API ───────────────────────────────────────────────────────────

    def embed_texts(self, texts: list[str]) -> EmbeddingResult:
        """Embed a batch of non-empty texts.

        Empty strings are embedded as zero vectors to keep index alignment.
        """
        if not texts:
            return EmbeddingResult(vectors=[], provider=self._provider)

        if self._provider == "openai":
            try:
                return self._embed_openai(texts)
            except Exception:
                # Graceful degradation: log and fall back to lexical so a
                # transient OpenAI outage doesn't break ingestion/chat.
                logger.exception(
                    "OpenAI embedding failed; falling back to lexical provider"
                )
                return self._embed_lexical(texts)
        return self._embed_lexical(texts)

    def embed_query(self, query: str) -> list[float]:
        """Embed a single search query. Returns the raw vector."""
        result = self.embed_texts([query])
        return result.vectors[0] if result.vectors else [0.0] * EMBEDDING_DIMENSIONS

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def model(self) -> str:
        return self._model

    # ── Provider resolution ──────────────────────────────────────────────────

    @staticmethod
    def _resolve_provider() -> str:
        configured = os.getenv("EMBEDDING_PROVIDER", "").strip().lower()
        if configured in ("openai", "lexical"):
            # Honor explicit choice, but require the key for openai.
            if configured == "openai" and not os.getenv("OPENAI_API_KEY"):
                logger.warning(
                    "EMBEDDING_PROVIDER=openai but OPENAI_API_KEY is unset; "
                    "using lexical fallback"
                )
                return "lexical"
            return configured
        # Auto: use openai if a key exists, else lexical.
        return "openai" if os.getenv("OPENAI_API_KEY") else "lexical"

    @staticmethod
    def _resolve_model() -> str:
        if EmbeddingService._resolve_provider() == "openai":
            return os.getenv("EMBEDDING_MODEL", "text-embedding-3-small").strip()
        return "local-lexical-v1"

    # ── OpenAI backend ───────────────────────────────────────────────────────

    def _embed_openai(self, texts: list[str]) -> EmbeddingResult:
        try:
            import openai
        except ImportError as exc:
            raise RuntimeError("openai package not installed") from exc

        client_kwargs: dict[str, str] = {"api_key": os.environ["OPENAI_API_KEY"]}
        base_url = (
            os.getenv("OPENAI_BASE_URL", "").strip()
            or os.getenv("OPENAI_API_BASE", "").strip()
            or None
        )
        if base_url:
            client_kwargs["base_url"] = base_url
        client = openai.OpenAI(**client_kwargs)

        all_vectors: list[list[float]] = []
        total_tokens = 0

        # OpenAI rejects empty strings; replace them with a placeholder and
        # zero out the result vector afterwards to preserve index alignment.
        sanitized = [t if t.strip() else "empty" for t in texts]
        empty_flags = [not t.strip() for t in texts]

        for start in range(0, len(sanitized), _OPENAI_BATCH_SIZE):
            batch = sanitized[start:start + _OPENAI_BATCH_SIZE]
            response = client.embeddings.create(
                model=self._model,
                input=batch,
            )
            batch_vectors = [list(d.embedding) for d in response.data]
            if response.usage:
                total_tokens += response.usage.total_tokens
            all_vectors.extend(batch_vectors)

        for i, is_empty in enumerate(empty_flags):
            if is_empty:
                all_vectors[i] = [0.0] * EMBEDDING_DIMENSIONS

        # Defensive: if the provider returned a different dim, pad/truncate.
        all_vectors = [EmbeddingService._fit_dim(v) for v in all_vectors]

        self._record_cost(total_tokens)

        return EmbeddingResult(
            vectors=all_vectors,
            provider="openai",
            tokens_used=total_tokens,
            model=self._model,
        )

    # ── Lexical backend ──────────────────────────────────────────────────────

    def _embed_lexical(self, texts: list[str]) -> EmbeddingResult:
        vectors = [_lexical_embedding(t) for t in texts]
        return EmbeddingResult(
            vectors=vectors,
            provider="lexical",
            tokens_used=0,
            model="local-lexical-v1",
        )

    # ── Helpers ──────────────────────────────────────────────────────────────

    @staticmethod
    def _fit_dim(vector: list[float]) -> list[float]:
        """Force a vector to exactly EMBEDDING_DIMENSIONS."""
        if len(vector) == EMBEDDING_DIMENSIONS:
            return vector
        if len(vector) < EMBEDDING_DIMENSIONS:
            return vector + [0.0] * (EMBEDDING_DIMENSIONS - len(vector))
        return vector[:EMBEDDING_DIMENSIONS]

    def _record_cost(self, tokens: int) -> None:
        """Persist embedding token usage to cost_tracking.

        Best-effort: failures here (e.g. outside an app context) must not
        abort the embedding call. The pricing lookup lives in
        api.core.pricing to avoid a circular import.
        """
        if not tokens or not self.tenant_id:
            return
        try:
            from api.extensions.ext_database import db
            from api.models.analytics import CostCategory, CostTracking
            from api.core.pricing import estimate_embedding_cost_cents

            cost_cents = estimate_embedding_cost_cents(
                model=self._model, tokens=tokens
            )
            db.session.add(
                CostTracking(
                    tenant_id=self.tenant_id,
                    category=CostCategory.CONTENT_INGESTION.value
                    if hasattr(CostCategory.CONTENT_INGESTION, "value")
                    else "content_ingestion",
                    operation="embed_texts",
                    model=self._model,
                    tokens_in=tokens,
                    tokens_out=0,
                    cost_cents=cost_cents,
                )
            )
            db.session.commit()
        except Exception:
            # Cost tracking is observability; never fatal to the embedding.
            logger.debug("Could not persist embedding cost", exc_info=True)


def get_embedding_service(*, tenant_id: str | None = None) -> EmbeddingService:
    """Factory used by callers that don't want to import the class directly."""
    return EmbeddingService(tenant_id=tenant_id)
