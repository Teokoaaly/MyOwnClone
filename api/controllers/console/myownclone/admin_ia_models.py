"""AI Model catalog and assignment admin API.

Requires platform_admin role. Used by the platform admin panel to manage
AI models and their tenant-level assignments.
"""

import logging
from flask import g, request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import login_required
from api.models.ai_models import AIModel, AIModelAssignment, AIModelType, AssignmentTask

logger = logging.getLogger(__name__)


# ─── Payload Schemas ──────────────────────────────────────────────────────────


class CreateModelPayload(BaseModel):
    provider: str = Field(..., min_length=1, description="Provider e.g. openai, anthropic")
    name: str = Field(..., min_length=1, description="Model name e.g. gpt-4o")
    model_type: str = Field(default="chat", description="Type: chat, embedding, rerank, tts, stt")
    capabilities: dict | None = Field(default=None, description="JSON object with capability flags")
    config: dict | None = Field(default=None, description="JSON object with model config")
    input_cost_per_1k: int = Field(default=0, ge=0, description="Cost in cents per 1K input tokens")
    output_cost_per_1k: int = Field(default=0, ge=0, description="Cost in cents per 1K output tokens")
    max_tokens: int | None = Field(default=None, ge=1, description="Maximum tokens per request")
    is_active: bool = Field(default=True, description="Whether model is available")


class UpdateModelPayload(BaseModel):
    provider: str | None = Field(default=None, min_length=1)
    name: str | None = Field(default=None, min_length=1)
    model_type: str | None = Field(default=None)
    capabilities: dict | None = Field(default=None)
    config: dict | None = Field(default=None)
    input_cost_per_1k: int | None = Field(default=None, ge=0)
    output_cost_per_1k: int | None = Field(default=None, ge=0)
    max_tokens: int | None = Field(default=None, ge=1)
    is_active: bool | None = Field(default=None)


class CreateAssignmentPayload(BaseModel):
    tenant_id: str | None = Field(default=None, description="NULL for global assignment")
    model_id: str = Field(..., min_length=1, description="FK to ai_models.id")
    label: str | None = Field(default=None, max_length=100)
    task: str = Field(..., min_length=1, description="Task: chat_primary, embedding, rerank, etc.")
    priority: int = Field(default=0, ge=0, description="Higher priority wins")
    is_active: bool = Field(default=True)


# ─── Helpers ──────────────────────────────────────────────────────────────────


def _pagination_args(default_limit: int = 20, max_limit: int = 50) -> tuple[int, int]:
    page = max(int(request.args.get("page", 1)), 1)
    limit = min(max(int(request.args.get("limit", default_limit)), 1), max_limit)
    return page, limit


def _pagination_payload(page: int, limit: int, total: int) -> dict:
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "pages": (total + limit - 1) // limit if total else 0,
    }


def _iso(value) -> str | None:
    return value.isoformat() if value else None


def _is_platform_admin() -> bool:
    """Check if current user is a platform admin."""
    if getattr(g, "account_role", None) == "platform_admin":
        return True
    from api.models.account import Account
    account_id = str(getattr(g, "account_id", "") or "").strip()
    if not account_id:
        return False
    try:
        account = db.session.execute(
            select(Account).where(Account.id == account_id)
        ).scalar_one_or_none()
    except Exception:
        logger.exception("Failed to fetch account for platform admin check")
        return False
    if account and hasattr(account, "is_platform_admin") and account.is_platform_admin:
        return True
    return False


def _require_platform_admin():
    if not _is_platform_admin():
        return {"error": "platform admin only"}, 403
    return None


# ─── Models CRUD ──────────────────────────────────────────────────────────────


