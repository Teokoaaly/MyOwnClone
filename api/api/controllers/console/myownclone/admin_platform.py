"""MyOwnClone platform-admin API.

All routes are gated on `role == "platform_admin"`. The contract is documented
in `TASK-ADMIN-BACKEND.md`. The canonical plan vocabulary in the API response
is English (`trial`, `basic`, `pro`, `scale`, `enterprise`); the database may
still store the Spanish labels from the original seed, so we translate at the
controller boundary.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from flask import g, request
from flask_restx import Resource
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import and_, case, func, or_, select
from sqlalchemy.exc import SQLAlchemyError

from api.controllers.common.schema import (
    register_response_schema_models,
    register_schema_models,
)
from api.controllers.console import console_ns
from api.controllers.console.wraps import (
    account_initialization_required,
    setup_required,
)
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.account import (
    ACTIVE_TENANT_STATUSES,
    PLAN_NAME_ALIASES_API_TO_DB,
    PLAN_NAME_ALIASES_DB_TO_API,
    Account,
    Tenant,
)
from api.models.myownclone import (
    AdminAuditLog,
    AnalyticsGap,
    AnalyticsQuestion,
    CloneConfig,
    CostTracking,
    Feedback,
    ImpersonationLog,
    ImpersonationToken,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Plan prices in cents. Use canonical English names; the controller maps to
# the DB label before issuing UPDATE statements.
PLAN_PRICES_CENTS: dict[str, int] = {
    "trial": 0,
    "basic": 4900,
    "pro": 9900,
    "scale": 19900,
    "enterprise": 49900,
}

PLAN_CANONICAL_ORDER: tuple[str, ...] = ("trial", "basic", "pro", "scale", "enterprise")

# Impersonation tokens are stored as SHA-256 of (token || secret_pepper) so
# DB compromise does not leak usable bearer tokens. The full token is
# returned to the admin exactly once.
IMPERSONATION_TOKEN_TTL_MINUTES = 30
IMPERSONATION_TOKEN_PEPPER = os.environ.get(
    "IMPERSONATION_TOKEN_PEPPER", "dev-pepper-rotate-in-prod"
)


# ---------------------------------------------------------------------------
# Pydantic payloads
# ---------------------------------------------------------------------------


class ImpersonatePayload(BaseModel):
    tenant_id: str = Field(min_length=1, max_length=36)
    reason: str = Field(min_length=10, max_length=1000)


class StopImpersonatePayload(BaseModel):
    token: str = Field(min_length=8, max_length=128)


class TenantPatchPayload(BaseModel):
    plan: Optional[str] = Field(default=None, pattern="^(trial|basic|pro|scale|enterprise)$")
    status: Optional[str] = Field(default=None, pattern="^(normal|active|suspended|cancelled|trial)$")


class CourtesyPayload(BaseModel):
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    name: str = Field(min_length=1, max_length=255)
    plan: str = Field(default="pro", pattern="^(trial|basic|pro|scale|enterprise)$")
    duration_days: int = Field(default=30, ge=1, le=365)


register_schema_models(
    console_ns,
    ImpersonatePayload,
    StopImpersonatePayload,
    TenantPatchPayload,
    CourtesyPayload,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _now_utc() -> datetime:
    """Naive UTC timestamp; matches the rest of the MyOwnClone schema."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def _hash_token(token: str) -> str:
    """SHA-256(token || pepper), hex-encoded. Used for impersonation_tokens."""
    h = hashlib.sha256()
    h.update(token.encode("utf-8"))
    h.update(b"|")
    h.update(IMPERSONATION_TOKEN_PEPPER.encode("utf-8"))
    return h.hexdigest()


def _iso(dt: Optional[datetime]) -> Optional[str]:
    """Format a naive UTC datetime as ISO 8601 with explicit Z suffix."""
    if dt is None:
        return None
    # Treat naive datetimes as UTC (consistent with the rest of the schema).
    return dt.replace(microsecond=dt.microsecond).isoformat() + "Z"


