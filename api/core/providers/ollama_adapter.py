"""Ollama provider adapter. OpenAI-compatible (localhost:11434/v1)."""
from __future__ import annotations
import os
from api.core.providers.openai_adapter import OpenAIAdapter


class OllamaAdapter(OpenAIAdapter):
    """Ollama exposes an OpenAI-compatible endpoint at /v1.

    Useful for self-hosted LLMs. No API key required in most setups.
    """
    name = "ollama"

    def __init__(self, api_key: str = "ollama", base_url: str = None, **kwargs):
        if base_url is None:
            base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def is_available(self) -> bool:
        """Ollama doesn't require a key; just check the base URL is reachable."""
        return True
