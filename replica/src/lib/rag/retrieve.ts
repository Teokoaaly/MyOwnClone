import { sql } from "drizzle-orm";
import { db, schema } from "@/lib/db";

interface RetrievedChunk {
  id: string;
  content: string;
  score: number;
  sourceId: string;
  metadata: Record<string, unknown> | null;
}

export async function searchSimilar(
  embedding: number[],
  cloneId: string,
  topK: number = 5,
  similarityThreshold: number = 0.75
): Promise<RetrievedChunk[]> {
  const formattedEmbedding = `[${embedding.join(",")}]`;

  const results = await db.execute<{
    id: string;
    content: string;
    score: number;
    source_id: string;
    metadata: Record<string, unknown> | null;
  }>(sql`
    SELECT
      c.id,
      c.content,
      1 - (c.embedding <=> ${formattedEmbedding}::vector) AS score,
      c.source_id,
      c.metadata
    FROM ${schema.chunks} c
    JOIN ${schema.sources} s ON s.id = c.source_id
    WHERE s.clone_id = ${cloneId}
      AND 1 - (c.embedding <=> ${formattedEmbedding}::vector) > ${similarityThreshold}
    ORDER BY c.embedding <=> ${formattedEmbedding}::vector
    LIMIT ${topK}
  `);

  return results.rows.map((r) => ({
    id: r.id,
    content: r.content,
    score: Number(r.score),
    sourceId: r.source_id,
    metadata: r.metadata,
  }));
}
