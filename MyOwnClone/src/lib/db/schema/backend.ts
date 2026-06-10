import {
  bigint,
  boolean,
  integer,
  pgEnum,
  pgTable,
  text,
  timestamp,
  index,
} from "drizzle-orm/pg-core";
import { cloneConfigs } from "./clones";
import { tenants } from "./tenants";
import { users } from "./users";

export const costCategoryEnum = pgEnum("cost_category", [
  "clone_response",
  "content_ingestion",
  "platform_ops",
]);

export const inboundEmailStatusEnum = pgEnum("inbound_email_status", [
  "pending",
  "sent",
  "discarded",
  "spam",
]);

export const cloneFeedbackRatingEnum = pgEnum("clone_feedback_rating", [
  "up",
  "down",
]);

export const myownclonePlans = pgTable("myownclone_plans", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  priceCents: integer("price_cents").notNull(),
  stripePriceId: text("stripe_price_id"),
  wordsTrainingLimit: bigint("words_training_limit", { mode: "number" })
    .notNull()
    .default(500000),
  responsesMonthLimit: integer("responses_month_limit").notNull().default(2000),
  modesActive: integer("modes_active").notNull().default(1),
  emailTriage: boolean("email_triage").notNull().default(false),
  booking: boolean("booking").notNull().default(false),
  apiAccess: boolean("api_access").notNull().default(false),
  multiClone: boolean("multi_clone").notNull().default(false),
  whitelabel: boolean("whitelabel").notNull().default(false),
});

export const emailInbound = pgTable(
  "email_inbound",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => cloneConfigs.id, { onDelete: "cascade" }),
    fromEmail: text("from_email"),
    fromName: text("from_name"),
    subject: text("subject"),
    bodyText: text("body_text"),
    bodyHtml: text("body_html"),
    draftReply: text("draft_reply"),
    status: inboundEmailStatusEnum("status").notNull().default("pending"),
    labels: text("labels").array(),
    classification: text("classification"),
    threadId: text("thread_id"),
    receivedAt: timestamp("received_at").notNull().defaultNow(),
    respondedAt: timestamp("responded_at"),
  },
  (table) => [
    index("email_inbound_clone_status_idx").on(table.cloneId, table.status),
  ],
);

export const emailTemplates = pgTable(
  "email_templates",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => cloneConfigs.id, { onDelete: "cascade" }),
    name: text("name").notNull(),
    subject: text("subject"),
    body: text("body"),
    triggerKeywords: text("trigger_keywords").array(),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
  },
  (table) => [
    index("email_templates_clone_id_idx").on(table.cloneId),
  ],
);

export const costTracking = pgTable(
  "cost_tracking",
  {
    id: text("id").primaryKey(),
    tenantId: text("tenant_id")
      .notNull()
      .references(() => tenants.id, { onDelete: "cascade" }),
    category: costCategoryEnum("category").notNull(),
    operation: text("operation"),
    model: text("model"),
    tokensIn: integer("tokens_in").notNull().default(0),
    tokensOut: integer("tokens_out").notNull().default(0),
    costCents: integer("cost_cents").notNull().default(0),
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [
    index("cost_tracking_tenant_category_ts_idx").on(
      table.tenantId,
      table.category,
      table.createdAt,
    ),
  ],
);

export const impersonationTokens = pgTable(
  "impersonation_tokens",
  {
    id: text("id").primaryKey(),
    token: text("token").notNull().unique(),
    adminId: text("admin_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    tenantId: text("tenant_id")
      .notNull()
      .references(() => tenants.id, { onDelete: "cascade" }),
    expiresAt: timestamp("expires_at").notNull(),
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [
    index("impersonation_tokens_admin_id_idx").on(table.adminId),
    index("impersonation_tokens_tenant_id_idx").on(table.tenantId),
  ],
);

export const cloneFeedback = pgTable(
  "clone_feedback",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => cloneConfigs.id, { onDelete: "cascade" }),
    conversationId: text("conversation_id"),
    messageId: text("message_id"),
    rating: cloneFeedbackRatingEnum("rating").notNull(),
    comment: text("comment"),
  },
  (table) => [
    index("clone_feedback_clone_id_idx").on(table.cloneId),
  ],
);
