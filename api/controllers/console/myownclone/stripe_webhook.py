"""Stripe webhook handler for subscription lifecycle events."""

import logging
import os

import stripe
from flask import request
from flask_restx import Resource

from api.configs import myownclone_config
from api.controllers.console import console_ns
from api.extensions.ext_database import db
from api.models.account import Tenant

logger = logging.getLogger(__name__)

stripe.api_key = (
    getattr(myownclone_config, "STRIPE_SECRET_KEY", None)
    or os.environ.get("STRIPE_SECRET_KEY", "")
)

WEBHOOK_SECRET = (
    getattr(myownclone_config, "STRIPE_WEBHOOK_SECRET", None)
    or os.environ.get("STRIPE_WEBHOOK_SECRET", "")
)


def _find_tenant_by_stripe_customer(customer_id: str) -> Tenant | None:
    return db.session.query(Tenant).filter_by(
        stripe_customer_id=customer_id
    ).first()


def _handle_checkout_completed(session):
    """Handle successful checkout — activate subscription."""
    customer_id = session.get("customer")
    subscription_id = session.get("subscription")
    metadata = session.get("metadata", {}) or {}
    tenant_id = metadata.get("tenant_id")

    if not tenant_id:
        logger.warning("checkout.completed missing tenant_id in metadata")
        return

    tenant = db.session.query(Tenant).filter_by(id=tenant_id).first()
    if not tenant:
        logger.warning("checkout.completed tenant %s not found", tenant_id)
        return

    tenant.stripe_customer_id = customer_id
    tenant.stripe_subscription_id = subscription_id
    tenant.subscription_status = "active"
    tenant.plan = metadata.get("plan_name", tenant.plan)
    db.session.commit()
    logger.info("Checkout completed for tenant %s, plan %s", tenant_id, tenant.plan)


def _handle_subscription_updated(subscription):
    """Handle subscription update — sync status."""
    customer_id = subscription.get("customer")
    status = subscription.get("status")

    tenant = _find_tenant_by_stripe_customer(customer_id)
    if not tenant:
        return

    status_map = {
        "active": "active",
        "past_due": "past_due",
        "unpaid": "unpaid",
        "canceled": "canceled",
        "incomplete": "incomplete",
        "incomplete_expired": "incomplete_expired",
        "trialing": "trialing",
    }
    tenant.subscription_status = status_map.get(status, status)
    db.session.commit()
    logger.info("Subscription %s updated: %s", tenant.id, status)


def _handle_subscription_deleted(subscription):
    """Handle subscription cancellation — downgrade to free."""
    customer_id = subscription.get("customer")

    tenant = _find_tenant_by_stripe_customer(customer_id)
    if not tenant:
        return

    tenant.subscription_status = "canceled"
    tenant.plan = "free"
    tenant.stripe_subscription_id = None
    db.session.commit()
    logger.info("Subscription deleted for tenant %s, downgraded to free", tenant.id)


def _handle_invoice_paid(invoice):
    """Handle successful payment."""
    customer_id = invoice.get("customer")
    tenant = _find_tenant_by_stripe_customer(customer_id)
    if tenant:
        tenant.subscription_status = "active"
        db.session.commit()
        logger.info("Invoice paid for tenant %s", tenant.id)


def _handle_invoice_payment_failed(invoice):
    """Handle failed payment."""
    customer_id = invoice.get("customer")
    tenant = _find_tenant_by_stripe_customer(customer_id)
    if tenant:
        tenant.subscription_status = "past_due"
        db.session.commit()
        logger.warning("Invoice payment failed for tenant %s", tenant.id)


EVENT_HANDLERS = {
    "checkout.session.completed": _handle_checkout_completed,
    "customer.subscription.updated": _handle_subscription_updated,
    "customer.subscription.deleted": _handle_subscription_deleted,
    "invoice.paid": _handle_invoice_paid,
    "invoice.payment_failed": _handle_invoice_payment_failed,
}


@console_ns.route("/myownclone/stripe/webhook")
class StripeWebhookApi(Resource):
    """Stripe webhook endpoint — no auth required (verified by signature)."""

    def post(self):
        if not WEBHOOK_SECRET:
            logger.error("Stripe webhook received but STRIPE_WEBHOOK_SECRET not configured")
            return {"error": "webhook not configured"}, 503

        payload = request.get_data()
        sig_header = request.headers.get("Stripe-Signature")

        if not sig_header:
            return {"error": "missing signature"}, 400

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
        except stripe.error.SignatureVerificationError:
            logger.warning("Invalid Stripe webhook signature")
            return {"error": "invalid signature"}, 400
        except Exception:
            logger.exception("Error verifying Stripe webhook")
            return {"error": "verification error"}, 400

        event_type = event["type"]
        event_data = event["data"]["object"]

        handler = EVENT_HANDLERS.get(event_type)
        if handler:
            try:
                handler(event_data)
            except Exception:
                logger.exception("Error handling Stripe event %s", event_type)
                return {"error": "handler error"}, 500
        else:
            logger.debug("Unhandled Stripe event type: %s", event_type)

        return {"received": True}, 200
