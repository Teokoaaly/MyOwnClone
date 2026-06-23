"""Together.ai provider adapter."""

from __future__ import annotations

from dataclasses import replace

from api.core.model_registry import ResolvedModelConfig

from .openai_compatible import OpenAICompatibleAdapter


class TogetherAdapter(OpenAICompatibleAdapter):
    provider_name = "together"

    def __init__(self, config: ResolvedModelConfig) -> None:
        if not config.base_url:
            config = replace(config, base_url="https://api.together.xyz/v1")
        super().__init__(config)
