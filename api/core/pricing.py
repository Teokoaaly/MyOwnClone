"""LLM and embedding pricing table (per 1M tokens, in USD cents).

Used by:
  - api.core.embeddings.EmbeddingService._record_cost
  - api.core.model_manager._dispatch (FASE 3 — LLM cost tracking)

Prices are approximate public list prices as of 2026-06. They exist to give
the platform admin a ballpark of spend in the cost_tracking table, NOT for
exact billing reconciliation. Update them when providers change pricing.

All functions return INTEGER cents (1 USD = 100 cents) to match the
`cost_tracking.cost_cents` column type.
"""

from __future__ import annotations


# (model_pattern, price_usd_per_1m_input_cents, price_usd_per_1m_output_cents)
# Prices in USD cents per 1_000_000 tokens.
_LLM_PRICES_CENTS_PER_M = [
    # OpenAI
    ("gpt-4o-mini",        150,    600),
    ("gpt-4o",            2500,  10000),
    ("gpt-4.1-mini",       400,   1600),
    ("gpt-3.5",            500,   1500),
    # DeepSeek (OpenAI-compatible)
    ("deepseek-chat",      140,    280),
    ("deepseek-reasoner",  550,   2200),
    # Anthropic
    ("claude-3-haiku",     250,   1250),
    ("claude-3-5-haiku",   800,   4000),
    ("claude-3-sonnet",   3000,  15000),
    # MiniMax
    ("minimax-m2.7",       100,    300),
    # Together.ai (Llama 3)
    ("llama-3-8b",         180,    180),
    ("llama-3-70b",        880,    880),
    # Fallback
    ("",                   200,    600),
]

# Embeddings: price in USD cents per 1_000_000 tokens (input only).
_EMBEDDING_PRICES_CENTS_PER_M = [
    ("text-embedding-3-small",   20),
    ("text-embedding-3-large",   130),
    ("text-embedding-ada-002",   100),
    ("",                         100),  # fallback
]


def _match(patterns: list[tuple], model: str, default_index: int = -1) -> tuple:
    needle = (model or "").lower()
    for entry in patterns:
        pattern = entry[0].lower()
        if pattern and pattern in needle:
            return entry
    return patterns[default_index]


def estimate_llm_cost_cents(
    *, model: str, tokens_in: int, tokens_out: int
) -> int:
    """Estimate the cost in USD cents of an LLM call."""
    _, in_per_m, out_per_m = _match(_LLM_PRICES_CENTS_PER_M, model)
    cost = (tokens_in * in_per_m + tokens_out * out_per_m) / 1_000_000
    return int(round(cost))


def estimate_embedding_cost_cents(*, model: str, tokens: int) -> int:
    """Estimate the cost in USD cents of an embedding call."""
    _, per_m = _match(_EMBEDDING_PRICES_CENTS_PER_M, model)
    return int(round(tokens * per_m / 1_000_000))
