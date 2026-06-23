"""Console API for configurable AI models and task assignments."""

from __future__ import annotations

import logging

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import or_, select

from api.controllers.common.schema import register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.model_manager import ModelManager
from api.core.model_registry import ModelRegistry
from api.extensions.ext_database import db
from api.libs.crypto import SecretCipher
from api.libs.login import current_account_with_tenant, login_required
from api.models.ai_models import AIModel, AIModelAssignment, AITask, TASK_CAPABILITY

logger = logging.getLogger(__name__)
ai_models_ns = console_ns


class AIModelPayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    provider: str = Field(..., min_length=1, max_length=20)
    model_id: str = Field(..., min_length=1, max_length=120)
    api_key: str = Field(..., min_length=1)
    base_url: str | None = None
    capabilities: list[str] = Field(default_factory=list)
    input_price_cents_per_mtok: int = 0
    output_price_cents_per_mtok: int = 0
    priority: int = 100
    temperature_default: float | None = None
    max_tokens_default: int | None = None
    max_input_tokens: int | None = None
    embedding_dimensions: int | None = None
    is_active: bool = True


class AIModelAssignmentPayload(BaseModel):
    task: str
    model_id: str
    override_params: dict | None = None
    is_active: bool = True


class AIModelConnectionPayload(BaseModel):
    model_id: str


register_schema_models(
    console_ns,
    AIModelPayload,
    AIModelAssignmentPayload,
    AIModelConnectionPayload,
)


def _tenant_id() -> str | None:
    _, tenant_id = current_account_with_tenant()
    return tenant_id


def _serialize_model(model: AIModel) -> dict:
    return {
        "id": str(model.id),
        "tenant_id": str(model.tenant_id) if model.tenant_id else None,
        "name": model.name,
        "provider": model.provider,
        "model_id": model.model_id,
        "base_url": model.base_url,
        "capabilities": list(model.capabilities or []),
        "input_price_cents_per_mtok": model.input_price_cents_per_mtok,
        "output_price_cents_per_mtok": model.output_price_cents_per_mtok,
        "priority": model.priority,
        "temperature_default": model.temperature_default,
        "max_tokens_default": model.max_tokens_default,
        "max_input_tokens": model.max_input_tokens,
        "embedding_dimensions": model.embedding_dimensions,
        "is_active": model.is_active,
        "has_api_key": bool(model.api_key_encrypted),
    }


def _serialize_assignment(assignment: AIModelAssignment) -> dict:
    return {
        "id": str(assignment.id),
        "tenant_id": str(assignment.tenant_id) if assignment.tenant_id else None,
        "task": assignment.task,
        "model_id": assignment.model_id,
        "override_params": assignment.override_params or {},
        "is_active": assignment.is_active,
    }


@console_ns.route("/myownclone/ai-models")
class AIModelListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        tenant_id = _tenant_id()
        stmt = (
            select(AIModel)
            .where(or_(AIModel.tenant_id == tenant_id, AIModel.tenant_id.is_(None)))
            .order_by(AIModel.priority.asc(), AIModel.created_at.desc())
        )
        items = db.session.execute(stmt).scalars().all()
        return [_serialize_model(item) for item in items], 200

    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.expect(AIModelPayload, location="json", validate=True)
    def post(self):
        tenant_id = _tenant_id()
        if not tenant_id:
            return {"error": "tenant not configured"}, 400

        payload = AIModelPayload.model_validate(request.json)
        model = AIModel(
            tenant_id=tenant_id,
            name=payload.name,
            provider=payload.provider,
            model_id=payload.model_id,
            api_key_encrypted=SecretCipher.encrypt(payload.api_key),
            base_url=payload.base_url,
            capabilities=payload.capabilities,
            input_price_cents_per_mtok=payload.input_price_cents_per_mtok,
            output_price_cents_per_mtok=payload.output_price_cents_per_mtok,
            priority=payload.priority,
            temperature_default=payload.temperature_default,
            max_tokens_default=payload.max_tokens_default,
            max_input_tokens=payload.max_input_tokens,
            embedding_dimensions=payload.embedding_dimensions,
            is_active=payload.is_active,
        )
        db.session.add(model)
        db.session.commit()
        ModelRegistry().invalidate(tenant_id=tenant_id)
        return _serialize_model(model), 201


@console_ns.route("/myownclone/ai-models/assignments")
class AIModelAssignmentsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        tenant_id = _tenant_id()
        stmt = (
            select(AIModelAssignment)
            .where(or_(AIModelAssignment.tenant_id == tenant_id, AIModelAssignment.tenant_id.is_(None)))
            .order_by(AIModelAssignment.task.asc(), AIModelAssignment.created_at.desc())
        )
        items = db.session.execute(stmt).scalars().all()
        return [_serialize_assignment(item) for item in items], 200

    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.expect(AIModelAssignmentPayload, location="json", validate=True)
    def put(self):
        tenant_id = _tenant_id()
        if not tenant_id:
            return {"error": "tenant not configured"}, 400

        payload = AIModelAssignmentPayload.model_validate(request.json)
        if payload.task not in {task.value for task in AITask}:
            return {"error": "invalid task"}, 400

        model = db.session.execute(
            select(AIModel).where(
                AIModel.id == payload.model_id,
                or_(AIModel.tenant_id == tenant_id, AIModel.tenant_id.is_(None)),
            )
        ).scalar_one_or_none()
        if not model:
            return {"error": "model not found"}, 404

        required_capability = TASK_CAPABILITY[AITask(payload.task)].value
        if required_capability not in (model.capabilities or []):
            return {"error": "model capability mismatch"}, 400

        existing = db.session.execute(
            select(AIModelAssignment).where(
                AIModelAssignment.tenant_id == tenant_id,
                AIModelAssignment.task == payload.task,
                AIModelAssignment.is_active.is_(True),
            )
        ).scalar_one_or_none()
        if existing:
            existing.is_active = False

        assignment = AIModelAssignment(
            tenant_id=tenant_id,
            task=payload.task,
            model_id=payload.model_id,
            override_params=payload.override_params,
            is_active=payload.is_active,
        )
        db.session.add(assignment)
        db.session.commit()
        ModelRegistry().invalidate(tenant_id=tenant_id, task=AITask(payload.task))
        return _serialize_assignment(assignment), 200


@console_ns.route("/myownclone/ai-models/test-connection")
class AIModelTestConnectionApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.expect(AIModelConnectionPayload, location="json", validate=True)
    def post(self):
        tenant_id = _tenant_id()
        payload = AIModelConnectionPayload.model_validate(request.json)
        model = db.session.execute(
            select(AIModel).where(
                AIModel.id == payload.model_id,
                or_(AIModel.tenant_id == tenant_id, AIModel.tenant_id.is_(None)),
            )
        ).scalar_one_or_none()
        if not model:
            return {"error": "model not found"}, 404

        resolved = ModelRegistry()._build_resolved_from_db(  # scoped helper reuse
            tenant_id=tenant_id,
            task=AITask.CHAT,
            assignment=AIModelAssignment(
                id="preview",
                tenant_id=tenant_id,
                task=AITask.CHAT.value,
                model_id=model.id,
                override_params={},
                is_active=True,
            ),
            model=model,
        )
        adapter = ModelManager()._provider_adapter_for(resolved)
        result = adapter.test_connection()
        return {"ok": result.ok, "message": result.message, "details": result.details}, 200


ns = ai_models_ns
