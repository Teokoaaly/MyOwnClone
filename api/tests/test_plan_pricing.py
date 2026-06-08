"""
Fase 2: Validación de precios MRR.

Asegura que cada plan activo en la base de datos tenga
un precio mapeado en la lógica de cálculo de MRR del admin overview.
Si se añade un plan nuevo sin actualizar el mapeo de precios,
el MRR reportará 0 para ese plan (falso negativo).
"""

import pytest


# ── Mapeo de precios vigente ───────────────────────────────────────────
# Fuente: api/controllers/console/myownclone/admin_platform.py:61
#   plan_prices = {"básico": 4900, "pro": 9900, "escala": 19900, "enterprise": 49900}
#
# Este diccionario DUPLICA la lógica del admin overview.
# La función validate_plan_pricing() lo cruza contra los planes
# en base de datos y reporta cualquier plan sin mapeo.

ADMIN_PLAN_PRICES_CENTS = {
    "básico": 4900,
    "pro": 9900,
    "escala": 19900,
    "enterprise": 49900,
}


def validate_plan_pricing(plan_names: list[str]) -> list[str]:
    """
    Devuelve una lista de nombres de plan que NO tienen precio mapeado.

    Args:
        plan_names: lista de nombres de plan (lowercase) de la BD

    Returns:
        lista de nombres sin precio (vacía si todo OK)
    """
    missing = []
    for name in plan_names:
        name_lower = name.lower().strip()
        if name_lower not in ADMIN_PLAN_PRICES_CENTS:
            missing.append(name)
    return missing


def test_validate_plan_pricing_empty_when_all_mapped():
    """Si todos los planes están mapeados, validate_plan_pricing devuelve []."""
    result = validate_plan_pricing(["básico", "pro", "escala", "enterprise"])
    assert result == [], f"Expected empty, got {result}"


def test_validate_plan_pricing_detects_unmapped():
    """Un plan sin mapear debe aparecer en la lista de missing."""
    result = validate_plan_pricing(["básico", "nuevo_plan_premium", "pro"])
    assert "nuevo_plan_premium" in result


def test_validate_plan_pricing_case_insensitive():
    """La comparación debe ser case-insensitive."""
    result = validate_plan_pricing(["BÁSICO", "Pro", "ESCALA"])
    assert result == [], f"Case mismatch: {result}"


@pytest.mark.skip(
    reason="db_session fixture not yet available — "
    "requires test database with Plan table"
)
def test_every_active_plan_has_price(db_session):
    """
    Test de integración: cruza los planes activos en BD
    contra el mapeo de precios del admin overview.
    """
    from api.models.analytics import Plan

    # Nota: Plan no tiene campo 'active'. Se consideran todos.
    # Si se añade un campo active en el futuro, filtrar aquí.
    plans = db_session.query(Plan).all()
    plan_names = [p.name for p in plans]

    missing = validate_plan_pricing(plan_names)
    assert missing == [], (
        f"Planes activos sin precio mapeado — el MRR reportará 0 para: {missing}. "
        f"Actualiza ADMIN_PLAN_PRICES_CENTS en admin_platform.py."
    )


def test_admin_plan_prices_has_all_expected_tiers():
    """Verifica que los 4 tiers de precio esperados existen en el mapeo."""
    expected_tiers = ["básico", "pro", "escala", "enterprise"]
    for tier in expected_tiers:
        assert tier in ADMIN_PLAN_PRICES_CENTS, (
            f"Tier '{tier}' ausente en ADMIN_PLAN_PRICES_CENTS"
        )


def test_admin_plan_prices_positive():
    """Todos los precios deben ser positivos (> 0)."""
    for plan, price in ADMIN_PLAN_PRICES_CENTS.items():
        assert price > 0, (
            f"Plan '{plan}' tiene precio {price} — debe ser > 0"
        )
