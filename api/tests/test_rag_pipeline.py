"""Tests for the standard RAG pipeline (FASE 1-3).

Pure unit tests that don't need a real database or OpenAI connection:
  - chunking: text splitting behavior
  - pricing: cost estimation math
  - embeddings: lexical fallback, provider resolution, dim fitting
  - model_manager: GenerationParams parsing, provider detection
"""

import math

import pytest

from api.core import chunking, pricing
from api.core.embeddings import (
    EmbeddingService,
    EmbeddingResult,
    EMBEDDING_DIMENSIONS,
    _hash_term,
    _lexical_embedding,
    _lexical_score,
    _terms,
)
from api.core.model_manager import GenerationParams, _detect_provider


# ── Chunking ────────────────────────────────────────────────────────────────


class TestChunking:
    def test_empty_text_returns_empty_list(self):
        assert chunking.chunk_text("") == []
        assert chunking.chunk_text("   \n\n  ") == []

    def test_short_text_returns_single_chunk(self):
        result = chunking.chunk_text("Hola mundo.")
        assert len(result) == 1
        assert "Hola mundo" in result[0]

    def test_respects_chunk_size_upper_bound(self):
        text = "palabra " * 5000  # ~35k chars
        chunks = chunking.chunk_text(text, chunk_size=1000, overlap=100)
        assert len(chunks) > 1
        for c in chunks:
            # Each chunk can slightly exceed chunk_size if it snaps to a
            # sentence boundary just past the limit, but never by much.
            assert len(c) <= 1200

    def test_overlap_keeps_context_between_chunks(self):
        text = "Frase uno. Frase dos. Frase tres. Frase cuatro. Frase cinco."
        chunks = chunking.chunk_text(text, chunk_size=30, overlap=10)
        # At least one pair of consecutive chunks should share some text
        # (the overlap window).
        if len(chunks) >= 2:
            shared = any(
                word in chunks[i + 1]
                for i in range(len(chunks) - 1)
                for word in chunks[i].split()
            )
            assert shared, "consecutive chunks should overlap"

    def test_count_words(self):
        assert chunking.count_words("uno dos tres") == 3
        assert chunking.count_words("") == 0
        assert chunking.count_words("   ") == 0


# ── Pricing ─────────────────────────────────────────────────────────────────


class TestPricing:
    def test_llm_cost_known_model(self):
        # gpt-4o-mini: 150 in / 600 out per 1M tokens
        cost = pricing.estimate_llm_cost_cents(
            model="gpt-4o-mini", tokens_in=1_000_000, tokens_out=0
        )
        assert cost == 150

    def test_llm_cost_output_tokens(self):
        cost = pricing.estimate_llm_cost_cents(
            model="gpt-4o-mini", tokens_in=0, tokens_out=1_000_000
        )
        assert cost == 600

    def test_llm_cost_unknown_model_uses_fallback(self):
        cost = pricing.estimate_llm_cost_cents(
            model="some-future-model", tokens_in=1_000_000, tokens_out=0
        )
        # Fallback entry is ("", 200, 600)
        assert cost == 200

    def test_llm_cost_case_insensitive_match(self):
        cost = pricing.estimate_llm_cost_cents(
            model="GPT-4O-MINI", tokens_in=1_000_000, tokens_out=0
        )
        assert cost == 150

    def test_llm_cost_zero_tokens(self):
        assert pricing.estimate_llm_cost_cents(
            model="gpt-4o-mini", tokens_in=0, tokens_out=0
        ) == 0

    def test_embedding_cost_small_model(self):
        # text-embedding-3-small: 20 cents per 1M tokens
        cost = pricing.estimate_embedding_cost_cents(
            model="text-embedding-3-small", tokens=1_000_000
        )
        assert cost == 20

    def test_embedding_cost_small_batch(self):
        cost = pricing.estimate_embedding_cost_cents(
            model="text-embedding-3-small", tokens=10_000
        )
        # 10k/1M * 20 = 0.2 → rounds to 0
        assert cost == 0


# ── Embeddings (lexical fallback path) ─────────────────────────────────────


class TestLexicalEmbedding:
    def test_returns_correct_dimension(self):
        vec = _lexical_embedding("hola mundo")
        assert len(vec) == EMBEDDING_DIMENSIONS

    def test_empty_text_returns_zero_vector(self):
        vec = _lexical_embedding("")
        assert len(vec) == EMBEDDING_DIMENSIONS
        assert all(v == 0.0 for v in vec)

    def test_normalized_vector_has_unit_length(self):
        vec = _lexical_embedding("precio tarifa valor costo")
        norm = math.sqrt(sum(v * v for v in vec))
        if norm > 0:
            assert abs(norm - 1.0) < 1e-6

    def test_hash_term_is_deterministic(self):
        assert _hash_term("precio") == _hash_term("precio")
        assert _hash_term("precio") != _hash_term("tarifa")

    def test_terms_filters_stopwords_and_short_words(self):
        terms = _terms("el la de precio ok a")
        # "el", "la", "de", "a" are stopwords; "ok" is < 3 chars
        assert "precio" in terms
        assert "el" not in terms
        assert "ok" not in terms

    def test_lexical_score_rewards_overlap(self):
        query_terms = {"precio", "tarifa"}
        score_hit = _lexical_score(query_terms, "el precio y la tarifa")
        score_miss = _lexical_score(query_terms, "no hay nada relacionado")
        assert score_hit > score_miss
        assert score_miss == 0.0

    def test_lexical_score_zero_for_empty_query(self):
        assert _lexical_score(set(), "algo") == 0.0