@console_ns.route("/myownclone/admin/ia-modelos/models")
class AdminIAModelsListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if err := _require_platform_admin():
            return err

        page, limit = _pagination_args()
        search = request.args.get("search", "").strip()
        provider = request.args.get("provider", "").strip()
        model_type = request.args.get("type", "").strip()
        is_active = request.args.get("is_active", "").strip()

        filters = []
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            filters.append(
                or_(
                    AIModel.name.ilike(f"%{escaped}%", escape="\\"),
                    AIModel.provider.ilike(f"%{escaped}%", escape="\\"),
                )
            )
        if provider:
            filters.append(AIModel.provider == provider)
        if model_type:
            filters.append(AIModel.model_type == model_type)
        if is_active in ("true", "false"):
            filters.append(AIModel.is_active == (is_active == "true"))

        total = db.session.execute(select(func.count(AIModel.id)).where(*filters)).scalar() or 0

        stmt = (
            select(AIModel)
            .where(*filters)
            .order_by(AIModel.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        models = db.session.execute(stmt).scalars().all()

        return {
            "items": [_model_to_dict(m) for m in models],
            "pagination": _pagination_payload(page, limit, total),
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if err := _require_platform_admin():
            return err

        data = CreateModelPayload.model_validate(request.json)

        # Check for duplicate provider+name
        existing = db.session.execute(
            select(AIModel).where(
                AIModel.provider == data.provider,
                AIModel.name == data.name,
            )
        ).scalar_one_or_none()
        if existing:
            return {"error": f"Model {data.provider}/{data.name} already exists"}, 409

        model = AIModel(
            provider=data.provider,
            name=data.name,
            model_type=data.model_type,
            capabilities=data.capabilities,
            config=data.config,
            input_cost_per_1k=data.input_cost_per_1k,
            output_cost_per_1k=data.output_cost_per_1k,
            max_tokens=data.max_tokens,
            is_active=data.is_active,
            created_by=g.account_id,
        )
        db.session.add(model)
        db.session.commit()

        logger.info("Admin created AIModel: provider=%s name=%s by=%s",
                     data.provider, data.name, g.account_id)

        return {"model": _model_to_dict(model)}, 201


@console_ns.route("/myownclone/admin/ia-modelos/models/<model_id>")
class AdminIAModelApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, model_id):
        if err := _require_platform_admin():
            return err

        model = db.session.execute(
            select(AIModel).where(AIModel.id == model_id)
        ).scalar_one_or_none()
        if not model:
            return {"error": "Model not found"}, 404

        return {"model": _model_to_dict(model)}, 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, model_id):
        if err := _require_platform_admin():
            return err

        model = db.session.execute(
            select(AIModel).where(AIModel.id == model_id)
        ).scalar_one_or_none()
        if not model:
            return {"error": "Model not found"}, 404

        data = UpdateModelPayload.model_validate(request.json)

        if data.provider is not None:
            model.provider = data.provider
        if data.name is not None:
            model.name = data.name
        if data.model_type is not None:
            model.model_type = data.model_type
        if data.capabilities is not None:
            model.capabilities = data.capabilities
        if data.config is not None:
            model.config = data.config
        if data.input_cost_per_1k is not None:
            model.input_cost_per_1k = data.input_cost_per_1k
        if data.output_cost_per_1k is not None:
            model.output_cost_per_1k = data.output_cost_per_1k
        if data.max_tokens is not None:
            model.max_tokens = data.max_tokens
        if data.is_active is not None:
            model.is_active = data.is_active

        db.session.commit()
        logger.info("Admin updated AIModel: id=%s by=%s", model_id, g.account_id)

        return {"model": _model_to_dict(model)}, 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, model_id):
        if err := _require_platform_admin():
            return err

        model = db.session.execute(
            select(AIModel).where(AIModel.id == model_id)
        ).scalar_one_or_none()
        if not model:
            return {"error": "Model not found"}, 404

        db.session.delete(model)
        db.session.commit()
        logger.info("Admin deleted AIModel: id=%s by=%s", model_id, g.account_id)

        return {"message": "Model deleted"}, 200


# ─── Assignments CRUD ──────────────────────────────────────────────────────────


