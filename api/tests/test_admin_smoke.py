"""
Fase 5: Smoke tests de admin.

Verifica que:
- Endpoints de admin requieren autenticación (401 sin token)
- Endpoints de admin rechazan tokens invalidos/expirados
- El contrato del auth header es el esperado (Bearer)

NOTA: Solo se incluyen los endpoints que EXISTEN realmente en el codigo.
"""

import os
import time
import jwt
import pytest

ADMIN_ENDPOINTS = [
    "/console/api/myownclone/admin/overview",
    "/console/api/myownclone/admin/tenants",
]


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_requires_auth(client, path):
    """Sin token, los endpoints de admin deben devolver 401."""
    assert client.get(path).status_code == 401


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_rejects_malformed_bearer(client, path):
    """Authorization sin prefijo Bearer debe rechazarse con 401."""
    r = client.get(path, headers={"Authorization": "Token foo"})
    assert r.status_code == 401


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_rejects_unsigned_token(client, path):
    """Un JWT firmado con una clave distinta no debe autenticar."""
    bad_token = jwt.encode(
        {"sub": "user-1", "role": "platform_admin", "exp": int(time.time()) + 3600},
        "attacker-secret-key",
        algorithm="HS256",
    )
    r = client.get(path, headers={"Authorization": f"Bearer {bad_token}"})
    assert r.status_code == 401


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_rejects_expired_token(client, path):
    """Un JWT firmado con la clave correcta pero expirado debe rechazarse."""
    import os

    # La clave usada por _verify_token en el test es JWT_SECRET_KEY del conftest,
    # o un secreto aleatorio por proceso si falta.
    from api.libs.jwt_utils import _get_secret_key

    secret = _get_secret_key()
    expired = jwt.encode(
        {"sub": "user-1", "role": "platform_admin", "exp": int(time.time()) - 60},
        secret,
        algorithm="HS256",
    )
    r = client.get(path, headers={"Authorization": f"Bearer {expired}"})
    assert r.status_code == 401


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_rejects_empty_bearer(client, path):
    """Bearer con token vacio debe rechazarse (no 200)."""
    r = client.get(path, headers={"Authorization": "Bearer "})
    assert r.status_code in (401, 403)


@pytest.mark.skipif(
    os.environ.get("DB_HOST") == "localhost",
    reason="Requires real PostgreSQL instance for platform_admin lookup",
)
def test_admin_overview_includes_unpriced_plans(client):
    """
    B7: GET /admin/overview returns unpriced_plans field.
    Requires PostgreSQL to verify platform_admin lookup succeeds.
    """
    from api.libs.jwt_utils import _get_secret_key

    secret = _get_secret_key()
    admin_token = jwt.encode(
        {"sub": "platform-admin-test", "role": "platform_admin", "exp": int(time.time()) + 3600},
        secret,
        algorithm="HS256",
    )
    resp = client.get(
        "/console/api/myownclone/admin/overview",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.data}"
    body = resp.get_json()
    assert "unpriced_plans" in body, f"Missing unpriced_plans in {body.keys()}"
    assert isinstance(body["unpriced_plans"], list), "unpriced_plans must be a list"
    # All 5 plans currently priced — expect empty list
    assert body["unpriced_plans"] == [], f"Expected empty, got {body['unpriced_plans']}"
