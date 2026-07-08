"""Audit rollups for configurable AI runtime usage."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta

from sqlalchemy import delete, select

from api.extensions.ext_database import db
from api.models.ai_models import AIInvocation, CostDailyRollup


@dataclass(slots=True)
class RollupRow:
    tenant_id: str
    day: date
    task: str
    model: str
    invocations: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    success_count: int = 0
    error_count: int = 0


def build_cost_daily_rollup_rows(
    invocations: list[AIInvocation],
) -> list[RollupRow]:
    buckets: dict[tuple[str, date, str, str], RollupRow] = {}
    for row in invocations:
        day = row.created_at.date()
        key = (row.tenant_id, day, row.task, row.model)
        bucket = buckets.get(key)
        if bucket is None:
            bucket = RollupRow(
                tenant_id=row.tenant_id,
                day=day,
                task=row.task,
                model=row.model,
            )
            buckets[key] = bucket
        bucket.invocations += 1
        bucket.prompt_tokens += row.prompt_tokens or 0
        bucket.completion_tokens += row.completion_tokens or 0
        if row.success:
            bucket.success_count += 1
        else:
            bucket.error_count += 1
    return sorted(
        buckets.values(),
        key=lambda item: (item.day, item.tenant_id, item.task, item.model),
    )


def refresh_cost_daily_rollup(*, days: int = 30) -> int:
    since = datetime.utcnow() - timedelta(days=days)
    invocations = db.session.execute(
        select(AIInvocation).where(AIInvocation.created_at >= since)
    ).scalars().all()
    rows = build_cost_daily_rollup_rows(invocations)
    min_day = since.date()

    db.session.execute(
        delete(CostDailyRollup).where(CostDailyRollup.day >= min_day)
    )
    for row in rows:
        db.session.add(
            CostDailyRollup(
                tenant_id=row.tenant_id,
                day=row.day,
                task=row.task,
                model=row.model,
                invocations=row.invocations,
                prompt_tokens=row.prompt_tokens,
                completion_tokens=row.completion_tokens,
                success_count=row.success_count,
                error_count=row.error_count,
            )
        )
    db.session.commit()
    return len(rows)