class TestEmbeddingService:
    def test_provider_auto_openai_when_key_present(self, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        monkeypatch.delenv("EMBEDDING_PROVIDER", raising=False)
        svc = EmbeddingService()
        assert svc.provider == "openai"
        assert svc.model == "text-embedding-3-small"

    def test_provider_auto_lexical_when_no_key(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("EMBEDDING_PROVIDER", raising=False)
        svc = EmbeddingService()
        assert svc.provider == "lexical"

    def test_provider_explicit_lexical_overrides_key(self, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        monkeypatch.setenv("EMBEDDING_PROVIDER", "lexical")
        svc = EmbeddingService()
        assert svc.provider == "lexical"

    def test_provider_openai_falls_back_without_key(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.setenv("EMBEDDING_PROVIDER", "openai")
        svc = EmbeddingService()
        # Auto-degrades to lexical when key is missing.
        assert svc.provider == "lexical"

    def test_embed_texts_lexical_returns_vectors(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("EMBEDDING_PROVIDER", raising=False)
        svc = EmbeddingService()
        result = svc.embed_texts(["hola", "mundo precio"])
        assert isinstance(result, EmbeddingResult)
        assert result.provider == "lexical"
        assert len(result.vectors) == 2
        for v in result.vectors:
            assert len(v) == EMBEDDING_DIMENSIONS

    def test_embed_texts_empty_list_returns_empty(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        svc = EmbeddingService()
        result = svc.embed_texts([])
        assert result.vectors == []

    def test_embed_query_returns_single_vector(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        svc = EmbeddingService()
        vec = svc.embed_query("precio")
        assert len(vec) == EMBEDDING_DIMENSIONS

    def test_fit_dim_truncates_oversize_vector(self):
        big = [0.1] * 2000
        out = EmbeddingService._fit_dim(big)
        assert len(out) == EMBEDDING_DIMENSIONS

    def test_fit_dim_pads_undersize_vector(self):
        small = [0.1] * 100
        out = EmbeddingService._fit_dim(small)
        assert len(out) == EMBEDDING_DIMENSIONS
        assert all(v == 0.0 for v in out[100:])


# ── Model manager ──────────────────────────────────────────────────────────


class TestGenerationParams:
    def test_defaults_when_env_unset(self, monkeypatch):
        for var in ("LLM_TEMPERATURE", "LLM_MAX_TOKENS", "LLM_TOP_P"):
            monkeypatch.delenv(var, raising=False)
        params = GenerationParams.from_env()
        assert params.temperature == 0.30
        assert params.max_tokens == 1024
        assert params.top_p == 1.0

    def test_reads_env_values(self, monkeypatch):
        monkeypatch.setenv("LLM_TEMPERATURE", "0.7")
        monkeypatch.setenv("LLM_MAX_TOKENS", "512")
        monkeypatch.setenv("LLM_TOP_P", "0.9")
        params = GenerationParams.from_env()
        assert params.temperature == 0.7
        assert params.max_tokens == 512
        assert params.top_p == 0.9

    def test_temperature_clamped_to_valid_range(self, monkeypatch):
        monkeypatch.setenv("LLM_TEMPERATURE", "5.0")
        params = GenerationParams.from_env()
        assert params.temperature == 2.0

        monkeypatch.setenv("LLM_TEMPERATURE", "-1.0")
        params = GenerationParams.from_env()
        assert params.temperature == 0.0

    def test_max_tokens_at_least_one(self, monkeypatch):
        monkeypatch.setenv("LLM_MAX_TOKENS", "0")
        params = GenerationParams.from_env()
        assert params.max_tokens == 1

    def test_top_p_clamped(self, monkeypatch):
        monkeypatch.setenv("LLM_TOP_P", "2.0")
        params = GenerationParams.from_env()
        assert params.top_p == 1.0

    def test_invalid_env_falls_back_to_default(self, monkeypatch):
        monkeypatch.setenv("LLM_TEMPERATURE", "not-a-number")
        params = GenerationParams.from_env()
        assert params.temperature == 0.30


class TestProviderDetection:
    def test_openai_wins_when_multiple_keys(self, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-1")
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-2")
        monkeypatch.setenv("MINIMAX_API_KEY", "sk-3")
        assert _detect_provider() == "openai"

    def test_anthropic_when_no_openai(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-2")
        monkeypatch.setenv("MINIMAX_API_KEY", "sk-3")
        assert _detect_provider() == "anthropic"

    def test_minimax_when_only_minimax(self, monkeypatch):
        for v in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "TOGETHER_API_KEY"):
            monkeypatch.delenv(v, raising=False)
        monkeypatch.setenv("MINIMAX_API_KEY", "sk-3")
        assert _detect_provider() == "minimax"

    def test_together_last_priority(self, monkeypatch):
        for v in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "MINIMAX_API_KEY"):
            monkeypatch.delenv(v, raising=False)
        monkeypatch.setenv("TOGETHER_API_KEY", "sk-4")
        assert _detect_provider() == "together"

    def test_none_when_no_keys(self, monkeypatch):
        for v in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "MINIMAX_API_KEY", "TOGETHER_API_KEY"):
            monkeypatch.delenv(v, raising=False)
        assert _detect_provider() is None
