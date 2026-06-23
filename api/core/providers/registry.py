"""Provider adapter registry."""

from __future__ import annotations

from typing import ClassVar

from .base import ProviderAdapter


class UnknownProviderError(LookupError):
    """Raised when a requested provider is not registered."""


class DuplicateProviderError(ValueError):
    """Raised when trying to register an already-known provider."""


class ProviderRegistry:
    """Singleton-backed registry for provider adapters."""

    _default: ClassVar["ProviderRegistry | None"] = None
    _adapters: ClassVar[dict[str, object]] = {}

    def __init__(self) -> None:
        self._providers: dict[str, ProviderAdapter] = {}

    @classmethod
    def get_default(cls) -> "ProviderRegistry":
        if cls._default is None:
            cls._default = cls()
        return cls._default

    @classmethod
    def reset_default(cls) -> "ProviderRegistry":
        cls._default = cls()
        return cls._default

    def register(self, adapter: ProviderAdapter) -> ProviderAdapter:
        name = getattr(adapter, "provider_name", "").strip()
        if not name:
            raise ValueError("Provider adapters must define a non-empty provider_name.")
        if name in self._providers:
            raise DuplicateProviderError(f"Provider '{name}' is already registered.")
        self._providers[name] = adapter
        return adapter

    def get(self, provider_name: str) -> ProviderAdapter:
        try:
            return self._providers[provider_name]
        except KeyError as exc:
            raise UnknownProviderError(f"Unknown provider '{provider_name}'.") from exc

    def has(self, provider_name: str) -> bool:
        return provider_name in self._providers

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._providers))
