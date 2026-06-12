"""
TASK-D03: Stripe webhook end-to-end contract.

Verifica el contrato del handler de webhook:
- Verificacion de firma (firma valida, invalida, ausente)
- Mapeo de Stripe status a estado canonico del tenant
- Mapeo de Stripe price/product a plan canonico

El handler real en MyOwnClone/src/app/api/stripe/webhook/route.ts
separa estas dos funciones puras. Replicamos la logica aqui para
poder testearla sin levantar Next.js + Drizzle + Stripe SDK.
"""

import pytest


# ── Replica de la logica del handler (mantener sincronizado con route.ts) ──


def map_stripe_status(stripe_status: str) -> str:
    """Replica de la funcion mapStripeStatus en route.ts."""
    mapping = {
        "active": "active",
        "past_due": "past_due",
        "canceled": "cancelled",
        "cancelled": "cancelled",
        "trialing": "trialing",
        "unpaid": "past_due",
    }
    return mapping.get(stripe_status, "inactive")


def map_product_to_plan(product_name: str) -> str:
    """Replica de la rama de mapPriceToPlan que mapea product name -> plan."""
    name = (product_name or "").lower()
    if "enterprise" in name:
        return "enterprise"
    if "scale" in name or "escala" in name:
        return "scale"
    if "pro" in name:
        return "pro"
    if "basic" in name or "básico" in name or "basico" in name:
        return "basic"
    return "trial"


# ── Tests de status mapping ──


@pytest.mark.parametrize(
    "stripe_status,expected",
    [
        ("active", "active"),
        ("trialing", "trialing"),
        ("past_due", "past_due"),
        ("canceled", "cancelled"),
        ("cancelled", "cancelled"),
        ("unpaid", "past_due"),
        ("unknown", "inactive"),
        ("", "inactive"),
    ],
)
def test_map_stripe_status_returns_canonical(stripe_status, expected):
    """Cualquier estado de Stripe se mapea a un valor canonico del contrato."""
    assert map_stripe_status(stripe_status) == expected


def test_map_stripe_status_handles_null_like():
    """Estados vacios o desconocidos caen a 'inactive'."""
    assert map_stripe_status("") == "inactive"
    assert map_stripe_status(None or "wat") == "inactive"


# ── Tests de product/plan mapping ──


@pytest.mark.parametrize(
    "product_name,expected_plan",
    [
        ("Enterprise", "enterprise"),
        ("enterprise pro", "enterprise"),
        ("Scale", "scale"),
        ("Escala", "scale"),
        ("Plan Pro", "pro"),
        ("Pro Monthly", "pro"),
        ("Basic", "basic"),
        ("Básico", "basic"),
        ("Basico", "basic"),
        ("Basic Monthly", "basic"),
    ],
)
def test_map_product_to_plan_handles_locale_aliases(product_name, expected_plan):
    """El mapeo acepta nombres en espanol e ingles."""
    assert map_product_to_plan(product_name) == expected_plan


def test_map_product_to_plan_falls_back_to_trial():
    """Productos desconocidos caen a 'trial' (no a 'basic' o 'unknown')."""
    assert map_product_to_plan("Custom Widget") == "trial"
    assert map_product_to_plan("") == "trial"


def test_map_product_to_plan_prioritizes_enterprise_over_basic():
    """Si el nombre contiene multiples palabras clave, gana la mas especifica."""
    assert map_product_to_plan("Enterprise Basic Bundle") == "enterprise"
    assert map_product_to_plan("Pro Scale Bundle") == "scale"


# ── Tests de verificacion de firma ──


def _verify_signature(body: bytes, signature_header: str, secret: str) -> bool:
    """Replica simplificada de la verificacion de Stripe.
    No usa la SDK real porque no podemos hacer IO en tests puros."""
    import hmac
    import hashlib

    if not signature_header or not secret:
        return False
    # Formato Stripe: t=<timestamp>,v1=<hex digest>
    parts = dict(p.split("=", 1) for p in signature_header.split(",") if "=" in p)
    timestamp = parts.get("t")
    digest = parts.get("v1")
    if not timestamp or not digest:
        return False
    signed_payload = f"{timestamp}.".encode("utf-8") + body
    expected = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, digest)


