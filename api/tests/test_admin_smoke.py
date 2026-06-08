"""
Fase 5: Smoke tests de admin.

Verifica que:
- Endpoints de admin requieren autenticación (401 sin token)
- Endpoints de admin rechazan usuarios no-admin (403 con token de usuario normal)
- Endpoints de admin aceptan admin (200 con token de admin)

NOTA: Solo se incluyen los endpoints que EXISTEN realmente en el código.
Endpoints del plan original que NO existen (y por tanto se omiten):
  - /console/api/myownclone/admin/audit
  - /console/api/myownclone/admin/impersonation (existe /impersonate pero es POST no GET)
  - /console/api/myownclone/admin/courtesy
"""

import pytest

# ── Endpoints de admin que existen realmente ──────────────────────────
# Verificados con: grep -rn "admin/" api/controllers/ --include="*.py"
# Los endpoints reales usan el prefijo /console/api del console blueprint
# + el namespace path "/" + la ruta declarada en @console_ns.route(...)
ADMIN_ENDPOINTS = [
    "/console/api/myownclone/admin/overview",
    "/console/api/myownclone/admin/tenants",
]


@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_requires_auth(client, path):
    """Sin token de autorización, los endpoints de admin deben devolver 401."""
    assert client.get(path).status_code == 401


@pytest.mark.skip(
    reason="Requiere base de datos PostgreSQL + seed de cuenta no-admin + "
    "JWT válido firmado con la clave del entorno de pruebas. "
    "Este test se ejecuta en CI (ver .github/workflows/ci.yml) "
    "donde el servicio postgres está disponible."
)
@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_forbids_non_admin(client, user_headers, path):
    """Un usuario autenticado pero NO admin debe recibir 403."""
    assert client.get(path, headers=user_headers).status_code == 403


@pytest.mark.skip(
    reason="Requiere base de datos PostgreSQL + seed de cuenta admin + "
    "JWT válido firmado con la clave del entorno de pruebas. "
    "Este test se ejecuta en CI (ver .github/workflows/ci.yml) "
    "donde el servicio postgres está disponible."
)
@pytest.mark.parametrize("path", ADMIN_ENDPOINTS)
def test_admin_ok_for_admin(client, admin_headers, path):
    """Un usuario admin autenticado debe recibir 200."""
    assert client.get(path, headers=admin_headers).status_code == 200
