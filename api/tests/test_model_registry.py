from __future__ import annotations

from types import SimpleNamespace

import pytest

from api.core.model_registry import ModelRegistry, ModelRegistryError, ResolvedModelConfig
from api.models.ai_models import AITask


def test_model_registry_prefers_tenant_specific_assignment(monkeypatch):
    registry = ModelRegistry()
    calls: list[str | None] = []

    def fake_select_assignment_row(*, tenant_id, task):
        calls.append(tenant_id)
        if tenant_id == "tenant-1":
            return (
                SimpleNamespace(id="assign-tenant", override_params={"temperature": 0.1}),
                SimpleNamespace(
                    id="model-tenant",
                    name="Tenant model",
                    provider="openai",
                    model_id="gpt-4o-mini",
                    api_key_encrypted="ciphertext-1",
                    base_url="https://tenant.example/v1",
                    capabilities=["llm"],
                    temperature_default=0.3,
                    max_tokens_default=123,
                    max_input_tokens=4000,
                    embedding_dimensions=None,
                    priority=10,
                ),
            )
        return (
            SimpleNamespace(id="assign-global", override_params={}),
            SimpleNamespace(
                id="model-global",
                name="Global model",
                provider="openai",
                model_id="gpt-4o",
                api_key_encrypted="ciphertext-2",
                base_url=None,
                capabilities=["llm"],
                temperature_default=None,
                max_tokens_default=None,
                max_input_tokens=None,
                embedding_dimensions=None,
                priority=100,
            ),
        )

    monkeypatch.setattr(registry, "_select_assignment_row", fake_select_assignment_row)
    monkeypatch.setattr("api.core.model_registry.SecretCipher.decrypt", lambda blob: f"plain:{blob}")

    resolved = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)

    assert resolved.source == "database"
    assert resolved.assignment_id == "assign-tenant"
    assert resolved.model_id == "gpt-4o-mini"
    assert resolved.api_key == "plain:ciphertext-1"
    assert calls == ["tenant-1"]


def test_model_registry_falls_back_to_global_assignment(monkeypatch):
    registry = ModelRegistry()
    calls: list[str | None] = []

    def fake_select_assignment_row(*, tenant_id, task):
        calls.append(tenant_id)
        if tenant_id == "tenant-1":
            return None
        return (
            SimpleNamespace(id="assign-global", override_params={}),
            SimpleNamespace(
                id="model-global",
                name="Global model",
                provider="openai",
                model_id="gpt-4o",
                api_key_encrypted="ciphertext-2",
                base_url=None,
                capabilities=["llm"],
                temperature_default=None,
                max_tokens_default=None,
                max_input_tokens=None,
                embedding_dimensions=None,
                priority=100,
            ),
        )

    monkeypatch.setattr(registry, "_select_assignment_row", fake_select_assignment_row)
    monkeypatch.setattr("api.core.model_registry.SecretCipher.decrypt", lambda blob: "plain-key")

    resolved = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)

    assert resolved.assignment_id == "assign-global"
    assert resolved.model_id == "gpt-4o"
    assert calls == ["tenant-1", None]


def test_model_registry_uses_cache_until_invalidated(monkeypatch):
    now = [100.0]
    registry = ModelRegistry(ttl_seconds=60, time_fn=lambda: now[0])
    calls = {"count": 0}

    def fake_db(*, tenant_id, task):
        calls["count"] += 1
        return ResolvedModelConfig(
            task=task,
            provider="openai",
            model_id=f"model-{calls['count']}",
            tenant_id=tenant_id,
            source="database",
        )

    monkeypatch.setattr(registry, "_resolve_from_db", fake_db)
    monkeypatch.setattr(registry, "_resolve_from_legacy_env", lambda **_: None)

    first = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)
    second = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)
    registry.invalidate(tenant_id="tenant-1", task=AITask.CHAT)
    third = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)

    assert first.model_id == "model-1"
    assert second.model_id == "model-1"
    assert third.model_id == "model-2"
    assert calls["count"] == 2


def test_model_registry_uses_stale_cache_when_db_errors(monkeypatch):
    now = [100.0]
    registry = ModelRegistry(ttl_seconds=10, time_fn=lambda: now[0])
    calls = {"count": 0}

    def fake_db(*, tenant_id, task):
        calls["count"] += 1
        if calls["count"] == 1:
            return ResolvedModelConfig(
                task=task,
                provider="openai",
                model_id="warm-cache",
                tenant_id=tenant_id,
                source="database",
            )
        raise RuntimeError("db offline")

    monkeypatch.setattr(registry, "_resolve_from_db", fake_db)
    monkeypatch.setattr(registry, "_resolve_from_legacy_env", lambda **_: None)

    warm = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)
    now[0] = 200.0
    stale = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)

    assert warm.model_id == "warm-cache"
    assert stale.model_id == "warm-cache"
    assert calls["count"] == 2


def test_model_registry_falls_back_to_legacy_env(monkeypatch):
    registry = ModelRegistry()
    monkeypatch.setattr(registry, "_resolve_from_db", lambda **_: None)
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-4o-mini")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://api.deepseek.com")

    resolved = registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)

    assert resolved.source == "legacy_env"
    assert resolved.provider == "openai"
    assert resolved.model_id == "gpt-4o-mini"
    assert resolved.api_key == "sk-test"
    assert resolved.base_url == "https://api.deepseek.com"


def test_model_registry_raises_when_no_db_or_legacy_model(monkeypatch):
    registry = ModelRegistry()
    monkeypatch.setattr(registry, "_resolve_from_db", lambda **_: None)
    monkeypatch.setattr(registry, "_resolve_from_legacy_env", lambda **_: None)

    with pytest.raises(ModelRegistryError):
        registry.resolve(tenant_id="tenant-1", task=AITask.CHAT)
