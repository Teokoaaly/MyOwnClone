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

Generation parameters (FASE 3 of the standard RAG pipeline):
  - LLM_TEMPERATURE  default 0.30   (factual; raise to 0.7 for sales)
  - LLM_MAX_TOKENS   default 1024   (bounded; prevents runaway cost)
  - LLM_TOP_P        default 1.0    (nucleus sampling)
  Per-mode override: chat_public reads CloneModePrompt.temperature when set.

Cost tracking (FASE 3):
  Each non-streaming call inserts a row into cost_tracking with the
  estimated cost in USD cents (see api.core.pricing).

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

import enum
import logging
import os
from dataclasses import dataclass, field
from typing import Generator

logger = logging.getLogger(__name__)


# ─── Public exceptions ───────────────────────────────────────────────────────

class ModelInvocationError(Exception):
    """Raised when the LLM invocation fails (model unavailable, timeout, etc.)."""


# ─── Value objects ───────────────────────────────────────────────────────────

class ModelType(enum.StrEnum):
    """Model type selector (mirrors graphon.model_runtime interface)."""
    LLM = "llm"
    EMBEDDING = "embedding"
    RERANKING = "reranking"
    SPEECH2TEXT = "speech2text"
    TTS = "tts"
    MODERATION = "moderation"


@dataclass
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


@dataclass
class ModelReply:
    """Reply returned by invoke_non_streaming."""

    text: str = ""
    usage: ModelUsage | None = None


# ─── Generation parameters ───────────────────────────────────────────────────


@dataclass(frozen=True)
class GenerationParams:
    """LLM sampling parameters.

    Resolve order: per-call override > CloneModePrompt.temperature (chat) >
    environment defaults.
    """
    temperature: float = 0.30
    max_tokens: int = 1024
    top_p: float = 1.0

    @classmethod
    def from_env(cls) -> "GenerationParams":
        """Read LLM_TEMPERATURE / LLM_MAX_TOKENS / LLM_TOP_P from the environment."""
        def _f(name: str, default: float) -> float:
            raw = os.getenv(name, "").strip()
            if not raw:
                return default
            try:
                return float(raw)
            except ValueError:
                logger.warning("Invalid %s=%r, using default %s", name, raw, default)
                return default

        def _i(name: str, default: int) -> int:
            raw = os.getenv(name, "").strip()
            if not raw:
                return default
            try:
                value = int(float(raw))
                return max(1, value)
            except ValueError:
                logger.warning("Invalid %s=%r, using default %s", name, raw, default)
                return default

        return cls(
            temperature=max(0.0, min(2.0, _f("LLM_TEMPERATURE", 0.30))),
            max_tokens=_i("LLM_MAX_TOKENS", 1024),
            top_p=max(0.0, min(1.0, _f("LLM_TOP_P", 1.0))),
        )


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


# ─── Cost tracking ───────────────────────────────────────────────────────────


def _record_llm_cost(
    *,
    tenant_id: str | None,
    model: str,
    usage: ModelUsage | None,
    operation: str = "invoke_llm",
) -> None:
    """Best-effort INSERT into cost_tracking. Never raises."""
    if not tenant_id or not usage or usage.total_tokens == 0:
        return
    try:
        from api.extensions.ext_database import db
        from api.models.analytics import CostTracking
        from api.core.pricing import estimate_llm_cost_cents

        cost_cents = estimate_llm_cost_cents(
            model=model,
            tokens_in=usage.prompt_tokens,
            tokens_out=usage.completion_tokens,
        )
        db.session.add(
            CostTracking(
                tenant_id=tenant_id,
                category="clone_response",
                operation=operation,
                model=model,
                tokens_in=usage.prompt_tokens,
                tokens_out=usage.completion_tokens,
                cost_cents=cost_cents,
            )
        )
        db.session.commit()
    except Exception:
        # Cost tracking is observability; never fatal to the chat.
        logger.debug("Could not persist LLM cost", exc_info=True)


# ─── OpenAI backend ──────────────────────────────────────────────────────────

