"""ModelManager — LLM invocation façade for MyOwnClone standalone.

Provides a concrete implementation that uses OpenAI-compatible APIs,
Anthropic, MiniMax, or Together directly, without requiring the external
`graphon` package.

Priority order for model selection:
  1. OPENAI_API_KEY  → uses OPENAI_MODEL or gpt-4o-mini
  2. ANTHROPIC_API_KEY → uses claude-3-haiku (fallback)
  3. MINIMAX_API_KEY → uses MiniMax OpenAI-compatible endpoint
  4. TOGETHER_API_KEY  → uses Llama 3 via Together.ai (budget option)
  5. No API key       → raises ModelInvocationError

OpenAI-compatible providers such as DeepSeek can be configured with:
  OPENAI_API_KEY=...
  OPENAI_BASE_URL=https://api.deepseek.com
  OPENAI_MODEL=deepseek-chat

`OPENAI_API_BASE` is accepted as a legacy alias for deployments that already
use that variable name.

Usage:
  from api.core.model_manager import ModelManager, ModelInvocationError

  reply = ModelManager.invoke_non_streaming(
      tenant_id="...",
      clone_id="...",
      message="Hello",
  )
  print(reply.text)
"""

from __future__ import annotations

import hashlib
import logging
import os
import time
from typing import Generator

from api.core.model_registry import ModelRegistry
from api.core.providers import (
    AnthropicAdapter,
    GenerationParams,
    LocalAdapter,
    ModelInvocationError,
    MiniMaxAdapter,
    ModelReply,
    ModelType,
    ModelUsage,
    OpenAIAdapter,
    OpenAICompatibleAdapter,
    ProviderAdapter,
    ProviderRegistry,
    TogetherAdapter,
)
from api.core.retry_client import RetryCandidate, RetryClient
from api.core.token_budget import EmbeddingDimensionError, TokenBudgetError, TokenBudgeter
from api.extensions import db
from api.models.ai_models import AIInvocation, AITask

logger = logging.getLogger(__name__)


# ─── Provider detection ──────────────────────────────────────────────────────

def _detect_provider() -> str | None:
    """Return the first available provider name, or None."""
    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    if os.getenv("ANTHROPIC_API_KEY"):
        return "anthropic"
    if os.getenv("MINIMAX_API_KEY"):
        return "minimax"
    if os.getenv("TOGETHER_API_KEY"):
        return "together"
    return None


# ─── Provider config ─────────────────────────────────────────────────────────

def _env(name: str, default: str) -> str:
    """Return a stripped environment value or a default when unset/blank."""
    return os.getenv(name, "").strip() or default


def _openai_base_url() -> str | None:
    """Return the OpenAI-compatible base URL, supporting the legacy alias."""
    return (
        os.getenv("OPENAI_BASE_URL", "").strip()
        or os.getenv("OPENAI_API_BASE", "").strip()
        or None
    )


def _openai_client_kwargs() -> dict[str, str]:
    kwargs = {"api_key": os.environ["OPENAI_API_KEY"]}
    base_url = _openai_base_url()
    if base_url:
        kwargs["base_url"] = base_url
    return kwargs


# ─── OpenAI backend ──────────────────────────────────────────────────────────

