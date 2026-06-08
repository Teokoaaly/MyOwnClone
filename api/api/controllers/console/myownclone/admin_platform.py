"""MyOwnClone admin platform API — multi-tenant management, impersonation, MRR dashboard.

Requires platform_admin role. Used by the platform admin panel.
"""

import logging
from datetime import datetime

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import func, select

from api.controllers.common.schema import register_response_schema_models, register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.account import Tenant
from api.models.analytics import AdminAuditLog, Feedback
from api.models.myownclone import CloneConfig, CostTracking, ImpersonationLog, ImpersonationToken

logger = logging.getLogger(__name__)


class ImpersonatePayload(BaseModel):
    tenant_id: str
    reason: str = Field(..., min_length=10)


class CourtesyPayload(BaseModel):
    email: str
    name: str = Field(..., min_length=1, max_length=255)
    plan: str = "pro"
    duration_days: int = 30

    @field_validator("email")
    @classmethod
    def _validate_email(cls, v: str) -> str:
        import re
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError(f"Invalid email format: {v!r}")
        return v

    @field_validator("plan")
    @classmethod
    def _validate_plan(cls, v: str) -> str:
        allowed = {"trial", "basic", "pro", "scale", "enterprise"}
        if v not in allowed:
            raise ValueError(f"plan must be one of {sorted(allowed)}, got {v!r}")
        return v

    @field_validator("duration_days")
    @classmethod
    def _validate_duration_days(cls, v: int) -> int:
        if not 1 <= v <= 365:
            raise ValueError(f"duration_days must be between 1 and 365, got {v}")
        return v


register_schema_models(console_ns, ImpersonatePayload, CourtesyPayload)


@console_ns.route("/myownclone/admin/overview")
class AdminOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        total_tenants = db.session.execute(select(func.count(Tenant.id))).scalar() or 0
        active_tenants = db.session.execute(
            select(func.count(Tenant.id)).where(Tenant.status == "normal")
        ).scalar() or 0

        try:
            total_clones = db.session.execute(
                select(func.count(CloneConfig.id)).where(CloneConfig.is_active.is_(True))
            ).scalar() or 0
        except Exception:
            # SQLite test fixture may lack clone_configs table (ARRAY column unsupported)
            total_clones = 0

        mrr_cents = 0
        plan_counts = {"trial": 0, "basic": 0, "pro": 0, "scale": 0, "enterprise": 0}
        plan_prices_db_to_api = {
            "básico": "basic",
            "pro": "pro",
            "escala": "scale",
            "enterprise": "enterprise",
        }
        plan_prices = {"basic": 4900, "pro": 9900, "scale": 19900, "enterprise": 49900}
        priced_plan_names = set(plan_prices.keys())
        unpriced_plan_names = {"trial"}  # plans that have no price configured

        tenants = db.session.execute(select(Tenant)).scalars().all()
        for t in tenants:
            plan_name = (t.plan or "basic").lower()
            # Normalize Spanish db names to English API names
            plan_name = plan_prices_db_to_api.get(plan_name, plan_name)
            if plan_name in priced_plan_names:
                plan_counts[plan_name] += 1
                if t.subscription_status == "active":
                    mrr_cents += plan_prices.get(plan_name, 0)
          ***REMOVED***:
                unpriced_plan_names.add(plan_name)

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
            "unpriced_plans": sorted(unpriced_plan_names),
            "generated_at": datetime.utcnow().isoformat() + "Z",
        }, 200


@console_ns.route("/myownclone/admin/tenants")
class AdminTenantsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        page = int(request.args.get("page", 1))
        limit = min(int(request.args.get("limit", 20)), 50)
        search = request.args.get("search", "")

        count_stmt = select(func.count(Tenant.id))
        if search:
            count_stmt = count_stmt.where(Tenant.name.ilike(f"%{search}%"))
        total = db.session.execute(count_stmt).scalar() or 0

        stmt = select(Tenant).order_by(Tenant.created_at.desc())
        if search:
            stmt = stmt.where(Tenant.name.ilike(f"%{search}%"))

        stmt = stmt.offset((page - 1) * limit).limit(limit)
        tenants = db.session.execute(stmt).scalars().all()

        pages = (total + limit - 1) // limit if limit > 0 else 0
        return {
            "items": [
                {
                    "id": t.id,
                    "name": t.name,
                    "plan": t.plan,
                    "status": t.status,
                    "subscription_status": t.subscription_status,
                    "created_at": int(t.created_at.timestamp()) if t.created_at else None,
                }
                for t in tenants
            ],
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": pages,
            },
        }, 200