def _format_eur(cents: int) -> str:
    return f"{(cents or 0) / 100:.2f}€"


def _normalise_plan_name_to_canonical(raw: Optional[str]) -> str:
    """Translate the DB-stored plan label to the canonical English API name."""
    if not raw:
        return "trial"
    return PLAN_NAME_ALIASES_DB_TO_API.get(raw.lower(), raw.lower())


def _normalise_plan_name_to_db(canonical: str) -> str:
    """Translate a canonical English plan name to the DB label."""
    return PLAN_NAME_ALIASES_API_TO_DB.get(canonical, canonical)


def _pagination_args() -> tuple[int, int]:
    """Return validated (page, limit) tuple; limit capped at 50."""
    try:
        page = max(int(request.args.get("page", 1)), 1)
    except (TypeError, ValueError):
        page = 1
    try:
        limit = int(request.args.get("limit", 20))
    except (TypeError, ValueError):
        limit = 20
    limit = min(max(limit, 1), 50)
    return page, limit


def _is_platform_admin(account_id: Optional[str]) -> bool:
    """Return True iff the account has the `platform_admin` role.

    Resolution order:
      1. JWT claim (cheap; populated by `login_required`).
      2. DB lookup on `accounts.role` — covers the dev path where the JWT is
         a stub and the actual role lives in the database.
    """
    if not account_id:
        return False

    jwt_role = getattr(g, "account_role", None)
    if jwt_role == "platform_admin":
        return True

    # Development override — never enable in production.
    if os.environ.get("DEV_PLATFORM_ADMIN_BYPASS") == "true":
        return True

    try:
        account = db.session.execute(
            select(Account).where(Account.id == account_id)
        ).scalar_one_or_none()
    except SQLAlchemyError:
        logger.exception("platform_admin lookup failed for account=%s", account_id)
        return False

    if account is None:
        return False
    return (account.role or "").lower() == "platform_admin"


def _require_platform_admin() -> Optional[tuple[dict, int]]:
    """Authenticate and authorise the request as a platform admin.

    Returns `(error_response, status_code)` on failure, `None` on success.
    """
    account_proxy = current_account_with_tenant()
    account_id = getattr(account_proxy, "id", None)
    if not account_id:
        return {"error": "unauthorized", "message": "Missing account context."}, 401
    if not _is_platform_admin(account_id):
        return {"error": "platform_admin_required", "message": "Platform admin role required."}, 403
    return None


def _write_audit(
    *,
    actor_id: str,
    action: str,
    target_type: Optional[str] = None,
    target_id: Optional[str] = None,
    reason: Optional[str] = None,
    metadata: Optional[dict[str, Any]] = None,
) -> None:
    """Append an audit row. Failures are logged but never break the request."""
    try:
        log = AdminAuditLog(
            actor_id=actor_id,
            action=action,
            target_type=target_type,
            target_id=target_id,
            reason=reason,
            metadata_json=json.dumps(metadata) if metadata else None,
            ip_address=request.headers.get("X-Forwarded-For", request.remote_addr),
            user_agent=(request.headers.get("User-Agent") or "")[:500],
        )
        db.session.add(log)
    except SQLAlchemyError:
        logger.exception("Failed to write audit row action=%s target=%s", action, target_id)


