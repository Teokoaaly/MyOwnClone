"""Prompt management module — CRUD for system prompts with versioning.

Stores prompts in the database with version tracking.
Optional Langfuse integration for A/B testing and evaluation.

Usage:
    from api.core.prompts import PromptService
    ps = PromptService()
    prompt = ps.create_prompt(name="support_bot", content="You are a support agent...")
    versions = ps.list_versions(prompt_id="...")
    active = ps.get_active_prompt(clone_id="...", task="chat")
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy import select, func

from api.extensions.ext_database import db

logger = logging.getLogger(__name__)


@dataclass
class PromptVersion:
    id: str
    prompt_id: str
    version: int
    content: str
    variables: dict | None
    is_active: bool
    created_at: datetime | None
    created_by: str | None


class PromptService:
    """Manage system prompts with versioning."""

    def get_or_create_prompt(
        self,
        name: str,
        clone_id: str | None = None,
        task: str = "chat",
    ) -> str:
        """Get or create a prompt by name. Returns prompt_id."""
        from api.models.prompt import Prompt

        existing = db.session.execute(
            select(Prompt).where(
                Prompt.name == name,
                Prompt.clone_id == clone_id,
            )
        ).scalar_one_or_none()

        if existing:
            return str(existing.id)

        prompt = Prompt(
            name=name,
            clone_id=clone_id,
            task=task,
            description=f"Auto-created prompt: {name}",
        )
        db.session.add(prompt)
        db.session.flush()
        return str(prompt.id)

    def create_version(
        self,
        prompt_id: str,
        content: str,
        variables: dict | None = None,
        created_by: str | None = None,
        activate: bool = True,
    ) -> PromptVersion:
        """Create a new version of a prompt."""
        from api.models.prompt import Prompt, PromptVersion as PromptVersionModel

        prompt = db.session.get(Prompt, prompt_id)
        if not prompt:
            raise ValueError(f"Prompt {prompt_id} not found")

        # Get next version number
        max_version = db.session.execute(
            select(func.coalesce(func.max(PromptVersionModel.version), 0))
            .where(PromptVersionModel.prompt_id == prompt_id)
        ).scalar() or 0

        new_version = max_version + 1

        if activate:
            # Deactivate all other versions
            db.session.query(PromptVersionModel).filter(
                PromptVersionModel.prompt_id == prompt_id,
                PromptVersionModel.is_active.is_(True),
            ).update({"is_active": False})

        pv = PromptVersionModel(
            prompt_id=prompt_id,
            version=new_version,
            content=content,
            variables=variables,
            is_active=activate,
            created_by=created_by,
        )
        db.session.add(pv)
        db.session.commit()

        return PromptVersion(
            id=str(pv.id),
            prompt_id=prompt_id,
            version=new_version,
            content=content,
            variables=variables,
            is_active=activate,
            created_at=pv.created_at,
            created_by=created_by,
        )

    def get_active_prompt(
        self,
        clone_id: str | None = None,
        task: str = "chat",
    ) -> tuple[str, dict] | None:
        """Get the active prompt content for a clone/task.

        Returns (content, variables) or None.
        """
        from api.models.prompt import Prompt, PromptVersion as PromptVersionModel

        stmt = (
            select(PromptVersionModel)
            .join(Prompt, Prompt.id == PromptVersionModel.prompt_id)
            .where(
                Prompt.clone_id == clone_id,
                Prompt.task == task,
                PromptVersionModel.is_active.is_(True),
            )
            .order_by(PromptVersionModel.version.desc())
            .limit(1)
        )
        pv = db.session.execute(stmt).scalar_one_or_none()
        if not pv:
            return None
        return (pv.content, pv.variables or {})

    def list_versions(self, prompt_id: str) -> list[PromptVersion]:
        """List all versions of a prompt."""
        from api.models.prompt import PromptVersion as PromptVersionModel

        stmt = (
            select(PromptVersionModel)
            .where(PromptVersionModel.prompt_id == prompt_id)
            .order_by(PromptVersionModel.version.desc())
        )
        rows = db.session.execute(stmt).scalars().all()
        return [
            PromptVersion(
                id=str(r.id),
                prompt_id=r.prompt_id,
                version=r.version,
                content=r.content,
                variables=r.variables,
                is_active=r.is_active,
                created_at=r.created_at,
                created_by=r.created_by,
            )
            for r in rows
        ]

    def list_prompts(self, clone_id: str | None = None) -> list[dict]:
        """List all prompts, optionally filtered by clone."""
        from api.models.prompt import Prompt, PromptVersion as PromptVersionModel

        stmt = select(Prompt)
        if clone_id:
            stmt = stmt.where(Prompt.clone_id == clone_id)
        stmt = stmt.order_by(Prompt.name)
        rows = db.session.execute(stmt).scalars().all()

        results = []
        for p in rows:
            vcount = db.session.execute(
                select(func.count()).select_from(PromptVersionModel).where(
                    PromptVersionModel.prompt_id == str(p.id)
                )
            ).scalar() or 0
            results.append({
                "id": str(p.id),
                "name": p.name,
                "clone_id": p.clone_id,
                "task": p.task,
                "description": p.description,
                "version_count": vcount,
            })
        return results
