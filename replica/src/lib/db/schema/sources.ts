import {
  pgTable,
  text,
  timestamp,
  varchar,
  pgEnum,
  json,
} from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const sourceTypeEnum = pgEnum("source_type", [
  "youtube",
  "pdf",
  "video",
  "text",
  "web",
  "interview",
]);

export const sourceStatusEnum = pgEnum("source_status", [
  "uploading",
  "processing",
  "ready",
  "error",
]);

export const sources = pgTable("sources", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  type: sourceTypeEnum("type").notNull(),
  title: varchar("title", { length: 500 }).notNull(),
  url: text("url"),
  status: sourceStatusEnum("status").notNull().default("uploading"),
  metadata: json("metadata").$type<Record<string, unknown>>(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});
