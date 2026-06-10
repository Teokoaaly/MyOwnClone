import {
  pgTable,
  text,
  timestamp,
  integer,
  boolean,
  pgEnum,
  index,
} from "drizzle-orm/pg-core";
import { clones } from "./clones";

export const bookingStatusEnum = pgEnum("booking_status", [
  "confirmed",
  "cancelled",
  "completed",
  "no_show",
]);

export const meetingTypes = pgTable(
  "meeting_types",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => clones.id, { onDelete: "cascade" }),
    name: text("name").notNull(),
    durationMinutes: integer("duration_minutes").notNull().default(30), // minutes
    priceCents: integer("price_cents").notNull().default(0), // cents
    description: text("description"),
    color: text("color"), // hex color
    active: boolean("active").notNull().default(true),
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [
    index("meeting_types_clone_id_idx").on(table.cloneId),
    index("meeting_types_active_idx").on(table.active),
  ],
);

export const availability = pgTable(
  "availability",
  {
    id: text("id").primaryKey(),
    cloneId: text("clone_id")
      .notNull()
      .references(() => clones.id, { onDelete: "cascade" }),
    dayOfWeek: integer("day_of_week").notNull(), // 0=Sunday, 1=Monday, ...
    startTime: text("start_time").notNull(), // "HH:MM"
    endTime: text("end_time").notNull(), // "HH:MM"
  },
  (table) => [
    index("availability_clone_id_idx").on(table.cloneId),
    index("availability_clone_day_idx").on(table.cloneId, table.dayOfWeek),
  ],
);

export const bookings = pgTable(
  "bookings",
  {
    id: text("id").primaryKey(),
    meetingTypeId: text("meeting_type_id")
      .notNull()
      .references(() => meetingTypes.id, { onDelete: "cascade" }),
    visitorName: text("visitor_name").notNull(),
    visitorEmail: text("visitor_email").notNull(),
    date: text("date").notNull(), // "YYYY-MM-DD"
    startTime: text("start_time").notNull(), // "HH:MM"
    endTime: text("end_time"), // "HH:MM"
    status: bookingStatusEnum("status").notNull().default("confirmed"),
    meetingUrl: text("meeting_url"),
    notes: text("notes"),
    createdAt: timestamp("created_at").notNull().defaultNow(),
  },
  (table) => [
    index("bookings_meeting_type_id_idx").on(table.meetingTypeId),
    index("bookings_meeting_date_idx").on(table.meetingTypeId, table.date),
    index("bookings_status_idx").on(table.status),
  ],
);
