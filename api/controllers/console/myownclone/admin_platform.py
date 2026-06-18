"""MyOwnClone admin platform API — multi-tenant management, impersonation, MRR dashboard.

Requires platform_admin role. Used by the platform admin panel.
"""

import hashlib
import logging
import os
import re
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from flask import g, request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import false, func, or_, select

from api.controllers.common.schema import register_response_schema_models, register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.contracts import (
    PLAN_KEYS,
    PLAN_PRICES_CENTS,
    TENANT_STATUS_KEYS,
    normalize_plan,
    normalize_tenant_status,
)
from api.extensions.ext_database import db
from api.libs.login import login_required
from api.models.account import Account, Tenant
from api.models.myownclone import CloneConfig, CostTracking, Feedback, ImpersonationLog, ImpersonationToken

logger = logging.getLogger(__name__)


class ImpersonatePayload(BaseModel):
    tenant_id: str
    reason: str


class CourtesyPayload(BaseModel):
    email: str
    name: str
    plan: str = "pro"
    duration_days: int = 30


class CreateTenantPayload(BaseModel):
    name: str = Field(..., min_length=1, description="Tenant name")
    slug: str = Field(..., min_length=1, description="Unique slug for the tenant")
    plan: str = Field(default="trial", description="Plan: trial, basic, pro, scale, enterprise")
    status: str = Field(default="trial", description="Status: active, trial, suspended, cancelled")


register_schema_models(console_ns, ImpersonatePayload, CourtesyPayload, CreateTenantPayload)


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


def _clone_counts_by_tenant(tenant_ids: list[str]) -> dict[str, int]:
    if not tenant_ids:
        return {}
    rows = db.session.execute(
        select(CloneConfig.tenant_id, func.count(CloneConfig.id))
        .where(CloneConfig.tenant_id.in_(tenant_ids))
        .group_by(CloneConfig.tenant_id)
    ).all()
    return {str(tenant_id): int(count or 0) for tenant_id, count in rows}


def _monthly_costs_by_tenant(tenant_ids: list[str]) -> dict[str, int]:
    if not tenant_ids:
        return {}
    since = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=30)
    rows = db.session.execute(
        select(CostTracking.tenant_id, func.sum(CostTracking.cost_cents))
        .where(CostTracking.tenant_id.in_(tenant_ids), CostTracking.created_at >= since)
        .group_by(CostTracking.tenant_id)
    ).all()
    return {str(tenant_id): int(total or 0) for tenant_id, total in rows}


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or f"tenant-{secrets.token_hex(3)}"


def _unique_tenant_slug(seed: str) -> str:
    base = _slugify(seed)[:80]
    slug = base
    index = 2
    while db.session.execute(select(Tenant.id).where(Tenant.slug == slug)).scalar_one_or_none():
        suffix = f"-{index}"
        slug = f"{base[:100 - len(suffix)]}{suffix}"
        index += 1
    return slug


def _ensure_admin_account(tenant_id_hint: str | None = None) -> str:
    account_id = str(getattr(g, "account_id", "") or "").strip()
    email = str(getattr(g, "account_email", "") or "").strip() or "admin@myownclone.local"

    if account_id:
        account = db.session.execute(select(Account).where(Account.id == account_id)).scalar_one_or_none()
        if account:
            return str(account.id)

    account = db.session.execute(select(Account).where(Account.email == email)).scalar_one_or_none()
    if account:
        return str(account.id)

    tenant_id = tenant_id_hint or getattr(g, "tenant_id", None)
    if not tenant_id:
        tenant_id = db.session.execute(select(Tenant.id).order_by(Tenant.created_at.asc())).scalar()
    if not tenant_id:
        tenant = Tenant(name="Platform", slug=_unique_tenant_slug("platform"), plan="trial", status="active")
        db.session.add(tenant)
        db.session.flush()
        tenant_id = str(tenant.id)

    account_kwargs = {
        "tenant_id": str(tenant_id),
        "email": email,
        "role": "platform_admin",
        "is_platform_admin": True,
    }
    if account_id:
        account_kwargs["id"] = account_id
    account = Account(**account_kwargs)
    db.session.add(account)
    db.session.flush()
    return str(account.id)


