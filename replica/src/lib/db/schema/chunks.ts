import { pgTable, text, integer, json, index } from "drizzle-orm/pg-core";
import { sources } from "./sources";
import { customType } from "drizzle-orm/pg-core";

export const vector = customType<{ data: number[]; notNull: true }>({
  dataType() {
    return "vector(1536)";
  },
});

export const chunks = pgTable(
  "chunks",
  {
    id: text("id").primaryKey(),
    sourceId: text("source_id")
      .notNull()
      .references(() => sources.id, { onDelete: "cascade" }),
    content: text("content").notNull(),
    embedding: vector("embedding").notNull(),
    tokenCount: integer("token_count"),
    metadata: json("metadata").$type<{
      position?: number;
      page?: number;
      timestamp?: string;
    }>(),
  },
  (table) => [
    index("chunks_embedding_idx").using(
      "ivfflat",
      table.embedding.asc().nullsLast()
    ),
  ]
);
