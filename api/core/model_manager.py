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

import logging
import os
from typing import Generator

from api.core.providers import (
    GenerationParams,
    ModelInvocationError,
    ModelReply,
    ModelType,
    ModelUsage,
)

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
    else:
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

    def __init__(self, provider: str):
        self._provider = provider

    def invoke_llm(self, *, prompt: str) -> str:
        reply = _dispatch(prompt, provider=self._provider)
        return reply.text if isinstance(reply, ModelReply) else ""

    def invoke_llm_stream(self, *, prompt: str) -> Generator[str, None, None]:
        yield from _dispatch_stream(prompt, provider=self._provider)


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
    ) -> ModelReply:
        """Invoke the LLM and return the complete reply (no streaming)."""
        provider = _detect_provider()
        if not provider:
            raise ModelInvocationError(
                "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
                "MINIMAX_API_KEY, or TOGETHER_API_KEY in .env"
            )
        try:
            return _dispatch(message, provider=provider)
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

        provider = _detect_provider()
        if not provider:
            raise ModelInvocationError(
                "No LLM API key configured. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, "
                "MINIMAX_API_KEY, or TOGETHER_API_KEY in .env"
            )

        return _ModelInstance(provider=provider)
