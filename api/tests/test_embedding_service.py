"""Tests for EmbeddingService."""
from __future__ import annotations
from unittest.mock import MagicMock, patch

import pytest

from api.core.embeddings import EmbeddingService, FallbackEmbeddingService


# ---------- FallbackEmbeddingService ----------

def test_fallback_embed_texts():
    service = FallbackEmbeddingService()
    vectors = service.embed_texts("tenant-1", ["hello", "world"])
    assert len(vectors) == 2
    assert all(len(v) == 1536 for v in vectors)
    assert vectors[0] != vectors[1]  # different inputs -> different vectors


def test_fallback_embed_query():
    service = FallbackEmbeddingService()
    v = service.embed_query("tenant-1", "test")
    assert len(v) == 1536


def test_fallback_embed_texts_empty():
    service = FallbackEmbeddingService()
    assert service.embed_texts("tenant-1", []) == []


# ---------- EmbeddingService (real) ----------

def test_real_embed_uses_registry_and_records_cost():
    service = EmbeddingService()
    mock_model = MagicMock()
    mock_model.id = "model-1"
    mock_model.provider = "openai"
    mock_model.name = "text-embedding-3-small"
    mock_model.input_cost_per_1k = 1
    mock_model.output_cost_per_1k = 0
    mock_model.config = {"api_key": "test-key"}
    
    mock_adapter = MagicMock()
    mock_adapter.embed.return_value = [[0.1, 0.2], [0.3, 0.4]]
    
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = mock_model
    
    mock_retry = MagicMock()
    mock_retry.call.return_value = [[0.1, 0.2], [0.3, 0.4]]
    
    with patch("api.core.embeddings.get_registry", return_value=mock_registry), \
         patch("api.core.embeddings.get_retry_client", return_value=mock_retry), \
         patch("api.core.embeddings._select_provider", return_value=mock_adapter), \
         patch("api.core.embeddings._record_llm_cost") as mock_record:
        result = service.embed_texts("tenant-1", ["hello", "world"])
    
    assert result == [[0.1, 0.2], [0.3, 0.4]]
    mock_registry.get_model_for_task.assert_called_once_with("tenant-1", "embedding")
    mock_record.assert_called_once()
    call_args = mock_record.call_args
    assert call_args.kwargs["tenant_id"] == "tenant-1"
    assert call_args.kwargs["model"] == "text-embedding-3-small"
    assert call_args.kwargs["category"].name == "CONTENT_INGESTION"


def test_real_embed_no_model_raises():
    service = EmbeddingService()
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = None
    with patch("api.core.embeddings.get_registry", return_value=mock_registry):
        with pytest.raises(RuntimeError, match="No embedding model"):
            service.embed_texts("tenant-1", ["hello"])


def test_real_embed_batch_processing():
    """Large input should be split into batches."""
    service = EmbeddingService(batch_size=2)
    mock_model = MagicMock()
    mock_model.id = "model-1"
    mock_model.provider = "openai"
    mock_model.name = "text-embedding-3-small"
    mock_model.input_cost_per_1k = 1
    mock_model.config = {"api_key": "test-key"}
    
    # Per-batch return values for adapter.embed
    batch_results = [
        [[0.1, 0.2], [0.3, 0.4]],  # batch 1
        [[0.5, 0.6], [0.7, 0.8]],  # batch 2
        [[0.9, 1.0]],              # batch 3 (partial)
    ]
    mock_adapter = MagicMock()
    mock_adapter.embed.side_effect = batch_results
    
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = mock_model
    
    # Use a callable side_effect so retry_client.call actually executes the lambda
    # (which in turn calls adapter.embed).
    def retry_call_side_effect(*args, **kwargs):
        # Execute the lambda passed as the first positional arg
        func = args[0] if args else kwargs.get('func')
        # Execute the lambda (which calls adapter.embed)
        return func()
    mock_retry = MagicMock()
    mock_retry.call.side_effect = retry_call_side_effect
    
    with patch("api.core.embeddings.get_registry", return_value=mock_registry), \
         patch("api.core.embeddings.get_retry_client", return_value=mock_retry), \
         patch("api.core.embeddings._select_provider", return_value=mock_adapter), \
         patch("api.core.embeddings._record_llm_cost"):
        result = service.embed_texts("tenant-1", ["a", "b", "c", "d", "e"])
    
    assert len(result) == 5
    assert mock_adapter.embed.call_count == 3  # 3 batches


def test_real_embed_empty_input_returns_empty():
    service = EmbeddingService()
    assert service.embed_texts("tenant-1", []) == []


def test_real_embed_records_failure_on_error():
    service = EmbeddingService()
    mock_model = MagicMock()
    mock_model.id = "model-1"
    mock_model.provider = "openai"
    mock_model.name = "text-embedding-3-small"
    mock_model.input_cost_per_1k = 1
    mock_model.config = {"api_key": "test-key"}
    
    mock_registry = MagicMock()
    mock_registry.get_model_for_task.return_value = mock_model
    
    mock_retry = MagicMock()
    mock_retry.call.side_effect = RuntimeError("embed failed")
    
    with patch("api.core.embeddings.get_registry", return_value=mock_registry), \
         patch("api.core.embeddings.get_retry_client", return_value=mock_retry), \
         patch("api.core.embeddings._select_provider", return_value=MagicMock()), \
         patch("api.core.embeddings._record_llm_cost") as mock_record:
        with pytest.raises(RuntimeError, match="embed failed"):
            service.embed_texts("tenant-1", ["hello"])
    
    mock_record.assert_called_once()
    call_args = mock_record.call_args
    assert call_args.kwargs["success"] is False
    assert "embed failed" in call_args.kwargs["error_message"]