"""ModerationService: 2-level content moderation.

Level 1 (instant): Regex patterns for obvious violations (CSAM keywords, weapons, doxxing).
Level 2 (~200ms): OpenAI Moderation API for nuanced detection.

Reads MODERATION_ENABLED env var. Records cost via _record_llm_cost if Level 2 is invoked.
"""
from __future__ import annotations

import hashlib
import logging
import os
import re
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


def _moderation_enabled() -> bool:
    """Check if moderation is enabled via env var."""
    return os.environ.get("MODERATION_ENABLED", "").strip().lower() in ("1", "true", "yes")


# ─── Level 1: Regex patterns ───────────────────────────────────────────────────

# Obvious violations that don't need LLM analysis
_LEVEL1_PATTERNS = [
    # CSAM keywords (simplified - real detection would use specialized tools)
    (r"\bcsam\b", "csam"),
    (r"\bchild[\s-]?exploit\b", "csam"),
    (r"\bchild[\s-]?abuse\b", "csam"),
    # Weapons / explosives
    (r"\bhow[\s-]?to[\s-]?make[\s-]?(bomb|explosive|grenade)\b", "weapons"),
    (r"\bpipe[\s-]?bomb[\s-]?(recipe|instructions?)\b", "weapons"),
    # Doxxing / personal data exposure
    (r"\bdox\b", "doxxing"),
    (r"\bpublish[\s-]?(someone['\s]?s)?[\s-]?(address|phone|ssn|social[\s-]?security)\b", "doxxing"),
    (r"\bswatt?ing\b", "doxxing"),
    # Extreme violence
    (r"\bhow[\s-]?to[\s-]?kill\b", "violence"),
    (r"\bhow[\s-]?to[\s-]?murder\b", "violence"),
]


@dataclass
class ModerationResult:
    """Result of a moderation check."""
    flagged: bool
    categories: list[str]
    reason: str
    level: str  # "level_1" or "level_2"


class ModerationService:
    """2-level content moderation service.

    Level 1: Regex (instant) for obvious violations
    Level 2: OpenAI Moderation API (~200ms) for nuanced detection

    Usage:
        service = ModerationService()
        result = service.check("some text to moderate")
        if result.flagged:
            print(f"Flagged: {result.categories} ({result.level})")
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize with optional API key override."""
        self._api_key = api_key
        self._openai_client = None

    def _get_openai_client(self):
        """Lazily create OpenAI client."""
        if self._openai_client is None:
            import openai
            key = self._api_key or os.environ.get("OPENAI_API_KEY", "")
            if not key:
                raise RuntimeError(
                    "OpenAI API key not configured. Set OPENAI_API_KEY environment variable."
                )
            self._openai_client = openai.OpenAI(api_key=key)
        return self._openai_client

    def check(self, text: str, tenant_id: Optional[str] = None) -> ModerationResult:
        """Run moderation check on text.

        Args:
            text: The text to moderate.
            tenant_id: Optional tenant ID for logging.

        Returns:
            ModerationResult with flagged status, categories, reason, and level.
        """
        if not _moderation_enabled():
            return ModerationResult(
                flagged=False,
                categories=[],
                reason="Moderation disabled",
                level="disabled",
            )

        # Level 1: Regex check (instant)
        level1_result = self._check_level1(text)
        if level1_result.flagged:
            self._record_event(tenant_id, text, level1_result)
            return level1_result

        # Level 2: OpenAI Moderation API (~200ms)
        level2_result = self._check_level2(text)
        self._record_event(tenant_id, text, level2_result)
        return level2_result

    def _check_level1(self, text: str) -> ModerationResult:
        """Run regex-based moderation check."""
        text_lower = text.lower()
        categories = []

        for pattern, category in _LEVEL1_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                if category not in categories:
                    categories.append(category)

        if categories:
            return ModerationResult(
                flagged=True,
                categories=categories,
                reason=f"Level 1 regex match: {', '.join(categories)}",
                level="level_1",
            )

        return ModerationResult(
            flagged=False,
            categories=[],
            reason="No Level 1 violations detected",
            level="level_1",
        )

    def _check_level2(self, text: str) -> ModerationResult:
        """Run OpenAI Moderation API check."""
        try:
            client = self._get_openai_client()
            response = client.moderations.create(input=text)
            result = response.results[0]

            categories = [
                cat for cat, flagged in result.categories.model_dump().items()
                if flagged
            ]

            if result.flagged:
                return ModerationResult(
                    flagged=True,
                    categories=categories,
                    reason=f"Level 2 OpenAI flag: {', '.join(categories)}",
                    level="level_2",
                )

            return ModerationResult(
                flagged=False,
                categories=[],
                reason="No violations detected",
                level="level_2",
            )
        except Exception as exc:
            logger.warning("Level 2 moderation check failed: %s", exc)
            # Don't block content if moderation API fails
            return ModerationResult(
                flagged=False,
                categories=[],
                reason=f"Level 2 check error (content allowed): {exc}",
                level="level_2",
            )

    def _record_event(
        self,
        tenant_id: Optional[str],
        text: str,
        result: ModerationResult,
    ) -> None:
        """Record a moderation event to the database."""
        try:
            from api.models import ModerationEvent
            from api.models.moderation_log import _sha256
            from api.extensions.ext_database import db

            text_hash = _sha256(text[:10000])  # Hash first 10k chars

            event = ModerationEvent(
                tenant_id=tenant_id,
                text_hash=text_hash,
                flagged=result.flagged,
                level=result.level,
                categories=",".join(result.categories) if result.categories else None,
                model="openai/moderation" if result.level == "level_2" else None,
            )
            db.session.add(event)
            db.session.commit()
        except Exception as exc:
            logger.warning("Failed to record moderation event: %s", exc)
            try:
                from api.extensions.ext_database import db
                db.session.rollback()
            except Exception:
                pass

        # Record cost if Level 2 was used
        if result.level == "level_2":
            self._record_cost(tenant_id)


    def _record_cost(self, tenant_id: Optional[str]) -> None:
        """Record moderation cost via _record_llm_cost."""
        try:
            from api.core.cost_recording import _record_llm_cost
            from api.models.analytics import CostCategory

            # OpenAI Moderation API is free, but we record the usage for tracking
            _record_llm_cost(
                tenant_id=tenant_id or "platform",
                category=CostCategory.MODERATION,
                operation="moderation",
                model="openai/moderation",
                tokens_in=0,
                tokens_out=0,
                cost_cents=0,  # Free API
                latency_ms=0,
                success=True,
                error_message=None,
            )
        except Exception as exc:
            logger.warning("Failed to record moderation cost: %s", exc)


# Add MODERATION to CostCategory if not exists
try:
    from api.models.analytics import CostCategory
    if "moderation" not in CostCategory._member_names_:
        import enum
        # We can't modify the enum at runtime easily, so we'll handle it in cost_recording
except ImportError:
    pass


# ─── Singleton instance ─────────────────────────────────────────────────────────

_moderation_service: Optional[ModerationService] = None


def get_moderation_service() -> ModerationService:
    """Get the process-wide ModerationService singleton."""
    global _moderation_service
    if _moderation_service is None:
        _moderation_service = ModerationService()
    return _moderation_service
