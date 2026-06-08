import {
  pgTable,
  text,
  timestamp,
  varchar,
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
  visitorId: varchar("visitor_id", { length: 255 }),
  mode: conversationModeEnum("mode").notNull().default("pedagogy"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const messages = pgTable("messages", {
  id: text("id").primaryKey(),
  conversationId: text("conversation_id")
    .notNull()
    .references(() => conversations.id, { onDelete: "cascade" }),
  role: varchar("role", { length: 20 }).notNull(),
  content: text("content").notNull(),
  confidence: text("confidence"), // stored as string for decimal precision
  sources: json("sources").$type<Array<{ chunkId: string; score: number }>>(),
  feedback: varchar("feedback", { length: 10 }), // "up", "down", null
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
