"""M13 — ``ai-backfill-from-env`` idempotency and correctness.

These tests inject a fake session (mirroring ``test_ai_audit_rotation``'s
db.session monkeypatch style) so no live PostgreSQL is required. They assert
the backfill creates the catalog from env vars, is idempotent on re-run, reuses
an already-correct active assignment, and updates an existing model whose
encrypted key no longer matches the environment.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from api.commands.ai_backfill import backfill_from_env
from api.libs.crypto import SecretCipher, generate_master_key
from api.models.ai_models import AIModel, AIModelAssignment


@pytest.fixture(autouse=True)
def _master_key(monkeypatch):
    monkeypatch.setenv("MODEL_SECRETS_KEY", generate_master_key())


class _FakeSession:
    """Returns ``models`` then ``assignments`` for the two ordered selects."""

    def __init__(self, models, assignments):
        self._results = [list(models), list(assignments)]
        self.added: list[object] = []
        self.committed = False

    def execute(self, _stmt):
        rows = self._results.pop(0)
        return SimpleNamespace(
            scalars=lambda rows=rows: SimpleNamespace(all=lambda: list(rows))
        )

    def add(self, obj):
        self.added.append(obj)

    def commit(self):
        self.committed = True


def _model(provider, model_id, *, key="sk-test", capabilities, dims=None):
    return AIModel(
        id=f"model-{provider}-{model_id}",
        tenant_id=None,
        name=f"{provider}/{model_id}",
        provider=provider,
        model_id=model_id,
        api_key_encrypted=SecretCipher.encrypt(key),
        capabilities=list(capabilities),
        embedding_dimensions=dims,
        is_active=True,
    )


def _assignment(task, model_pk):
    return AIModelAssignment(
        id=f"assign-{task}",
        tenant_id=None,
        task=task,
        model_id=model_pk,
        is_active=True,
    )


def test_backfill_creates_models_and_assignments_from_env():
    session = _FakeSession(models=[], assignments=[])
    result = backfill_from_env(session=session, env={"OPENAI_API_KEY": "sk-test"})

    assert result.providers_detected == ("openai",)
    # openai serves chat (gpt-4o-mini), embedding (text-embedding-3-small),
    # and stt (whisper-1) → 3 distinct models.
    assert result.models_created == 3
    assert result.models_updated == 0
    # 5 tasks (chat, embedding, email_classification, email_draft, stt) → 5 assignments.
    assert result.assignments_created == 5
    assert result.assignments_reused == 0
    assert result.skipped_tasks == ()
    assert session.committed is True
    assert len(session.added) == 8  # 3 models + 5 assignments


def test_backfill_is_idempotent_on_rerun():
    env = {"OPENAI_API_KEY": "sk-test"}
    chat = _model("openai", "gpt-4o-mini", capabilities=["llm"])
    emb = _model("openai", "text-embedding-3-small", capabilities=["embedding"], dims=1536)
    stt = _model("openai", "whisper-1", capabilities=["stt"])
    assignments = [
        _assignment("chat", chat.id),
        _assignment("embedding", emb.id),
        _assignment("email_classification", chat.id),
        _assignment("email_draft", chat.id),
        _assignment("stt", stt.id),
    ]
    session = _FakeSession(models=[chat, emb, stt], assignments=assignments)

    result = backfill_from_env(session=session, env=env)

    assert result.models_created == 0
    assert result.models_updated == 0
    assert result.assignments_created == 0
    assert result.assignments_reused == 5
    assert session.added == []


def test_backfill_reuses_correct_active_assignment_and_creates_missing():
    env = {"OPENAI_API_KEY": "sk-test"}
    chat = _model("openai", "gpt-4o-mini", capabilities=["llm"])
    emb = _model("openai", "text-embedding-3-small", capabilities=["embedding"], dims=1536)
    stt = _model("openai", "whisper-1", capabilities=["stt"])
    # Only the chat assignment pre-exists and is already correct.
    session = _FakeSession(
        models=[chat, emb, stt],
        assignments=[_assignment("chat", chat.id)],
    )

    result = backfill_from_env(session=session, env=env)

    assert result.models_created == 0
    assert result.assignments_reused == 1  # chat
    assert result.assignments_created == 4  # the other 4 tasks
    added_assignments = [a for a in session.added if isinstance(a, AIModelAssignment)]
    assert len(added_assignments) == 4


def test_backfill_updates_existing_model_when_key_changed():
    env = {"OPENAI_API_KEY": "sk-new"}
    # Existing chat model encrypted with a DIFFERENT plaintext.
    chat = _model("openai", "gpt-4o-mini", key="sk-old", capabilities=["llm"])
    session = _FakeSession(models=[chat], assignments=[])

    result = backfill_from_env(session=session, env=env)

    assert result.models_updated == 1  # chat model re-encrypted
    assert result.models_created == 2  # embedding + stt models created
    # The chat row now decrypts to the new key.
    assert SecretCipher.decrypt(chat.api_key_encrypted) == "sk-new"
    assert result.assignments_created == 5


def test_backfill_no_providers_is_noop():
    session = _FakeSession(models=[], assignments=[])
    result = backfill_from_env(session=session, env={})

    assert result.providers_detected == ()
    assert result.models_created == 0
    assert result.assignments_created == 0
    assert session.added == []
    assert session.committed is False  # nothing to commit


def test_dry_run_does_not_write():
    session = _FakeSession(models=[], assignments=[])
    result = backfill_from_env(
        session=session, env={"OPENAI_API_KEY": "sk-test"}, dry_run=True
    )

    assert result.models_created == 3
    assert result.assignments_created == 5
    assert session.added == []
    assert session.committed is False
