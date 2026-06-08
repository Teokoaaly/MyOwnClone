import {
  pgTable,
  text,
  timestamp,
  pgEnum,
  json,
} from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const conversationModeEnum = pgEnum("conversation_mode", [
  "pedagogy",
  "sales",
  "support",
]);

export const conversations = pgTable("conversations", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  visitorId: text("visitor_id"),
  mode: conversationModeEnum("mode").notNull().default("pedagogy"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const messages = pgTable("messages", {
  id: text("id").primaryKey(),
  conversationId: text("conversation_id")
    .notNull()
    .references(() => conversations.id, { onDelete: "cascade" }),
  role: text("role").notNull(),
  content: text("content").notNull(),
  confidence: text("confidence"), // stored as string for decimal precision
  sources: json("sources").$type<Array<{ chunkId: string; score: number }>>(),
  feedback: text("feedback"), // "up", "down", null
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
