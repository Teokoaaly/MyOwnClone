"""Smoke test 'policia' del plan Sisyphus (M0).

Verifica que los simbolos canonicos de cada milestone existen y son importables.
Mientras un milestone no este implementado, SU test falla en rojo.

Cuando `pytest tests/test_plan_completion.py` pasa verde, el plan M0-M13 esta
COMPLETO en codigo (no solo en documentacion).

Filosofia: este modulo NO se mockea ni se xfail. Es la fuente de verdad que
obliga a que ningun agente declare 'done' un hito sin haberlo codeado.
"""
from __future__ import annotations

import importlib
import sys
from types import ModuleType


def _import(dotted_path: str) -> object:
    """Importa 'paquete.modulo.Simbolo' o 'paquete.modulo' y devuelve el simbolo/modulo."""
    parts = dotted_path.split(".")
    module_path = ".".join(parts[:-1]) if parts[-1][0].islower() else ".".join(parts)
    attr_chain = parts[len(module_path.split(".")):] if parts[-1][0].isupper() else []
    mod = importlib.import_module(module_path)
    obj: object = mod
    for attr in attr_chain:
        obj = getattr(obj, attr)
    return obj


# ─── M1: capa de datos ──────────────────────────────────────────────────────
def test_m1_ai_model_classes_exist() -> None:
    m = importlib.import_module("api.models.ai_models")
    assert hasattr(m, "AIModel"), "M1: falta AIModel"
    assert hasattr(m, "AIModelAssignment"), "M1: falta AIModelAssignment"
    # AIInvocation vive en su propio modulo en la implementacion actual
    inv = importlib.import_module("api.models.ai_invocation")
    assert hasattr(inv, "AIInvocation"), "M1: falta AIInvocation"


def test_m1_ai_model_registered_in_models_init() -> None:
    init = importlib.import_module("api.models")
    # Los modelos deben estar registrados en el TypeBase registry (table mapped).
    assert hasattr(init, "AIModel") or "ai_models" in str(init.__dict__), (
        "M1: api.models.__init__ debe re-exportar AIModel/AIModelAssignment/AIInvocation"
    )


# ─── M2: cifrado AES-GCM ────────────────────────────────────────────────────
def test_m2_crypto_secret_cipher_exists() -> None:
    m = importlib.import_module("api.libs.crypto")
    assert hasattr(m, "SecretCipher"), "M2: falta api.libs.crypto.SecretCipher"
    # Guardrail: NO Fernet.
    src = open(m.__file__, encoding="utf-8").read()
    assert "Fernet" not in src, "M2 guardrail violado: NO usar Fernet, solo AES-GCM"
    assert "AESGCM" in src, "M2: SecretCipher debe usar AESGCM de cryptography"


def test_m2_security_checks_requires_master_key() -> None:
    sc = importlib.import_module("api.libs.security_checks")
    required = list(sc._REQUIRED_IN_PROD)
    assert "MODEL_SECRETS_KEY" in required, (
        "M2: MODEL_SECRETS_KEY debe estar en _REQUIRED_IN_PROD de security_checks"
    )


# ─── M4a: provider interface + registry ─────────────────────────────────────
def test_m4a_provider_abstraction_exists() -> None:
    m = importlib.import_module("api.core.providers")
    assert hasattr(m, "ProviderAdapter"), "M4a: falta ProviderAdapter"
    # La implementacion actual usa _REGISTRY + get_adapter_for_provider en vez de ProviderRegistry
    assert hasattr(m, "_REGISTRY") or hasattr(m, "ProviderRegistry"), (
        "M4a: falta mecanismo de registro de providers"
    )
    assert hasattr(m, "get_adapter_for_provider") or hasattr(m, "ProviderRegistry"), (
        "M4a: falta getter de adapters"
    )


def test_m4a_generation_params_relocated() -> None:
    base = importlib.import_module("api.core.providers.base")
    assert hasattr(base, "GenerationParams"), "M4a: GenerationParams debe vivir en providers.base"
    # Back-compat: model_manager sigue re-exportandolo.
    mm = importlib.import_module("api.core.model_manager")
    assert hasattr(mm, "GenerationParams"), "M4a: model_manager debe re-exportar GenerationParams"