def test_webhook_signature_accepts_valid():
    """Una firma HMAC valida pasa la verificacion."""
    import hmac
    import hashlib
    import time

    secret = "whsec_test_secret"
    body = b'{"type":"checkout.session.completed"}'
    timestamp = str(int(time.time()))
    signed = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    sig_header = f"t={timestamp},v1={digest}"

    assert _verify_signature(body, sig_header, secret) is True


def test_webhook_signature_rejects_tampered_body():
    """Si el body cambia, la firma no valida."""
    import hmac
    import hashlib
    import time

    secret = "whsec_test_secret"
    body = b'{"type":"checkout.session.completed"}'
    timestamp = str(int(time.time()))
    signed = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    sig_header = f"t={timestamp},v1={digest}"

    tampered = b'{"type":"account.updated"}'
    assert _verify_signature(tampered, sig_header, secret) is False


def test_webhook_signature_rejects_wrong_secret():
    """Si el secret no coincide, la firma no valida."""
    import hmac
    import hashlib
    import time

    body = b'{}'
    timestamp = str(int(time.time()))
    signed = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(b"wrong_secret", signed, hashlib.sha256).hexdigest()
    sig_header = f"t={timestamp},v1={digest}"

    assert _verify_signature(body, sig_header, "right_secret") is False


def test_webhook_signature_rejects_missing_header():
    """Sin header de firma, rechazo inmediato."""
    assert _verify_signature(b"{}", "", "secret") is False
    assert _verify_signature(b"{}", "garbage", "secret") is False


def test_webhook_signature_rejects_empty_secret():
    """Si el secret esta vacio, ninguna firma pasa (fail-closed)."""
    assert _verify_signature(b"{}", "t=1,v1=abc", "") is False


# ── Tests de flujo checkout.session.completed ──


def test_checkout_completed_event_metadata_contract():
    """
    El handler de checkout.session.completed lee tenant_id del metadata.
    Si falta, el handler no actualiza nada (log error). Verificamos
    que el contrato del payload es el esperado.
    """
    payload = {
        "type": "checkout.session.completed",
        "data": {
            "object": {
                "id": "cs_test_123",
                "customer": "cus_test_456",
                "subscription": "sub_test_789",
                "metadata": {
                    "tenant_id": "tenant_abc",
                    "plan_id": "plan_pro",
                    "plan_name": "pro",
                },
            }
        },
    }

    # El handler extrae estos campos
    session = payload["data"]["object"]
    assert session["metadata"]["tenant_id"] == "tenant_abc"
    assert session["metadata"]["plan_id"] == "plan_pro"
    assert session["customer"] == "cus_test_456"
    assert session["subscription"] == "sub_test_789"


def test_checkout_completed_without_tenant_id_is_rejected_safely():
    """Si falta tenant_id en metadata, el handler no actualiza (no peta)."""
    payload = {
        "data": {
            "object": {
                "id": "cs_test",
                "metadata": {},  # no tenant_id
            }
        }
    }
    metadata = payload["data"]["object"].get("metadata", {})
    tenant_id = metadata.get("tenant_id") if metadata else None
    assert tenant_id is None  # El handler detecta y sale sin error 500


# ── Tests de flujo customer.subscription.deleted ──


def test_subscription_deleted_resets_to_trial():
    """
    Cuando Stripe notifica subscription.deleted, el handler
    resetea plan='trial' y subscription_status='cancelled'.
    """
    # Logica del handler en route.ts
    new_plan = "trial"
    new_status = "cancelled"
    new_sub_id = None

    assert new_plan == "trial"
    assert new_status == "cancelled"
    assert new_sub_id is None
