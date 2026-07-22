"""Prompt management API endpoints.

CRUD for system prompts with versioning.
"""

from __future__ import annotations

import logging

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.myownclone import CloneConfig

logger = logging.getLogger(__name__)


def _clone_owned_by_tenant(clone_id: str | None, tenant_id: str | None) -> bool:
    """SECURITY (P0.4 / H-04): verify clone belongs to caller's tenant.

    Prompts are scoped via ``clone_id``; without this check any authenticated
    tenant could read/write every other tenant's prompts (which contain system
    instructions and business logic). Mirrors the helper in clone.py/feedback.py.
    """
    if not clone_id or not tenant_id:
        return False
    found = db.session.execute(
        select(CloneConfig.id).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    return found is not None


class PromptCreatePayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    clone_id: str = Field(..., min_length=1)
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
        _account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400
        ps = PromptService()
        clone_id = request.args.get("clone_id")

        # P0.4 (H-04): si se filtra por clone_id, verificar tenancy.
        if clone_id and not _clone_owned_by_tenant(clone_id, tenant_id):
            return {"error": "clone not found"}, 404

        # P0.4 (H-04, residual cerrado por verifier): cuando NO hay clone_id,
        # scope por el set de clones del tenant para evitar cross-tenant read
        # de prompts (system instructions / business logic). Antes,
        # list_prompts(clone_id=None) devolvia TODOS los prompts de TODOS los
        # tenants.
        if clone_id:
            prompts = ps.list_prompts(clone_id=clone_id)
        else:
            tenant_clone_ids = {
                row[0] for row in db.session.execute(
                    select(CloneConfig.id).where(CloneConfig.tenant_id == tenant_id)
                ).all()
            }
            prompts = ps.list_prompts(clone_ids=tenant_clone_ids)
        return {"prompts": prompts, "total": len(prompts)}, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.core.prompts import PromptService
        _account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400
        ps = PromptService()
        payload = PromptCreatePayload.model_validate(request.get_json(silent=True) or {})
        # P0.4 (H-04): el clone_id (si viene) debe pertenecer al tenant.
        if not _clone_owned_by_tenant(payload.clone_id, tenant_id):
            return {"error": "clone not found"}, 404
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
        _account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400

        ps = PromptService()
        prompt = db.session.get(Prompt, prompt_id)
        if not prompt:
            return {"error": "prompt not found"}, 404

        # P0.4 (H-04): verificar tenency via clone_id del prompt.
        if not prompt.clone_id or not _clone_owned_by_tenant(prompt.clone_id, tenant_id):
            # No revelar existencia a quien no es dueno (404, no 403).
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
        from api.models.prompt import Prompt
        _account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400

        # P0.4 (H-04): verificar tenency del prompt antes de versionar.
        prompt = db.session.get(Prompt, prompt_id)
        if not prompt:
            return {"error": "prompt not found"}, 404
        if not prompt.clone_id or not _clone_owned_by_tenant(prompt.clone_id, tenant_id):
            return {"error": "prompt not found"}, 404

        ps = PromptService()
        payload = PromptVersionPayload.model_validate(request.get_json(silent=True) or {})

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
        _account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400
        ps = PromptService()
        clone_id = request.args.get("clone_id")
        task = request.args.get("task", "chat")

        if not clone_id:
            return {"error": "clone_id is required"}, 400

        # P0.4 (H-04): verificar tenency del clone.
        if not _clone_owned_by_tenant(clone_id, tenant_id):
            return {"error": "clone not found"}, 404

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
