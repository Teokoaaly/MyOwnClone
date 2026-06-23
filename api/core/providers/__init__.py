"""Provider contracts and registry for configurable AI runtimes."""

from .anthropic import AnthropicAdapter
from .base import (
    GenerationParams,
    ModelInvocationError,
    ModelReply,
    ModelType,
    ModelUsage,
    ProviderAdapter,
    TestResult,
)
from .local import LocalAdapter
from .minimax import MiniMaxAdapter
from .openai import OpenAIAdapter
from .openai_compatible import OpenAICompatibleAdapter
from .registry import DuplicateProviderError, ProviderRegistry, UnknownProviderError
from .together import TogetherAdapter

ProviderRegistry._adapters.update(
    {
        "openai": OpenAIAdapter,
        "anthropic": AnthropicAdapter,
        "minimax": MiniMaxAdapter,
        "together": TogetherAdapter,
        "openai_compatible": OpenAICompatibleAdapter,
        "local": LocalAdapter,
    }
)

__all__ = [
    "AnthropicAdapter",
    "DuplicateProviderError",
    "GenerationParams",
    "LocalAdapter",
    "ModelInvocationError",
    "ModelReply",
    "ModelType",
    "ModelUsage",
    "MiniMaxAdapter",
    "OpenAIAdapter",
    "OpenAICompatibleAdapter",
    "ProviderAdapter",
    "ProviderRegistry",
    "TestResult",
    "TogetherAdapter",
    "UnknownProviderError",
]
