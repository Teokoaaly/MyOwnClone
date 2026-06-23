"""Anthropic provider adapter."""

from __future__ import annotations

import time

from api.core.model_registry import ResolvedModelConfig

from .base import GenerationParams, ModelInvocationError, ModelReply, ModelUsage, ProviderAdapter, TestResult


class AnthropicAdapter(ProviderAdapter):
    provider_name = "anthropic"

    def __init__(self, config: ResolvedModelConfig) -> None:
        self.config = config

    def _require_api_key(self) -> str:
        if not self.config.api_key:
            raise ModelInvocationError("Anthropic adapter requires a decrypted api_key.")
        return self.config.api_key

    def _client(self):
        try:
            import anthropic
        except ImportError as exc:
            raise ModelInvocationError("anthropic package not installed") from exc
        return anthropic.Anthropic(api_key=self._require_api_key())

    def _model_name(self, params: GenerationParams | None) -> str:
        return (params.model if params and params.model else None) or self.config.model_id

    def generate(self, *, prompt: str, params: GenerationParams | None = None) -> ModelReply:
        started = time.monotonic()
        try:
            response = self._client().messages.create(
                model=self._model_name(params),
                max_tokens=(params.max_tokens if params and params.max_tokens else self.config.max_tokens_default) or 2048,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:
            raise ModelInvocationError(f"Anthropic invocation failed: {exc}") from exc
        usage = getattr(response, "usage", None)
        total_tokens = 0
        if usage is not None:
            total_tokens = (getattr(usage, "input_tokens", 0) or 0) + (getattr(usage, "output_tokens", 0) or 0)
        return ModelReply(
            text=response.content[0].text if response.content else "",
            usage=ModelUsage(
                prompt_tokens=getattr(usage, "input_tokens", 0) or 0,
                completion_tokens=getattr(usage, "output_tokens", 0) or 0,
                total_tokens=total_tokens,
            ),
            latency_ms=int((time.monotonic() - started) * 1000),
            raw_response=response,
        )

    def generate_stream(self, *, prompt: str, params: GenerationParams | None = None):
        try:
            with self._client().messages.stream(
                model=self._model_name(params),
                max_tokens=(params.max_tokens if params and params.max_tokens else self.config.max_tokens_default) or 2048,
                messages=[{"role": "user", "content": prompt}],
            ) as stream_ctx:
                for text in stream_ctx.text_stream:
                    yield text
        except Exception as exc:
            raise ModelInvocationError(f"Anthropic streaming invocation failed: {exc}") from exc

    def test_connection(self) -> TestResult:
        try:
            self._client().messages.create(
                model=self.config.model_id,
                max_tokens=1,
                messages=[{"role": "user", "content": "ping"}],
            )
        except Exception as exc:
            return TestResult(ok=False, message=str(exc))
        return TestResult(ok=True, message="Anthropic connection ok")
