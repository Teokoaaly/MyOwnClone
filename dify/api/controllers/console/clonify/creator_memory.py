"""Clonify creator memory API — CRUD for memories, signatures, and templates."""

import logging

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select

from controllers.common.schema import register_response_schema_models, register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from fields.base import ResponseModel
from libs.login import current_account_with_tenant, login_required
from models.clonify import CloneConfig, CreatorMemory, CreatorMemoryType

logger = logging.getLogger(__name__)


class MemoryPayload(BaseModel):
    clone_id: str
    type: str = Field(..., pattern="^(memory|signature|template)$")
    content: str = Field(..., min_length=1)
    trigger_condition: str | None = None
    priority: int = Field(default=0)


class MemoryResponse(ResponseModel):
    id: str
    clone_id: str
    type: str
    content: str
    trigger_condition: str | None = None
    priority: int
    created_at: int
    updated_at: int | None = None


register_schema_models(console_ns, MemoryPayload)
register_response_schema_models(console_ns, MemoryResponse)


@console_ns.route("/clonify/clones/<string:clone_id>/memories")
class CreatorMemoryListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        memory_type = request.args.get("type")

        stmt = select(CreatorMemory).where(CreatorMemory.clone_id == clone_id)
        if memory_type:
            stmt = stmt.where(CreatorMemory.type == memory_type)
        stmt = stmt.order_by(CreatorMemory.priority.desc(), CreatorMemory.created_at.desc())

        memories = db.session.execute(stmt).scalars().all()
        return [_serialize_memory(m) for m in memories], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        data = MemoryPayload.model_validate({**request.json, "clone_id": clone_id})

        memory = CreatorMemory(
            clone_id=clone_id,
            type=data.type,
            content=data.content,
            trigger_condition=data.trigger_condition,
            priority=data.priority,
        )
        db.session.add(memory)
        db.session.commit()
        return _serialize_memory(memory), 201


@console_ns.route("/clonify/memories/<string:memory_id>")
class CreatorMemoryApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def put(self, memory_id: str):
        account, tenant_id = current_account_with_tenant()
        memory = db.session.execute(
            select(CreatorMemory).where(CreatorMemory.id == memory_id)
        ).scalar_one_or_none()
        if not memory:
            return {"error": "memory not found"}, 404
        _verify_clone_access(memory.clone_id, tenant_id)

        data = MemoryPayload.model_validate({**request.json, "clone_id": memory.clone_id})
        memory.type = data.type
        memory.content = data.content
        memory.trigger_condition = data.trigger_condition
        memory.priority = data.priority
        db.session.commit()
        return _serialize_memory(memory), 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, memory_id: str):
        account, tenant_id = current_account_with_tenant()
        memory = db.session.execute(
            select(CreatorMemory).where(CreatorMemory.id == memory_id)
        ).scalar_one_or_none()
        if not memory:
            return {"error": "memory not found"}, 404
        _verify_clone_access(memory.clone_id, tenant_id)
        db.session.delete(memory)
        db.session.commit()
        return "", 204


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    if not clone:
        from werkzeug.exceptions import NotFound
        raise NotFound("clone not found")


def _serialize_memory(memory: CreatorMemory) -> dict:
    return {
        "id": memory.id,
        "clone_id": memory.clone_id,
        "type": memory.type,
        "content": memory.content,
        "trigger_condition": memory.trigger_condition,
        "priority": memory.priority,
        "created_at": int(memory.created_at.timestamp()) if memory.created_at else 0,
        "updated_at": int(memory.updated_at.timestamp()) if memory.updated_at else None,
    }
