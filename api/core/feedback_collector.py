"""FeedbackCollector — records user feedback on AI responses.

Records to response_feedback table and updates MetricsCollector quality score
for the SmartRouter (M15).
"""
from __future__ import annotations

import logging
from typing import Optional

from sqlalchemy import select

from api.extensions.ext_database import db
from api.models import ResponseFeedback
from api.models.ai_invocation import AIInvocation

logger = logging.getLogger(__name__)


class FeedbackCollector:
    """Records user feedback on AI responses.

    Usage:
        collector = FeedbackCollector()
        collector.record(
            tenant_id="tenant-123",
            invocation_id="inv-456",
            rating=1,  # +1 or -1
            comment="Great answer!",
        )
    """

    def record(
        self,
        tenant_id: Optional[str],
        invocation_id: str,
        rating: int,
        implicit_signal: Optional[int] = None,
        comment: Optional[str] = None,
    ) -> ResponseFeedback:
        """Record feedback on an AI response.

        Args:
            tenant_id: The tenant that owns this feedback.
            invocation_id: The ai_invocations.id being feedback'd.
            rating: +1 (thumbs up) or -1 (thumbs down).
            implicit_signal: Optional implicit signal (e.g., time spent).
            comment: Optional comment.

        Returns:
            The created ResponseFeedback record.
        """
        if rating not in (-1, 1):
            raise ValueError("rating must be +1 or -1")

        feedback = ResponseFeedback(
            tenant_id=tenant_id,
            invocation_id=invocation_id,
            rating=rating,
            implicit_signal=implicit_signal,
            comment=comment,
        )
        db.session.add(feedback)
        db.session.commit()

        # Update quality score in MetricsCollector
        self._update_quality_score(invocation_id, rating)

        logger.debug(
            "Recorded feedback: invocation_id=%s rating=%s",
            invocation_id,
            rating,
        )

        return feedback

    def _update_quality_score(
        self,
        invocation_id: str,
        rating: int,
    ) -> None:
        """Update the quality score in MetricsCollector for the model used in this invocation."""
        try:
            # Look up the model used in this invocation
            invocation = db.session.execute(
                select(AIInvocation).where(AIInvocation.id == invocation_id)
            ).scalar_one_or_none()

            if not invocation or not invocation.model_id:
                logger.debug("No model_id found for invocation %s", invocation_id)
                return

            # Map rating (-1, +1) to quality score (0.0-1.0)
            # +1 → 1.0, -1 → 0.0
            quality_score = 1.0 if rating > 0 else 0.0

            # Update MetricsCollector
            from api.core.metrics_collector import get_metrics_collector
            metrics = get_metrics_collector()
            metrics.record_quality(invocation.model_id, quality_score)

            logger.debug(
                "Updated quality score for model_id=%s score=%.1f",
                invocation.model_id,
                quality_score,
            )
        except Exception as exc:
            logger.warning("Failed to update quality score: %s", exc)


# ─── Singleton instance ─────────────────────────────────────────────────────────

_collector: Optional[FeedbackCollector] = None


def get_feedback_collector() -> FeedbackCollector:
    """Get the process-wide FeedbackCollector singleton."""
    global _collector
    if _collector is None:
        _collector = FeedbackCollector()
    return _collector
