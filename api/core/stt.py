"""Speech-to-text runtime routed through the configurable model registry."""

from __future__ import annotations

from io import BytesIO

from openai import OpenAI

from api.core.model_registry import ModelRegistry, ResolvedModelConfig
from api.core.providers.base import ModelInvocationError
from api.models.ai_models import AITask


class SpeechToTextService:
    """Resolve the active STT model and transcribe an audio payload."""

    def __init__(self, *, registry: ModelRegistry | None = None) -> None:
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
        client = self._client_for(resolved)
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

    def _client_for(self, resolved: ResolvedModelConfig) -> OpenAI:
        if resolved.provider not in {"openai", "openai_compatible"}:
            raise ModelInvocationError(
                f"Provider {resolved.provider!r} does not support STT in M10."
            )
        if not resolved.api_key:
            raise ModelInvocationError("STT provider is missing an API key.")
        return OpenAI(
            api_key=resolved.api_key,
            base_url=resolved.base_url,
        )
