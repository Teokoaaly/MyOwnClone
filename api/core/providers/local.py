"""Local OpenAI-compatible provider adapter."""

from __future__ import annotations

from dataclasses import replace

from api.core.model_registry import ResolvedModelConfig

from .openai_compatible import OpenAICompatibleAdapter


class LocalAdapter(OpenAICompatibleAdapter):
    provider_name = "local"

    def __init__(self, config: ResolvedModelConfig) -> None:
        if not config.base_url:
            config = replace(config, base_url="http://127.0.0.1:11434/v1")
        if not config.api_key:
            config = replace(config, api_key="local-dev-key")
        super().__init__(config)
