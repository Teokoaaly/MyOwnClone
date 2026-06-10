import { NextRequest, NextResponse } from "next/server";
import Stripe from "stripe";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY ?? "", {
  apiVersion: "2025-02-24.acacia",
});

const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET ?? "";

export async function POST(request: NextRequest) {
  if (!webhookSecret) {
    console.error("STRIPE_WEBHOOK_SECRET not configured");
    return NextResponse.json({ error: "Webhook not configured" }, { status: 500 });
  }

  const body = await request.text();
  const signature = request.headers.get("stripe-signature");

  if (!signature) {
    return NextResponse.json({ error: "Missing signature" }, { status: 400 });
  }

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(body, signature, webhookSecret);
  } catch (err: any) {
    console.error("Webhook signature verification failed:", err.message);
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
  }

  try {
    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object as Stripe.Checkout.Session;
        await handleCheckoutCompleted(session);
        break;
      }
      case "customer.subscription.updated": {
        const subscription = event.data.object as Stripe.Subscription;
        await handleSubscriptionUpdated(subscription);
        break;
      }
      case "customer.subscription.deleted": {
        const subscription = event.data.object as Stripe.Subscription;
        await handleSubscriptionDeleted(subscription);
        break;
      }
      case "invoice.payment_succeeded": {
        const invoice = event.data.object as Stripe.Invoice;
        await handlePaymentSucceeded(invoice);
        break;
      }
      case "invoice.payment_failed": {
        const invoice = event.data.object as Stripe.Invoice;
        await handlePaymentFailed(invoice);
        break;
      }
      default:
        console.log(`Unhandled event type: ${event.type}`);
    }

    return NextResponse.json({ received: true });
  } catch (err: any) {
    console.error(`Error processing webhook ${event.type}:`, err);
    return NextResponse.json({ error: "Webhook handler failed" }, { status: 500 });
  }
}

async function handleCheckoutCompleted(session: Stripe.Checkout.Session) {
  const customerId = session.customer as string;
  const subscriptionId = session.subscription as string;
  const tenantId = session.metadata?.tenant_id;

  if (!tenantId) {
    console.error("No tenant_id in checkout session metadata");
    return;
  }

  // Fetch subscription to get plan details
  const subscription = await stripe.subscriptions.retrieve(subscriptionId);
  const priceId = subscription.items.data[0]?.price.id;

  // Map Stripe price ID to plan name
  const planName = await mapPriceToPlan(priceId);

  await db
    .update(schema.tenants)
    .set({
      stripeCustomerId: customerId,
      stripeSubscriptionId: subscriptionId,
      plan: planName as any,
      subscriptionStatus: "active",
      status: "active",
    })
    .where(eq(schema.tenants.id, tenantId));

  console.log(`Checkout completed for tenant ${tenantId}: plan=${planName}`);
}

async function handleSubscriptionUpdated(subscription: Stripe.Subscription) {
  const customerId = subscription.customer as string;
  const tenant = await findTenantByStripeCustomerId(customerId);

  if (!tenant) {
    console.error(`No tenant found for customer ${customerId}`);
    return;
  }

  const priceId = subscription.items.data[0]?.price.id;
  const planName = await mapPriceToPlan(priceId);
  const status = mapStripeStatus(subscription.status);

  await db
    .update(schema.tenants)
    .set({
      plan: planName as any,
      subscriptionStatus: status,
    })
    .where(eq(schema.tenants.id, tenant.id));

  console.log(`Subscription updated for tenant ${tenant.id}: plan=${planName}, status=${status}`);
}

async function handleSubscriptionDeleted(subscription: Stripe.Subscription) {
  const customerId = subscription.customer as string;
  const tenant = await findTenantByStripeCustomerId(customerId);

  if (!tenant) return;

  await db
    .update(schema.tenants)
    .set({
      plan: "trial" as any,
      subscriptionStatus: "cancelled",
      stripeSubscriptionId: null,
    })
    .where(eq(schema.tenants.id, tenant.id));

  console.log(`Subscription deleted for tenant ${tenant.id}`);
}

async function handlePaymentSucceeded(invoice: Stripe.Invoice) {
  const customerId = invoice.customer as string;
  const tenant = await findTenantByStripeCustomerId(customerId);

  if (!tenant) return;

  // Reset to active if was past due
  if (tenant.subscriptionStatus === "past_due") {
    await db
      .update(schema.tenants)
      .set({ subscriptionStatus: "active" })
      .where(eq(schema.tenants.id, tenant.id));
  }
}

async function handlePaymentFailed(invoice: Stripe.Invoice) {
  const customerId = invoice.customer as string;
  const tenant = await findTenantByStripeCustomerId(customerId);

  if (!tenant) return;

  await db
    .update(schema.tenants)
    .set({ subscriptionStatus: "past_due" })
    .where(eq(schema.tenants.id, tenant.id));

  console.log(`Payment failed for tenant ${tenant.id}`);
}

async function findTenantByStripeCustomerId(customerId: string) {
  const [tenant] = await db
    .select()
    .from(schema.tenants)
    .where(eq(schema.tenants.stripeCustomerId, customerId))
    .limit(1);
  return tenant ?? null;
}

async function mapPriceToPlan(priceId: string | null): Promise<string> {
  if (!priceId) return "trial";

  // Fetch price from Stripe to get the product
  try {
    const price = await stripe.prices.retrieve(priceId);
    const product = await stripe.products.retrieve(price.product as string);

    // Map product name to plan
    const name = product.name.toLowerCase();
    if (name.includes("enterprise")) return "enterprise";
    if (name.includes("scale") || name.includes("escala")) return "scale";
    if (name.includes("pro")) return "pro";
    if (name.includes("basic") || name.includes("básico")) return "basic";
  } catch {
    console.error(`Failed to resolve price ${priceId}`);
  }

  return "trial";
}

function mapStripeStatus(status: string): "active" | "cancelled" | "inactive" | "trialing" | "past_due" {
  switch (status) {
    case "active":
      return "active";
    case "past_due":
      return "past_due";
    case "canceled":
    case "cancelled":
      return "cancelled";
    case "trialing":
      return "trialing";
    case "unpaid":
      return "past_due";
    default:
      return "inactive";
  }
}