def _invoke_openai(prompt: str, *, model: str | None = None) -> ModelReply:
    """Invoke OpenAI (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed") from exc
    model = model or _env("OPENAI_MODEL", "gpt-4o-mini")
    client = openai.OpenAI(**_openai_client_kwargs())
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    usage = response.usage
    return ModelReply(
        text=response.choices[0].message.content or "",
        usage=ModelUsage(
            prompt_tokens=usage.prompt_tokens if usage else 0,
            completion_tokens=usage.completion_tokens if usage else 0,
            total_tokens=usage.total_tokens if usage else 0,
        ),
    )


def _invoke_openai_stream(prompt: str, *, model: str | None = None):
    """Invoke OpenAI (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed") from exc
    model = model or _env("OPENAI_MODEL", "gpt-4o-mini")
    client = openai.OpenAI(**_openai_client_kwargs())
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── Anthropic backend ───────────────────────────────────────────────────────

def _invoke_anthropic(prompt: str, *, model: str | None = None) -> ModelReply:
    """Invoke Anthropic (non-streaming)."""
    try:
        import anthropic
    except ImportError as exc:
        raise ModelInvocationError("anthropic package not installed") from exc
    model = model or _env("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.content[0].text if response.content else ""
    usage = response.usage
    return ModelReply(
        text=content,
        usage=ModelUsage(
            prompt_tokens=usage.input_tokens if usage else 0,
            completion_tokens=usage.output_tokens if usage else 0,
            total_tokens=(usage.input_tokens + usage.output_tokens) if usage else 0,
        ),
    )


def _invoke_anthropic_stream(prompt: str, *, model: str | None = None):
    """Invoke Anthropic (streaming)."""
    try:
        import anthropic
    except ImportError as exc:
        raise ModelInvocationError("anthropic package not installed") from exc
    model = model or _env("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    with client.messages.stream(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    ) as stream_ctx:
        for text in stream_ctx.text_stream:
            yield text


# ─── Together.ai backend (Llama 3) ───────────────────────────────────────────

def _invoke_together(prompt: str, *, model: str | None = None) -> ModelReply:
    """Invoke Together.ai (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for Together.ai client)") from exc
    model = model or _env("TOGETHER_MODEL", "meta-llama/Llama-3-8b-chat-hf")
    client = openai.OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return ModelReply(
        text=response.choices[0].message.content or "",
        usage=None,
    )


def _invoke_together_stream(prompt: str, *, model: str | None = None):
    """Invoke Together.ai (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for Together.ai client)") from exc
    model = model or _env("TOGETHER_MODEL", "meta-llama/Llama-3-8b-chat-hf")
    client = openai.OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── MiniMax backend (OpenAI-compatible) ─────────────────────────────────────

def _invoke_minimax(prompt: str, *, model: str | None = None) -> ModelReply:
    """Invoke MiniMax via its OpenAI-compatible endpoint (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for MiniMax)") from exc
    model = model or _env("MINIMAX_MODEL", "minimax-m2.7")
    client = openai.OpenAI(
        api_key=os.environ["MINIMAX_API_KEY"],
        base_url="https://api.minimax.io/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    usage = response.usage
    return ModelReply(
        text=response.choices[0].message.content or "",
        usage=ModelUsage(
            prompt_tokens=usage.prompt_tokens if usage else 0,
            completion_tokens=usage.completion_tokens if usage else 0,
            total_tokens=usage.total_tokens if usage else 0,
        ),
    )


def _invoke_minimax_stream(prompt: str, *, model: str | None = None):
    """Invoke MiniMax via its OpenAI-compatible endpoint (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for MiniMax)") from exc
    model = model or _env("MINIMAX_MODEL", "minimax-m2.7")
    client = openai.OpenAI(
        api_key=os.environ["MINIMAX_API_KEY"],
        base_url="https://api.minimax.io/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── Dispatch ────────────────────────────────────────────────────────────────

def _dispatch(prompt: str, *, provider: str) -> ModelReply:
    if provider == "openai":
        return _invoke_openai(prompt)
    elif provider == "anthropic":
        return _invoke_anthropic(prompt)
    elif provider == "minimax":
        return _invoke_minimax(prompt)
    elif provider == "together":
        return _invoke_together(prompt)
  ***REMOVED***:
        raise ModelInvocationError(
            "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
            "MINIMAX_API_KEY, or TOGETHER_API_KEY in your environment."
        )


def _dispatch_stream(prompt: str, *, provider: str) -> Generator[str, None, None]:
    if provider == "openai":
        yield from _invoke_openai_stream(prompt)
    elif provider == "anthropic":
        yield from _invoke_anthropic_stream(prompt)
    elif provider == "minimax":
        yield from _invoke_minimax_stream(prompt)
    elif provider == "together":
        yield from _invoke_together_stream(prompt)
  ***REMOVED***:
        raise ModelInvocationError(
            "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
            "MINIMAX_API_KEY, or TOGETHER_API_KEY in your environment."
        )


# ─── Model instance (graphon-compatible interface) ───────────────────────────

class _ModelInstance:
    """Minimal model instance interface compatible with the existing chat endpoints.

    The streaming chat endpoint calls:
      model_instance.invoke_llm_stream(prompt=...)
    The non-streaming path calls:
      model_instance.invoke_llm(prompt=...)
    """

    def __init__(self, *, tenant_id: str, model_manager: "ModelManager"):
        self._tenant_id = tenant_id
        self._model_manager = model_manager

    def invoke_llm(self, *, prompt: str) -> str:
        reply = self._model_manager.invoke_for_task(
            tenant_id=self._tenant_id,
            clone_id=None,
            task=AITask.CHAT,
            message=prompt,
        )
        return reply.text if isinstance(reply, ModelReply) else ""

    def invoke_llm_stream(self, *, prompt: str) -> Generator[str, None, None]:
        yield from self._model_manager.invoke_for_task_stream(
            tenant_id=self._tenant_id,
            clone_id=None,
            task=AITask.CHAT,
            message=prompt,
        )


# ─── Public façade ───────────────────────────────────────────────────────────

class ModelManager:
    """Façade for LLM calls used by MyOwnClone endpoints.

    Provides both the class-method interface (used by chat_public_simple)
    and an instance interface with get_default_model_instance (used by
    the streaming endpoint for graphon compatibility).
    """

    _ADAPTER_TYPES = {
        "openai": OpenAIAdapter,
        "anthropic": AnthropicAdapter,
        "minimax": MiniMaxAdapter,
        "together": TogetherAdapter,
        "openai_compatible": OpenAICompatibleAdapter,
        "local": LocalAdapter,
    }

    def __init__(
        self,
        *,
        registry: ModelRegistry | None = None,
        retry_client: RetryClient | None = None,
        token_budgeter: TokenBudgeter | None = None,
    ) -> None:
        self.registry = registry or ModelRegistry()
        self.retry_client = retry_client or RetryClient()
        self.token_budgeter = token_budgeter or TokenBudgeter()

    @staticmethod
    def _prompt_hash(message: str) -> str:
        return hashlib.sha256(message.encode("utf-8")).hexdigest()

    def _provider_adapter_for(self, resolved) -> ProviderAdapter:
        adapter_type = self._ADAPTER_TYPES.get(resolved.provider)
        if adapter_type is None:
            raise ModelInvocationError(f"Unsupported provider {resolved.provider!r}.")
        return adapter_type(resolved)

    def _build_generation_params(self, resolved) -> GenerationParams:
        override = resolved.override_params or {}
        return GenerationParams(
            model=resolved.model_id,
            temperature=override.get("temperature", resolved.temperature_default),
            max_tokens=override.get("max_tokens", resolved.max_tokens_default),
            metadata={"source": resolved.source, "provider": resolved.provider},
        )

    def _record_invocation(
        self,
        *,
        tenant_id: str,
        clone_id: str | None,
        task: AITask,
        model_name: str,
        message: str,
        success: bool,
        usage: ModelUsage | None = None,
        latency_ms: int = 0,
        error_message: str | None = None,
    ) -> None:
        row = AIInvocation(
            tenant_id=tenant_id,
            clone_id=clone_id,
            task=task.value,
            model=model_name,
            prompt_hash=self._prompt_hash(message),
            prompt_tokens=usage.prompt_tokens if usage else 0,
            completion_tokens=usage.completion_tokens if usage else 0,
            latency_ms=latency_ms,
            success=success,
            error_message=error_message,
        )
        db.session.add(row)
        db.session.commit()

    def invoke_for_task(
        self,
        *,
        tenant_id: str,
        clone_id: str | None,
        task: AITask,
        message: str,
    ) -> ModelReply:
        try:
            resolved = self.registry.get_model_for_task(tenant_id=tenant_id, task=task)
            if task == AITask.EMBEDDING:
                self.token_budgeter.validate_embedding_model(model=resolved)
          ***REMOVED***tted = self.token_budgeter.fit_text(
                text=message,
                model=resolved,
                task=task,
                truncate=False,
            )
            adapter = self._provider_adapter_for(resolved)
            params = self._build_generation_params(resolved)
            candidate = RetryCandidate(
                provider_name=resolved.provider,
                model_id=resolved.model_id,
                priority=resolved.priority,
                invoke=lambda: adapter.generate(prompt=fitted.text, params=params),
            )
            reply = self.retry_client.invoke([candidate])
            self._record_invocation(
                tenant_id=tenant_id,
                clone_id=clone_id,
                task=task,
                model_name=resolved.model_id,
                message=fitted.text,
                success=True,
                usage=reply.usage,
                latency_ms=reply.latency_ms or 0,
            )
            return reply
        except (EmbeddingDimensionError, TokenBudgetError, ModelInvocationError) as exc:
            try:
                self._record_invocation(
                    tenant_id=tenant_id,
                    clone_id=clone_id,
                    task=task,
                    model_name=locals().get("resolved").model_id if "resolved" in locals() else "unresolved",
                    message=message,
                    success=False,
                    error_message=str(exc),
                )
            except Exception:
                logger.exception("Failed to persist AIInvocation failure row")
            raise ModelInvocationError(str(exc)) from exc

    def invoke_for_task_stream(
        self,
        *,
        tenant_id: str,
        clone_id: str | None,
        task: AITask,
        message: str,
    ) -> Generator[str, None, None]:
        started = time.monotonic()
        resolved = self.registry.get_model_for_task(tenant_id=tenant_id, task=task)
      ***REMOVED***tted = self.token_budgeter.fit_text(
            text=message,
            model=resolved,
            task=task,
            truncate=False,
        )
        adapter = self._provider_adapter_for(resolved)
        params = self._build_generation_params(resolved)
        chunks: list[str] = []
        try:
            for chunk in adapter.generate_stream(prompt=fitted.text, params=params):
                chunks.append(chunk)
                yield chunk
            self._record_invocation(
                tenant_id=tenant_id,
                clone_id=clone_id,
                task=task,
                model_name=resolved.model_id,
                message=fitted.text,
                success=True,
                usage=None,
                latency_ms=int((time.monotonic() - started) * 1000),
                error_message="stream_usage_missing",
            )
        except Exception as exc:
            self._record_invocation(
                tenant_id=tenant_id,
                clone_id=clone_id,
                task=task,
                model_name=resolved.model_id,
                message=fitted.text,
                success=False,
                latency_ms=int((time.monotonic() - started) * 1000),
                error_message=str(exc),
            )
            raise ModelInvocationError(str(exc)) from exc

    @staticmethod
    def invoke_non_streaming(
        *,
        tenant_id: str,
        clone_id: str,
        message: str,
        session_id: str | None = None,
    ) -> ModelReply:
        """Invoke the LLM and return the complete reply (no streaming)."""
        try:
            return ModelManager().invoke_for_task(
                tenant_id=tenant_id,
                clone_id=clone_id,
                task=AITask.CHAT,
                message=message,
            )
        except Exception as exc:
            logger.exception("invoke_non_streaming failed for clone=%s", clone_id)
            raise ModelInvocationError(str(exc)) from exc

    def get_default_model_instance(
        self,
        *,
        tenant_id: str,
        model_type: ModelType,
    ) -> _ModelInstance:
        """Return a model instance for the given tenant and model type.

        For LLM type, uses the first available API key.
        Other model types are not yet implemented in standalone mode.
        """
        if model_type != ModelType.LLM:
            raise ModelInvocationError(
                f"Model type {model_type!r} is not supported in standalone mode yet."
            )

        return _ModelInstance(tenant_id=tenant_id, model_manager=self)
