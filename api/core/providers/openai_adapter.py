"""OpenAI provider adapter. Supports chat, embeddings, moderation."""
from __future__ import annotations
import os
from typing import Iterator, Any
import httpx

from api.core.providers.base import ProviderAdapter, ProviderError


OPENAI_API_BASE = "https://api.openai.com/v1"


class OpenAIAdapter(ProviderAdapter):
    name = "openai"

    def __init__(self, api_key: str = None, base_url: str = OPENAI_API_BASE, **kwargs):
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY", "")
        super().__init__(api_key, base_url=base_url, **kwargs)
        self.base_url = base_url

    def is_available(self) -> bool:
        return bool(self.api_key)

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def chat(
        self,
        model: str,
        messages: list[dict[str, str]],
        *,
        max_tokens: int = 1024,
        temperature: float = 0.7,
        stream: bool = False,
        **kwargs,
    ):
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream,
            **kwargs,
        }
        if stream:
            return self._stream_chat(url, payload)
        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"OpenAI chat failed: {exc}", retriable=True) from exc

        choice = data["choices"][0]
        usage = data.get("usage", {})
        return {
            "content": choice["message"]["content"],
            "tokens_in": usage.get("prompt_tokens", 0),
            "tokens_out": usage.get("completion_tokens", 0),
            "model": data.get("model", model),
        }

    def _stream_chat(self, url: str, payload: dict) -> Iterator[str]:
        try:
            with httpx.Client(timeout=60.0) as client:
                with client.stream("POST", url, json=payload, headers=self._headers()) as resp:
                    self._raise_for_status(resp)
                    for line in resp.iter_lines():
                        if line.startswith("data: "):
                            chunk_data = line[6:]
                            if chunk_data == "[DONE]":
                                break
                            try:
                                import json
                                chunk = json.loads(chunk_data)
                                delta = chunk.get("choices", [{}])[0].get("delta", {})
                                content = delta.get("content")
                                if content:
                                    yield content
                            except (json.JSONDecodeError, KeyError, IndexError):
                                continue
        except httpx.HTTPError as exc:
            raise ProviderError(f"OpenAI stream failed: {exc}", retriable=True) from exc

    def embed(self, model: str, texts: list[str], **kwargs) -> list[list[float]]:
        """Default: text-embedding-3-small (1536d) or text-embedding-3-large (3072d)."""
        url = f"{self.base_url}/embeddings"
        payload = {"model": model, "input": texts, **kwargs}
        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"OpenAI embed failed: {exc}", retriable=True) from exc
        return [item["embedding"] for item in data["data"]]

    def moderate(self, text: str, **kwargs) -> dict:
        """OpenAI Moderation API. Free as of 2024-06."""
        url = f"{self.base_url}/moderations"
        payload = {"input": text, **kwargs}
        try:
            with httpx.Client(timeout=30.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"OpenAI moderate failed: {exc}", retriable=True) from exc
        result = data["results"][0]
        return {
            "flagged": result["flagged"],
            "categories": result["categories"],
            "scores": result["category_scores"],
        }

    def _raise_for_status(self, resp):
        if resp.status_code >= 400:
            retriable = resp.status_code in (429, 500, 502, 503, 504)
            try:
                body = resp.json()
                msg = body.get("error", {}).get("message", resp.text)
            except Exception:
                msg = resp.text
            raise ProviderError(
                f"OpenAI API {resp.status_code}: {msg}",
                retriable=retriable,
                status_code=resp.status_code,
            )
