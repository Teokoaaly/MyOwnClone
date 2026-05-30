"""Clonify admin platform API — multi-tenant management, impersonation, MRR dashboard.

Requires platform_admin role. Used by the platform admin panel.
"""

import logging
from datetime import datetime

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from controllers.common.schema import register_response_schema_models, register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from libs.login import current_account_with_tenant, login_required
from models.account import Tenant, TenantAccountJoin, TenantAccountRole
from models.clonify import CloneConfig, CostTracking, ImpersonationLog, ImpersonationToken

logger = logging.getLogger(__name__)


class ImpersonatePayload(BaseModel):
    tenant_id: str
    reason: str


class CourtesyPayload(BaseModel):
    email: str
    name: str
    plan: str = "pro"
    duration_days: int = 30


register_schema_models(console_ns, ImpersonatePayload, CourtesyPayload)


@console_ns.route("/clonify/admin/overview")
class AdminOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account.id):
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


@console_ns.route("/clonify/admin/tenants")
class AdminTenantsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account.id):
            return {"error": "platform admin only"}, 403

        page = int(request.args.get("page", 1))
        limit = min(int(request.args.get("limit", 20)), 50)
        search = request.args.get("search", "")

        stmt = select(Tenant).order_by(Tenant.created_at.desc())
        if search:
            stmt = stmt.where(Tenant.name.ilike(f"%{search}%"))

        stmt = stmt.offset((page - 1) * limit).limit(limit)
        tenants = db.session.execute(stmt).scalars().all()

        return [
            {
                "id": t.id,
                "name": t.name,
                "plan": t.plan,
                "status": t.status,
                "subscription_status": t.subscription_status,
                "created_at": int(t.created_at.timestamp()) if t.created_at else None,
            }
            for t in tenants
        ], 200


@console_ns.route("/clonify/admin/impersonate")
class AdminImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        import secrets
        from datetime import timedelta

        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account.id):
            return {"error": "platform admin only"}, 403

        data = ImpersonatePayload.model_validate(request.json)

        log = ImpersonationLog(
            admin_id=account.id,
            tenant_id=data.tenant_id,
            reason=data.reason,
        )
        db.session.add(log)

        token_str = secrets.token_urlsafe(32)
        expires = datetime.utcnow() + timedelta(minutes=30)

        imp_token = ImpersonationToken(
            token=token_str,
            admin_id=account.id,
            tenant_id=data.tenant_id,
            expires_at=expires,
        )
        db.session.add(imp_token)
        db.session.commit()

        logger.info(
            "Impersonation: admin=%s → tenant=%s reason=%s token=%s",
            account.id,
            data.tenant_id,
            data.reason,
            token_str[:8] + "...",
        )

        return {
            "impersonation_id": log.id,
            "token": token_str,
            "tenant_id": data.tenant_id,
            "tenant_name": data.tenant_id,
            "expires_at": expires.isoformat(),
            "message": "Impersonation started — use X-Impersonate-Token header. 30 minute timeout.",
        }, 200


@console_ns.route("/clonify/admin/impersonate/stop")
class AdminStopImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, _ = current_account_with_tenant()
        token_str = request.headers.get("X-Impersonate-Token", "")
        if not token_str:
            return {"error": "no impersonation token provided"}, 400

        imp_token = db.session.execute(
            select(ImpersonationToken).where(
                ImpersonationToken.token == token_str,
                ImpersonationToken.admin_id == account.id,
                ImpersonationToken.expires_at > datetime.utcnow(),
            )
        ).scalar_one_or_none()

        if imp_token:
            db.session.delete(imp_token)

        log = db.session.execute(
            select(ImpersonationLog).where(
                ImpersonationLog.admin_id == account.id,
                ImpersonationLog.ended_at.is_(None),
            ).order_by(ImpersonationLog.started_at.desc())
        ).scalar_one_or_none()
        if log:
            log.ended_at = datetime.utcnow()

        db.session.commit()
        return {"status": "stopped"}, 200


def _is_platform_admin(account_id: str) -> bool:
    stmt = select(TenantAccountJoin).where(
        TenantAccountJoin.account_id == account_id,
        TenantAccountJoin.role == TenantAccountRole.OWNER,
    )
    result = db.session.execute(stmt).scalar_one_or_none()
    if result is not None:
        return True

    from models.account import Account
    account = db.session.execute(
        select(Account).where(Account.id == account_id)
    ).scalar_one_or_none()
    if account and hasattr(account, "is_platform_admin"):
        return bool(account.is_platform_admin)
    return False
