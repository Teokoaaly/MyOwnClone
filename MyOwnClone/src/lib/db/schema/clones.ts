import {
  pgTable,
  text,
  timestamp,
  boolean,
  pgEnum,
  json,
  index,
} from "drizzle-orm/pg-core";
import { tenants } from "./tenants";

export const cloneModeEnum = pgEnum("clone_mode", [
  "pedagogy",
  "support",
  "sales",
]);

export const cloneConfigs = pgTable(
  "clone_configs",
  {
    id: text("id").primaryKey(),
    tenantId: text("tenant_id")
      .notNull()
      .references(() => tenants.id, { onDelete: "cascade" }),
    name: text("name").notNull(),
    slug: text("slug").notNull().unique(),
    description: text("description"),
    avatarUrl: text("avatar_url"),
    personalityTone: text("personality_tone"),
    language: text("language").notNull().default("es"),
    customDomain: text("custom_domain"),
    activeModes: json("active_modes"),
    isActive: boolean("is_active").notNull().default(true),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
  },
  (table) => [
    index("clone_configs_tenant_id_idx").on(table.tenantId),
    index("clone_configs_is_active_idx").on(table.isActive),
  ],
);

export const cloneModePrompts = pgTable(
  "clone_mode_prompts",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => cloneConfigs.id, { onDelete: "cascade" }),
    mode: cloneModeEnum("mode").notNull(),
    systemPrompt: text("system_prompt").notNull(),
    isActive: boolean("is_active").notNull().default(true),
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [
    index("clone_mode_prompts_clone_id_idx").on(table.cloneId),
  ],
);

// Backward-compatible aliases
export const clones = cloneConfigs;
export const cloneModes = cloneModePrompts;
