"""Embedding generation through the configurable model registry."""

from __future__ import annotations

import requests
from typing import Iterable

from api.core.model_registry import ModelRegistry, ResolvedModelConfig
from api.core.providers import ModelInvocationError
from api.core.token_budget import TokenBudgeter
from api.models.ai_models import AITask

_OPENAI_BATCH_SIZE = 64


class EmbeddingService:
    """Resolve embedding model configuration and generate embeddings in batches."""

    def __init__(
        self,
        *,
        registry: ModelRegistry | None = None,
        token_budgeter: TokenBudgeter | None = None,
    ) -> None:
        self.registry = registry or ModelRegistry()
        self.token_budgeter = token_budgeter or TokenBudgeter()

    def embed_texts(
        self,
        texts: list[str],
        *,
        tenant_id: str | None = None,
        model: ResolvedModelConfig | None = None,
    ) -> list[list[float]]:
        if not texts:
            return []

        resolved = model or self.registry.get_model_for_task(
            tenant_id=tenant_id,
            task=AITask.EMBEDDING,
        )
        self.token_budgeter.validate_embedding_model(model=resolved)
        batches = [texts[i:i + _OPENAI_BATCH_SIZE] for i in range(0, len(texts), _OPENAI_BATCH_SIZE)]
        vectors: list[list[float]] = []
        for batch in batches:
            vectors.extend(self._embed_batch(batch, model=resolved))
        return vectors

    def _embed_batch(
        self,
        texts: list[str],
        *,
        model: ResolvedModelConfig,
    ) -> list[list[float]]:
        if model.provider not in {"openai", "openai_compatible", "local", "minimax", "together"}:
            raise ModelInvocationError(
                f"Provider {model.provider!r} does not support embeddings in M8."
            )
        if not model.api_key:
            raise ModelInvocationError("Embedding model requires a decrypted api_key.")
        if model.provider == "local":
            return self._embed_batch_local(texts, model=model)
        if model.provider == "minimax":
            return self._embed_batch_minimax(texts, model=model)

        try:
            import openai
        except ImportError as exc:
            raise ModelInvocationError("openai package not installed") from exc

        kwargs = {"api_key": model.api_key}
        if model.base_url:
            kwargs["base_url"] = model.base_url
        client = openai.OpenAI(**kwargs)
        response = client.embeddings.create(
            model=model.model_id,
            input=texts,
        )
        return [row.embedding for row in response.data]

    def _embed_batch_minimax(
        self,
        texts: list[str],
        *,
        model: ResolvedModelConfig,
    ) -> list[list[float]]:
        base_url = (model.base_url or "https://api.minimax.io/v1").rstrip("/")
        response = requests.post(
            f"{base_url}/embeddings",
            headers={
                "Authorization": f"Bearer {model.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model.model_id,
                "texts": texts,
                "type": "db",
            },
            timeout=60,
        )
        if response.status_code >= 400:
            raise ModelInvocationError(
                f"MiniMax embeddings request failed with status {response.status_code}: "
                f"{response.text[:200]}"
            )

        payload = response.json()
        base_resp = payload.get("base_resp") or {}
        if base_resp.get("status_code") not in (0, None):
            raise ModelInvocationError(
                f"MiniMax embeddings error {base_resp.get('status_code')}: "
                f"{base_resp.get('status_msg', 'unknown error')}"
            )

        vectors = payload.get("vectors")
        if not isinstance(vectors, list):
            raise ModelInvocationError("MiniMax embeddings response did not include vectors.")
        return vectors

    def _embed_batch_local(
        self,
        texts: list[str],
        *,
        model: ResolvedModelConfig,
    ) -> list[list[float]]:
        base_url = (model.base_url or "http://127.0.0.1:11434/v1").rstrip("/")
        if base_url.endswith("/v1"):
            base_url = base_url[:-3]

        response = requests.post(
            f"{base_url}/api/embed",
            headers={"Content-Type": "application/json"},
            json={
                "model": model.model_id,
                "input": texts if len(texts) > 1 else texts[0],
            },
            timeout=180,
        )
        if response.status_code >= 400:
            raise ModelInvocationError(
                f"Local embeddings request failed with status {response.status_code}: "
                f"{response.text[:200]}"
            )

        payload = response.json()
        vectors = payload.get("embeddings")
        if not isinstance(vectors, list):
            raise ModelInvocationError("Local embeddings response did not include embeddings.")
        return [list(vector) for vector in vectors]
