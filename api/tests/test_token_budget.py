"""Tests for TokenBudgeter and DimensionGuard."""
from __future__ import annotations
import pytest
from unittest.mock import MagicMock

from api.core.token_budget import (
    TokenBudgeter,
    DimensionGuard,
    DimensionMismatchError,
    FallbackTokenizer,
    GptTokenizerWrapper,
    TiktokenWrapper,
)


# ---------- Tokenizer ----------

def test_fallback_tokenizer_estimates_chars():
    tok = FallbackTokenizer()
    est = tok.count("hello world")  # 11 chars → ~3 tokens
    assert est.tokens >= 2
    assert est.tokens <= 5
    assert est.method == "fallback"


def test_token_budgeter_count_uses_tokenizer():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer())
    assert budgeter.count("hello") >= 1


def test_token_budgeter_effective_budget_applies_margin():
    budgeter = TokenBudgeter(safety_margin=0.10)
    assert budgeter.effective_budget(1000) == 900
    assert budgeter.effective_budget(100) == 90


def test_token_budgeter_truncation_does_not_affect_short_text():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer())
    text = "Short text"
    result = budgeter.truncate_to_budget(text, model_max_tokens=10000)
    assert result == text


def test_token_budgeter_truncation_shortens_long_text():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer(), safety_margin=0.0)
    # 1000 chars ~ 250 tokens; budget of 100 tokens = 400 chars
    text = "a" * 1000
    result = budgeter.truncate_to_budget(text, model_max_tokens=100)
    assert len(result) < 1000
    assert len(result) > 0


def test_token_budgeter_fit_chunks_packs_in_order():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer(), safety_margin=0.0)
    chunks = [
        "a" * 40,   # ~10 tokens
        "b" * 40,   # ~10 tokens
        "c" * 40,   # ~10 tokens — won't fit
    ]
    result = budgeter.fit_chunks(chunks, model_max_tokens=20)  # budget = 20
    assert len(result) == 2
    assert result[0].startswith("a")
    assert result[1].startswith("b")


def test_token_budgeter_fit_chunks_truncates_last_to_fit():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer(), safety_margin=0.0)
    chunks = [
        "a" * 40,   # ~10 tokens
        "b" * 200,  # ~50 tokens — only some fits
    ]
    result = budgeter.fit_chunks(chunks, model_max_tokens=20)
    assert len(result) == 2
    assert result[0] == "a" * 40
    assert len(result[1]) < 200  # truncated


def test_token_budgeter_fit_chunks_returns_empty_if_first_too_big():
    budgeter = TokenBudgeter(tokenizer=FallbackTokenizer(), safety_margin=0.0)
    chunks = ["a" * 10000]  # way too big
    result = budgeter.fit_chunks(chunks, model_max_tokens=10)
    assert result == []


# ---------- Dimension Guard ----------

def test_dimension_guard_check_postgres_passes():
    session = MagicMock()
    session.execute.return_value.first.return_value = (1536,)
    guard = DimensionGuard(expected_dim=1536)
    guard.check_postgres(session, "chunks")  # should not raise


def test_dimension_guard_check_postgres_fails_on_mismatch():
    session = MagicMock()
    session.execute.return_value.first.return_value = (768,)
    guard = DimensionGuard(expected_dim=1536)
    with pytest.raises(DimensionMismatchError) as exc_info:
        guard.check_postgres(session, "chunks")
    assert exc_info.value.expected == 1536
    assert exc_info.value.actual == 768
    assert exc_info.value.store == "postgres"


def test_dimension_guard_check_postgres_no_column_raises():
    session = MagicMock()
    session.execute.return_value.first.return_value = None
    guard = DimensionGuard(expected_dim=1536)
    with pytest.raises(DimensionMismatchError, match="No 'embedding' column"):
        guard.check_postgres(session, "chunks")


def test_dimension_guard_check_weaviate_passes():
    client = MagicMock()
    client.schema.get.return_value = {
        "vectorIndexConfig": {"size": 1536, "distance": "cosine"}
    }
    guard = DimensionGuard(expected_dim=1536)
    guard.check_weaviate(client, "Chunk")  # should not raise


def test_dimension_guard_check_weaviate_fails_on_mismatch():
    client = MagicMock()
    client.schema.get.return_value = {
        "vectorIndexConfig": {"size": 768, "distance": "cosine"}
    }
    guard = DimensionGuard(expected_dim=1536)
    with pytest.raises(DimensionMismatchError) as exc_info:
        guard.check_weaviate(client, "Chunk")
    assert exc_info.value.expected == 1536
    assert exc_info.value.actual == 768
    assert exc_info.value.store == "weaviate"


def test_dimension_guard_check_weaviate_falls_back_to_known_vectorizer():
    client = MagicMock()
    client.schema.get.return_value = {
        "vectorizer": "text2vec-openai",  # known: 1536
    }
    guard = DimensionGuard(expected_dim=1536)
    guard.check_weaviate(client, "Chunk")  # should not raise


def test_dimension_guard_check_weaviate_unknown_vectorizer_raises():
    client = MagicMock()
    client.schema.get.return_value = {
        "vectorizer": "custom-unknown-vectorizer",
    }
    guard = DimensionGuard(expected_dim=1536)
    with pytest.raises(DimensionMismatchError, match="Could not determine"):
        guard.check_weaviate(client, "Chunk")


def test_dimension_guard_check_both_calls_both():
    session = MagicMock()
    session.execute.return_value.first.return_value = (1536,)
    client = MagicMock()
    client.schema.get.return_value = {"vectorIndexConfig": {"size": 1536}}
    guard = DimensionGuard(expected_dim=1536)
    guard.check_both(session, client, "Chunk")  # should not raise


def test_dimension_guard_check_both_short_circuits_on_postgres_failure():
    session = MagicMock()
    session.execute.return_value.first.return_value = (768,)  # mismatch
    client = MagicMock()
    guard = DimensionGuard(expected_dim=1536)
    with pytest.raises(DimensionMismatchError) as exc_info:
        guard.check_both(session, client, "Chunk")
    assert exc_info.value.store == "postgres"
    # Weaviate should NOT be called
    client.schema.get.assert_not_called()
