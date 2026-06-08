import {
  pgTable,
  text,
  timestamp,
  varchar,
  boolean,
  pgEnum,
  json,
} from "drizzle-orm/pg-core";
import { tenants } from "./tenants";

export const cloneModeEnum = pgEnum("clone_mode", [
  "pedagogy",
  "support",
  "sales",
]);

export const cloneConfigs = pgTable("clone_configs", {
  id: text("id").primaryKey(),
  tenantId: text("tenant_id")
    .notNull()
    .references(() => tenants.id, { onDelete: "cascade" }),
  name: varchar("name", { length: 255 }).notNull(),
  slug: varchar("slug", { length: 255 }).notNull().unique(),
  description: text("description"),
  avatarUrl: text("avatar_url"),
  personality: text("personality"),
  tone: varchar("tone", { length: 50 }),
  language: varchar("language", { length: 10 }).notNull().default("es"),
  customDomain: varchar("custom_domain", { length: 255 }),
  activeModes: json("active_modes"),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const cloneModePrompts = pgTable("clone_mode_prompts", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => cloneConfigs.id, { onDelete: "cascade" }),
  mode: cloneModeEnum("mode").notNull(),
  systemPrompt: text("system_prompt").notNull(),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

// Backward-compatible aliases
export const clones = cloneConfigs;
export const cloneModes = cloneModePrompts;
