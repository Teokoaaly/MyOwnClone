"""Speech-to-text runtime routed through the configurable model registry.

Resolves the active STT model for a tenant and dispatches to a provider
adapter by name. The previous implementation hard-coded the OpenAI SDK;
that path is still supported for the OpenAI / OpenAI-compatible
providers, and a new ``local_whisper`` provider runs faster-whisper
in-process so STT works without any external API key.
"""
from __future__ import annotations

import logging
from io import BytesIO

from openai import OpenAI

from api.core.model_registry import ModelRegistry, ResolvedModelConfig
from api.core.providers.anthropic import AnthropicAdapter
from api.core.providers.base import ModelInvocationError
from api.core.providers.local import LocalAdapter
from api.core.providers.local_whisper import LocalWhisperAdapter
from api.core.providers.minimax import MiniMaxAdapter
from api.core.providers.openai import OpenAIAdapter
from api.core.providers.openai_compatible import OpenAICompatibleAdapter
from api.core.providers.together import TogetherAdapter
from api.models.ai_models import AITask

logger = logging.getLogger(__name__)


# Map of provider name -> adapter class. Mirrors ``ModelManager._ADAPTER_TYPES``
# so STT, LLM and embeddings share one source of truth. Classes (not
# instances) because adapters carry per-request configuration and must
# be instantiated with a ``ResolvedModelConfig``.
ADAPTER_TYPES = {
    "openai": OpenAIAdapter,
    "openai_compatible": OpenAICompatibleAdapter,
    "anthropic": AnthropicAdapter,
    "minimax": MiniMaxAdapter,
    "together": TogetherAdapter,
    "local": LocalAdapter,
    "local_whisper": LocalWhisperAdapter,
}


class SpeechToTextService:
    """Resolve the active STT model and transcribe an audio payload."""

    def __init__(
        self,
        *,
        registry: ModelRegistry | None = None,
    ) -> None:
        self.registry = registry or ModelRegistry()

    def transcribe(
        self,
        *,
        tenant_id: str | None,
        audio_bytes: bytes,
      ***REMOVED***lename: str,
        content_type: str | None = None,
        language: str | None = "es",
    ) -> str:
        resolved = self.registry.get_model_for_task(tenant_id=tenant_id, task=AITask.STT)
        provider_name = (resolved.provider or "").strip() or "openai"

        if provider_name in ADAPTER_TYPES:
            adapter_cls = ADAPTER_TYPES[provider_name]
      ***REMOVED***:
            # Unknown provider: fall back to OpenAI-compatible legacy
            # path so old configs keep working.
            logger.warning(
                "Unknown STT provider %r; falling back to openai_compatible",
                provider_name,
            )
            adapter_cls = ADAPTER_TYPES["openai_compatible"]
            provider_name = "openai_compatible"

        adapter = adapter_cls(resolved)

        # If the adapter exposes transcribe() AND reports speech2text
        # support, delegate to it. Otherwise fall back to the OpenAI
        # SDK path for adapters that only implement generate().
        if adapter.supports("speech2text") and hasattr(adapter, "transcribe"):
            try:
                return adapter.transcribe(
                    audio_bytes=audio_bytes,
                  ***REMOVED***lename=filename,
                    content_type=content_type,
                    language=language,
                )
            except ModelInvocationError:
                raise
            except Exception as exc:  # noqa: BLE001
                raise ModelInvocationError(
                    f"{provider_name} transcription failed: {exc}"
                ) from exc

        if provider_name in {"openai", "openai_compatible", "local"}:
            return self._legacy_openai_transcribe(
                resolved, audio_bytes, filename, language
            )

        raise ModelInvocationError(
            f"Provider {provider_name!r} does not support speech-to-text."
        )

    # --- legacy fallback ---------------------------------------------------------
    def _legacy_openai_transcribe(
        self,
        resolved: ResolvedModelConfig,
        audio_bytes: bytes,
      ***REMOVED***lename: str,
        language: str | None,
    ) -> str:
        if not resolved.api_key:
            raise ModelInvocationError("STT provider is missing an API key.")
        client = OpenAI(api_key=resolved.api_key, base_url=resolved.base_url)
        payload = BytesIO(audio_bytes)
        payload.name = filename or "audio.webm"
        response = client.audio.transcriptions.create(
            model=resolved.model_id or "whisper-1",
          ***REMOVED***le=payload,
            language=language or "es",
        )
        text = getattr(response, "text", "") or ""
        if not isinstance(text, str):
            raise ModelInvocationError("STT provider returned an invalid transcription payload.")
        return text