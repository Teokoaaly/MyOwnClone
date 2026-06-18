"""MyOwnClone Stripe integration — checkout, webhooks, and plan management.

Adds MyOwnClone-specific product/price handling.
"""

import logging
import os
from urllib.parse import urlparse

import stripe
from flask import g, jsonify, request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from api.configs import myownclone_config
from api.controllers.common.schema import register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.contracts import normalize_plan, normalize_tenant_status
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.myownclone import Plan
from api.models.analytics import CostTracking

logger = logging.getLogger(__name__)

stripe.api_key = (
    getattr(myownclone_config, "STRIPE_SECRET_KEY", None)
    or os.environ.get("STRIPE_SECRET_KEY", "")
)

DEFAULT_DASHBOARD_SUCCESS_PATH = "/resumen"
DEFAULT_DASHBOARD_CANCEL_PATH = "/facturacion"


class CheckoutPayload(BaseModel):
    plan_id: str
    success_url: str = Field(default=DEFAULT_DASHBOARD_SUCCESS_PATH)
    cancel_url: str = Field(default=DEFAULT_DASHBOARD_CANCEL_PATH)


register_schema_models(console_ns, CheckoutPayload)


def _site_url() -> str:
    return (
        os.environ.get("MYOWNCLONE_SITE_URL")
        or os.environ.get("NEXTAUTH_URL")
        or os.environ.get("PUBLIC_APP_URL")
        or request.host_url.rstrip("/")
    ).rstrip("/")


def _safe_redirect_url(value: str, fallback_path: str) -> str:
    if not value:
        value = fallback_path

    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        allowed_origin = _site_url()
        allowed = urlparse(allowed_origin)
        if parsed.scheme == allowed.scheme and parsed.netloc == allowed.netloc:
            return value
        return f"{allowed_origin}{fallback_path}"

    if not value.startswith("/"):
        value = f"/{value}"
    if value.startswith("/dashboard/"):
        value = value.removeprefix("/dashboard")
    return f"{_site_url()}{value}"


def _account_email(account) -> str | None:
    forwarded_email = getattr(g, "account_email", None)
    if forwarded_email:
        return forwarded_email
    email = getattr(account, "email", None)
    if email:
        return email
    return None


@console_ns.route("/myownclone/plans")
class PlansApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        plans = db.session.execute(
            select(Plan).order_by(Plan.price_cents)
        ).scalars().all()

        return [
            {
                "id": p.id,
                "name": p.name,
                "price_cents": p.price_cents,
                "price_display": f"{(p.price_cents / 100):.0f}€/mes",
                "stripe_price_id": p.stripe_price_id,
                "words_training_limit": p.words_training_limit,
                "responses_month_limit": p.responses_month_limit,
                "modes_active": p.modes_active,
                "email_triage": p.email_triage,
                "booking": p.booking,
                "api_access": p.api_access,
                "multi_clone": p.multi_clone,
                "whitelabel": p.whitelabel,
            }
            for p in plans
        ], 200


@console_ns.route("/myownclone/stripe/checkout")
class StripeCheckoutApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, tenant_id = current_account_with_tenant()
        data = CheckoutPayload.model_validate(request.json)

        if not stripe.api_key:
            return {"error": "stripe_not_configured"}, 503

        if not tenant_id:
            return {"error": "tenant not found"}, 400

        plan = db.session.execute(
            select(Plan).where(Plan.id == data.plan_id)
        ).scalar_one_or_none()

        if not plan:
            return {"error": "plan not found"}, 404

        if not plan.stripe_price_id:
            return {"error": "plan is not available for checkout"}, 409

        customer_email = _account_email(account)
        if not customer_email:
            return {"error": "account email not available"}, 400

        try:
            checkout_session = stripe.checkout.Session.create(
                mode="subscription",
                line_items=[{
                    "price": plan.stripe_price_id,
                    "quantity": 1,
                }],
                metadata={
                    "tenant_id": tenant_id,
                    "plan_id": plan.id,
                    "plan_name": plan.name,
                },
                success_url=_safe_redirect_url(data.success_url, DEFAULT_DASHBOARD_SUCCESS_PATH),
                cancel_url=_safe_redirect_url(data.cancel_url, DEFAULT_DASHBOARD_CANCEL_PATH),
                customer_email=customer_email,
                subscription_data={
                    "trial_period_days": 14,
                    "metadata": {
                        "tenant_id": tenant_id,
                        "plan_id": plan.id,
                    },
                },
            )
            return {"url": checkout_session.url}, 200
        except stripe.error.StripeError as e:
            logger.error("Stripe checkout error: %s", e)
            return {"error": str(e)}, 400


@console_ns.route("/myownclone/stripe/billing")
class StripeBillingApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, tenant_id = current_account_with_tenant()
        from api.models.account import Tenant

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == tenant_id)
        ).scalar_one_or_none()
        usage_cost_cents = db.session.execute(
            select(func.coalesce(func.sum(CostTracking.cost_cents), 0)).where(
                CostTracking.tenant_id == tenant_id
            )
        ).scalar_one()

        base_payload = {
            "plan": normalize_plan(getattr(tenant, "plan", None) if tenant else None),
            "status": normalize_tenant_status(getattr(tenant, "status", None) if tenant else None),
            "subscription_status": getattr(tenant, "subscription_status", None) if tenant else None,
            "stripe_customer_id": getattr(tenant, "stripe_customer_id", None) if tenant else None,
            "stripe_subscription_id": getattr(tenant, "stripe_subscription_id", None) if tenant else None,
            "currency": "usd",
            "balance_cents": 0,
            "cash_cents": 0,
            "voucher_cents": 0,
            "credit_cents": 0,
            "outstanding_cents": 0,
            "usage_cost_cents": int(usage_cost_cents or 0),
            "trial_ends_at": getattr(tenant, "trial_ends_at", None).isoformat() if tenant and getattr(tenant, "trial_ends_at", None) else None,
            "balance_alert_enabled": False,
            "auto_billing_enabled": False,
            "payment_history": [],
            "voucher_records": [],
        }

        if not tenant or not tenant.stripe_customer_id:
            return {
                **base_payload,
                "has_stripe": False,
                "portal_url": None,
            }, 200

        if not stripe.api_key:
            return {
                **base_payload,
                "has_stripe": True,
                "portal_url": None,
                "error": "stripe_not_configured",
            }, 200

        try:
            portal_session = stripe.billing_portal.Session.create(
                customer=tenant.stripe_customer_id,
                return_url=f"{_site_url()}{DEFAULT_DASHBOARD_CANCEL_PATH}",
            )
            return {
                **base_payload,
                "has_stripe": True,
                "portal_url": portal_session.url,
            }, 200
        except stripe.error.StripeError as e:
            logger.error("Stripe portal error: %s", e)
            return {
                **base_payload,
                "has_stripe": True,
                "portal_url": None,
            }, 200
