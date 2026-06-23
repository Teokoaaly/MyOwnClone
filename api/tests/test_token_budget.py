from __future__ import annotations

import logging

import pytest

from api.core.model_registry import ResolvedModelConfig
from api.core.token_budget import (
    EXPECTED_EMBEDDING_DIMENSIONS,
    EmbeddingDimensionError,
    TokenBudgetError,
    TokenBudgeter,
)
from api.models.ai_models import AITask


def _model(**overrides) -> ResolvedModelConfig:
    data = {
        "task": AITask.CHAT,
        "provider": "openai",
        "model_id": "demo-model",
        "tenant_id": "tenant-1",
        "source": "database",
        "max_input_tokens": 100,
        "max_tokens_default": 20,
        "embedding_dimensions": EXPECTED_EMBEDDING_DIMENSIONS,
    }
    data.update(overrides)
    return ResolvedModelConfig(**data)


def test_token_budgeter_allows_text_within_budget():
    budgeter = TokenBudgeter(chars_per_token=4)
    model = _model(max_input_tokens=100, max_tokens_default=20)
    text = "a" * 120  # 30 tokens

    result = budgeter.fit_text(text=text, model=model, task=AITask.CHAT)

    assert result.text == text
    assert result.estimated_tokens == 30
    assert result.was_truncated is False
    assert result.available_tokens == 80


def test_token_budgeter_truncates_when_allowed(caplog):
    caplog.set_level(logging.WARNING)
    budgeter = TokenBudgeter(chars_per_token=4)
    model = _model(max_input_tokens=40, max_tokens_default=10)
    text = "x" * 200

    result = budgeter.fit_text(
        text=text,
        model=model,
        task=AITask.CHAT,
        truncate=True,
    )

    assert result.was_truncated is True
    assert len(result.text) == 120
    assert result.available_tokens == 30
    assert "truncated input" in caplog.text


def test_token_budgeter_rejects_oversized_text_without_truncation():
    budgeter = TokenBudgeter(chars_per_token=4)
    model = _model(max_input_tokens=40, max_tokens_default=10)
    text = "x" * 200

    with pytest.raises(TokenBudgetError):
        budgeter.fit_text(text=text, model=model, task=AITask.CHAT, truncate=False)


def test_token_budgeter_uses_override_max_tokens():
    budgeter = TokenBudgeter(chars_per_token=4)
    model = _model(max_input_tokens=100, max_tokens_default=20)

    available = budgeter.available_prompt_tokens(
        model=model,
        override_max_tokens=35,
    )

    assert available == 65


def test_embedding_dimension_guard_accepts_1536():
    budgeter = TokenBudgeter()

    budgeter.validate_embedding_model(model=_model(task=AITask.EMBEDDING, embedding_dimensions=1536))


def test_embedding_dimension_guard_rejects_non_1536():
    budgeter = TokenBudgeter()

    with pytest.raises(EmbeddingDimensionError):
        budgeter.validate_embedding_model(
            model=_model(task=AITask.EMBEDDING, embedding_dimensions=768)
        )