# ---------------------------------------------------------------------------
# /admin/overview
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/overview")
class AdminOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        # ---- totals -------------------------------------------------------
        total_tenants = (
            db.session.execute(select(func.count(Tenant.id))).scalar() or 0
        )
        active_tenants = (
            db.session.execute(
                select(func.count(Tenant.id)).where(
                    or_(
                        Tenant.status.in_(ACTIVE_TENANT_STATUSES),
                        Tenant.subscription_status.in_(ACTIVE_TENANT_STATUSES),
                    )
                )
            ).scalar()
            or 0
        )
        total_clones = (
            db.session.execute(
                select(func.count(CloneConfig.id)).where(CloneConfig.is_active.is_(True))
            ).scalar()
            or 0
        )

        # ---- 30-day cost window -----------------------------------------
        cutoff = _now_utc() - timedelta(days=30)
        total_costs_cents = (
            db.session.execute(
                select(func.coalesce(func.sum(CostTracking.cost_cents), 0)).where(
                    CostTracking.created_at >= cutoff
                )
            ).scalar()
            or 0
        )

        # ---- MRR: sum plan prices for tenants with active subscription ----
        plan_price_cases = [
            case(
                (
                    func.lower(Tenant.plan) == db_label,
                    PLAN_PRICES_CENTS[canonical],
                ),
              ***REMOVED***_=0,
            )
            for db_label, canonical in PLAN_NAME_ALIASES_DB_TO_API.items()
        ]
        mrr_cents = (
            db.session.execute(
                select(func.coalesce(func.sum(sum(plan_price_cases)), 0)).where(
                    func.lower(func.coalesce(Tenant.subscription_status, "")) == "active"
                )
            ).scalar()
            or 0
        )

        # ---- plan breakdown (counts per canonical name) -------------------
        plan_counts: dict[str, int] = {p: 0 for p in PLAN_CANONICAL_ORDER}
        rows = db.session.execute(
            select(func.lower(Tenant.plan), func.count(Tenant.id)).group_by(
                func.lower(Tenant.plan)
            )
        ).all()
        for raw_plan, count in rows:
            canonical = _normalise_plan_name_to_canonical(raw_plan)
            if canonical in plan_counts:
                plan_counts[canonical] += int(count or 0)
          ***REMOVED***:
                plan_counts[canonical] = int(count or 0)

        return {
            "total_tenants": int(total_tenants),
            "active_tenants": int(active_tenants),
            "total_clones": int(total_clones),
            "mrr_cents": int(mrr_cents),
            "mrr_display": _format_eur(int(mrr_cents)),
            "total_costs_cents": int(total_costs_cents),
            "total_costs_display": _format_eur(int(total_costs_cents)),
            "margin_cents": int(mrr_cents) - int(total_costs_cents),
            "margin_display": _format_eur(int(mrr_cents) - int(total_costs_cents)),
            "plan_breakdown": plan_counts,
            "generated_at": _iso(_now_utc()),
        }, 200


# ---------------------------------------------------------------------------
# /admin/tenants  (list, paginated)
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/tenants")
class AdminTenantsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        page, limit = _pagination_args()
        search = (request.args.get("search") or "").strip()
        status_filter = (request.args.get("status") or "").strip().lower() or None
        plan_filter_raw = (request.args.get("plan") or "").strip().lower() or None
        plan_filter = _normalise_plan_name_to_db(plan_filter_raw) if plan_filter_raw else None
        sort = (request.args.get("sort") or "created_at").strip().lower()
        direction = (request.args.get("direction") or "desc").strip().lower()
        if direction not in ("asc", "desc"):
            direction = "desc"

        sort_columns = {
            "created_at": Tenant.created_at,
            "name": Tenant.name,
            "plan": Tenant.plan,
            "status": Tenant.status,
        }
        sort_col = sort_columns.get(sort, Tenant.created_at)
        order_clause = sort_col.asc() if direction == "asc" else sort_col.desc()

        # ---- per-tenant aggregates (clones + 30d cost) -------------------
        cutoff = _now_utc() - timedelta(days=30)
        clone_count_sq = (
            select(func.count(CloneConfig.id))
            .where(CloneConfig.tenant_id == Tenant.id)
            .where(CloneConfig.is_active.is_(True))
            .correlate(Tenant)
            .scalar_subquery()
        )
        cost_sum_sq = (
            select(func.coalesce(func.sum(CostTracking.cost_cents), 0))
            .where(CostTracking.tenant_id == Tenant.id)
            .where(CostTracking.created_at >= cutoff)
            .correlate(Tenant)
            .scalar_subquery()
        )

        stmt = select(
            Tenant,
            clone_count_sq.label("clone_count"),
            cost_sum_sq.label("monthly_cost_cents"),
        )

        if search:
            like = f"%{search}%"
            stmt = stmt.where(or_(Tenant.name.ilike(like), Tenant.slug.ilike(like)))
        if status_filter:
            stmt = stmt.where(
                or_(
                    func.lower(Tenant.status) == status_filter,
                    func.lower(Tenant.subscription_status) == status_filter,
                )
            )
        if plan_filter:
            stmt = stmt.where(func.lower(Tenant.plan) == plan_filter.lower())

        # ---- count for pagination ----------------------------------------
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = int(db.session.execute(count_stmt).scalar() or 0)

        stmt = stmt.order_by(order_clause).offset((page - 1) * limit).limit(limit)
        rows = db.session.execute(stmt).all()

        items = []
        for tenant, clone_count, monthly_cost in rows:
            items.append(
                {
                    "id": tenant.id,
                    "slug": tenant.slug,
                    "name": tenant.name,
                    "plan": _normalise_plan_name_to_canonical(tenant.plan),
                    "status": tenant.status,
                    "subscription_status": tenant.subscription_status,
                    "clone_count": int(clone_count or 0),
                    "monthly_cost_cents": int(monthly_cost or 0),
                    "created_at": _iso(tenant.created_at),
                    "updated_at": _iso(tenant.updated_at),
                }
            )

        return {
            "items": items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": (total + limit - 1) // limit if limit else 0,
            },
        }, 200


