"""OpenAI-compatible provider adapter."""

from __future__ import annotations

from api.core.model_registry import ResolvedModelConfig

from .base import ModelInvocationError, TestResult
from .openai import OpenAIAdapter


class OpenAICompatibleAdapter(OpenAIAdapter):
    provider_name = "openai_compatible"

    def __init__(self, config: ResolvedModelConfig) -> None:
        if not config.base_url:
            raise ModelInvocationError(
                "openai_compatible adapter requires a base_url in the resolved config."
            )
        super().__init__(config)

    def test_connection(self) -> TestResult:
        result = super().test_connection()
        if result.ok:
            return TestResult(ok=True, message=f"OpenAI-compatible connection ok: {self.config.base_url}")
        return result