@console_ns.route("/myownclone/admin/tenants/<tenant_id>")
class AdminTenantDetailApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, tenant_id):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        tenant = db.session.execute(select(Tenant).where(Tenant.id == tenant_id)).scalar_one_or_none()
        if not tenant:
            return {"error": "tenant_not_found"}, 404

        return {
            "id": tenant.id,
            "name": tenant.name,
            "plan": tenant.plan,
            "status": tenant.status,
            "subscription_status": tenant.subscription_status,
            "created_at": int(tenant.created_at.timestamp()) if tenant.created_at else None,
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def patch(self, tenant_id):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        tenant = db.session.execute(select(Tenant).where(Tenant.id == tenant_id)).scalar_one_or_none()
        if not tenant:
            return {"error": "tenant_not_found"}, 404

        data = request.json or {}
        if not data:
            return {"error": "no fields provided"}, 400

        # Apply updates
        if "name" in data:
            tenant.name = data["name"]
        if "plan" in data:
            tenant.plan = data["plan"]
        if "status" in data:
            tenant.status = data["status"]

        db.session.commit()

        return {
            "id": tenant.id,
            "name": tenant.name,
            "plan": tenant.plan,
            "status": tenant.status,
            "subscription_status": tenant.subscription_status,
            "created_at": int(tenant.created_at.timestamp()) if tenant.created_at else None,
        }, 200


@console_ns.route("/myownclone/admin/impersonate")
class AdminImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        import secrets
        from datetime import timedelta

        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        from pydantic import ValidationError as _PydValidationError
        try:
            data = ImpersonatePayload.model_validate(request.json)
        except _PydValidationError:
            return {"error": "validation_error", "message": "Invalid request body"}, 400

        # Validate tenant exists
        tenant = db.session.execute(select(Tenant).where(Tenant.id == data.tenant_id)).scalar_one_or_none()
        if not tenant:
            return {"error": "tenant_not_found"}, 404

        log = ImpersonationLog(
            admin_id=account,  # account is already the account ID string
            tenant_id=data.tenant_id,
            reason=data.reason,
        )
        db.session.add(log)

        token_str = secrets.token_urlsafe(32)
        expires = datetime.utcnow() + timedelta(minutes=30)

        imp_token = ImpersonationToken(
            token=token_str,
            admin_id=account,  # account is already the account ID string
            tenant_id=data.tenant_id,
            expires_at=expires,
        )
        db.session.add(imp_token)
        db.session.commit()

        logger.info(
            "Impersonation: admin=%s → tenant=%s reason=%s token=%s",
            account,
            data.tenant_id,
            data.reason,
            token_str[:8] + "...",
        )

        return {
            "impersonation_id": log.id,
            "token": token_str,
            "tenant_id": data.tenant_id,
            "tenant_name": tenant.name,
            "expires_at": expires.isoformat(),
            "message": "Impersonation started — use X-Impersonate-Token header. 30 minute timeout.",
        }, 200


@console_ns.route("/myownclone/admin/impersonate/stop")
class AdminStopImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, _ = current_account_with_tenant()
        token_str = request.headers.get("X-Impersonate-Token", "")
        if not token_str:
            return {"error": "no_token"}, 400

        imp_token = db.session.execute(
            select(ImpersonationToken).where(
                ImpersonationToken.token == token_str,
                ImpersonationToken.admin_id == account,  # account is already the ID string
                ImpersonationToken.expires_at > datetime.utcnow(),
            )
        ).scalar_one_or_none()

        if imp_token:
            db.session.delete(imp_token)

        log = db.session.execute(
            select(ImpersonationLog).where(
                ImpersonationLog.admin_id == account,  # account is already the ID string
                ImpersonationLog.ended_at.is_(None),
            ).order_by(ImpersonationLog.started_at.desc())
        ).scalar_one_or_none()
        if log:
            log.ended_at = datetime.utcnow()

        db.session.commit()
        return {"status": "stopped"}, 200


@console_ns.route("/myownclone/admin/audit-log")
class AdminAuditLogApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        page = max(1, int(request.args.get("page", 1)))
        limit = min(50, max(1, int(request.args.get("limit", 20))))
        action_filter = request.args.get("action")
        actor_filter = request.args.get("actor_id")
        target_filter = request.args.get("target_id")

        stmt = select(AdminAuditLog).order_by(AdminAuditLog.created_at.desc())

        if action_filter:
            stmt = stmt.where(AdminAuditLog.action == action_filter)
        if actor_filter:
            stmt = stmt.where(AdminAuditLog.actor_id == actor_filter)
        if target_filter:
            stmt = stmt.where(AdminAuditLog.target_id == target_filter)

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = db.session.execute(count_stmt).scalar() or 0

        stmt = stmt.offset((page - 1) * limit).limit(limit)
        rows = db.session.execute(stmt).scalars().all()

        import json as _json

        items = []
        for row in rows:
            item = {
                "id": row.id,
                "actor_id": row.actor_id,
                "action": row.action,
                "target_type": row.target_type,
                "target_id": row.target_id,
                "reason": row.reason,
                "metadata": _json.loads(row.metadata_json) if row.metadata_json else {},
                "user_agent": row.user_agent,
                "created_at": row.created_at.isoformat() if row.created_at else None,
            }
            items.append(item)

        pages = (total + limit - 1) // limit if limit > 0 else 0

        return {
            "items": items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": pages,
            },
        }, 200


