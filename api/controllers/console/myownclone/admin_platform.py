"""MyOwnClone admin platform API — multi-tenant management, impersonation, MRR dashboard.

Requires platform_admin role. Used by the platform admin panel.
"""

import hashlib
import logging
import os
import re
import secrets
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
from api.libs.datetime_utils import naive_utc_now
from api.libs.login import login_required
from api.models.account import Account, Tenant
from api.models.myownclone import AdminInvitation, CloneConfig, CostTracking, Feedback, ImpersonationLog, ImpersonationToken

# Fail-fast validation for required secrets
_impersonation_pepper = os.environ.get('IMPERSONATION_TOKEN_PEPPER', '')
if not _impersonation_pepper or _impersonation_pepper == 'change-me':
    raise ValueError(
        "IMPERSONATION_TOKEN_PEPPER environment variable must be set to a non-empty value. "
        "Do not use default or placeholder values in production."
    )

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
    since = naive_utc_now() - timedelta(days=30)
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


def _get_existing_admin_account() -> str | None:
    """Get the current user's account if they are a platform admin.

    Returns the account_id if the current user is an existing platform admin,
    otherwise returns None.

    NOTE: This does NOT auto-create accounts. Admin access requires an explicit
    invitation through the admin invitation flow.
    """
    account_id = str(getattr(g, "account_id", "") or "").strip()
    if not account_id:
        return None

    account = db.session.execute(
        select(Account).where(Account.id == account_id)
    ).scalar_one_or_none()

    if account and _is_platform_admin(account_id):
        return str(account.id)

    return None