@console_ns.route("/myownclone/admin/ia-modelos/assignments")
class AdminIAModelsAssignmentsListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if err := _require_platform_admin():
            return err

        page, limit = _pagination_args()
        tenant_id = request.args.get("tenant_id", "").strip()
        task = request.args.get("task", "").strip()
        is_active = request.args.get("is_active", "").strip()

        filters = []
        if tenant_id:
            filters.append(AIModelAssignment.tenant_id == tenant_id)
        if task:
            filters.append(AIModelAssignment.task == task)
        if is_active in ("true", "false"):
            filters.append(AIModelAssignment.is_active == (is_active == "true"))

        total = db.session.execute(
            select(func.count(AIModelAssignment.id)).where(*filters)
        ).scalar() or 0

        stmt = (
            select(AIModelAssignment, AIModel)
            .outerjoin(AIModel, AIModel.id == AIModelAssignment.model_id)
            .where(*filters)
            .order_by(AIModelAssignment.priority.desc(), AIModelAssignment.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = db.session.execute(stmt).all()

        return {
            "items": [
                {
                    "assignment": _assignment_to_dict(a),
                    "model": _model_to_dict(m) if m else None,
                }
                for a, m in rows
            ],
            "pagination": _pagination_payload(page, limit, total),
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if err := _require_platform_admin():
            return err

        data = CreateAssignmentPayload.model_validate(request.json)

        # Verify model exists
        model = db.session.execute(
            select(AIModel).where(AIModel.id == data.model_id)
        ).scalar_one_or_none()
        if not model:
            return {"error": "Model not found"}, 400

        assignment = AIModelAssignment(
            tenant_id=data.tenant_id,
            model_id=data.model_id,
            label=data.label,
            task=data.task,
            priority=data.priority,
            is_active=data.is_active,
            created_by=g.account_id,
        )
        db.session.add(assignment)
        db.session.commit()

        logger.info("Admin created AIModelAssignment: model_id=%s task=%s tenant_id=%s by=%s",
                    data.model_id, data.task, data.tenant_id, g.account_id)

        return {"assignment": _assignment_to_dict(assignment)}, 201


@console_ns.route("/myownclone/admin/ia-modelos/assignments/<assignment_id>")
class AdminIAModelsAssignmentApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, assignment_id):
        if err := _require_platform_admin():
            return err

        assignment = db.session.execute(
            select(AIModelAssignment).where(AIModelAssignment.id == assignment_id)
        ).scalar_one_or_none()
        if not assignment:
            return {"error": "Assignment not found"}, 404

        db.session.delete(assignment)
        db.session.commit()
        logger.info("Admin deleted AIModelAssignment: id=%s by=%s", assignment_id, g.account_id)

        return {"message": "Assignment deleted"}, 200


# ─── Circuit Breaker States ───────────────────────────────────────────────────


@console_ns.route("/myownclone/admin/ia-modelos/breaker-states")
class AdminIABreakerStatesApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if err := _require_platform_admin():
            return err

        from api.core.retry_client import get_retry_client

        client = get_retry_client()
        # Get all known breaker keys from the registry
        from api.core.model_registry import get_registry
        registry = get_registry()
        known_keys = set()
        for model in registry._models.values():
            known_keys.add(f"{model.provider}/{model.name}")

        # Include any breakers that have been instantiated even if not in registry
        all_breaker_keys = set(client._breakers.keys()) | known_keys

        states = []
        for key in sorted(all_breaker_keys):
            state = client.get_breaker_state(key)
            states.append(state)

        return {"breakers": states}, 200


# ─── Serialization Helpers ─────────────────────────────────────────────────────


def _model_to_dict(m: AIModel) -> dict:
    return {
        "id": str(m.id),
        "provider": m.provider,
        "name": m.name,
        "model_type": m.model_type,
        "capabilities": m.capabilities,
        "config": m.config,
        "input_cost_per_1k": m.input_cost_per_1k,
        "output_cost_per_1k": m.output_cost_per_1k,
        "max_tokens": m.max_tokens,
        "is_active": m.is_active,
        "created_by": m.created_by,
        "created_at": _iso(m.created_at),
        "updated_at": _iso(m.updated_at),
    }


def _assignment_to_dict(a: AIModelAssignment) -> dict:
    return {
        "id": str(a.id),
        "tenant_id": a.tenant_id,
        "model_id": str(a.model_id),
        "label": a.label,
        "task": a.task,
        "priority": a.priority,
        "is_active": a.is_active,
        "created_by": a.created_by,
        "created_at": _iso(a.created_at),
        "updated_at": _iso(a.updated_at),
    }


# Import these at module level for or_ to work
from sqlalchemy import or_
