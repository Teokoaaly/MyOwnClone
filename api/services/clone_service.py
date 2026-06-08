"""CloneService — public-facing clone lookups used by public endpoints."""

from __future__ import annotations

from sqlalchemy import select

from api.extensions.ext_database import db
from api.models.myownclone import CloneConfig


class CloneService:
    """Service for retrieving clone data for public-facing endpoints."""

    @staticmethod
    def get_public_clone_by_slug(slug: str) -> CloneConfig | None:
        """Return the active clone matching *slug*, or None."""
        return db.session.execute(
            select(CloneConfig).where(
                CloneConfig.slug == slug,
                CloneConfig.is_active.is_(True),
            )
        ).scalar_one_or_none()
