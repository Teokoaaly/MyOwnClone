"""Tests for the refactored ModelManager.

Verifies:
- invoke_for_task uses ModelRegistry to select model
- invoke_for_task uses RetryClient for retries
- invoke_for_task records cost via _record_llm_cost
- _select_provider dispatches to the right adapter
"""
from __future__ import annotations
import time
from unittest.mock import MagicMock, patch

import pytest

from api.core.cost_recording import _record_llm_cost
from api.core.providers import OpenAIAdapter
from api.core.providers.base import ProviderError


# --- _select_provider ---

def test_select_provider_openai():
    from api.core.model_manager import _select_provider
    model = MagicMock(provider="openai", name="gpt-4o-mini")
    api_key = "test-key"
    adapter = _select_provider(model, api_key)
    assert isinstance(adapter, OpenAIAdapter)


def test_select_provider_unknown_raises():
    from api.core.model_manager import _select_provider
    model = MagicMock(provider="unknown", name="x")
    with pytest.raises(ValueError, match="Unknown provider"):
        _select_provider(model, "key")


# --- _calculate_cost_cents ---

def test_calculate_cost_cents_basic():
    from api.core.model_manager import _calculate_cost_cents
    # 1000 input tokens @ 10 cents/1k = 10 cents
    # 500 output tokens @ 20 cents/1k = 10 cents
    # Total: 20 cents
    cost = _calculate_cost_cents(
        tokens_in=1000, tokens_out=500,
        cost_per_1k_input_cents=10,  # 10 cents per 1k input
        cost_per_1k_output_cents=20,  # 20 cents per 1k output
    )
    # (1000/1000)*10 + (500/1000)*20 = 10 + 10 = 20
    assert cost == 20


def test_calculate_cost_cents_with_zero_costs():
    from api.core.model_manager import _calculate_cost_cents
    cost = _calculate_cost_cents(1000, 1000, None, None)
    assert cost == 0


# --- invoke_for_task (high-level) ---

def test_invoke_for_task_uses_registry_and_records_cost():
    """End-to-end: registry picks model, retry calls adapter, cost is recorded."""
    from api.core.model_manager import invoke_for_task

    # Mock AIModel (using actual field names: input_cost_per_1k, output_cost_per_1k)
    mock_model = MagicMock()
    mock_model.id = "model-1"
    mock_model.provider = "openai"
    mock_model.name = "gpt-4o-mini"
    mock_model.input_cost_per_1k = 10
    mock_model.output_cost_per_1k = 20
    mock_model.config = {}

    # Mock adapter
    mock_adapter = MagicMock()
    mock_adapter.chat.return_value = {
        "content": "Hello",
        "tokens_in": 100,
        "tokens_out": 50,
        "model": "gpt-4o-mini",
    }

    # Mock registry
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = mock_model

    # Mock retry client
    mock_retry = MagicMock()
    mock_retry.call.return_value = mock_adapter.chat.return_value

    # Mock cost recording - patch where the function is defined, not where it's imported
    with patch("api.core.model_registry.get_registry", return_value=mock_registry), \
         patch("api.core.retry_client.get_retry_client", return_value=mock_retry), \
         patch("api.core.model_manager._select_provider", return_value=mock_adapter), \
         patch("api.core.cost_recording._record_llm_cost") as mock_record:
        result = invoke_for_task(
            tenant_id="tenant-1",
            task="chat",
            messages=[{"role": "user", "content": "Hi"}],
        )

    assert result["content"] == "Hello"
    mock_registry.get_model_for_task.assert_called_once_with("tenant-1", "chat", session=None)
    mock_retry.call.assert_called_once()
    mock_record.assert_called_once()
    # Verify cost recording args
    call_args = mock_record.call_args
    assert call_args.kwargs["tenant_id"] == "tenant-1"
    assert call_args.kwargs["model"] == "gpt-4o-mini"
    assert call_args.kwargs["tokens_in"] == 100
    assert call_args.kwargs["tokens_out"] == 50


def test_invoke_for_task_no_model_raises():
    from api.core.model_manager import invoke_for_task
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = None
    with patch("api.core.model_registry.get_registry", return_value=mock_registry):
        with pytest.raises(RuntimeError, match="No active model"):
            invoke_for_task(
                tenant_id="tenant-1",
                task="chat",
                messages=[{"role": "user", "content": "Hi"}],
            )


def test_invoke_for_task_records_failure():
    """If all retries fail, the cost helper is called with success=False."""
    from api.core.model_manager import invoke_for_task

    mock_model = MagicMock()
    mock_model.id = "model-1"
    mock_model.provider = "openai"
    mock_model.name = "gpt-4o-mini"
    mock_model.input_cost_per_1k = 10
    mock_model.output_cost_per_1k = 20
    mock_model.config = {}

    mock_adapter = MagicMock()
    mock_adapter.chat.side_effect = ProviderError("boom", retriable=True)

    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = mock_model

    mock_retry = MagicMock()
    mock_retry.call.side_effect = ProviderError("boom", retriable=True)

    with patch("api.core.model_registry.get_registry", return_value=mock_registry), \
         patch("api.core.retry_client.get_retry_client", return_value=mock_retry), \
         patch("api.core.model_manager._select_provider", return_value=mock_adapter), \
         patch("api.core.cost_recording._record_llm_cost") as mock_record:
        with pytest.raises(ProviderError):
            invoke_for_task(
                tenant_id="tenant-1",
                task="chat",
                messages=[{"role": "user", "content": "Hi"}],
            )
    # Failure was recorded
    mock_record.assert_called_once()
    call_args = mock_record.call_args
    assert call_args.kwargs["success"] is False
    assert call_args.kwargs["error_message"] == "boom"
