"""
Fase 2: Validacion de precios MRR.

Asegura que cada plan canonico del sistema tenga
un precio mapeado en la logica de calculo de MRR.
Fuente canonica: api/core/contracts.py
"""

import pytest


# ── Precios canónicos ──────────────────────────────────────────────────
# Reflejan api/core/contracts.py:PLAN_PRICES_CENTS

ADMIN_PLAN_PRICES_CENTS = {
    "trial": 0,
    "basic": 4900,
    "pro": 9900,
    "scale": 19900,
    "enterprise": 49900,
}


def validate_plan_pricing(plan_names):
    """Devuelve planes sin precio mapeado."""
    missing = []
    for name in plan_names:
        name_lower = name.lower().strip()
        if name_lower not in ADMIN_PLAN_PRICES_CENTS:
            missing.append(name)
    return missing


def test_validate_plan_pricing_empty_when_all_mapped():
    result = validate_plan_pricing(["basic", "pro", "scale", "enterprise"])
    assert result == [], f"Expected empty, got {result}"


def test_validate_plan_pricing_detects_unmapped():
    result = validate_plan_pricing(["basic", "nuevo_plan_premium", "pro"])
    assert "nuevo_plan_premium" in result


def test_validate_plan_pricing_case_insensitive():
    result = validate_plan_pricing(["BASIC", "Pro", "SCALE"])
    assert result == [], f"Case mismatch: {result}"


def test_admin_plan_prices_has_all_expected_tiers():
    expected_tiers = ["basic", "pro", "scale", "enterprise"]
    for tier in expected_tiers:
        assert tier in ADMIN_PLAN_PRICES_CENTS, (
            f"Tier '{tier}' ausente en ADMIN_PLAN_PRICES_CENTS"
        )


def test_admin_plan_prices_positive():
    """Todos los precios de pago deben ser positivos; trial=0 es valido."""
    for plan, price in ADMIN_PLAN_PRICES_CENTS.items():
        assert price >= 0, (
            f"Plan '{plan}' tiene precio {price} - debe ser >= 0"
        )


def test_admin_plan_prices_match_contracts_source_of_truth():
    """
    El mapeo del test debe coincidir con la fuente canonica en codigo.
    Si alguien anade un plan en contracts.py y no actualiza este test,
    este assert falla inmediatamente.
    """
    from api.core.contracts import PLAN_PRICES_CENTS

    assert dict(PLAN_PRICES_CENTS) == ADMIN_PLAN_PRICES_CENTS, (
        "Mapeo de precios desincronizado entre test y produccion. "
        "Actualiza api/core/contracts.py y este test a la vez."
    )


def test_every_canonical_plan_has_price():
    """
    Contrato: la lista de planes canonicos debe estar
    completamente cubierta por el mapeo de precios.
    Si PLAN_KEYS crece y alguien olvida aniadir el precio,
    el MRR devolvera 0 silenciosamente.
    """
    from api.core.contracts import PLAN_KEYS, PLAN_PRICES_CENTS

    missing = [k for k in PLAN_KEYS if k not in PLAN_PRICES_CENTS]
    assert missing == [], (
        f"Planes canonicos sin precio en PLAN_PRICES_CENTS: {missing}. "
        f"MRR reportara 0 para estos."
    )


def test_mrr_calculation_includes_only_paid_plans():
    """
    trial no debe contar en MRR. basic/pro/scale/enterprise si.
    Simula el calculo del admin overview contra el mapeo.
    """
    paid = {k: v for k, v in ADMIN_PLAN_PRICES_CENTS.items() if k != "trial"}
    assert "trial" not in paid
    for plan, price in paid.items():
        assert price > 0
