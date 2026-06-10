import {
  pgTable,
  text,
  timestamp,
  pgEnum,
  index,
} from "drizzle-orm/pg-core";

export const tenantStatusEnum = pgEnum("tenant_status", [
  "active",
  "suspended",
  "cancelled",
  "trial",
]);

export const planEnum = pgEnum("plan", [
  "basic",
  "pro",
  "scale",
  "enterprise",
  "trial",
]);

export const subscriptionStatusEnum = pgEnum("subscription_status", [
  "active",
  "inactive",
  "trialing",
  "past_due",
  "cancelled",
]);

export const tenants = pgTable(
  "tenants",
  {
    id: text("id").primaryKey(),
    slug: text("slug").notNull().unique(),
    name: text("name").notNull(),
    plan: planEnum("plan").notNull().default("trial"),
    status: tenantStatusEnum("status").notNull().default("trial"),
    subscriptionStatus: subscriptionStatusEnum("subscription_status")
      .notNull()
      .default("inactive"),
    trialEndsAt: timestamp("trial_ends_at"),
    stripeCustomerId: text("stripe_customer_id"),
    stripeSubscriptionId: text("stripe_subscription_id"),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
  },
  (table) => [
    index("tenants_status_idx").on(table.status),
    index("tenants_subscription_status_idx").on(table.subscriptionStatus),
  ],
);
