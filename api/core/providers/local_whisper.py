"""Local faster-whisper provider adapter for speech-to-text.

Runs faster-whisper in-process (CPU CTranslate2 backend) so the api
container can transcribe audio without any external API key. Designed
for low-resource hosts (whisper ``tiny`` int8 fits in ~400 MB RAM and
runs roughly 3x realtime on 2 vCPUs).

Provider name: ``local_whisper``. Selected automatically by the model
registry as the STT fallback when ``OPENAI_API_KEY`` is unset.
"""
from __future__ import annotations

import io
import logging
import os
import threading
from typing import Any

from api.core.model_registry import ResolvedModelConfig

from .base import GenerationParams, ModelInvocationError, ModelReply, TestResult

logger = logging.getLogger(__name__)


class LocalWhisperAdapter:
    """In-process faster-whisper STT provider."""

    provider_name = "local_whisper"
    supported_model_types = ("speech2text",)

    # Default model: tiny.en int8 (~75 MB on disk, ~400 MB RSS).
    DEFAULT_MODEL_SIZE = os.environ.get("LOCAL_WHISPER_MODEL", "tiny")
    DEFAULT_DEVICE = os.environ.get("LOCAL_WHISPER_DEVICE", "cpu")
    DEFAULT_COMPUTE_TYPE = os.environ.get(
        "LOCAL_WHISPER_COMPUTE_TYPE", "int8"
    )
    DEFAULT_DOWNLOAD_ROOT = os.environ.get(
        "LOCAL_WHISPER_DOWNLOAD_ROOT", "/tmp/whisper"
    )

    def __init__(self, config: ResolvedModelConfig) -> None:
        self.config = config
        self._model = None
        self._model_lock = threading.Lock()

    def supports(self, model_type) -> bool:
        return str(model_type) == "speech2text"

    # --- ProviderAdapter contract ------------------------------------------------
    def generate(
        self,
        *,
        prompt: str,
        params: GenerationParams | None = None,
    ) -> ModelReply:
        raise ModelInvocationError(
            "LocalWhisperAdapter only supports speech-to-text (use transcribe)."
        )

    def generate_stream(self, *, prompt: str, params: GenerationParams | None = None):
        raise ModelInvocationError(
            "LocalWhisperAdapter does not stream; use transcribe()."
        )
        yield ""  # pragma: no cover

    def test_connection(self) -> TestResult:
        try:
            self._ensure_model()
            return TestResult(
                ok=True,
                message="local whisper ready",
                details={"model": self._model_name()},
            )
        except Exception as exc:  # noqa: BLE001
            return TestResult(ok=False, message=str(exc))

    # --- STT-specific ------------------------------------------------------------
    def transcribe(
        self,
        *,
        audio_bytes: bytes,
      ***REMOVED***lename: str,
        content_type: str | None = None,
        language: str | None = "es",
        **_unused: Any,
    ) -> str:
        if not audio_bytes:
            raise ModelInvocationError("Empty audio payload.")
        try:
            model = self._ensure_model()
        except Exception as exc:  # noqa: BLE001
            raise ModelInvocationError(
                f"Local Whisper model failed to load: {exc}"
            ) from exc

        # faster-whisper accepts a file-like with a ``name`` attribute to
        # detect the format; pass the original filename so it picks the
        # right decoder.
        buffer = io.BytesIO(audio_bytes)
        buffer.name = filename or "audio.webm"

        try:
            segments, _info = model.transcribe(
                buffer,
                language=language or "es",
                vad_filter=True,
                beam_size=1,  # tiny: beam search gives little uplift at high latency cost
            )
            text = " ".join(seg.text.strip() for seg in segments).strip()
        except Exception as exc:  # noqa: BLE001
            raise ModelInvocationError(
                f"Local Whisper transcription failed: {exc}"
            ) from exc

        if not text:
            raise ModelInvocationError(
                "Local Whisper returned no text (audio too quiet or unsupported)."
            )
        return text

    # --- internals ---------------------------------------------------------------
    def _model_name(self) -> str:
        explicit = (self.config.model_id or "").strip()
        return explicit or self.DEFAULT_MODEL_SIZE

    def _ensure_model(self):
        """Lazy-load the model (and download on first call)."""
        if self._model is not None:
            return self._model
        with self._model_lock:
            if self._model is not None:
                return self._model
            from faster_whisper import WhisperModel  # local import keeps cold-start cheap

            os.makedirs(self.DEFAULT_DOWNLOAD_ROOT, exist_ok=True)
            model_size = self._model_name()
            logger.info(
                "Loading local Whisper model %s on %s (%s)",
                model_size, self.DEFAULT_DEVICE, self.DEFAULT_COMPUTE_TYPE,
            )
            self._model = WhisperModel(
                model_size,
                device=self.DEFAULT_DEVICE,
                compute_type=self.DEFAULT_COMPUTE_TYPE,
                download_root=self.DEFAULT_DOWNLOAD_ROOT,
            )
            return self._model