@console_ns.route("/myownclone/admin/overview")
class AdminOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        total_tenants = db.session.execute(select(func.count(Tenant.id))).scalar() or 0
        active_tenants = 0

        total_clones = db.session.execute(
            select(func.count(CloneConfig.id)).where(CloneConfig.is_active.is_(True))
        ).scalar() or 0

        mrr_cents = 0
        plan_counts = {plan: 0 for plan in PLAN_KEYS}

        tenants = db.session.execute(select(Tenant)).scalars().all()
        for t in tenants:
            plan_name = normalize_plan(t.plan)
            if plan_name in plan_counts:
                plan_counts[plan_name] += 1
                if t.subscription_status == "active":
                    mrr_cents += PLAN_PRICES_CENTS.get(plan_name, 0)
            if normalize_tenant_status(t.status) == "active":
                active_tenants += 1

        cost_data = db.session.execute(
            select(func.sum(CostTracking.cost_cents))
        ).scalar() or 0

        return {
            "total_tenants": total_tenants,
            "active_tenants": active_tenants,
            "total_clones": total_clones,
            "mrr_cents": mrr_cents,
            "mrr_display": f"{(mrr_cents / 100):.2f}€",
            "total_costs_cents": cost_data,
            "total_costs_display": f"{(cost_data / 100):.2f}€",
            "margin_cents": mrr_cents - cost_data,
            "margin_display": f"{((mrr_cents - cost_data) / 100):.2f}€",
            "plan_breakdown": plan_counts,
        }, 200


@console_ns.route("/myownclone/admin/tenants")
class AdminTenantsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        page, limit = _pagination_args()
        search = request.args.get("search", "").strip()
        plan = request.args.get("plan", "").strip()
        status = request.args.get("status", "").strip()

        filters = []
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            filters.append(
                or_(
                    Tenant.name.ilike(f"%{escaped}%", escape="\\"),
                    Tenant.slug.ilike(f"%{escaped}%", escape="\\"),
                )
            )
        if plan:
            filters.append(Tenant.plan == normalize_plan(plan))
        if status:
            filters.append(Tenant.status == normalize_tenant_status(status))

        total = db.session.execute(select(func.count(Tenant.id)).where(*filters)).scalar() or 0

        stmt = (
            select(Tenant)
            .where(*filters)
            .order_by(Tenant.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        tenants = db.session.execute(stmt).scalars().all()

        clone_counts = _clone_counts_by_tenant([str(t.id) for t in tenants])
        monthly_costs = _monthly_costs_by_tenant([str(t.id) for t in tenants])

        return {
            "items": [
                {
                    "id": str(t.id),
                    "slug": t.slug,
                    "name": t.name,
                    "plan": normalize_plan(t.plan),
                    "status": normalize_tenant_status(t.status),
                    "subscription_status": t.subscription_status,
                    "clone_count": clone_counts.get(str(t.id), 0),
                    "monthly_cost_cents": monthly_costs.get(str(t.id), 0),
                    "created_at": _iso(t.created_at),
                    "updated_at": _iso(t.updated_at),
                }
                for t in tenants
            ],
            "pagination": _pagination_payload(page, limit, total),
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = CreateTenantPayload.model_validate(request.json)

        slug = _slugify(data.slug)
        existing = db.session.execute(
            select(Tenant).where(Tenant.slug == slug)
        ).scalar_one_or_none()
        if existing:
            return {"error": f"A tenant with slug '{slug}' already exists"}, 409

        plan = normalize_plan(data.plan)
        status = normalize_tenant_status(data.status)
        if plan not in PLAN_KEYS:
            return {"error": "invalid plan"}, 400
        if status not in TENANT_STATUS_KEYS:
            return {"error": "invalid tenant status"}, 400

        tenant = Tenant(
            name=data.name,
            slug=slug,
            plan=plan,
            status=status,
        )
        db.session.add(tenant)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            logger.exception("Admin tenant creation failed: name=%s slug=%s", data.name, data.slug)
            return {"error": "failed to create tenant"}, 500

        logger.info("Admin created tenant: name=%s slug=%s plan=%s status=%s",
                     data.name, data.slug, plan, status)

        return {
            "message": "Tenant created successfully",
            "tenant": {
                "id": str(tenant.id),
                "name": tenant.name,
                "slug": tenant.slug,
                "plan": normalize_plan(tenant.plan),
                "status": normalize_tenant_status(tenant.status),
                "created_at": int(tenant.created_at.timestamp()) if tenant.created_at else None,
            },
        }, 201


@console_ns.route("/myownclone/admin/tenants/<string:tenant_id>")
class AdminTenantDetailApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, tenant_id):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        # Validate format (DB column is VARCHAR, not native UUID type)
        try:
            uuid.UUID(tenant_id)
        except ValueError:
            return {"error": "invalid tenant_id"}, 400

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == tenant_id)
        ).scalar_one_or_none()

        if not tenant:
            return {"error": "tenant not found"}, 404

        clone_count = db.session.execute(
            select(func.count(CloneConfig.id)).where(
                CloneConfig.tenant_id == tenant_id,
            )
        ).scalar() or 0

        return {
            "id": str(tenant.id),
            "slug": tenant.slug,
            "name": tenant.name,
            "plan": normalize_plan(tenant.plan),
            "status": normalize_tenant_status(tenant.status),
            "subscription_status": tenant.subscription_status,
            "clone_count": clone_count,
            "created_at": _iso(tenant.created_at),
            "updated_at": _iso(tenant.updated_at),
        }, 200

