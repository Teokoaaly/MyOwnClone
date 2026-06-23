"""OpenAI provider adapter."""

from __future__ import annotations

import time

from api.core.model_registry import ResolvedModelConfig

from .base import GenerationParams, ModelInvocationError, ModelReply, ModelUsage, ProviderAdapter, TestResult


def _usage_to_model_usage(usage) -> ModelUsage | None:
    if usage is None:
        return None
    return ModelUsage(
        prompt_tokens=getattr(usage, "prompt_tokens", 0) or 0,
        completion_tokens=getattr(usage, "completion_tokens", 0) or 0,
        total_tokens=getattr(usage, "total_tokens", 0) or 0,
    )


class OpenAIAdapter(ProviderAdapter):
    provider_name = "openai"

    def __init__(self, config: ResolvedModelConfig) -> None:
        self.config = config

    def _require_api_key(self) -> str:
        if not self.config.api_key:
            raise ModelInvocationError("OpenAI adapter requires a decrypted api_key.")
        return self.config.api_key

    def _model_name(self, params: GenerationParams | None) -> str:
        return (params.model if params and params.model else None) or self.config.model_id

    def _client(self):
        try:
            import openai
        except ImportError as exc:
            raise ModelInvocationError("openai package not installed") from exc

        kwargs = {"api_key": self._require_api_key()}
        if self.config.base_url:
            kwargs["base_url"] = self.config.base_url
        return openai.OpenAI(**kwargs)

    def generate(self, *, prompt: str, params: GenerationParams | None = None) -> ModelReply:
        started = time.monotonic()
        try:
            response = self._client().chat.completions.create(
                model=self._model_name(params),
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:
            raise ModelInvocationError(f"OpenAI invocation failed: {exc}") from exc
        return ModelReply(
            text=response.choices[0].message.content or "",
            usage=_usage_to_model_usage(getattr(response, "usage", None)),
            latency_ms=int((time.monotonic() - started) * 1000),
            raw_response=response,
        )

    def generate_stream(self, *, prompt: str, params: GenerationParams | None = None):
        try:
            response = self._client().chat.completions.create(
                model=self._model_name(params),
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
        except Exception as exc:
            raise ModelInvocationError(f"OpenAI streaming invocation failed: {exc}") from exc
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    def test_connection(self) -> TestResult:
        try:
            self._client().models.list()
        except Exception as exc:
            return TestResult(ok=False, message=str(exc))
        return TestResult(ok=True, message="OpenAI connection ok")
