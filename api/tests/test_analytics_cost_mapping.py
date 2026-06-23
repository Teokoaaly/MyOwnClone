"""M13 — defect #3 analytics cost mapping regression.

Guards that the cost-breakdown endpoint maps categories through the explicit
``CostCategory`` enum mapping instead of the previous fragile implicit
``f"{row[0]}_cents"`` derivation.
"""

from __future__ import annotations

import importlib.util

from api.models.analytics import CostCategory


def _analytics_source() -> str:
    spec = importlib.util.find_spec(
        "api.controllers.console.myownclone.analytics"
    )
    assert spec is not None and spec.origin
    with open(spec.origin, encoding="utf-8") as handle:
        return handle.read()


def test_cost_breakdown_uses_explicit_cost_category_mapping():
    src = _analytics_source()
    # Explicit enum-driven mapping is present.
    assert "CostCategory" in src
    assert "_COST_CATEGORY_TO_FIELD" in src
    # The fragile implicit derivation is gone from the code (the phrase may
    # still appear inside the explanatory comment, so we assert on the actual
    # statements that implemented it, not the bare substring).
    assert 'key = f"{row[0]}_cents"' not in src
    assert "if key in costs" not in src


def test_cost_category_enum_covers_expected_members():
    values = {c.value for c in CostCategory}
    assert {"clone_response", "content_ingestion", "platform_ops"} <= values