def _invoke_openai(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
    tenant_id: str | None = None,
) -> ModelReply:
    """Invoke OpenAI (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("OPENAI_MODEL", "gpt-4o-mini")
    client = openai.OpenAI(**_openai_client_kwargs())
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
    )
    usage = response.usage
    model_usage = ModelUsage(
        prompt_tokens=usage.prompt_tokens if usage else 0,
        completion_tokens=usage.completion_tokens if usage else 0,
        total_tokens=usage.total_tokens if usage else 0,
    )
    _record_llm_cost(tenant_id=tenant_id, model=model, usage=model_usage)
    return ModelReply(text=response.choices[0].message.content or "", usage=model_usage)


def _invoke_openai_stream(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
):
    """Invoke OpenAI (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("OPENAI_MODEL", "gpt-4o-mini")
    client = openai.OpenAI(**_openai_client_kwargs())
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── Anthropic backend ───────────────────────────────────────────────────────

def _invoke_anthropic(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
    tenant_id: str | None = None,
) -> ModelReply:
    """Invoke Anthropic (non-streaming)."""
    try:
        import anthropic
    except ImportError as exc:
        raise ModelInvocationError("anthropic package not installed") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=model,
        max_tokens=params.max_tokens,
        temperature=params.temperature,
        top_p=params.top_p,
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.content[0].text if response.content else ""
    usage = response.usage
    model_usage = ModelUsage(
        prompt_tokens=usage.input_tokens if usage else 0,
        completion_tokens=usage.output_tokens if usage else 0,
        total_tokens=(usage.input_tokens + usage.output_tokens) if usage else 0,
    )
    _record_llm_cost(tenant_id=tenant_id, model=model, usage=model_usage)
    return ModelReply(text=content, usage=model_usage)


def _invoke_anthropic_stream(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
):
    """Invoke Anthropic (streaming)."""
    try:
        import anthropic
    except ImportError as exc:
        raise ModelInvocationError("anthropic package not installed") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    with client.messages.stream(
        model=model,
        max_tokens=params.max_tokens,
        temperature=params.temperature,
        top_p=params.top_p,
        messages=[{"role": "user", "content": prompt}],
    ) as stream_ctx:
        for text in stream_ctx.text_stream:
            yield text


# ─── Together.ai backend (Llama 3) ───────────────────────────────────────────

def _invoke_together(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
    tenant_id: str | None = None,
) -> ModelReply:
    """Invoke Together.ai (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for Together.ai client)") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("TOGETHER_MODEL", "meta-llama/Llama-3-8b-chat-hf")
    client = openai.OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
    )
    usage = response.usage
    model_usage = ModelUsage(
        prompt_tokens=usage.prompt_tokens if usage else 0,
        completion_tokens=usage.completion_tokens if usage else 0,
        total_tokens=usage.total_tokens if usage else 0,
    )
    _record_llm_cost(tenant_id=tenant_id, model=model, usage=model_usage)
    return ModelReply(text=response.choices[0].message.content or "", usage=model_usage)


def _invoke_together_stream(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
):
    """Invoke Together.ai (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for Together.ai client)") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("TOGETHER_MODEL", "meta-llama/Llama-3-8b-chat-hf")
    client = openai.OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── MiniMax backend (OpenAI-compatible) ─────────────────────────────────────

def _invoke_minimax(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
    tenant_id: str | None = None,
) -> ModelReply:
    """Invoke MiniMax via its OpenAI-compatible endpoint (non-streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for MiniMax)") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("MINIMAX_MODEL", "minimax-m2.7")
    client = openai.OpenAI(
        api_key=os.environ["MINIMAX_API_KEY"],
        base_url="https://api.minimax.io/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
    )
    usage = response.usage
    model_usage = ModelUsage(
        prompt_tokens=usage.prompt_tokens if usage else 0,
        completion_tokens=usage.completion_tokens if usage else 0,
        total_tokens=usage.total_tokens if usage else 0,
    )
    _record_llm_cost(tenant_id=tenant_id, model=model, usage=model_usage)
    return ModelReply(text=response.choices[0].message.content or "", usage=model_usage)


def _invoke_minimax_stream(
    prompt: str,
    *,
    model: str | None = None,
    params: GenerationParams | None = None,
):
    """Invoke MiniMax via its OpenAI-compatible endpoint (streaming)."""
    try:
        import openai
    except ImportError as exc:
        raise ModelInvocationError("openai package not installed (needed for MiniMax)") from exc
    params = params or GenerationParams.from_env()
    model = model or _env("MINIMAX_MODEL", "minimax-m2.7")
    client = openai.OpenAI(
        api_key=os.environ["MINIMAX_API_KEY"],
        base_url="https://api.minimax.io/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        top_p=params.top_p,
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ─── Dispatch ────────────────────────────────────────────────────────────────

def _dispatch(
    prompt: str,
    *,
    provider: str,
    params: GenerationParams | None = None,
    tenant_id: str | None = None,
) -> ModelReply:
    if provider == "openai":
        return _invoke_openai(prompt, params=params, tenant_id=tenant_id)
    elif provider == "anthropic":
        return _invoke_anthropic(prompt, params=params, tenant_id=tenant_id)
    elif provider == "minimax":
        return _invoke_minimax(prompt, params=params, tenant_id=tenant_id)
    elif provider == "together":
        return _invoke_together(prompt, params=params, tenant_id=tenant_id)
    else:
        raise ModelInvocationError(
            "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
            "MINIMAX_API_KEY, or TOGETHER_API_KEY in your environment."
        )


def _dispatch_stream(
    prompt: str,
    *,
    provider: str,
    params: GenerationParams | None = None,
) -> Generator[str, None, None]:
    if provider == "openai":
        yield from _invoke_openai_stream(prompt, params=params)
    elif provider == "anthropic":
        yield from _invoke_anthropic_stream(prompt, params=params)
    elif provider == "minimax":
        yield from _invoke_minimax_stream(prompt, params=params)
    elif provider == "together":
        yield from _invoke_together_stream(prompt, params=params)
    else:
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

    def __init__(self, provider: str, params: GenerationParams | None = None, tenant_id: str | None = None):
        self._provider = provider
        self._params = params
        self._tenant_id = tenant_id

    def invoke_llm(self, *, prompt: str) -> str:
        reply = _dispatch(
            prompt,
            provider=self._provider,
            params=self._params,
            tenant_id=self._tenant_id,
        )
        return reply.text if isinstance(reply, ModelReply) else ""

    def invoke_llm_stream(self, *, prompt: str) -> Generator[str, None, None]:
        yield from _dispatch_stream(prompt, provider=self._provider, params=self._params)


# ─── Public façade ───────────────────────────────────────────────────────────

class ModelManager:
    """Façade for LLM calls used by MyOwnClone endpoints.

    Provides both the class-method interface (used by chat_public_simple)
    and an instance interface with get_default_model_instance (used by
    the streaming endpoint for graphon compatibility).
    """

    @staticmethod
    def invoke_non_streaming(
        *,
        tenant_id: str,
        clone_id: str,
        message: str,
        session_id: str | None = None,
        params: GenerationParams | None = None,
    ) -> ModelReply:
        """Invoke the LLM and return the complete reply (no streaming)."""
        provider = _detect_provider()
        if not provider:
            raise ModelInvocationError(
                "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
                "MINIMAX_API_KEY, or TOGETHER_API_KEY in .env"
            )
        try:
            return _dispatch(message, provider=provider, params=params, tenant_id=tenant_id)
        except Exception as exc:
            logger.exception("invoke_non_streaming failed for clone=%s", clone_id)
            raise ModelInvocationError(str(exc)) from exc

    def get_default_model_instance(
        self,
        *,
        tenant_id: str,
        model_type: ModelType,
        params: GenerationParams | None = None,
    ) -> _ModelInstance:
        """Return a model instance for the given tenant and model type.

        For LLM type, uses the first available API key.
        Other model types are not yet implemented in standalone mode.
        """
        if model_type != ModelType.LLM:
            raise ModelInvocationError(
                f"Model type {model_type!r} is not supported in standalone mode yet."
            )

        provider = _detect_provider()
        if not provider:
            raise ModelInvocationError(
                "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
                "MINIMAX_API_KEY, or TOGETHER_API_KEY in .env"
            )

        return _ModelInstance(provider=provider, params=params, tenant_id=tenant_id)
