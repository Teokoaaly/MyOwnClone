from api.controllers.console.myownclone.clone import _serialize_clone
from api.core.contracts import (
    PLAN_PRICES_CENTS,
    normalize_conversation_mode,
    normalize_plan,
    normalize_silo,
    normalize_silo_list,
    normalize_tenant_status,
)
from api.models.myownclone import CloneConfig, CloneModePrompt


def test_plan_and_status_normalization_accepts_legacy_values():
    assert normalize_plan("básico") == "basic"
    assert normalize_plan("basico") == "basic"
    assert normalize_plan("escala") == "scale"
    assert normalize_plan("enterprise") == "enterprise"
    assert normalize_plan(None) == "trial"

    assert normalize_tenant_status("normal") == "active"
    assert normalize_tenant_status("banned") == "suspended"
    assert normalize_tenant_status("cancelled") == "cancelled"
    assert normalize_tenant_status(None) == "trial"

    assert PLAN_PRICES_CENTS["basic"] == 4900
    assert PLAN_PRICES_CENTS["scale"] == 19900


def test_silo_and_conversation_mode_normalization_bridges_ui_and_db_terms():
    assert normalize_silo("pedagogy") == "teach"
    assert normalize_silo("learn") == "teach"
    assert normalize_silo("support") == "support"
    assert normalize_silo("sales") == "sales"

    assert normalize_conversation_mode("teach") == "pedagogy"
    assert normalize_conversation_mode("pedagogy") == "pedagogy"

    assert normalize_silo_list(["pedagogy", "teach", "sales"]) == ["teach", "sales"]
    assert normalize_silo_list([]) == ["teach"]


def test_clone_serializer_returns_frontend_silo_contract(monkeypatch):
    clone = CloneConfig(
        id="clone_1",
        tenant_id="tenant_1",
        name="Hacchi",
        slug="hacchi",
        language="es",
        active_modes=["pedagogy", "support"],
        is_active=True,
    )
    prompt = CloneModePrompt(
        id="prompt_1",
        clone_id="clone_1",
        mode="pedagogy",
        system_prompt="Teach clearly.",
        is_active=True,
    )

    class FakeResult:
        def scalars(self):
            return self

        def all(self):
            return [prompt]

    class FakeSession:
        def execute(self, _stmt):
            return FakeResult()

    monkeypatch.setattr("api.controllers.console.myownclone.clone.db.session", FakeSession())

    payload = _serialize_clone(clone)

    assert payload["active_modes"] == ["teach", "support"]
    assert payload["mode_prompts"][0]["mode"] == "teach"
