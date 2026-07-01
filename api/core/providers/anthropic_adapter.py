"""Anthropic provider adapter. Supports chat only (no embeddings natively)."""
from __future__ import annotations
import os
from typing import Iterator
import httpx

from api.core.providers.base import ProviderAdapter, ProviderError


ANTHROPIC_API_BASE = "https://api.anthropic.com/v1"
ANTHROPIC_API_VERSION = "2023-06-01"


class AnthropicAdapter(ProviderAdapter):
    name = "anthropic"

    def __init__(self, api_key: str = None, base_url: str = ANTHROPIC_API_BASE, **kwargs):
        if api_key is None:
            api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        super().__init__(api_key, base_url=base_url, **kwargs)
        self.base_url = base_url

    def is_available(self) -> bool:
        return bool(self.api_key)

    def _headers(self) -> dict:
        return {
            "x-api-key": self.api_key,
            "anthropic-version": ANTHROPIC_API_VERSION,
            "Content-Type": "application/json",
        }

    def chat(self, model, messages, *, max_tokens=1024, temperature=0.7, stream=False, **kwargs):
        # Extract system message if present
        system_msg = None
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_msg = msg["content"]
            else:
                chat_messages.append(msg)

        url = f"{self.base_url}/messages"
        payload = {
            "model": model,
            "messages": chat_messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            **kwargs,
        }
        if system_msg:
            payload["system"] = system_msg
        if stream:
            return self._stream_chat(url, payload)

        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, json=payload, headers=self._headers())
                self._raise_for_status(resp)
                data = resp.json()
        except httpx.HTTPError as exc:
            raise ProviderError(f"Anthropic chat failed: {exc}", retriable=True) from exc

        return {
            "content": data["content"][0]["text"],
            "tokens_in": data["usage"]["input_tokens"],
            "tokens_out": data["usage"]["output_tokens"],
            "model": data.get("model", model),
        }

    def _stream_chat(self, url, payload):
        # Anthropic SSE format with content_block_delta events
        try:
            with httpx.Client(timeout=60.0) as client:
                with client.stream("POST", url, json=payload, headers=self._headers()) as resp:
                    self._raise_for_status(resp)
                    for line in resp.iter_lines():
                        if line.startswith("data: "):
                            try:
                                import json
                                event = json.loads(line[6:])
                                if event.get("type") == "content_block_delta":
                                    delta = event.get("delta", {})
                                    text = delta.get("text")
                                    if text:
                                        yield text
                            except (json.JSONDecodeError, KeyError):
                                continue
        except httpx.HTTPError as exc:
            raise ProviderError(f"Anthropic stream failed: {exc}", retriable=True) from exc

    def _raise_for_status(self, resp):
        if resp.status_code >= 400:
            retriable = resp.status_code in (429, 500, 502, 503, 504, 529)
            try:
                body = resp.json()
                msg = body.get("error", {}).get("message", resp.text)
            except Exception:
                msg = resp.text
            raise ProviderError(
                f"Anthropic API {resp.status_code}: {msg}",
                retriable=retriable,
                status_code=resp.status_code,
            )
