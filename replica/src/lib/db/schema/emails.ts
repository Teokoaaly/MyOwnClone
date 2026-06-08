import {
  pgTable,
  text,
  timestamp,
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
  fromEmail: text("from_email").notNull(),
  fromName: text("from_name"),
  subject: text("subject").notNull(),
  body: text("body").notNull(),
  draftReply: text("draft_reply"),
  status: emailStatusEnum("status").notNull().default("pending"),
  threadId: text("thread_id"),
  receivedAt: timestamp("received_at").notNull().defaultNow(),
  sentAt: timestamp("sent_at"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
