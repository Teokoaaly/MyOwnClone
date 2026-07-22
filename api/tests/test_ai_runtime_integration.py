from io import BytesIO
from types import SimpleNamespace

from api.libs.login import AuthenticatedIdentity
from api.models.ai_models import AITask
from api.models.email import EmailInbound


def _auth_headers():
    return {"Authorization": "Bearer test-token"}


def _mock_auth(monkeypatch) -> None:
    monkeypatch.setattr("api.libs.login._verify_token", lambda token: {"sub": "user-1"})
    monkeypatch.setattr(
        "api.libs.login._load_authoritative_identity",
        lambda account_id: AuthenticatedIdentity(
            account_id="user-1",
            tenant_id="tenant-1",
            role="admin",
            email="user@example.com",
        ),
    )
    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime._check_rate_limit",
        lambda endpoint, limit, window: (True, None),
    )


def test_embeddings_endpoint_uses_embedding_service(app, monkeypatch):
    _mock_auth(monkeypatch)
    captured = {}

    def fake_embed(self, texts, tenant_id=None, model=None):
        captured["texts"] = texts
        captured["tenant_id"] = tenant_id
        return [[0.1] * 1536 for _ in texts]

    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime.EmbeddingService.embed_texts",
        fake_embed,
    )

    client = app.test_client()
    response = client.post(
        "/console/api/myownclone/embeddings",
        json={"texts": ["hola", "mundo"]},
        headers=_auth_headers(),
    )

    assert response.status_code == 200
    assert captured == {"texts": ["hola", "mundo"], "tenant_id": "tenant-1"}
    assert response.get_json()["count"] == 2


def test_stt_endpoint_uses_registry_service(app, monkeypatch):
    _mock_auth(monkeypatch)
    captured = {}

    def fake_transcribe(self, **kwargs):
        captured.update(kwargs)
        return "texto transcrito"

    monkeypatch.setattr(
        "api.controllers.console.myownclone.runtime.SpeechToTextService.transcribe",
        fake_transcribe,
    )

    client = app.test_client()
    response = client.post(
        "/console/api/myownclone/stt/transcribe",
        data={
            "audio": (BytesIO(b"audio-bytes"), "voice.webm"),
            "language": "es",
        },
        content_type="multipart/form-data",
        headers=_auth_headers(),
    )

    assert response.status_code == 200
    assert response.get_json()["text"] == "texto transcrito"
    assert captured["tenant_id"] == "tenant-1"
    assert captured["filename"] == "voice.webm"
    assert captured["language"] == "es"


def test_classify_and_draft_uses_task_specific_assignments(monkeypatch):
    clone = SimpleNamespace(id="clone-1", tenant_id="tenant-1")
    email = EmailInbound(
        id="email-1",
        clone_id="clone-1",
        from_name="Ana",
        from_email="ana@example.com",
        subject="Consulta",
        body_text="Necesito ayuda",
    )
    calls = []

    class FakeExecuteResult:
        def scalar_one_or_none(self):
            return clone

    monkeypatch.setattr(
        "api.controllers.myownclone_public.db.session.execute",
        lambda stmt: FakeExecuteResult(),
    )
    monkeypatch.setattr(
        "api.controllers.myownclone_public._get_clone_context",
        lambda clone_id: ("memory", "templates"),
    )
    monkeypatch.setattr(
        "api.controllers.myownclone_public.classify_email",
        lambda **kwargs: SimpleNamespace(category=kwargs["llm_callable"]("classification")),
    )
    monkeypatch.setattr(
        "api.controllers.myownclone_public.generate_draft_reply",
        lambda **kwargs: SimpleNamespace(body=kwargs["llm_callable"]("draft")),
    )

    def fake_invoke_for_task(self, *, tenant_id, clone_id, task, message):
        calls.append((tenant_id, clone_id, task, message))
        if task == AITask.EMAIL_CLASSIFICATION:
            return SimpleNamespace(text="venta")
        if task == AITask.EMAIL_DRAFT:
            return SimpleNamespace(text="Te respondo.")
        raise AssertionError(f"unexpected task {task}")

    monkeypatch.setattr(
        "api.core.model_manager.ModelManager.invoke_for_task",
        fake_invoke_for_task,
    )

    from api.controllers.myownclone_public import _classify_and_draft

    _classify_and_draft(email, "clone-1")

    assert email.classification == "venta"
    assert email.draft_reply == "Te respondo."
    assert [task for _, _, task, _ in calls] == [
        AITask.EMAIL_CLASSIFICATION,
        AITask.EMAIL_DRAFT,
    ]
