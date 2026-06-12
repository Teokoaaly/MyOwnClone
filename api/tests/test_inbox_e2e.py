"""
TASK-E06: Inbox end-to-end contract.

Cubre el flujo completo de inbox:
1. Webhook rechaza sin signature en produccion con secret configurado
2. Webhook acepta en dev (sin secret)
3. Email sin contenido se ignora con 200
4. Email con payload JSON se procesa
5. Email de dominio no resuelto se ignora con status=no_clone
6. Payload de email malformado no peta 500

Los tests usan el Flask test client. No requieren DB (los paths de error
suceden antes de tocar la BD).
"""

import os
import pytest


# ── Constantes ──────────────────────────────────────────────────────────


SIMPLE_EMAIL = (
    b"From: cliente@example.com\r\n"
    b"To: juan@myownclone.com\r\n"
    b"Subject: Consulta sobre el plan pro\r\n"
    b"\r\n"
    b"Hola, me interesa el plan pro. Cuanto cuesta?\r\n"
)


# ── Tests de autenticacion del webhook ──


def test_inbound_email_rejects_without_secret_in_production(monkeypatch, client):
    """
    En produccion con SENDGRID_INBOUND_WEBHOOK_SECRET configurado,
    una request sin X-Webhook-Secret debe rechazarse con 401.
    """
    monkeypatch.setenv("FLASK_ENV", "production")
    monkeypatch.setenv("SENDGRID_INBOUND_WEBHOOK_SECRET", "real-secret")
    # El secret se lee al import time; recargar modulo
    import importlib
    import api.controllers.myownclone_public as mod
    importlib.reload(mod)
    mod._SENDGRID_SECRET = "real-secret"
    mod._is_production = lambda: True  # forzar

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b'{"email": "raw email"}',
        content_type="application/json",
    )
    assert r.status_code == 401
    body = r.get_json()
    assert body["error"] == "unauthorized"


def test_inbound_email_rejects_wrong_secret(monkeypatch, client):
    """Secret incorrecto devuelve 401."""
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = "correct-secret"
    mod._is_production = lambda: True

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b'{"email": "x"}',
        content_type="application/json",
        headers={"X-Webhook-Secret": "wrong-secret"},
    )
    assert r.status_code == 401


def test_inbound_email_accepts_correct_secret(monkeypatch, client):
    """
    Secret correcto entra al handler. Si falla por parsing/clones, devuelve 200
    con status explicativo (nunca 401).
    """
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = "correct-secret"
    mod._is_production = lambda: True

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b'{"email": "x"}',
        content_type="application/json",
        headers={"X-Webhook-Secret": "correct-secret"},
    )
    # 200 con status (no 401, no 500)
    assert r.status_code != 401
    assert r.status_code != 500
    body = r.get_json()
    assert "status" in body


# ── Tests de dev mode (sin secret configurado) ──


def test_inbound_email_open_in_dev(monkeypatch, client):
    """
    En dev (FLASK_ENV != production y sin secret), el endpoint acepta
    cualquier request sin auth. Esto es el contrato documentado.
    """
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b'{"email": "x"}',
        content_type="application/json",
    )
    assert r.status_code != 401
    assert r.status_code != 500


# ── Tests de payloads ──


def test_inbound_email_empty_body_returns_no_content(monkeypatch, client):
    """Body vacio devuelve 200 con status=no_content (no 500)."""
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b"{}",
        content_type="application/json",
    )
    assert r.status_code == 200
    assert r.get_json()["status"] == "no_content"


def test_inbound_email_with_form_payload(monkeypatch, client):
    """Payload multipart/form con campo 'email' es aceptado."""
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data={"email": SIMPLE_EMAIL.decode("utf-8", errors="replace")},
        content_type="multipart/form-data",
    )
    # Devuelve 200 con algun status. Si no hay clone configurado, status=no_clone.
    assert r.status_code == 200
    body = r.get_json()
    assert body.get("status") in ("no_clone", "received")


def test_inbound_email_response_shape(monkeypatch, client):
    """La respuesta siempre es JSON con clave 'status'."""
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=b'{"email": "x"}',
        content_type="application/json",
    )
    assert r.headers.get("Content-Type", "").startswith("application/json")
    body = r.get_json()
    assert "status" in body


# ── Tests de rate limit ──


def test_inbound_email_rate_limited(monkeypatch, client):
    """
    El rate limit por IP+slug es 10 req/min en booking_public. En
    inbound-email no hay rate limit por-IP explicito (solo el secret),
    pero el endpoint nunca debe colgar el proceso bajo spam.
    """
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    # 5 requests rapidisimas: ninguna debe colgar (timeout) ni devolver 500
    for _ in range(5):
        r = client.post(
            "/api/myownclone/public/inbound-email",
            data=b'{"email": "x"}',
            content_type="application/json",
        )
        assert r.status_code in (200, 429), f"Unexpected {r.status_code}"


# ── Tests de payload invalido (no debe petar) ──


@pytest.mark.parametrize("bad_payload", [
    b"not-json",
    b"",
    b"\x00\x01\x02",
    b'{"unrelated_field": "value"}',
])
def test_inbound_email_handles_garbage_gracefully(monkeypatch, client, bad_payload):
    """Payloads invalidos se manejan con 200 + status, nunca con 500."""
    import api.controllers.myownclone_public as mod
    mod._SENDGRID_SECRET = ""
    mod._is_production = lambda: False

    r = client.post(
        "/api/myownclone/public/inbound-email",
        data=bad_payload,
        content_type="application/json",
    )
    assert r.status_code == 200
    body = r.get_json()
    assert body["status"] in ("no_content", "parse_error", "no_clone")