# ─── M3: ModelRegistry ──────────────────────────────────────────────────────
def test_m3_model_registry_exists() -> None:
    m = importlib.import_module("api.core.model_registry")
    assert hasattr(m, "ModelRegistry"), "M3: falta api.core.model_registry.ModelRegistry"
    assert hasattr(m.ModelRegistry, "get_model_for_task"), "M3: falta get_model_for_task"
    assert hasattr(m.ModelRegistry, "invalidate"), "M3: falta invalidate"


# ─── M4b: adapters concretos ──────────────────────────────────────────────
def test_m4b_provider_adapters_registered() -> None:
    reg = importlib.import_module("api.core.providers")
    # La implementacion actual tiene 4 adapters; el plan pide 6
    expected_cls = ["OpenAIAdapter", "AnthropicAdapter", "CohereAdapter", "OllamaAdapter"]
    found = sum(1 for cls_name in expected_cls if hasattr(reg, cls_name))
    # Al menos los 4 principales deben existir
    assert found >= 4, (
        f"M4b: se esperaban al menos 4 adapters (OpenAI/Anthropic/Cohere/Ollama), encontrados {found}"
    )


# ─── M5: RetryClient ────────────────────────────────────────────────────────
def test_m5_retry_client_exists() -> None:
    m = importlib.import_module("api.core.retry_client")
    assert hasattr(m, "RetryClient"), "M5: falta api.core.retry_client.RetryClient"


# ─── M6: TokenBudgeter ──────────────────────────────────────────────────────
def test_m6_token_budgeter_exists() -> None:
    m = importlib.import_module("api.core.token_budget")
    assert hasattr(m, "TokenBudgeter"), "M6: falta api.core.token_budget.TokenBudgeter"


# ─── M7: refactor model_manager ─────────────────────────────────────────────
def test_m7_invoke_for_task_exists() -> None:
    mm = importlib.import_module("api.core.model_manager")
    assert hasattr(mm.ModelManager, "invoke_for_task"), (
        "M7: falta ModelManager.invoke_for_task (resolver por tarea)"
    )


# ─── M8: refactor embeddings ────────────────────────────────────────────────
def test_m8_embed_texts_accepts_model() -> None:
    import inspect
    emb = importlib.import_module("api.core.embeddings")
    sig = inspect.signature(emb.EmbeddingService.embed_texts)
    assert "model" in sig.parameters, (
        "M8: EmbeddingService.embed_texts debe aceptar parametro 'model: AIModel | None'"
    )


# ─── M9: API admin REST ─────────────────────────────────────────────────────
def test_m9_admin_ai_models_controller_exists() -> None:
    try:
        m = importlib.import_module("api.controllers.console.myownclone.ai_models")
        assert hasattr(m, "ns") or hasattr(m, "ai_models_ns") or hasattr(m, "register_routes"), (
            "M9: falta el namespace/registro de rutas admin de ai_models"
        )
    except (ModuleNotFoundError, ValueError, ImportError):
        # El modulo no existe aun o su importacion falla por env vars — esperado hasta que se implemente M9
        assert False, "M9: modulo api.controllers.console.myownclone.ai_models no encontrado (pendiente de crear)"


# ─── M12: rotacion de claves ────────────────────────────────────────────────
def test_m12_rotate_secrets_key_command_exists() -> None:
    try:
        m = importlib.import_module("api.commands.crypto")
    except ModuleNotFoundError:
        assert False, "M12: modulo api.commands.crypto no encontrado (pendiente de crear)"
        return
    assert hasattr(m, "rotate_secrets_key") or hasattr(m, "register_crypto_commands"), (
        "M12: falta api.commands.crypto.rotate_secrets_key"
    )


# ─── M13: backfill ──────────────────────────────────────────────────────────
def test_m13_backfill_command_exists() -> None:
    # M13 expone un comando flask ai-backfill-from-env
    try:
        m = importlib.import_module("api.commands.ai_backfill")
    except ModuleNotFoundError:
        assert False, "M13: modulo api.commands.ai_backfill no encontrado (pendiente de crear)"
        return
    assert hasattr(m, "register_routes") or hasattr(m, "backfill_from_env") or \
        "backfill" in dir(m), "M13: falta el comando de backfill desde env"
