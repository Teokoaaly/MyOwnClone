"""Regression tests for P0.3 backend crash fixes (auditoria 2026-07-13).

Covers:
- C-05: ``AITask.CHAT_FALLBACK`` exists and resolves (was AttributeError).
- C-06: ``record_llm_cost`` persists a row with real columns (was passing
  ``provider``/``tokens_in``/``tokens_out``/``cost_cents`` that do not exist
  on ``AIInvocation``).
- C-07: ``api.core.myownclone.email_ai._get_clone_context`` imports cleanly.
- C-08: ``api.controllers.common.schema.get_or_create_model`` import path
  is package-qualified.
- C-09: ``deploy._run`` timeout path returns ``(124, str)`` (was NameError).
- C-14: ``RetrievalService.retrieve`` returns a list (was a dict that broke
  ``len()`` / iteration downstream).
"""
from __future__ import annotations

import subprocess
from unittest.mock import MagicMock, patch

from api.controllers.common import schema as schema_module
from api.controllers import deploy as deploy_module
from api.core.rag.datasource.retrieval_service import RetrievalService
from api.models.ai_models import AITask, TASK_CAPABILITY, AICapability


# ── C-05: AITask.CHAT_FALLBACK ─────────────────────────────────────────

def test_chat_fallback_member_exists():
    """C-05: CHAT_FALLBACK must be a member of AITask (was AttributeError)."""
    assert hasattr(AITask, "CHAT_FALLBACK")
    assert AITask.CHAT_FALLBACK.value == "chat_fallback"


def test_chat_fallback_has_llm_capability():
    """C-05: CHAT_FALLBACK maps to the LLM capability (needed by registry)."""
    assert TASK_CAPABILITY[AITask.CHAT_FALLBACK] is AICapability.LLM


def test_chat_fallback_resolves_without_attribute_error():
    """C-05 regression: resolving a fallback model must not raise AttributeError.

    Previously ``registry.get_model_for_task(task=AITask.CHAT_FALLBACK)``
    raised AttributeError mid-invocation and was swallowed by a bare
    ``except Exception`` in ``ModelManager.invoke_for_task``.
    """
    # Accessing the enum member is the exact line that raised.
    _ = AITask.CHAT_FALLBACK
    # And it must be usable as a dict key / argument.
    assert AITask.CHAT_FALLBACK in TASK_CAPABILITY


# ── C-06: record_llm_cost persists with real columns ───────────────────

def test_record_llm_cost_maps_to_real_columns(monkeypatch):
    """C-06: record_llm_cost must persist using AIInvocation's real columns.

    The function previously passed ``provider``/``tokens_in``/``tokens_out``/
    ``cost_cents`` to ``AIInvocation(...)``, none of which exist on the model.
    SQLAlchemy raised and the whole call was swallowed as non-fatal, so no
    cost row was ever persisted.
    """
    captured: dict = {}

    class FakeAIInvocation:
        def __init__(self, **kwargs):
            captured.update(kwargs)

    class FakeSession:
        def add(self, obj):
            captured["_added"] = obj

        def commit(self):
            captured["_committed"] = True

        def rollback(self):
            captured["_rolled_back"] = True

    class FakeDb:
        session = FakeSession()

    # Patch the lazy imports inside record_llm_cost.
    import sys
    import api.core.model_manager as mm
    import api.extensions.ext_database as ext_db_module
    import api.models.ai_models as ai_models_module

    monkeypatch.setattr(ai_models_module, "AIInvocation", FakeAIInvocation)
    # The function does ``from api.extensions.ext_database import db`` lazily;
    # patch the attribute on the module it imports from.
    monkeypatch.setattr(ext_db_module, "db", FakeDb())

    mm.record_llm_cost(
        tenant_id="tenant-1",
        model="gpt-test",
        provider="openai",
        tokens_in=10,
        tokens_out=20,
        cost_cents=5,
        task="chat",
        clone_id="clone-1",
    )

    assert captured.get("_committed") is True
    # Must use the real column names, not the old broken ones.
    assert "prompt_tokens" in captured and captured["prompt_tokens"] == 10
    assert "completion_tokens" in captured and captured["completion_tokens"] == 20
    assert "success" in captured and captured["success"] is True
    # Old broken kwargs must NOT be present.
    assert "tokens_in" not in captured
    assert "tokens_out" not in captured
    assert "cost_cents" not in captured
    assert "provider" not in captured
    # Provider should be folded into the model label for traceability.
    assert captured["model"] == "openai/gpt-test"


def test_record_llm_cost_failure_is_non_fatal(capfd):
    """C-06: a DB failure must be swallowed (never break the user response)."""
    import api.core.model_manager as mm

    # Force the lazy import to fail by patching the target module attribute.
    import api.extensions.ext_database as ext_db_module

    class ExplodingSession:
        def add(self, obj):
            raise RuntimeError("db down")

        def rollback(self):
            pass

    class ExplodingDb:
        session = ExplodingSession()

    orig = ext_db_module.db
    ext_db_module.db = ExplodingDb()
    try:
        # Must NOT raise.
        mm.record_llm_cost(
            tenant_id="t",
            model="m",
            provider="p",
            tokens_in=1,
            tokens_out=1,
            cost_cents=1,
        )
    finally:
        ext_db_module.db = orig


# ── C-07: email_ai imports cleanly ─────────────────────────────────────

def test_email_ai_module_imports():
    """C-07: _get_clone_context must import without ModuleNotFoundError.

    Previously used ``from extensions.ext_database import db`` (missing the
    ``api.`` package prefix).
    """
    from api.core.myownclone import email_ai  # noqa: F401

    assert callable(email_ai._get_clone_context)


# ── C-08: schema.get_or_create_model import path ───────────────────────

def test_schema_module_imports():
    """C-08: schema module must import without ModuleNotFoundError."""
    assert hasattr(schema_module, "get_or_create_model")
    assert callable(schema_module.get_or_create_model)


# ── C-09: deploy._run timeout returns (124, str) ───────────────────────

def test_deploy_run_timeout_returns_124(monkeypatch):
    """C-09: ``_run`` timeout path must return ``(124, str)``, not NameError.

    Previously the line read ``return124, ...`` (no space) which raised
    NameError on the timeout path, masking deploy failures as 500s.
    """
    def fake_run(*args, **kwargs):
        raise subprocess.TimeoutExpired(cmd=args[0], timeout=kwargs.get("timeout", 1))

    monkeypatch.setattr(deploy_module.subprocess, "run", fake_run)

    code, output = deploy_module._run(["sleep", "999"], timeout=1)

    assert code == 124
    assert isinstance(output, str)
    assert "timed out" in output.lower()


# ── C-14: RetrievalService.retrieve returns a list ─────────────────────

def test_retrieval_service_class_level_retrieve_returns_list():
    """C-14: class-level retrieve must return a list (was dict).

    ``api/core/retrieval.py`` calls ``RetrievalService.retrieve(...)`` as a
    class method and then does ``len(documents)`` and iterates over it
    expecting objects with ``.metadata``. A dict returned the keys (strings)
    and ``getattr(str, "metadata", {})`` silently produced empty output.
    """
    result = RetrievalService.retrieve(query="x", dataset_id="d")
    assert isinstance(result, list)
    assert len(result) == 0


def test_retrieval_service_instance_retrieve_returns_list():
    """C-14: instance-level retrieve must also return a list."""
    svc = RetrievalService(dataset_id="d")
    result = svc.retrieve(query="x")
    assert isinstance(result, list)