# ---------------------------------------------------------------------------
# /admin/tenants/<tenant_id>  (detail + PATCH)
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/tenants/<string:tenant_id>")
class AdminTenantDetailApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, tenant_id: str):
        denied = _require_platform_admin()
        if denied:
            return denied

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == tenant_id)
        ).scalar_one_or_none()
        if tenant is None:
            return {"error": "tenant_not_found", "message": "Tenant does not exist."}, 404

        cutoff = _now_utc() - timedelta(days=30)

        clone_count = (
            db.session.execute(
                select(func.count(CloneConfig.id)).where(
                    CloneConfig.tenant_id == tenant.id,
                    CloneConfig.is_active.is_(True),
                )
            ).scalar()
            or 0
        )
        cost_30d = (
            db.session.execute(
                select(func.coalesce(func.sum(CostTracking.cost_cents), 0)).where(
                    CostTracking.tenant_id == tenant.id,
                    CostTracking.created_at >= cutoff,
                )
            ).scalar()
            or 0
        )
        tokens_in_30d = (
            db.session.execute(
                select(func.coalesce(func.sum(CostTracking.tokens_in), 0)).where(
                    CostTracking.tenant_id == tenant.id,
                    CostTracking.created_at >= cutoff,
                )
            ).scalar()
            or 0
        )
        tokens_out_30d = (
            db.session.execute(
                select(func.coalesce(func.sum(CostTracking.tokens_out), 0)).where(
                    CostTracking.tenant_id == tenant.id,
                    CostTracking.created_at >= cutoff,
                )
            ).scalar()
            or 0
        )
        questions_30d = (
            db.session.execute(
                select(func.coalesce(func.sum(AnalyticsQuestion.count), 0)).where(
                    AnalyticsQuestion.clone_id.in_(
                        select(CloneConfig.id).where(CloneConfig.tenant_id == tenant.id)
                    )
                )
            ).scalar()
            or 0
        )
        gaps_open = (
            db.session.execute(
                select(func.count(AnalyticsGap.id)).where(
                    AnalyticsGap.clone_id.in_(
                        select(CloneConfig.id).where(CloneConfig.tenant_id == tenant.id)
                    ),
                    AnalyticsGap.status == "open",
                )
            ).scalar()
            or 0
        )

        clones = db.session.execute(
            select(CloneConfig).where(CloneConfig.tenant_id == tenant.id)
        ).scalars().all()

        return {
            "tenant": {
                "id": tenant.id,
                "slug": tenant.slug,
                "name": tenant.name,
                "plan": _normalise_plan_name_to_canonical(tenant.plan),
                "status": tenant.status,
                "subscription_status": tenant.subscription_status,
                "stripe_customer_id": tenant.stripe_customer_id,
                "stripe_subscription_id": tenant.stripe_subscription_id,
                "created_at": _iso(tenant.created_at),
                "updated_at": _iso(tenant.updated_at),
            },
            "usage": {
                "clone_count": int(clone_count),
                "cost_cents_30d": int(cost_30d),
                "tokens_in_30d": int(tokens_in_30d),
                "tokens_out_30d": int(tokens_out_30d),
                "questions_30d": int(questions_30d),
                "gaps_open": int(gaps_open),
            },
            "clones": [
                {
                    "id": c.id,
                    "name": c.name,
                    "slug": c.slug,
                    "is_active": bool(c.is_active),
                    "language": c.language,
                    "created_at": _iso(c.created_at),
                }
                for c in clones
            ],
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def patch(self, tenant_id: str):
        denied = _require_platform_admin()
        if denied:
            return denied

        account_id = getattr(current_account_with_tenant(), "id", None)
        try:
            payload = TenantPatchPayload.model_validate(request.json or {})
        except ValidationError as exc:
            return {"error": "invalid_payload", "details": exc.errors()}, 400
        if payload.plan is None and payload.status is None:
            return {"error": "no_op", "message": "Nothing to update."}, 400

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == tenant_id)
        ).scalar_one_or_none()
        if tenant is None:
            return {"error": "tenant_not_found", "message": "Tenant does not exist."}, 404

        changes: dict[str, Any] = {}
        if payload.plan is not None:
            new_db_label = _normalise_plan_name_to_db(payload.plan)
            if tenant.plan != new_db_label:
                changes["plan"] = {"from": tenant.plan, "to": new_db_label}
                tenant.plan = new_db_label
        if payload.status is not None:
            if tenant.status != payload.status:
                changes["status"] = {"from": tenant.status, "to": payload.status}
                tenant.status = payload.status

        if not changes:
            return {"ok": True, "tenant": {"id": tenant.id}}, 200

        _write_audit(
            actor_id=account_id or "unknown",
            action="tenant_updated",
            target_type="tenant",
            target_id=tenant.id,
            metadata=changes,
        )
        db.session.commit()

        return {
            "ok": True,
            "tenant": {
                "id": tenant.id,
                "plan": _normalise_plan_name_to_canonical(tenant.plan),
                "status": tenant.status,
            },
        }, 200


