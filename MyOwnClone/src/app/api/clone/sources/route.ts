import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { NextResponse, NextRequest } from "next/server";
import { auth } from "@/lib/auth";

const MAX_CHUNK_CHARS = 1200;
const CHUNK_OVERLAP_CHARS = 160;
const EMBEDDING_DIMENSIONS = 1536;
const STOPWORDS = new Set([
  "the", "and", "for", "from", "about", "with", "that", "this", "you",
  "que", "con", "para", "por", "del", "las", "los", "una", "uno", "como",
  "este", "esta", "sobre", "sus",
]);

/**
 * Resolve the active clone ID from cookie or env var fallback.
 */
function getCloneIdFromRequest(request: NextRequest): string | null {
  const cookieCloneId = request.cookies.get("moc_active_clone_id")?.value;
  if (cookieCloneId) return cookieCloneId;
  return process.env.DEFAULT_CLONE_ID || null;
}

function countWords(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

function tokenize(text: string): string[] {
  const matches = text.toLowerCase().match(/[\p{L}\p{N}_]{3,}/gu) ?? [];
  return matches.filter((term) => !STOPWORDS.has(term));
}

function hashTerm(term: string): number {
  let hash = 2166136261;
  for (let i = 0; i < term.length; i += 1) {
    hash ^= term.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function lexicalEmbedding(text: string): number[] {
  const vector = Array.from({ length: EMBEDDING_DIMENSIONS }, () => 0);
  const terms = tokenize(text);
  for (const term of terms) {
    const hash = hashTerm(term);
    const index = hash % EMBEDDING_DIMENSIONS;
    const sign = hash % 2 === 0 ? 1 : -1;
    vector[index] += sign;
  }

  const norm = Math.sqrt(vector.reduce((sum, value) => sum + value * value, 0));
  if (norm === 0) return vector;
  return vector.map((value) => value / norm);
}

function chunkText(text: string): string[] {
  const normalized = text.replace(/\r\n/g, "\n").replace(/\n{3,}/g, "\n\n").trim();
  if (!normalized) return [];

  const chunks: string[] = [];
  let start = 0;
  while (start < normalized.length) {
    let end = Math.min(start + MAX_CHUNK_CHARS, normalized.length);
    if (end < normalized.length) {
      const sentenceBreak = normalized.lastIndexOf(".", end);
      const paragraphBreak = normalized.lastIndexOf("\n\n", end);
      const breakAt = Math.max(sentenceBreak, paragraphBreak);
      if (breakAt > start + MAX_CHUNK_CHARS * 0.55) {
        end = breakAt + 1;
      }
    }

    const chunk = normalized.slice(start, end).trim();
    if (chunk) chunks.push(chunk);

    if (end >= normalized.length) break;
    start = Math.max(end - CHUNK_OVERLAP_CHARS, start + 1);
  }

  return chunks;
}

export async function GET(request: NextRequest) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = getCloneIdFromRequest(request);
  if (!cloneId) {
    return NextResponse.json(
      { error: "No clone configured. Create a clone first." },
      { status: 404 }
    );
  }

  try {
    const items = await db
      .select()
      .from(schema.sources)
      .where(eq(schema.sources.cloneId, cloneId));

    // Format the records so they match the UI contract.
    const formatted = items.map((item) => ({
      id: item.id,
      title: item.title,
      type: item.type,
      status: item.status,
      silo: (item.metadata as any)?.silo || "teach",
      wordCount: (item.metadata as any)?.wordCount || 0,
      createdAt: item.createdAt.toISOString(),
    }));

    return NextResponse.json(formatted);
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = getCloneIdFromRequest(request);
  if (!cloneId) {
    return NextResponse.json(
      { error: "No clone configured. Create a clone first." },
      { status: 404 }
    );
  }

  try {
    const formData = await request.formData();
    const silo = (formData.get("silo") as string) || "teach";
    const type = (formData.get("type") as string) || "text";
    const content = (formData.get("content") as string) || "";
    const url = (formData.get("url") as string) || "";
    const file = formData.get("file") as File | null;

    if (!["teach", "support", "sales"].includes(silo)) {
      return NextResponse.json({ error: "Invalid content silo." }, { status: 400 });
    }

    if (!["pdf", "youtube", "text", "web", "interview"].includes(type)) {
      return NextResponse.json({ error: "Invalid content type." }, { status: 400 });
    }

    if (type === "text" && !content.trim()) {
      return NextResponse.json(
        { error: "Paste or write content before submitting." },
        { status: 400 }
      );
    }

    if ((type === "youtube" || type === "web") && !url.trim()) {
      return NextResponse.json(
        { error: "Add a URL before submitting this source." },
        { status: 400 }
      );
    }

    if (type === "pdf" && !file) {
      return NextResponse.json(
        { error: "Choose a file before submitting this source." },
        { status: 400 }
      );
    }

    if (type === "interview") {
      return NextResponse.json(
        { error: "AI interview is not available yet." },
        { status: 400 }
      );
    }

    const ingestableContent = type === "text" ? content.trim() : "";
    const chunks = chunkText(ingestableContent);
    if (type === "text" && chunks.length === 0) {
      return NextResponse.json(
        { error: "Content is too short to index." },
        { status: 400 }
      );
    }

    let title = "New content";
    if (type === "text") {
      title = content.substring(0, 30) || "Text content";
    } else if (type === "youtube" || type === "web") {
      title = url || "Web link";
    } else if (type === "pdf" && file) {
      title = file.name;
    }

    const newSource = {
      id: crypto.randomUUID(),
      cloneId,
      type: type as any,
      title,
      url: url || null,
      status: (type === "text" ? "ready" : "processing") as any,
      metadata: {
        silo,
        wordCount: countWords(ingestableContent),
        chunkCount: chunks.length,
        ingestion: type === "text" ? "local_lexical_v1" : "pending_external_ingestion",
      },
    };

    await db.insert(schema.sources).values(newSource);
    if (chunks.length > 0) {
      await db.insert(schema.chunks).values(
        chunks.map((chunk, index) => ({
          id: crypto.randomUUID(),
          sourceId: newSource.id,
          content: chunk,
          embedding: lexicalEmbedding(chunk),
          tokenCount: countWords(chunk),
          metadata: {
            position: index,
            silo,
          },
        }))
      );
    }

    return NextResponse.json({ success: true, source: newSource });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
