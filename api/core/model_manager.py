"""ModelManager — LLM invocation façade (MyOwnClone subset).

This module provides the interface expected by the public chat endpoints,
delegating to the underlying graphon model runtime when available.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


class ModelInvocationError(Exception):
    """Raised when the LLM invocation fails (model unavailable, timeout, etc.)."""


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


class ModelManager:
    """Façade for LLM calls used by MyOwnClone endpoints.

    The real implementation lives in graphon.model_runtime; this module
    provides the interface expected by the public chat endpoints (phase 0.4).
    """

    @staticmethod
    def invoke_non_streaming(
        *,
        tenant_id: str,
        clone_id: str,
        message: str,
        session_id: str | None = None,
    ) -> ModelReply:
        """Invoke the LLM and return the complete reply (no streaming).

        Uses the same ModelManager/ModelType pattern as the existing
        streaming endpoint and inbox helpers.
        """
        try:
            from api.core.model_manager import ModelManager as _Mg  # noqa: F811
            from graphon.model_runtime.entities.model_entities import ModelType

            model_manager = _Mg()
            model_instance = model_manager.get_default_model_instance(
                tenant_id=tenant_id, model_type=ModelType.LLM
            )
            # Build a simple prompt from the message (no RAG here —
            # the plan keeps this endpoint simple; RAG lives in chat_public).
            prompt = message
            reply_text = model_instance.invoke_llm(prompt=prompt)

            return ModelReply(text=reply_text, usage=None)

        except ImportError as exc:
            logger.warning("ModelManager dependencies not available: %s", exc)
            raise ModelInvocationError(
                "LLM runtime (graphon) is not installed or configured."
            ) from exc
        except Exception as exc:
            logger.exception("invoke_non_streaming failed for clone=%s", clone_id)
            raise ModelInvocationError(str(exc)) from exc