# ---------------------------------------------------------------------------
# /admin/feedback
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/feedback")
class AdminFeedbackApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        page, limit = _pagination_args()
        search = (request.args.get("search") or "").strip()
        rating = (request.args.get("rating") or "").strip().lower() or None
        clone_id = (request.args.get("clone_id") or "").strip() or None
        tenant_id = (request.args.get("tenant_id") or "").strip() or None

        stmt = select(Feedback, CloneConfig, Tenant).outerjoin(
            CloneConfig, CloneConfig.id == Feedback.clone_id
        ).outerjoin(Tenant, Tenant.id == CloneConfig.tenant_id)

        if rating in ("up", "down"):
            stmt = stmt.where(Feedback.rating == rating)
        if clone_id:
            stmt = stmt.where(Feedback.clone_id == clone_id)
        if tenant_id:
            stmt = stmt.where(Tenant.id == tenant_id)
        if search:
            like = f"%{search}%"
            stmt = stmt.where(or_(Feedback.comment.ilike(like), CloneConfig.name.ilike(like)))

        total = int(
            db.session.execute(
                select(func.count()).select_from(stmt.subquery())
            ).scalar()
            or 0
        )

        rows = db.session.execute(
            stmt.order_by(Feedback.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        ).all()

        items = []
        for fb, clone, tenant in rows:
            items.append(
                {
                    "id": fb.id,
                    "clone_id": fb.clone_id,
                    "clone_name": clone.name if clone else None,
                    "tenant_id": tenant.id if tenant else None,
                    "tenant_name": tenant.name if tenant else None,
                    "rating": fb.rating,
                    "comment": fb.comment,
                    "created_at": _iso(fb.created_at),
                }
            )

        return {
            "items": items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": (total + limit - 1) // limit if limit else 0,
            },
        }, 200


