import {
  pgTable,
  text,
  timestamp,
  varchar,
  pgEnum,
} from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const emailStatusEnum = pgEnum("email_status", [
  "pending",
  "sent",
  "discarded",
]);

export const emails = pgTable("emails", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  fromEmail: varchar("from_email", { length: 255 }).notNull(),
  fromName: varchar("from_name", { length: 255 }),
  subject: text("subject").notNull(),
  body: text("body").notNull(),
  draftReply: text("draft_reply"),
  status: emailStatusEnum("status").notNull().default("pending"),
  threadId: text("thread_id"),
  receivedAt: timestamp("received_at").notNull().defaultNow(),
  sentAt: timestamp("sent_at"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
