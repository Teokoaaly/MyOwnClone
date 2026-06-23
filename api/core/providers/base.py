"""Base provider contracts for configurable AI runtimes."""

from __future__ import annotations

import enum
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Generator


class ModelInvocationError(RuntimeError):
    """Raised when a provider invocation fails or is misconfigured."""


class ModelType(enum.StrEnum):
    """Model type selector shared by the configurable runtime."""

    LLM = "llm"
    EMBEDDING = "embedding"
    RERANKING = "reranking"
    SPEECH2TEXT = "speech2text"
    TTS = "tts"
    MODERATION = "moderation"


@dataclass(slots=True)
class GenerationParams:
    """Normalized generation parameters accepted by provider adapters."""

    model: str | None = None
    temperature: float | None = None
    max_tokens: int | None = None
    top_p: float | None = None
    stop: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ModelUsage:
    """Minimal usage metadata returned by the model runtime."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

    def as_dict(self) -> dict[str, int]:
        return {
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
        }


@dataclass(slots=True)
class ModelReply:
    """Reply returned by a provider adapter."""

    text: str = ""
    usage: ModelUsage | None = None
    latency_ms: int | None = None
    raw_response: Any | None = None


@dataclass(slots=True)
class TestResult:
    """Simple connection test result for admin/runtime checks."""

    ok: bool
    message: str = ""
    details: dict[str, Any] = field(default_factory=dict)


TestResult.__test__ = False


class ProviderAdapter(ABC):
    """Abstract provider contract used by the configurable runtime."""

    provider_name: str
    supported_model_types: tuple[ModelType, ...] = (ModelType.LLM,)

    def supports(self, model_type: ModelType) -> bool:
        return model_type in self.supported_model_types

    @abstractmethod
    def generate(
        self,
        *,
        prompt: str,
        params: GenerationParams | None = None,
    ) -> ModelReply:
        """Return a non-streaming generation reply."""

    @abstractmethod
    def generate_stream(
        self,
        *,
        prompt: str,
        params: GenerationParams | None = None,
    ) -> Generator[str, None, None]:
        """Yield a streaming generation reply."""

    @abstractmethod
    def test_connection(self) -> TestResult:
        """Validate whether the provider can be reached with current config."""
