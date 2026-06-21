"""Provider adapters for AI models.

Exports:
- ProviderAdapter, ProviderError: base classes
- OpenAIAdapter, AnthropicAdapter, CohereAdapter, OllamaAdapter
- get_adapter_for_provider: factory by name
"""
from api.core.providers.base import ProviderAdapter, ProviderError
from api.core.providers.openai_adapter import OpenAIAdapter
from api.core.providers.anthropic_adapter import AnthropicAdapter
from api.core.providers.cohere_adapter import CohereAdapter
from api.core.providers.ollama_adapter import OllamaAdapter


_REGISTRY = {
    "openai": OpenAIAdapter,
    "anthropic": AnthropicAdapter,
    "cohere": CohereAdapter,
    "ollama": OllamaAdapter,
}


def get_adapter_for_provider(provider: str, **kwargs) -> ProviderAdapter:
    """Factory: instantiate the right adapter by provider name.

    Raises ValueError if provider is unknown.
    """
    cls = _REGISTRY.get(provider.lower())
    if cls is None:
        raise ValueError(
            f"Unknown provider: {provider!r}. "
            f"Supported: {sorted(_REGISTRY.keys())}"
        )
    return cls(**kwargs)


__all__ = [
    "ProviderAdapter",
    "ProviderError",
    "OpenAIAdapter",
    "AnthropicAdapter",
    "CohereAdapter",
    "OllamaAdapter",
    "get_adapter_for_provider",
]