# ---------------------------------------------------------------------------
# /admin/impersonate
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/impersonate")
class AdminImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        account_id = getattr(current_account_with_tenant(), "id", None)
        try:
            data = ImpersonatePayload.model_validate(request.json or {})
        except ValidationError as exc:
            return {"error": "invalid_payload", "details": exc.errors()}, 400

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == data.tenant_id)
        ).scalar_one_or_none()
        if tenant is None:
            return {
                "error": "tenant_not_found",
                "message": f"Tenant {data.tenant_id} does not exist.",
            }, 404

        token_str = secrets.token_urlsafe(32)
        token_hash = _hash_token(token_str)
        expires_at = _now_utc() + timedelta(minutes=IMPERSONATION_TOKEN_TTL_MINUTES)

        log = ImpersonationLog(
            admin_id=account_id or "unknown",
            tenant_id=tenant.id,
            reason=data.reason,
        )
        db.session.add(log)
        db.session.flush()  # populate log.id

        imp_token = ImpersonationToken(
            token=token_hash,
            admin_id=account_id or "unknown",
            tenant_id=tenant.id,
            expires_at=expires_at,
        )
        db.session.add(imp_token)

        _write_audit(
            actor_id=account_id or "unknown",
            action="impersonation_started",
            target_type="tenant",
            target_id=tenant.id,
            reason=data.reason,
            metadata={
                "impersonation_log_id": log.id,
                "expires_at": _iso(expires_at),
                "token_prefix": token_str[:8],
            },
        )

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            logger.exception("Failed to start impersonation for tenant=%s", tenant.id)
            return {"error": "impersonation_failed"}, 500

        logger.info(
            "impersonation_started admin=%s tenant=%s log=%s token_prefix=%s",
            account_id,
            tenant.id,
            log.id,
            token_str[:8],
        )

        return {
            "impersonation_id": log.id,
            "token": token_str,
            "tenant_id": tenant.id,
            "tenant_name": tenant.name,
            "expires_at": _iso(expires_at),
            "message": (
                f"Impersonation started — use X-Impersonate-Token header. "
                f"{IMPERSONATION_TOKEN_TTL_MINUTES} minute timeout."
            ),
        }, 200


@console_ns.route("/myownclone/admin/impersonate/stop")
class AdminStopImpersonateApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        account_id = getattr(current_account_with_tenant(), "id", None)
        body = request.json or {}
        provided_token = body.get("token") or request.headers.get("X-Impersonate-Token", "")
        if not provided_token:
            return {
                "error": "no_token",
                "message": "Provide the impersonation token in the body or X-Impersonate-Token header.",
            }, 400

        token_hash = _hash_token(provided_token)
        imp_token = db.session.execute(
            select(ImpersonationToken).where(
                ImpersonationToken.token == token_hash,
                ImpersonationToken.admin_id == account_id,
                ImpersonationToken.expires_at > _now_utc(),
            )
        ).scalar_one_or_none()

        if imp_token is None:
            return {
                "error": "no_active_impersonation",
                "message": "No active impersonation matches the provided token.",
            }, 404

        # Close the *matching* log (log.tenant_id == token.tenant_id and
        # still open) — never close an unrelated log.
        log = db.session.execute(
            select(ImpersonationLog).where(
                ImpersonationLog.admin_id == imp_token.admin_id,
                ImpersonationLog.tenant_id == imp_token.tenant_id,
                ImpersonationLog.ended_at.is_(None),
            ).order_by(ImpersonationLog.started_at.desc())
        ).first()
        log_obj = log[0] if log else None

        if log_obj is not None:
            log_obj.ended_at = _now_utc()

        tenant_id = imp_token.tenant_id
        db.session.delete(imp_token)

        _write_audit(
            actor_id=account_id or "unknown",
            action="impersonation_stopped",
            target_type="tenant",
            target_id=tenant_id,
            metadata={"impersonation_log_id": log_obj.id if log_obj else None},
        )

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            logger.exception("Failed to stop impersonation for tenant=%s", tenant_id)
            return {"error": "stop_failed"}, 500

        return {"status": "stopped", "tenant_id": tenant_id}, 200


