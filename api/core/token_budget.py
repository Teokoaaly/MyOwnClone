"""Token budget and embedding dimension guards for configurable AI models."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from api.core.model_registry import ResolvedModelConfig
from api.models.ai_models import AITask

logger = logging.getLogger(__name__)

class TokenBudgetError(ValueError):
    """Raised when an input cannot fit the allowed token budget."""


class EmbeddingDimensionError(ValueError):
    """Raised when an embedding model does not match the required dimensions."""


@dataclass(slots=True)
class BudgetResult:
    text: str
    estimated_tokens: int
    was_truncated: bool
    available_tokens: int


class TokenBudgeter:
    """Estimate prompt size, truncate when allowed, and enforce embedding contracts."""

    def __init__(self, *, chars_per_token: int = 4) -> None:
        if chars_per_token <= 0:
            raise ValueError("chars_per_token must be > 0")
        self.chars_per_token = chars_per_token

    def estimate_tokens(self, text: str) -> int:
        if not text:
            return 0
        return max(1, (len(text) + self.chars_per_token - 1) // self.chars_per_token)

    def available_prompt_tokens(
        self,
        *,
        model: ResolvedModelConfig,
        override_max_tokens: int | None = None,
        reserved_completion_tokens: int | None = None,
    ) -> int | None:
        max_input = model.max_input_tokens
        if max_input is None:
            return None

        reserve = reserved_completion_tokens
        if reserve is None:
            reserve = override_max_tokens if override_max_tokens is not None else model.max_tokens_default
        reserve = reserve or 0
        return max(0, max_input - reserve)

    def fit_text(
        self,
        *,
        text: str,
        model: ResolvedModelConfig,
        task: AITask,
        truncate: bool = False,
        override_max_tokens: int | None = None,
    ) -> BudgetResult:
        available = self.available_prompt_tokens(
            model=model,
            override_max_tokens=override_max_tokens,
        )
        estimated = self.estimate_tokens(text)
        if available is None or estimated <= available:
            return BudgetResult(
                text=text,
                estimated_tokens=estimated,
                was_truncated=False,
                available_tokens=available if available is not None else estimated,
            )

        if not truncate:
            raise TokenBudgetError(
                f"Input for task={task.value!r} requires {estimated} tokens but only {available} are available."
            )

        max_chars = available * self.chars_per_token
        truncated_text = text[:max_chars]
        truncated_tokens = self.estimate_tokens(truncated_text)
        logger.warning(
            "TokenBudgeter truncated input for task=%s model=%s from %s to %s estimated tokens",
            task.value,
            model.model_id,
            estimated,
            truncated_tokens,
        )
        return BudgetResult(
            text=truncated_text,
            estimated_tokens=truncated_tokens,
            was_truncated=True,
            available_tokens=available,
        )

    def validate_embedding_model(self, *, model: ResolvedModelConfig) -> None:
        if model.embedding_dimensions is None or model.embedding_dimensions <= 0:
            raise EmbeddingDimensionError(
                f"Embedding model {model.model_id!r} must expose a positive embedding_dimensions value, "
                f"got {model.embedding_dimensions!r}."
            )
