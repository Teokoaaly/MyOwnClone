import {
  pgTable,
  text,
  timestamp,
  varchar,
  pgEnum,
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

export const tenants = pgTable("tenants", {
  id: text("id").primaryKey(),
  slug: varchar("slug", { length: 50 }).notNull().unique(),
  name: varchar("name", { length: 255 }).notNull(),
  plan: planEnum("plan").notNull().default("trial"),
  status: tenantStatusEnum("status").notNull().default("trial"),
  trialEndsAt: timestamp("trial_ends_at"),
  stripeCustomerId: text("stripe_customer_id"),
  stripeSubscriptionId: text("stripe_subscription_id"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});
