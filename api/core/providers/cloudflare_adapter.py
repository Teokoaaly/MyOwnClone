"""Cloudflare Workers AI provider adapter. OpenAI-compatible.

base_url configurable via CLOUDFLARE_BASE_URL env var.
10k neurons/day free tier per model (documented as comment).

API docs: https://developers.cloudflare.com/workers-ai/
"""
from __future__ import annotations

import os

from api.core.providers.openai_adapter import OpenAIAdapter


class CloudflareAdapter(OpenAIAdapter):
    """Cloudflare Workers AI — OpenAI-compatible adapter.

    Free tier: 10,000 neurons/day per account.
    Models: @cf/meta/llama-3-8b-instruct, @cf/tiiuae/falcon-7b-instruct, etc.

    Usage:
        adapter = CloudflareAdapter()
        response = adapter.chat("llama-3-8b-instruct", messages)
    """
    name = "cloudflare"

    # Default Cloudflare Workers AI base URL
    DEFAULT_BASE_URL = "https://api.cloudflare.com/client/v4"

    def __init__(self, api_key: str = None, base_url: str = None, **kwargs):
        if api_key is None:
            api_key = os.environ.get("CLOUDFLARE_API_KEY", "")
        if base_url is None:
            base_url = os.environ.get("CLOUDFLARE_BASE_URL", self.DEFAULT_BASE_URL)
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

    def is_available(self) -> bool:
        """Check if Cloudflare API key is configured."""
        return bool(self.api_key)

    def _headers(self):
        """Add Cloudflare-specific headers."""
        headers = super()._headers()
        # Cloudflare uses Authorization: Bearer <API_KEY>
        return headers