def _get_platform_admin_account_or_error() -> str:
    """Get a platform admin account or raise an error.

    Returns the account_id of an existing platform admin.
    Raises a 403 error if no platform admin exists or the current user is not one.

    Use this for operations that require an established admin identity.
    For first-time setup, use the admin invitation flow instead.
    """
    admin_id = _get_existing_admin_account()
    if admin_id:
        return admin_id

    # Check if any platform admin exists at all
    any_admin = db.session.execute(
        select(Account.id).where(Account.is_platform_admin == True)
    ).scalar_one_or_none()

    if any_admin:
        raise PermissionError("Current user is not a platform admin")

    raise PermissionError(
        "No platform admin exists. Use POST /console/api/myownclone/admin/invitation/first "
        "to create the first platform admin account."
    )


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

        # Use SQL aggregation instead of loading all tenants into memory
        # Get per-plan counts and MRR in a single query
        plan_stats = db.session.execute(
            select(Tenant.plan, Tenant.status, Tenant.subscription_status, func.count(Tenant.id))
            .group_by(Tenant.plan, Tenant.status, Tenant.subscription_status)
        ).all()

        for plan_key, status, sub_status, count in plan_stats:
            plan_name = normalize_plan(plan_key)
            if plan_name in plan_counts:
                plan_counts[plan_name] += count
                if sub_status == "active":
                    mrr_cents += PLAN_PRICES_CENTS.get(plan_name, 0) * count
            if normalize_tenant_status(status) == "active":
                active_tenants += count

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

      ***REMOVED***lters = []
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
          ***REMOVED***lters.append(
                or_(
                    Tenant.name.ilike(f"%{escaped}%", escape="\\"),
                    Tenant.slug.ilike(f"%{escaped}%", escape="\\"),
                )
            )
        if plan:
          ***REMOVED***lters.append(Tenant.plan == normalize_plan(plan))
        if status:
          ***REMOVED***lters.append(Tenant.status == normalize_tenant_status(status))

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

      ***REMOVED***lters = []
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
          ***REMOVED***lters.append(
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
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = ImpersonatePayload.model_validate(request.json)

        # Use the authenticated platform admin's account (already verified above)
        admin_id = g.account_id

        log = ImpersonationLog(
            admin_id=admin_id,
            tenant_id=data.tenant_id,
            reason=data.reason,
        )
        db.session.add(log)

        token_str = secrets.token_urlsafe(32)
        expires = naive_utc_now() + timedelta(minutes=30)

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
      ***REMOVED***:
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
                ImpersonationToken.expires_at > naive_utc_now(),
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
            log.ended_at = naive_utc_now()

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

      ***REMOVED***lters = [ImpersonationLog.reason.ilike("Courtesy account:%")]
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
          ***REMOVED***lters.append(
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
        trial_ends_at = naive_utc_now() + timedelta(days=data.duration_days)

        plan = normalize_plan(data.plan)
        tenant = Tenant(
            name=data.name,
            slug=_unique_tenant_slug(data.email.split("@")[0] or data.name),
            plan=plan,
            status="trial",
            subscription_status="trialing",
            trial_ends_at=trial_ends_at,
        )
        db.session.add(tenant)
        db.session.flush()

        # Use the authenticated platform admin's account (already verified above)
        admin_id = g.account_id

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

      ***REMOVED***lters = []
        if actor_id:
          ***REMOVED***lters.append(ImpersonationLog.admin_id == actor_id)
        if target_id:
          ***REMOVED***lters.append(ImpersonationLog.tenant_id == target_id)
        if action == "impersonation_stopped":
          ***REMOVED***lters.append(ImpersonationLog.ended_at.is_not(None))
        elif action and action != "impersonation_started":
          ***REMOVED***lters.append(false())

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

      ***REMOVED***lters = []
        if rating in {"up", "down"}:
          ***REMOVED***lters.append(Feedback.rating == rating)
        if search:
            escaped = search.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
          ***REMOVED***lters.append(
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


# ─── Admin Invitation Flow ────────────────────────────────────────────────────
# Security: No auto-creation of admins. Admin access requires explicit invitation.


class FirstAdminSetupPayload(BaseModel):
    email: str = Field(..., min_length=1, description="Email for the first platform admin")
    name: str = Field(..., min_length=1, description="Name of the first platform admin")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")


class AcceptInvitationPayload(BaseModel):
    token: str = Field(..., min_length=1, description="Invitation token")
    email: str = Field(..., min_length=1, description="Email address to associate with this account")
    name: str = Field(..., min_length=1, description="Name for the account")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")


class InviteAdminPayload(BaseModel):
    email: str = Field(..., min_length=1, description="Email to invite as platform admin")


register_schema_models(console_ns, FirstAdminSetupPayload, AcceptInvitationPayload, InviteAdminPayload)


def _check_any_platform_admin_exists() -> bool:
    """Check if any platform admin account exists in the system."""
    return db.session.execute(
        select(Account.id).where(Account.is_platform_admin == True).limit(1)
    ).scalar_one_or_none() is not None


def _create_admin_invitation_token() -> str:
    """Generate a secure random invitation token."""
    return secrets.token_urlsafe(32)


def _hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    import bcrypt
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


@console_ns.route("/myownclone/admin/invitation/first")
class AdminFirstSetupApi(Resource):
    """Create the first platform admin account.

    SECURITY: This endpoint is only available when NO platform admin exists.
    It is intended for initial system setup only.
    Once a platform admin exists, this endpoint is disabled.
    """

    def post(self):
        # Check if any platform admin already exists
        if _check_any_platform_admin_exists():
            return {
                "error": "A platform admin already exists. Use the invitation flow to add more admins."
            }, 403

        data = FirstAdminSetupPayload.model_validate(request.json)

        # Check if email is already in use
        existing = db.session.execute(
            select(Account).where(Account.email == data.email)
        ).scalar_one_or_none()
        if existing:
            return {"error": "An account with this email already exists"}, 409

        # Get or create platform tenant
        platform_tenant = db.session.execute(
            select(Tenant).order_by(Tenant.created_at.asc())
        ).scalar_one_or_none()

        if not platform_tenant:
            platform_tenant = Tenant(
                name="Platform",
                slug=_unique_tenant_slug("platform"),
                plan="trial",
                status="active",
            )
            db.session.add(platform_tenant)
            db.session.flush()

        # Create the admin account
        account = Account(
            tenant_id=str(platform_tenant.id),
            email=data.email,
            password=_hash_password(data.password),
            name=data.name,
            role="platform_admin",
            is_platform_admin=True,
            status="active",
        )
        db.session.add(account)
        db.session.commit()

        logger.info("First platform admin created: email=%s", data.email)

        return {
            "message": "Platform admin account created successfully",
            "email": data.email,
            "account_id": str(account.id),
        }, 201


@console_ns.route("/myownclone/admin/invitation/accept")
class AdminAcceptInvitationApi(Resource):
    """Accept an admin invitation and create account.

    Validates the invitation token and creates the platform admin account.
    """

    def post(self):
        data = AcceptInvitationPayload.model_validate(request.json)

        # Find the invitation
        invitation = db.session.execute(
            select(AdminInvitation).where(
                AdminInvitation.token == data.token,
                AdminInvitation.status == "pending",
                AdminInvitation.expires_at > naive_utc_now(),
            )
        ).scalar_one_or_none()

        if not invitation:
            return {"error": "Invalid or expired invitation token"}, 400

        # Verify email matches
        if invitation.email.lower() != data.email.lower():
            return {"error": "Email does not match invitation"}, 400

        # Check if account already exists
        existing = db.session.execute(
            select(Account).where(Account.email == data.email)
        ).scalar_one_or_none()
        if existing:
            return {"error": "An account with this email already exists"}, 409

        # Determine tenant (use invitation's tenant_id or get platform tenant)
        if invitation.tenant_id:
            tenant_id = invitation.tenant_id
      ***REMOVED***:
            platform_tenant = db.session.execute(
                select(Tenant).order_by(Tenant.created_at.asc())
            ).scalar_one_or_none()
            if not platform_tenant:
                # Create platform tenant if it doesn't exist
                platform_tenant = Tenant(
                    name="Platform",
                    slug=_unique_tenant_slug("platform"),
                    plan="trial",
                    status="active",
                )
                db.session.add(platform_tenant)
                db.session.flush()
            tenant_id = str(platform_tenant.id)

        # Create the admin account
        account = Account(
            tenant_id=tenant_id,
            email=data.email,
            password=_hash_password(data.password),
            name=data.name,
            role="platform_admin",
            is_platform_admin=True,
            status="active",
        )
        db.session.add(account)

        # Mark invitation as accepted
        invitation.status = "accepted"
        invitation.accepted_at = naive_utc_now()

        db.session.commit()

        logger.info("Admin invitation accepted: email=%s by=%s", data.email, invitation.email)

        return {
            "message": "Platform admin account created successfully",
            "email": data.email,
            "account_id": str(account.id),
        }, 201


@console_ns.route("/myownclone/admin/invitation/create")
class AdminCreateInvitationApi(Resource):
    """Create an invitation for a new platform admin.

    Requires existing platform admin authentication.
    """

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        data = InviteAdminPayload.model_validate(request.json)

        # Check if email already has an account
        existing = db.session.execute(
            select(Account).where(Account.email == data.email)
        ).scalar_one_or_none()
        if existing:
            return {"error": "An account with this email already exists. Cannot create invitation."}, 409

        # Check for existing pending invitation
        existing_invite = db.session.execute(
            select(AdminInvitation).where(
                AdminInvitation.email == data.email,
                AdminInvitation.status == "pending",
                AdminInvitation.expires_at > naive_utc_now(),
            )
        ).scalar_one_or_none()
        if existing_invite:
            return {"error": "A pending invitation already exists for this email"}, 409

        # Get platform tenant
        platform_tenant = db.session.execute(
            select(Tenant).order_by(Tenant.created_at.asc())
        ).scalar_one_or_none()

        # Create invitation
        token = _create_admin_invitation_token()
        invitation = AdminInvitation(
            token=token,
            email=data.email,
            created_by=g.account_id,
            expires_at=naive_utc_now() + timedelta(days=7),
            tenant_id=str(platform_tenant.id) if platform_tenant else None,
            status="pending",
        )
        db.session.add(invitation)
        db.session.commit()

        logger.info("Admin invitation created: email=%s by=%s", data.email, g.account_id)

        return {
            "message": "Invitation created successfully",
            "invitation_token": token,
            "expires_at": invitation.expires_at.isoformat(),
            "email": data.email,
        }, 201


@console_ns.route("/myownclone/admin/invitation/revoke/<invitation_id>")
class AdminRevokeInvitationApi(Resource):
    """Revoke a pending admin invitation.

    Requires existing platform admin authentication.
    """

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, invitation_id):
        if not _is_platform_admin(g.account_id):
            return {"error": "platform admin only"}, 403

        invitation = db.session.execute(
            select(AdminInvitation).where(AdminInvitation.id == invitation_id)
        ).scalar_one_or_none()

        if not invitation:
            return {"error": "Invitation not found"}, 404

        if invitation.status != "pending":
            return {"error": "Can only revoke pending invitations"}, 400

        invitation.status = "revoked"
        db.session.commit()

        logger.info("Admin invitation revoked: id=%s by=%s", invitation_id, g.account_id)

        return {"message": "Invitation revoked successfully"}, 200


def _is_platform_admin(account_id: str) -> bool:
    if getattr(g, "account_role", None) == "platform_admin":
        return True

    from api.models.account import Account

    try:
        account = db.session.execute(
            select(Account).where(Account.id == account_id)
        ).scalar_one_or_none()
    except Exception:
        logger.exception("Failed to fetch account for platform admin check")
        return False

    if account and hasattr(account, "is_platform_admin") and account.is_platform_admin:
        return True

    # Explicit platform admin check only - no fallback to tenant ownership
    return False
