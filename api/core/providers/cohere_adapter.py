"""Cohere provider adapter. Supports chat and rerank."""
from __future__ import annotations
import os
import httpx

from api.core.providers.base import ProviderAdapter, ProviderError


COHERE_API_BASE = "https://api.cohere.ai/v1"


class CohereAdapter(ProviderAdapter):
    name = "cohere"

    def __init__(self, api_key: str = None, base_url: str = COHERE_API_BASE, **kwargs):
        if api_key is None:
            api_key = os.environ.get("COHERE_API_KEY", "")
        super().__init__(api_key, base_url=base_url, **kwargs)
        self.base_url = base_url

    def is_available(self) -> bool:
        return bool(self.api_key)

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def chat(self, model, messages, *, max_tokens=1024, temperature=0.7, stream=False, **kwargs):
        # Cohere uses 'preamble' for system + 'message' for last user
        preamble = None
        chat_history = []
        last_user = None
        for msg in messages:
            if msg["role"] == "system":
                preamble = msg["content"]
            elif msg["role"] == "user":
                last_user = msg["content"]
            elif msg["role"] == "assistant" and last_user:
                chat_history.append({"role": "CHATBOT", "message": msg["content"]})
        if not last_user:
            raise ProviderError("Cohere chat requires at least one user message", retriable=False)

        url = f"{self.base_url}/chat"
        payload = {
            "model": model,
            "message": last_user,
            "max_tokens": max_tokens,
            "temperature": temperature,
            **({"preamble": preamble} if preamble else {}),
            **({"chat_history": chat_history} if chat_history else {}),
            **kwargs,
        }
        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"Cohere chat failed: {exc}", retriable=True) from exc

        return {
            "content": data["text"],
            "tokens_in": data.get("meta", {}).get("tokens", {}).get("input_tokens", 0),
            "tokens_out": data.get("meta", {}).get("tokens", {}).get("output_tokens", 0),
            "model": model,
        }

    def rerank(self, model, query, documents, top_n=3, **kwargs):
        """Cohere rerank-v3.0. Returns list of {index, score}."""
        url = f"{self.base_url}/rerank"
        payload = {
            "model": model,
            "query": query,
            "documents": [{"text": d} for d in documents],
            "top_n": top_n,
            **kwargs,
        }
        try:
            with httpx.Client(timeout=30.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"Cohere rerank failed: {exc}", retriable=True) from exc

        return [
            {"index": r["index"], "score": r["relevance_score"]}
            for r in data["results"]
        ]

    def _raise_for_status(self, resp):
        if resp.status_code >= 400:
            retriable = resp.status_code in (429, 500, 502, 503, 504)
            try:
                body = resp.json()
                msg = body.get("message", resp.text)
            except Exception:
                msg = resp.text
            raise ProviderError(
                f"Cohere API {resp.status_code}: {msg}",
                retriable=retriable,
                status_code=resp.status_code,
            )
