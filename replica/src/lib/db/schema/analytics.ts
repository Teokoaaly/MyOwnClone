import { pgTable, text, integer, timestamp, pgEnum, boolean } from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const memoryTypeEnum = pgEnum("memory_type", [
  "memory",
  "signature",
  "template",
]);

export const productStatusEnum = pgEnum("product_status", [
  "active",
  "inactive",
]);

export const memories = pgTable("memories", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  type: memoryTypeEnum("type").notNull().default("memory"),
  title: text("title").notNull(),
  content: text("content").notNull(),
  triggerCondition: text("trigger_condition"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const analyticsQuestions = pgTable("analytics_questions", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  question: text("question").notNull(),
  count: integer("count").notNull().default(1),
  lastAskedAt: timestamp("last_asked_at").notNull().defaultNow(),
});

export const analyticsGaps = pgTable("analytics_gaps", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  question: text("question").notNull(),
  count: integer("count").notNull().default(1),
  suggestedSource: text("suggested_source"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const products = pgTable("products", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  name: text("name").notNull(),
  description: text("description"),
  price: integer("price"),
  url: text("url"),
  imageUrl: text("image_url"),
  active: productStatusEnum("status").notNull().default("active"),
  priority: integer("priority").notNull().default(0),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const impersonationLogs = pgTable("impersonation_logs", {
  id: text("id").primaryKey(),
  adminId: text("admin_id").notNull(),
  tenantId: text("tenant_id").notNull(),
  reason: text("reason").notNull(),
  startedAt: timestamp("started_at").notNull().defaultNow(),
  endedAt: timestamp("ended_at"),
});