@console_ns.route("/myownclone/admin/impersonation")
class AdminImpersonationLogApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        page, limit = _pagination_args()
        search = request.args.get("search", "").strip()

        filters = []
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            filters.append(
                or_(
                    Account.email.ilike(f"%{escaped}%", escape="\\"),
                    Tenant.name.ilike(f"%{escaped}%", escape="\\"),
                    ImpersonationLog.reason.ilike(f"%{escaped}%", escape="\\"),
                )
            )

        count_stmt = (
            select(func.count(ImpersonationLog.id))
            .select_from(ImpersonationLog)
            .outerjoin(Tenant, Tenant.id == ImpersonationLog.tenant_id)
            .outerjoin(Account, Account.id == ImpersonationLog.admin_id)
            .where(*filters)
        )
        total = db.session.execute(count_stmt).scalar() or 0

        stmt = (
            select(ImpersonationLog, Tenant, Account)
            .outerjoin(Tenant, Tenant.id == ImpersonationLog.tenant_id)
            .outerjoin(Account, Account.id == ImpersonationLog.admin_id)
            .where(*filters)
            .order_by(ImpersonationLog.started_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = db.session.execute(stmt).all()

        return {
            "items": [
                {
                    "id": str(log.id),
                    "admin_id": str(log.admin_id),
                    "admin_email": account.email if account else None,
                    "tenant_id": str(log.tenant_id),
                    "tenant_name": tenant.name if tenant else None,
                    "started_at": _iso(log.started_at),
                    "ended_at": _iso(log.ended_at),
                    "reason": log.reason,
                }
                for log, tenant, account in rows
            ],
            "pagination": _pagination_payload(page, limit, total),
        }, 200


@console_ns.route("/myownclone/admin/impersonate")
class AdminImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from datetime import timedelta, timezone

        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = ImpersonatePayload.model_validate(request.json)

        admin_id = _ensure_admin_account(data.tenant_id)

        log = ImpersonationLog(
            admin_id=admin_id,
            tenant_id=data.tenant_id,
            reason=data.reason,
        )
        db.session.add(log)

        token_str = secrets.token_urlsafe(32)
        expires = datetime.now(timezone.utc) + timedelta(minutes=30)

        # Hash token with SHA-256 + PEPPER before storing
        pepper = os.environ.get("IMPERSONATION_TOKEN_PEPPER", "")
        token_hash = hashlib.sha256((token_str + pepper).encode("utf-8")).hexdigest()

        imp_token = ImpersonationToken(
            token=token_hash,
            admin_id=admin_id,
            tenant_id=data.tenant_id,
            expires_at=expires,
        )
        db.session.add(imp_token)
        db.session.commit()

        logger.info(
            "Impersonation: admin=%s → tenant=%s reason=%s token=%s",
            g.account_id,
            data.tenant_id,
            data.reason,
            token_str[:8] + "...",
        )

        tenant = db.session.execute(select(Tenant).where(Tenant.id == data.tenant_id)).scalar_one_or_none()
        if tenant:
            tenant_name = tenant.name
        else:
            logger.warning("Tenant not found for id=%s, using fallback", data.tenant_id)
            tenant_name = f"Unknown tenant ({data.tenant_id})"

        return {
            "impersonation_id": log.id,
            "token": token_str,
            "tenant_id": data.tenant_id,
            "tenant_name": tenant_name,
            "expires_at": expires.isoformat(),
            "message": "Impersonation started — use X-Impersonate-Token header. 30 minute timeout.",
        }, 200


@console_ns.route("/myownclone/admin/impersonate/stop")
class AdminStopImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        token_str = request.headers.get("X-Impersonate-Token", "")
        if not token_str:
            return {"error": "no impersonation token provided"}, 400

        # Hash the incoming token with SHA-256 + PEPPER before DB lookup
        pepper = os.environ.get("IMPERSONATION_TOKEN_PEPPER", "")
        token_hash = hashlib.sha256((token_str + pepper).encode("utf-8")).hexdigest()

        imp_token = db.session.execute(
            select(ImpersonationToken).where(
                ImpersonationToken.token == token_hash,
                ImpersonationToken.admin_id == _ensure_admin_account(),
                ImpersonationToken.expires_at > datetime.now(timezone.utc),
            )
        ).scalar_one_or_none()

        if imp_token:
            db.session.delete(imp_token)

        log = db.session.execute(
            select(ImpersonationLog).where(
                ImpersonationLog.admin_id == _ensure_admin_account(),
                ImpersonationLog.ended_at.is_(None),
            ).order_by(ImpersonationLog.started_at.desc())
        ).scalar_one_or_none()
        if log:
            log.ended_at = datetime.now(timezone.utc)

        db.session.commit()
        return {"status": "stopped"}, 200


@console_ns.route("/myownclone/admin/courtesy-account")
class AdminCourtesyAccountApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        page, limit = _pagination_args()
        search = request.args.get("search", "").strip()

        filters = [ImpersonationLog.reason.ilike("Courtesy account:%")]
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            filters.append(
                or_(
                    ImpersonationLog.reason.ilike(f"%{escaped}%", escape="\\"),
                    Tenant.name.ilike(f"%{escaped}%", escape="\\"),
                )
            )

        count_stmt = (
            select(func.count(ImpersonationLog.id))
            .select_from(ImpersonationLog)
            .outerjoin(Tenant, Tenant.id == ImpersonationLog.tenant_id)
            .where(*filters)
        )
        total = db.session.execute(count_stmt).scalar() or 0

        stmt = (
            select(ImpersonationLog, Tenant, Account)
            .outerjoin(Tenant, Tenant.id == ImpersonationLog.tenant_id)
            .outerjoin(Account, Account.id == ImpersonationLog.admin_id)
            .where(*filters)
            .order_by(ImpersonationLog.started_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = db.session.execute(stmt).all()

        return {
            "items": [
                {
                    "id": str(log.id),
                    "tenant_id": str(log.tenant_id),
                    "tenant_name": tenant.name if tenant else None,
                    "granted_by": account.email if account else str(log.admin_id),
                    "amount_cents": 0,
                    "reason": log.reason,
                    "created_at": _iso(log.started_at),
                }
                for log, tenant, account in rows
            ],
            "pagination": _pagination_payload(page, limit, total),
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = CourtesyPayload.model_validate(request.json)
        trial_ends_at = datetime.now(timezone.utc) + timedelta(days=data.duration_days)

        plan = normalize_plan(data.plan)
        tenant = Tenant(
            name=data.name,
            slug=_unique_tenant_slug(data.email.split("@")[0] or data.name),
            plan=plan,
            status="trial",
            subscription_status="trialing",
            trial_ends_at=trial_ends_at.replace(tzinfo=None),
        )
        db.session.add(tenant)
        db.session.flush()

        admin_id = _ensure_admin_account(str(tenant.id))

        log = ImpersonationLog(
            admin_id=admin_id,
            tenant_id=str(tenant.id),
            reason=f"Courtesy account: {data.name} ({plan}, {data.duration_days}d)",
        )
        db.session.add(log)
        db.session.commit()

        return {
            "message": "Courtesy account created",
            "tenant_id": str(tenant.id),
            "tenant_name": tenant.name,
            "plan": normalize_plan(tenant.plan),
            "trial_ends_at": trial_ends_at.isoformat(),
        }, 201


@console_ns.route("/myownclone/admin/audit-log")
class AdminAuditLogApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        page, limit = _pagination_args()
        action = request.args.get("action", "").strip()
        actor_id = request.args.get("actor_id", "").strip()
        target_id = request.args.get("target_id", "").strip()

        filters = []
        if actor_id:
            filters.append(ImpersonationLog.admin_id == actor_id)
        if target_id:
            filters.append(ImpersonationLog.tenant_id == target_id)
        if action == "impersonation_stopped":
            filters.append(ImpersonationLog.ended_at.is_not(None))
        elif action and action != "impersonation_started":
            filters.append(false())

        total = db.session.execute(
            select(func.count(ImpersonationLog.id)).where(*filters)
        ).scalar() or 0
        rows = db.session.execute(
            select(ImpersonationLog)
            .where(*filters)
            .order_by(ImpersonationLog.started_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        ).scalars().all()

        items = []
        for log in rows:
            stopped = action == "impersonation_stopped" and log.ended_at is not None
            items.append({
                "id": str(log.id),
                "actor_id": str(log.admin_id),
                "action": "impersonation_stopped" if stopped else "impersonation_started",
                "target_type": "tenant",
                "target_id": str(log.tenant_id),
                "reason": log.reason,
                "metadata": {"ended_at": _iso(log.ended_at)} if log.ended_at else None,
                "ip_address": None,
                "user_agent": None,
                "created_at": _iso(log.ended_at if stopped else log.started_at),
            })

        return {
            "items": items,
            "pagination": _pagination_payload(page, limit, total),
        }, 200


@console_ns.route("/myownclone/admin/feedback")
class AdminFeedbackApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        page, limit = _pagination_args()
        rating = request.args.get("rating", "").strip()
        search = request.args.get("search", "").strip()

        filters = []
        if rating in {"up", "down"}:
            filters.append(Feedback.rating == rating)
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            filters.append(
                or_(
                    Feedback.comment.ilike(f"%{escaped}%", escape="\\"),
                    CloneConfig.name.ilike(f"%{escaped}%", escape="\\"),
                    Tenant.name.ilike(f"%{escaped}%", escape="\\"),
                )
            )

        count_stmt = (
            select(func.count(Feedback.id))
            .select_from(Feedback)
            .outerjoin(CloneConfig, CloneConfig.id == Feedback.clone_id)
            .outerjoin(Tenant, Tenant.id == CloneConfig.tenant_id)
            .where(*filters)
        )
        total = db.session.execute(count_stmt).scalar() or 0

        order_column = getattr(Feedback, "created_at", None)
        if order_column is None:
            order_column = Feedback.id
        stmt = (
            select(Feedback, CloneConfig, Tenant)
            .outerjoin(CloneConfig, CloneConfig.id == Feedback.clone_id)
            .outerjoin(Tenant, Tenant.id == CloneConfig.tenant_id)
            .where(*filters)
            .order_by(order_column.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        rows = db.session.execute(stmt).all()

        return {
            "items": [
                {
                    "id": str(feedback.id),
                    "clone_id": str(feedback.clone_id),
                    "clone_name": clone.name if clone else None,
                    "tenant_id": str(tenant.id) if tenant else None,
                    "tenant_name": tenant.name if tenant else None,
                    "rating": feedback.rating,
                    "comment": feedback.comment,
                    "created_at": _iso(getattr(feedback, "created_at", None)),
                }
                for feedback, clone, tenant in rows
            ],
            "pagination": _pagination_payload(page, limit, total),
        }, 200


def _is_platform_admin(account_id: str) -> bool:
    if getattr(g, "account_role", None) == "platform_admin":
        return True

    from api.models.account import Account

    try:
        account = db.session.execute(
            select(Account).where(Account.id == account_id)
        ).scalar_one_or_none()
    except Exception:
        return False

    if account and hasattr(account, "is_platform_admin") and account.is_platform_admin:
        return True

    # Explicit platform admin check only - no fallback to tenant ownership
    return False
