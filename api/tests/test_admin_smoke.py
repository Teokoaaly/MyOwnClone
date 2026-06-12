"""
Fase 5: Smoke tests de admin.

Verifica que:
- Endpoints de admin requieren autenticación (401 sin token)
- Endpoints de admin rechazan tokens invalidos/expirados
- El contrato del auth header es el esperado (Bearer)

NOTA: Solo se incluyen los endpoints que EXISTEN realmente en el codigo.
"""

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
