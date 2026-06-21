"""SmartRouter: score-based model selection for (tenant_id, task).

SCORE = cost_score * 0.4 + latency_score * 0.3 + success_score * 0.2 + priority_score * 0.1

Uses MetricsCollector for real-time latency and success metrics.
Records every decision in routing_decisions table.
"""
from __future__ import annotations

import os
import logging
from typing import Optional

from sqlalchemy import select

from api.extensions.ext_database import db
from api.models import AIModel, AIModelAssignment, RoutingDecision
from api.core.metrics_collector import MetricsCollector, get_metrics_collector

logger = logging.getLogger(__name__)

# Score weights
WEIGHT_COST = 0.4
WEIGHT_LATENCY = 0.3
WEIGHT_SUCCESS = 0.2
WEIGHT_PRIORITY = 0.1


def _smart_router_enabled() -> bool:
    """Check if SmartRouter is enabled via env var."""
    return os.environ.get("SMART_ROUTER_ENABLED", "").strip().lower() in ("1", "true", "yes")


class SmartRouter:
    """Score-based model router.

    When SMART_ROUTER_ENABLED is true, route() is called instead of
    the default priority-based selection in ModelRegistry.

    SCORE = cost_score * 0.4 + latency_score * 0.3 + success_score * 0.2 + priority_score * 0.1
    """

    def __init__(self, metrics: Optional[MetricsCollector] = None):
        self._metrics = metrics or get_metrics_collector()

    def route(
        self,
        tenant_id: str,
        task: str,
        candidates: list[AIModel],
    ) -> AIModel:
        """Select the best model from candidates based on composite score.

        Returns the highest-scoring model, or the first candidate if SmartRouter
        is disabled or no metrics are available.

        Args:
            tenant_id: The tenant requesting the route.
            task: The task type (e.g., chat_primary, embedding).
            candidates: List of candidate AIModel objects.

        Returns:
            The selected AIModel with the highest composite score.
        """
        if not _smart_router_enabled():
            # Fallback to first candidate (priority-based selection)
            if candidates:
                return candidates[0]
            raise RuntimeError(f"No candidates for task={task}")

        if not candidates:
            raise RuntimeError(f"No candidates for task={task}")

        if len(candidates) == 1:
            return candidates[0]

        # Score all candidates
        scored = []
        for model in candidates:
            score, reason = self._score_model(model)
            scored.append((score, reason, model))

        # Sort by score descending
        scored.sort(key=lambda x: x[0], reverse=True)
        best_score, best_reason, best_model = scored[0]

        # Record the decision
        self._record_decision(
            tenant_id=tenant_id,
            task=task,
            candidates_considered=len(candidates),
            chosen_model_id=str(best_model.id) if best_model else None,
            score=best_score,
            reason=best_reason,
        )

        logger.debug(
            "SmartRouter selected model=%s/%s score=%.3f reason=%s",
            best_model.provider if best_model else None,
            best_model.name if best_model else None,
            best_score,
            best_reason,
        )

        return best_model

    def _score_model(self, model: AIModel) -> tuple[float, str]:
        """Compute composite score for a single model.

        Returns (score, reason_string).
        """
        reasons = []
        total_score = 0.0

        # Cost score (lower cost = higher score)
        # Input + output cost per 1K tokens
        cost_per_1k = (model.input_cost_per_1k or 0) + (model.output_cost_per_1k or 0)
        # Normalize: 0 cost = 1.0, 10+ cents = 0.0
        cost_score = max(0.0, 1.0 - (cost_per_1k / 10.0))
        reasons.append(f"cost={cost_score:.2f}")
        total_score += cost_score * WEIGHT_COST

        # Latency score (lower latency = higher score)
        # Use p95 latency from MetricsCollector
        model_id = str(model.id)
        p95_latency = self._metrics.get_p95_latency_ms(model_id)
        # Normalize: 0ms = 1.0, 5000ms+ = 0.0
        latency_score = max(0.0, 1.0 - (p95_latency / 5000.0))
        reasons.append(f"latency={latency_score:.2f}(p95={p95_latency:.0f}ms)")
        total_score += latency_score * WEIGHT_LATENCY

        # Success rate score
        success_rate = self._metrics.get_success_rate(model_id)
        reasons.append(f"success={success_rate:.2f}")
        total_score += success_rate * WEIGHT_SUCCESS

        # Priority score (higher priority = higher score)
        # Normalize: priority 0 = 0.0, priority 100+ = 1.0
        # We don't have direct access to priority here since we're scoring AIModel
        # The priority is on AIModelAssignment, not AIModel
        # So we use a neutral priority score
        priority_score = 0.5
        reasons.append(f"priority={priority_score:.2f}")
        total_score += priority_score * WEIGHT_PRIORITY

        reason = ", ".join(reasons)
        return total_score, reason

    def _record_decision(
        self,
        tenant_id: str,
        task: str,
        candidates_considered: int,
        chosen_model_id: Optional[str],
        score: Optional[float],
        reason: Optional[str],
    ) -> None:
        """Record a routing decision in the database."""
        try:
            decision = RoutingDecision(
                tenant_id=tenant_id,
                task=task,
                candidates_considered=candidates_considered,
                chosen_model_id=chosen_model_id,
                score=score,
                reason=reason,
            )
            db.session.add(decision)
            db.session.commit()
        except Exception as exc:
            logger.warning("Failed to record routing decision: %s", exc)
            db.session.rollback()


# ─── Integration helper ────────────────────────────────────────────────────────

def get_candidates_for_task(
    tenant_id: str,
    task: str,
) -> list[AIModel]:
    """Get all active candidate models for (tenant_id, task).

    Unlike ModelRegistry.get_model_for_task which returns ONE model,
    this returns ALL candidates for SmartRouter to score.
    """
    from sqlalchemy import and_, or_

    stmt = (
        select(AIModel)
        .join(AIModelAssignment, AIModelAssignment.model_id == AIModel.id)
        .where(
            and_(
                AIModelAssignment.task == task,
                AIModelAssignment.is_active.is_(True),
                AIModel.is_active.is_(True),
                or_(
                    AIModelAssignment.tenant_id == tenant_id,
                    AIModelAssignment.tenant_id.is_(None),
                ),
            )
        )
    )
    return list(db.session.execute(stmt).scalars().all())
