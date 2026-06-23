"""MiniMax provider adapter."""

from __future__ import annotations

from dataclasses import replace

from api.core.model_registry import ResolvedModelConfig

from .openai_compatible import OpenAICompatibleAdapter


class MiniMaxAdapter(OpenAICompatibleAdapter):
    provider_name = "minimax"

    def __init__(self, config: ResolvedModelConfig) -> None:
        if not config.base_url:
            config = replace(config, base_url="https://api.minimax.io/v1")
        super().__init__(config)
