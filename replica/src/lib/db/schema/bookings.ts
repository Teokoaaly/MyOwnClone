import {
  pgTable,
  text,
  timestamp,
  varchar,
  integer,
  boolean,
  pgEnum,
} from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const bookingStatusEnum = pgEnum("booking_status", [
  "confirmed",
  "cancelled",
  "completed",
  "no_show",
]);

export const meetingTypes = pgTable("meeting_types", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  name: varchar("name", { length: 255 }).notNull(),
  duration: integer("duration").notNull(), // minutes
  price: integer("price").notNull().default(0), // cents
  description: text("description"),
  color: varchar("color", { length: 7 }), // hex color
  active: boolean("active").notNull().default(true),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export const availability = pgTable("availability", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id")
    .notNull()
    .references(() => clones.id, { onDelete: "cascade" }),
  dayOfWeek: integer("day_of_week").notNull(), // 0=Sunday, 1=Monday, ...
  startTime: varchar("start_time", { length: 5 }).notNull(), // "HH:MM"
  endTime: varchar("end_time", { length: 5 }).notNull(), // "HH:MM"
});

export const bookings = pgTable("bookings", {
  id: text("id").primaryKey(),
  meetingTypeId: text("meeting_type_id")
    .notNull()
    .references(() => meetingTypes.id, { onDelete: "cascade" }),
  visitorName: varchar("visitor_name", { length: 255 }).notNull(),
  visitorEmail: varchar("visitor_email", { length: 255 }).notNull(),
  date: varchar("date", { length: 10 }).notNull(), // "YYYY-MM-DD"
  time: varchar("time", { length: 5 }).notNull(), // "HH:MM"
  status: bookingStatusEnum("status").notNull().default("confirmed"),
  meetingUrl: text("meeting_url"),
  notes: text("notes"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
