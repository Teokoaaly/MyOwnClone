"""Helper centralizado para cost tracking. Usado por TODO el código."""
from typing import Optional
from api.models.analytics import CostCategory, CostTracking
from api.extensions.ext_database import db


def _record_llm_cost(
    tenant_id: str,
    category: CostCategory,
    operation: str,
    model: str,
    tokens_in: int,
    tokens_out: int,
    cost_cents: int,
    latency_ms: int,
    success: bool = True,
    error_message: Optional[str] = None,
) -> None:
    """Insert en cost_tracking con CostCategory enum. Usado por TODA invocación."""
    record = CostTracking(
        tenant_id=tenant_id,
        category=category,
        operation=operation,
        model=model,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_cents=cost_cents,
        latency_ms=latency_ms,
        success=success,
        error_message=error_message,
    )
    db.session.add(record)
    db.session.commit()
