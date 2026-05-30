"""Clonify Stripe integration — checkout, webhooks, and plan management.

Uses the same Stripe key as Dify but adds Clonify-specific product/price handling.
"""

import logging

import stripe
from flask import jsonify, request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select

from configs import dify_config
from controllers.common.schema import register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from libs.login import current_account_with_tenant, login_required
from models.clonify import Plan

logger = logging.getLogger(__name__)

stripe.api_key = getattr(dify_config, "STRIPE_SECRET_KEY", None) or ""


class CheckoutPayload(BaseModel):
    plan_id: str
    success_url: str = Field(default="/dashboard/resumen")
    cancel_url: str = Field(default="/dashboard/facturacion")


register_schema_models(console_ns, CheckoutPayload)


@console_ns.route("/clonify/plans")
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


@console_ns.route("/clonify/stripe/checkout")
class StripeCheckoutApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, tenant_id = current_account_with_tenant()
        data = CheckoutPayload.model_validate(request.json)

        plan = db.session.execute(
            select(Plan).where(Plan.id == data.plan_id)
        ).scalar_one_or_none()

        if not plan:
            return {"error": "plan not found"}, 404

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
                success_url=data.success_url,
                cancel_url=data.cancel_url,
                customer_email=account.email,
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


@console_ns.route("/clonify/stripe/billing")
class StripeBillingApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, tenant_id = current_account_with_tenant()
        from models.account import Tenant

        tenant = db.session.execute(
            select(Tenant).where(Tenant.id == tenant_id)
        ).scalar_one_or_none()

        if not tenant or not tenant.stripe_customer_id:
            return {
                "has_stripe": False,
                "plan": None,
                "subscription_status": None,
                "portal_url": None,
            }, 200

        try:
            portal_session = stripe.billing_portal.Session.create(
                customer=tenant.stripe_customer_id,
                return_url=request.host_url.rstrip("/") + "/dashboard/facturacion",
            )
            return {
                "has_stripe": True,
                "plan": tenant.plan,
                "subscription_status": tenant.subscription_status,
                "portal_url": portal_session.url,
            }, 200
        except stripe.error.StripeError as e:
            logger.error("Stripe portal error: %s", e)
            return {
                "has_stripe": True,
                "plan": tenant.plan,
                "subscription_status": tenant.subscription_status,
                "portal_url": None,
            }, 200
