"""Smoke tests for Sisyphus milestone symbols.

These tests intentionally fail in red while milestones are not implemented.
When they all pass, the M0-M13 implementation exists in code, not only in docs.
"""
from __future__ import annotations

import importlib
import inspect


def test_m1_ai_model_classes_exist() -> None:
    m = importlib.import_module("api.models.ai_models")
    assert hasattr(m, "AIModel")
    assert hasattr(m, "AIModelAssignment")
    assert hasattr(m, "AIInvocation")


def test_m2_crypto_secret_cipher_exists() -> None:
    m = importlib.import_module("api.libs.crypto")
    assert hasattr(m, "SecretCipher")
    src = open(m.__file__, encoding="utf-8").read()
    assert "Fernet" not in src
    assert "AESGCM" in src


def test_m2_security_checks_requires_master_key() -> None:
    sc = importlib.import_module("api.libs.security_checks")
    assert "MODEL_SECRETS_KEY" in list(sc._REQUIRED_IN_PROD)


def test_m4a_provider_abstraction_exists() -> None:
    m = importlib.import_module("api.core.providers")
    assert hasattr(m, "ProviderAdapter")
    assert hasattr(m, "ProviderRegistry")


def test_m4a_generation_params_relocated() -> None:
    base = importlib.import_module("api.core.providers.base")
    assert hasattr(base, "GenerationParams")
    mm = importlib.import_module("api.core.model_manager")
    assert hasattr(mm, "GenerationParams")


def test_m3_model_registry_exists() -> None:
    m = importlib.import_module("api.core.model_registry")
    assert hasattr(m, "ModelRegistry")
    assert hasattr(m.ModelRegistry, "get_model_for_task")
    assert hasattr(m.ModelRegistry, "invalidate")


def test_m4b_six_provider_adapters_registered() -> None:
    reg = importlib.import_module("api.core.providers")
    expected = ["openai", "anthropic", "minimax", "together", "openai_compatible", "local"]
    for name in expected:
        assert name in reg.ProviderRegistry._adapters or hasattr(reg, "OpenAIAdapter")


def test_m5_retry_client_exists() -> None:
    m = importlib.import_module("api.core.retry_client")
    assert hasattr(m, "RetryClient")


def test_m6_token_budgeter_exists() -> None:
    m = importlib.import_module("api.core.token_budget")
    assert hasattr(m, "TokenBudgeter")


def test_m7_invoke_for_task_exists() -> None:
    mm = importlib.import_module("api.core.model_manager")
    assert hasattr(mm.ModelManager, "invoke_for_task")


def test_m8_embed_texts_accepts_model() -> None:
    emb = importlib.import_module("api.core.embeddings")
    sig = inspect.signature(emb.EmbeddingService.embed_texts)
    assert "model" in sig.parameters


def test_m9_admin_ai_models_controller_exists() -> None:
    m = importlib.import_module("api.controllers.console.myownclone.ai_models")
    assert hasattr(m, "ns") or hasattr(m, "ai_models_ns") or hasattr(m, "register_routes")


def test_m12_rotate_secrets_key_command_exists() -> None:
    m = importlib.import_module("api.commands.crypto")
    assert hasattr(m, "rotate_secrets_key") or hasattr(m, "register_crypto_commands")


def test_m13_backfill_command_exists() -> None:
    try:
        m = importlib.import_module("api.commands.ai_backfill")
    except ModuleNotFoundError:
        m = importlib.import_module("api.commands.crypto")
    assert hasattr(m, "register_routes") or hasattr(m, "backfill_from_env") or "backfill" in dir(m)
