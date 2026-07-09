"""Prompt management API endpoints.

CRUD for system prompts with versioning.
"""

from __future__ import annotations

import logging

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import login_required

logger = logging.getLogger(__name__)


class PromptCreatePayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    clone_id: str | None = None
    task: str = Field(default="chat")
    description: str | None = None


class PromptVersionPayload(BaseModel):
    content: str = Field(..., min_length=1)
    variables: dict | None = None
    activate: bool = True


@console_ns.route("/myownclone/prompts")
class PromptListApi(Resource):
    """List all prompts."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.core.prompts import PromptService
        ps = PromptService()
        clone_id = request.args.get("clone_id")
        prompts = ps.list_prompts(clone_id=clone_id)
        return {"prompts": prompts, "total": len(prompts)}, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.core.prompts import PromptService
        ps = PromptService()
        payload = PromptCreatePayload.model_validate(request.json)
        prompt_id = ps.get_or_create_prompt(
            name=payload.name,
            clone_id=payload.clone_id,
            task=payload.task,
        )
        return {"id": prompt_id, "name": payload.name}, 201


@console_ns.route("/myownclone/prompts/<string:prompt_id>")
class PromptDetailApi(Resource):
    """Get prompt details and versions."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self, prompt_id: str):
        from api.core.prompts import PromptService
        from api.models.prompt import Prompt

        ps = PromptService()
        prompt = db.session.get(Prompt, prompt_id)
        if not prompt:
            return {"error": "prompt not found"}, 404

        versions = ps.list_versions(prompt_id)
        return {
            "id": str(prompt.id),
            "name": prompt.name,
            "clone_id": prompt.clone_id,
            "task": prompt.task,
            "description": prompt.description,
            "versions": [
                {
                    "id": v.id,
                    "version": v.version,
                    "content": v.content,
                    "variables": v.variables,
                    "is_active": v.is_active,
                    "created_by": v.created_by,
                    "created_at": v.created_at.isoformat() if v.created_at else None,
                }
                for v in versions
            ],
        }, 200


@console_ns.route("/myownclone/prompts/<string:prompt_id>/versions")
class PromptVersionApi(Resource):
    """Create a new version of a prompt."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, prompt_id: str):
        from api.core.prompts import PromptService
        ps = PromptService()
        payload = PromptVersionPayload.model_validate(request.json)

        try:
            version = ps.create_version(
                prompt_id=prompt_id,
                content=payload.content,
                variables=payload.variables,
                activate=payload.activate,
            )
            return {
                "id": version.id,
                "version": version.version,
                "is_active": version.is_active,
            }, 201
        except ValueError as exc:
            return {"error": str(exc)}, 404


@console_ns.route("/myownclone/prompts/active")
class PromptActiveApi(Resource):
    """Get the active prompt for a clone/task."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.core.prompts import PromptService
        ps = PromptService()
        clone_id = request.args.get("clone_id")
        task = request.args.get("task", "chat")

        result = ps.get_active_prompt(clone_id=clone_id, task=task)
        if not result:
            return {"error": "no active prompt found"}, 404

        content, variables = result
        return {
            "content": content,
            "variables": variables,
            "clone_id": clone_id,
            "task": task,
        }, 200