# ---------------------------------------------------------------------------
# /admin/audit-log
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/audit-log")
class AdminAuditLogApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        page, limit = _pagination_args()
        action = (request.args.get("action") or "").strip() or None
        actor_id = (request.args.get("actor_id") or "").strip() or None
        target_id = (request.args.get("target_id") or "").strip() or None

        stmt = select(AdminAuditLog)
        if action:
            stmt = stmt.where(AdminAuditLog.action == action)
        if actor_id:
            stmt = stmt.where(AdminAuditLog.actor_id == actor_id)
        if target_id:
            stmt = stmt.where(AdminAuditLog.target_id == target_id)

        total = int(
            db.session.execute(
                select(func.count()).select_from(stmt.subquery())
            ).scalar()
            or 0
        )
        rows = db.session.execute(
            stmt.order_by(AdminAuditLog.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        ).scalars().all()

        items = []
        for row in rows:
            metadata: Optional[dict[str, Any]] = None
            if row.metadata_json:
                try:
                    metadata = json.loads(row.metadata_json)
                except (TypeError, ValueError):
                    metadata = {"_raw": row.metadata_json}
            items.append(
                {
                    "id": row.id,
                    "actor_id": row.actor_id,
                    "action": row.action,
                    "target_type": row.target_type,
                    "target_id": row.target_id,
                    "reason": row.reason,
                    "metadata": metadata,
                    "ip_address": row.ip_address,
                    "user_agent": row.user_agent,
                    "created_at": _iso(row.created_at),
                }
            )

        return {
            "items": items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": (total + limit - 1) // limit if limit else 0,
            },
        }, 200


# ---------------------------------------------------------------------------
# /admin/courtesy  (create tenant + account on behalf of a partner)
# ---------------------------------------------------------------------------


@console_ns.route("/myownclone/admin/courtesy")
class AdminCourtesyApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        denied = _require_platform_admin()
        if denied:
            return denied

        account_id = getattr(current_account_with_tenant(), "id", None)
        try:
            data = CourtesyPayload.model_validate(request.json or {})
        except ValidationError as exc:
            return {"error": "invalid_payload", "details": exc.errors()}, 400

        # Translate plan + slug + name for the new tenant.
        plan_db_label = _normalise_plan_name_to_db(data.plan)
        slug = data.email.split("@", 1)[0].lower().replace(".", "-")[:80]
        trial_ends = _now_utc() + timedelta(days=data.duration_days)

        new_tenant = Tenant(
            name=data.name,
            status="trial",
            plan=plan_db_label,
            slug=slug,
            subscription_status="trial",
        )
        db.session.add(new_tenant)
        db.session.flush()  # populate new_tenant.id

        new_account = Account(
            tenant_id=new_tenant.id,
            email=data.email,
            name=data.name,
            role="owner",
        )
        db.session.add(new_account)

        _write_audit(
            actor_id=account_id or "unknown",
            action="tenant_created",
            target_type="tenant",
            target_id=new_tenant.id,
            reason=f"Courtesy signup via {data.plan} for {data.duration_days}d",
            metadata={"plan": data.plan, "email": data.email, "trial_ends_at": _iso(trial_ends)},
        )

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            logger.exception("Courtesy signup failed for %s", data.email)
            return {"error": "courtesy_failed"}, 500

        return {
            "tenant_id": new_tenant.id,
            "account_id": new_account.id,
            "plan": data.plan,
            "trial_ends_at": _iso(trial_ends),
        }, 201


__all__ = [
    "AdminOverviewApi",
    "AdminTenantsApi",
    "AdminTenantDetailApi",
    "AdminFeedbackApi",
    "AdminImpersonateApi",
    "AdminStopImpersonateApi",
    "AdminAuditLogApi",
    "AdminCourtesyApi",
]
