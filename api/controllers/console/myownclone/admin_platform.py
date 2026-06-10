"""MyOwnClone admin platform API — multi-tenant management, impersonation, MRR dashboard.

Requires platform_admin role. Used by the platform admin panel.
"""

import hashlib
import logging
import os
from datetime import datetime, timedelta, timezone

from flask import g, request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from api.controllers.common.schema import register_response_schema_models, register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import login_required
from api.models.account import Tenant
from api.models.myownclone import CloneConfig, CostTracking, ImpersonationLog, ImpersonationToken

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


@console_ns.route("/myownclone/admin/overview")
class AdminOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        total_tenants = db.session.execute(select(func.count(Tenant.id))).scalar() or 0
        active_tenants = db.session.execute(
            select(func.count(Tenant.id)).where(Tenant.status == "normal")
        ).scalar() or 0

        total_clones = db.session.execute(
            select(func.count(CloneConfig.id)).where(CloneConfig.is_active.is_(True))
        ).scalar() or 0

        mrr_cents = 0
        plan_counts = {"básico": 0, "pro": 0, "escala": 0, "enterprise": 0}
        plan_prices = {"básico": 4900, "pro": 9900, "escala": 19900, "enterprise": 49900}

        tenants = db.session.execute(select(Tenant)).scalars().all()
        for t in tenants:
            plan_name = (t.plan or "básico").lower()
            if plan_name in plan_counts:
                plan_counts[plan_name] += 1
                if t.subscription_status == "active":
                    mrr_cents += plan_prices.get(plan_name, 0)

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

        page = int(request.args.get("page", 1))
        limit = min(int(request.args.get("limit", 20)), 50)
        search = request.args.get("search", "").strip()

        stmt = select(Tenant).order_by(Tenant.created_at.desc())
        if search:
            # Escape SQL LIKE wildcards so a user typing '%' doesn't
            # accidentally match every tenant. SQLAlchemy's ilike
            # uses ESCAPE for this.
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            stmt = stmt.where(Tenant.name.ilike(f"%{escaped}%", escape="\\"))

        stmt = stmt.offset((page - 1) * limit).limit(limit)
        tenants = db.session.execute(stmt).scalars().all()

        return [
            {
                "id": str(t.id),
                "name": t.name,
                "plan": t.plan,
                "status": t.status,
                "subscription_status": t.subscription_status,
                "created_at": int(t.created_at.timestamp()) if t.created_at else None,
            }
            for t in tenants
        ], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = CreateTenantPayload.model_validate(request.json)

        existing = db.session.execute(
            select(Tenant).where(Tenant.slug == data.slug)
        ).scalar_one_or_none()
        if existing:
            return {"error": f"A tenant with slug '{data.slug}' already exists"}, 409

        tenant = Tenant(
            name=data.name,
            slug=data.slug,
            plan=data.plan,
            status=data.status,
        )
        db.session.add(tenant)
        db.session.commit()

        logger.info("Admin created tenant: name=%s slug=%s plan=%s status=%s",
                     data.name, data.slug, data.plan, data.status)

        return {
            "message": "Tenant created successfully",
            "tenant": {
                "id": str(tenant.id),
                "name": tenant.name,
                "slug": tenant.slug,
                "plan": tenant.plan,
                "status": tenant.status,
                "created_at": int(tenant.created_at.timestamp()) if tenant.created_at else None,
            },
        }, 201


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

        log = ImpersonationLog(
            admin_id=g.account_id,
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
            admin_id=g.account_id,
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
                ImpersonationToken.admin_id == g.account_id,
                ImpersonationToken.expires_at > datetime.now(timezone.utc),
            )
        ).scalar_one_or_none()

        if imp_token:
            db.session.delete(imp_token)

        log = db.session.execute(
            select(ImpersonationLog).where(
                ImpersonationLog.admin_id == g.account_id,
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
    def post(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = CourtesyPayload.model_validate(request.json)
        log = ImpersonationLog(
            admin_id=g.account_id,
            tenant_id=data.email,
            reason=f"Courtesy account: {data.name} ({data.plan}, {data.duration_days}d)",
        )
        db.session.add(log)
        db.session.commit()

        tenant = Tenant(
            name=data.name,
            slug=data.email.split("@")[0],
            plan=data.plan,
        )
        db.session.add(tenant)
        db.session.commit()

        return {
            "message": "Courtesy account created",
            "tenant_id": str(tenant.id),
            "tenant_name": tenant.name,
            "plan": tenant.plan,
        }, 201


def _is_platform_admin(account_id: str) -> bool:
    # Service accounts (from proxy) are always considered platform admin
    if account_id and account_id.startswith("proxy-"):
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
