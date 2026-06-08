"""
Fase 2: Tests de scoping tenant_id.
Verifica que los endpoints de consola (no-admin) devuelvan
solo los recursos del tenant autenticado, no de otros.

NON_ADMIN_ENDPOINTS recopilado inspeccionando api/controllers/console/:
- console_bp (todas usan @login_required + @account_initialization_required + @setup_required)
- Excluidos los admin-only (/myownclone/admin/*) que requieren _is_platform_admin
- Excluidos los públicos sin auth (/api/myownclone/public/* y /console/api/auth/*)
"""

import pytest

# ── Endpoints de consola que un tenant normal PUEDE ver ─────────────────
# Inspeccionados de:
#   api/controllers/console/__init__.py → console_ns
#   api/controllers/console/myownclone/clone.py
#   api/controllers/console/myownclone/analytics.py
#   api/controllers/console/myownclone/booking.py
#   api/controllers/console/myownclone/creator_memory.py
#   api/controllers/console/myownclone/feedback.py
#   api/controllers/console/myownclone/inbox.py
#   api/controllers/console/myownclone/stripe_ctrl.py

NON_ADMIN_ENDPOINTS = [
    # Clones (clone.py)
    ("GET", "/console/api/myownclone/clones"),
    ("POST", "/console/api/myownclone/clones"),
    # Clone detail — la ruta usa parámetro; se testea con ID fijo
    # Clone prompts — requiere clone_id real

    # Analytics (analytics.py) — requieren clone_id real, se omiten de la parametrización
    #   GET  /console/api/myownclone/clones/<clone_id>/analytics/overview
    #   GET  /console/api/myownclone/clones/<clone_id>/analytics/top-questions
    #   GET  /console/api/myownclone/clones/<clone_id>/analytics/gaps
    #   POST /console/api/myownclone/clones/<clone_id>/analytics/gaps
    #   GET  /console/api/myownclone/clones/<clone_id>/analytics/costs

    # Booking (booking.py) — requieren clone_id real
    #   GET  /console/api/myownclone/clones/<clone_id>/meeting-types
    #   POST /console/api/myownclone/clones/<clone_id>/meeting-types
    #   GET  /console/api/myownclone/clones/<clone_id>/availability
    #   POST /console/api/myownclone/clones/<clone_id>/availability
    #   POST /console/api/myownclone/clones/<clone_id>/products
    #   GET  /console/api/myownclone/clones/<clone_id>/bookings
    #   POST /console/api/myownclone/clones/<clone_id>/bookings

    # Creator Memory (creator_memory.py) — requieren clone_id real
    #   GET  /console/api/myownclone/clones/<clone_id>/memories
    #   POST /console/api/myownclone/clones/<clone_id>/memories
    #   PUT  /console/api/myownclone/memories/<memory_id>
    #   DELETE /console/api/myownclone/memories/<memory_id>

    # Inbox (inbox.py) — requieren clone_id real
    #   GET  /console/api/myownclone/clones/<clone_id>/inbox
    #   GET  /console/api/myownclone/inbox/<email_id>
    #   PUT  /console/api/myownclone/inbox/<email_id>
    #   DELETE /console/api/myownclone/inbox/<email_id>
    #   POST /console/api/myownclone/inbox/<email_id>/generate-draft

    # Plans (stripe_ctrl.py)
    ("GET", "/console/api/myownclone/plans"),

    # Stripe (stripe_ctrl.py)
    ("POST", "/console/api/myownclone/stripe/checkout"),
    ("GET", "/console/api/myownclone/stripe/billing"),

    # Feedback (feedback.py)
    ("POST", "/console/api/myownclone/feedback"),
    ("GET", "/console/api/myownclone/feedback/stats"),
]


@pytest.mark.parametrize("method,path", NON_ADMIN_ENDPOINTS)
def test_non_admin_endpoint_exists_and_requires_auth(client, method, path):
    """
    Verifica que cada endpoint no-admin:
    1. Existe (no es 404)
    2. Requiere autenticación (sin token → 401 o 403)
    """
    r = client.open(path, method=method)
    # Sin auth, debe rechazar (401/403) o 400 si falta body en POST
    # Nunca 200 porque todos requieren login
    assert r.status_code != 200, (
        f"{method} {path} returned 200 without auth — "
        f"endpoint not protected!"
    )
    assert r.status_code not in (404, 405), (
        f"{method} {path} returned {r.status_code} — "
        f"route may not exist or wrong method"
    )


@pytest.mark.skip(
    reason="tenant_a/tenant_b fixtures + test DB not yet available — "
    "requires seeded multi-tenant data"
)
@pytest.mark.parametrize("method,path", NON_ADMIN_ENDPOINTS)
def test_endpoint_scopes_by_tenant(client, tenant_a, tenant_b, method, path):
    """
    FUTURE: Cuando existan fixtures tenant_a/tenant_b con datos reales,
    este test verifica que tenant_b NO vea los recursos de tenant_a.

    tenant_a crea un recurso; tenant_b no debe verlo.
    """
    res_a = client.open(path, method=method, headers=tenant_a.auth_headers)
    res_b = client.open(path, method=method, headers=tenant_b.auth_headers)
    assert res_a.status_code == 200
    assert res_b.status_code == 200
    ids_a = {item["id"] for item in res_a.json.get("items", [])}
    ids_b = {item["id"] for item in res_b.json.get("items", [])}
    assert ids_a.isdisjoint(ids_b), f"Tenant leak detected in {method} {path}"