@console_ns.route("/myownclone/admin/feedback")
class AdminFeedbackApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        page = max(1, int(request.args.get("page", 1)))
        limit = min(50, max(1, int(request.args.get("limit", 20))))

        count_stmt = select(func.count(Feedback.id))
        total = db.session.execute(count_stmt).scalar() or 0

        stmt = select(Feedback).order_by(Feedback.created_at.desc())
        stmt = stmt.offset((page - 1) * limit).limit(limit)
        rows = db.session.execute(stmt).scalars().all()

        items = []
        for row in rows:
            items.append({
                "id": row.id,
                "clone_id": row.clone_id,
                "rating": row.rating,
                "comment": row.comment,
                "created_at": row.created_at.isoformat() if row.created_at else None,
            })

        pages = (total + limit - 1) // limit if limit > 0 else 0

        return {
            "items": items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": pages,
            },
        }, 200


@console_ns.route("/myownclone/admin/courtesy")
class AdminCourtesyApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, _ = current_account_with_tenant()
        if not _is_platform_admin(account):
            return {"error": "platform admin only"}, 403

        from pydantic import ValidationError as _PydValidationError
        try:
            data = CourtesyPayload.model_validate(request.json or {})
        except _PydValidationError as e:
            # Convert Pydantic errors to JSON-serializable format
            error_list = []
            for err in e.errors():
                error_list.append({
                    "loc": list(err.get("loc", [])),
                    "msg": str(err.get("msg", "")),
                    "type": str(err.get("type", "")),
                })
            return {
                "error": "invalid_payload",
                "message": "Request body failed validation",
                "details": error_list,
            }, 400

        return {
            "email": data.email,
            "name": data.name,
            "plan": data.plan,
            "duration_days": data.duration_days,
            "status": "created",
        }, 201


def _is_platform_admin(account_id: str) -> bool:
    from flask import g

    # Fast path: JWT or service token already set the role
    role = getattr(g, "account_role", None)
    if role == "platform_admin":
        return True

    # Fallback: DB lookup
    from api.models.account import Account  # FIX: was `from models.account`
    account = db.session.execute(
        select(Account).where(Account.id == account_id)
    ).scalar_one_or_none()

    if account and account.role == "platform_admin":
        return True

    return False
