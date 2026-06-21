"""Abstract base class for provider adapters."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterator, Any, Optional


class ProviderError(Exception):
    """Raised when a provider call fails."""
    def __init__(self, message: str, *, retriable: bool = True, status_code: Optional[int] = None):
        super().__init__(message)
        self.retriable = retriable
        self.status_code = status_code


class ProviderAdapter(ABC):
    """Abstract interface for AI provider adapters.

    All adapters must implement:
    - chat() for LLM chat completions
    - embed() for text embeddings (only if provider supports it)
    - name (provider identifier, e.g. "openai")
    - is_available() to check credentials/config
    """
    name: str = "abstract"

    def __init__(self, api_key: str, **kwargs):
        if not api_key:
            raise ValueError(f"api_key is required for {self.name}")
        self.api_key = api_key
        self.config = kwargs

    @abstractmethod
    def is_available(self) -> bool:
        """Check if the adapter is configured and can make calls."""
        ...

    @abstractmethod
    def chat(
        self,
        model: str,
        messages: list[dict[str, str]],
        *,
        max_tokens: int = 1024,
        temperature: float = 0.7,
        stream: bool = False,
        **kwargs,
    ):
        """Send chat completion request.

        If stream=True, returns Iterator[str] yielding text chunks.
        If stream=False, returns dict with keys:
            - content: str
            - tokens_in: int
            - tokens_out: int
            - model: str
        """
        ...

    def embed(
        self,
        model: str,
        texts: list[str],
        **kwargs,
    ) -> list[list[float]]:
        """Generate embeddings. Default: not supported."""
        raise NotImplementedError(f"{self.name} does not support embeddings")

    def rerank(
        self,
        model: str,
        query: str,
        documents: list[str],
        top_n: int = 3,
        **kwargs,
    ) -> list[dict]:
        """Rerank documents. Default: not supported.

        Returns list of {index, score, document?} dicts, sorted by score desc.
        """
        raise NotImplementedError(f"{self.name} does not support reranking")

    def moderate(
        self,
        text: str,
        **kwargs,
    ) -> dict:
        """Moderate content. Default: not supported.

        Returns {flagged: bool, categories: {...}, scores: {...}}.
        """
        raise NotImplementedError(f"{self.name} does not support moderation")
