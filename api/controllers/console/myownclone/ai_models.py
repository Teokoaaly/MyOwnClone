"""Console API for configurable AI models and task assignments."""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import or_, select

from api.controllers.common.schema import register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.model_manager import ModelManager
from api.core.model_registry import ModelRegistry
from api.core.providers.base import GenerationParams
from api.extensions.ext_database import db
from api.libs.crypto import SecretCipher
from api.libs.login import current_account_with_tenant, login_required
from api.models.ai_models import (
    AIInvocation,
    AIModel,
    AIModelAssignment,
    AITask,
    CostDailyRollup,
    TASK_CAPABILITY,
)

logger = logging.getLogger(__name__)
ai_models_ns = console_ns


class AIModelPayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    provider: str = Field(..., min_length=1, max_length=20)
    model_id: str = Field(..., min_length=1, max_length=120)
    api_key: str | None = Field(default=None, min_length=1)
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


class AIModelPlaygroundPayload(BaseModel):
    model_id: str
    prompt: str = Field(..., min_length=1, max_length=12000)
    task: str = Field(default=AITask.CHAT.value)


register_schema_models(
    console_ns,
    AIModelPayload,
    AIModelAssignmentPayload,
    AIModelConnectionPayload,
    AIModelPlaygroundPayload,
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


def _resolve_model_for_preview(*, tenant_id: str | None, model: AIModel, task: AITask):
    return ModelRegistry()._build_resolved_from_db(
        tenant_id=tenant_id,
        task=task,
        assignment=AIModelAssignment(
            id="preview",
            tenant_id=tenant_id,
            task=task.value,
            model_id=model.id,
            override_params={},
            is_active=True,
        ),
        model=model,
    )


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

        payload = AIModelPayload.model_validate(request.json)
        if not payload.api_key:
            return {"error": "api_key is required"}, 400
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


@console_ns.route("/myownclone/ai-models/<string:model_id>")
class AIModelDetailApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.expect(AIModelPayload, location="json", validate=True)
    def put(self, model_id: str):
        tenant_id = _tenant_id()
        payload = AIModelPayload.model_validate(request.json)

        model = db.session.execute(
            select(AIModel).where(
                AIModel.id == model_id,
                or_(AIModel.tenant_id == tenant_id, AIModel.tenant_id.is_(None)),
            )
        ).scalar_one_or_none()
        if not model:
            return {"error": "model not found"}, 404

        model.name = payload.name
        model.provider = payload.provider
        model.model_id = payload.model_id
        model.base_url = payload.base_url
        model.capabilities = payload.capabilities
        model.input_price_cents_per_mtok = payload.input_price_cents_per_mtok
        model.output_price_cents_per_mtok = payload.output_price_cents_per_mtok
        model.priority = payload.priority
        model.temperature_default = payload.temperature_default
        model.max_tokens_default = payload.max_tokens_default
        model.max_input_tokens = payload.max_input_tokens
        model.embedding_dimensions = payload.embedding_dimensions
        model.is_active = payload.is_active
        if payload.api_key:
            model.api_key_encrypted = SecretCipher.encrypt(payload.api_key)
        db.session.commit()
        ModelRegistry().invalidate(tenant_id=tenant_id)
        return _serialize_model(model), 200


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

        resolved = _resolve_model_for_preview(tenant_id=tenant_id, model=model, task=AITask.CHAT)
        adapter = ModelManager()._provider_adapter_for(resolved)
        result = adapter.test_connection()
        return {"ok": result.ok, "message": result.message, "details": result.details}, 200


@console_ns.route("/myownclone/ai-models/playground")
class AIModelPlaygroundApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.expect(AIModelPlaygroundPayload, location="json", validate=True)
    def post(self):
        tenant_id = _tenant_id()
        payload = AIModelPlaygroundPayload.model_validate(request.json)
        if payload.task not in {task.value for task in AITask}:
            return {"error": "invalid task"}, 400

        task = AITask(payload.task)
        model = db.session.execute(
            select(AIModel).where(
                AIModel.id == payload.model_id,
                or_(AIModel.tenant_id == tenant_id, AIModel.tenant_id.is_(None)),
            )
        ).scalar_one_or_none()
        if not model:
            return {"error": "model not found"}, 404

        required_capability = TASK_CAPABILITY[task].value
        if required_capability not in (model.capabilities or []):
            return {"error": "model capability mismatch"}, 400

        resolved = _resolve_model_for_preview(tenant_id=tenant_id, model=model, task=task)
        adapter = ModelManager()._provider_adapter_for(resolved)
        params = ModelManager()._build_generation_params(resolved)
        reply = adapter.generate(prompt=payload.prompt, params=params)
        return {
            "text": reply.text,
            "usage": reply.usage.as_dict() if reply.usage else None,
            "latency_ms": reply.latency_ms,
        }, 200


@console_ns.route("/myownclone/ai-models/costs")
class AIModelCostsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        tenant_id = _tenant_id()
        since = datetime.now(timezone.utc) - timedelta(days=7)
        daily: dict[str, dict[str, int]] = {}
        totals = {"invocations": 0, "prompt_tokens": 0, "completion_tokens": 0}
        by_model: dict[str, dict[str, int]] = {}

        rollup_stmt = select(CostDailyRollup).where(CostDailyRollup.day >= since.date())
        if tenant_id:
            rollup_stmt = rollup_stmt.where(CostDailyRollup.tenant_id == tenant_id)
        rollups = db.session.execute(
            rollup_stmt.order_by(CostDailyRollup.day.asc())
        ).scalars().all()

        if rollups:
            for row in rollups:
                day = row.day.isoformat()
                bucket = daily.setdefault(day, {
                    "day": day,
                    "invocations": 0,
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                })
                bucket["invocations"] += row.invocations or 0
                bucket["prompt_tokens"] += row.prompt_tokens or 0
                bucket["completion_tokens"] += row.completion_tokens or 0
                totals["invocations"] += row.invocations or 0
                totals["prompt_tokens"] += row.prompt_tokens or 0
                totals["completion_tokens"] += row.completion_tokens or 0

            # Per-model breakdown from invocations table (rollup is daily aggregates)
            inv_stmt = select(AIInvocation).where(AIInvocation.created_at >= since.replace(tzinfo=None))
            if tenant_id:
                inv_stmt = inv_stmt.where(AIInvocation.tenant_id == tenant_id)
            inv_rows = db.session.execute(inv_stmt).scalars().all()
            for row in inv_rows:
                key = row.model_id or "unknown"
                entry = by_model.setdefault(key, {"model_id": key, "invocations": 0, "prompt_tokens": 0, "completion_tokens": 0})
                entry["invocations"] += 1
                entry["prompt_tokens"] += row.prompt_tokens or 0
                entry["completion_tokens"] += row.completion_tokens or 0
      ***REMOVED***:
            stmt = select(AIInvocation).where(AIInvocation.created_at >= since.replace(tzinfo=None))
            if tenant_id:
                stmt = stmt.where(AIInvocation.tenant_id == tenant_id)
            rows = db.session.execute(stmt.order_by(AIInvocation.created_at.asc())).scalars().all()
            for row in rows:
                day = row.created_at.date().isoformat() if row.created_at else "unknown"
                bucket = daily.setdefault(day, {
                    "day": day,
                    "invocations": 0,
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                })
                bucket["invocations"] += 1
                bucket["prompt_tokens"] += row.prompt_tokens or 0
                bucket["completion_tokens"] += row.completion_tokens or 0
                totals["invocations"] += 1
                totals["prompt_tokens"] += row.prompt_tokens or 0
                totals["completion_tokens"] += row.completion_tokens or 0
                key = row.model_id or "unknown"
                entry = by_model.setdefault(key, {"model_id": key, "invocations": 0, "prompt_tokens": 0, "completion_tokens": 0})
                entry["invocations"] += 1
                entry["prompt_tokens"] += row.prompt_tokens or 0
                entry["completion_tokens"] += row.completion_tokens or 0

        return {
            "series": list(daily.values()),
            "totals": totals,
            "by_model": list(by_model.values()),
        }, 200


# ── M14: Admin monitoring & control panels ──────────────────────────

@console_ns.route("/myownclone/ai-models/registry-status")
class RegistryStatusApi(Resource):
    """Return the ModelRegistry balancer state (cache + per-task resolution)."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        tenant_id = _tenant_id()
        reg = ModelRegistry()
        return reg.dump_status(tenant_id=tenant_id), 200


@console_ns.route("/myownclone/ai-models/embedding-status")
class EmbeddingStatusApi(Resource):
    """Return embedding runtime constants for the admin panel."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.controllers.console.myownclone.runtime import _MAX_EMBED_TEXTS

        return {
            "max_embed_texts": _MAX_EMBED_TEXTS,
            "client_batch_size": 64,
            "embedding_dimensions": 1536,
        }, 200


@console_ns.route("/myownclone/ai-models/backfill")
class AIModelBackfillApi(Resource):
    """Trigger ai-backfill-from-env from the admin UI (M14)."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from dataclasses import asdict

        from api.commands.ai_backfill import backfill_from_env

        report = backfill_from_env(dry_run=False)
        ModelRegistry().invalidate()
        return asdict(report), 200


ns = ai_models_ns
