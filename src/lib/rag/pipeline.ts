// @ts-nocheck — deprecated module, RAG handled by Dify backend
import { generateEmbedding } from "./ingest";
import { searchSimilar } from "./retrieve";
import { buildSystemPrompt, generateResponse } from "./generate";
import { db, schema } from "@/lib/db";
import { eq, and } from "drizzle-orm";

function generateId(): string {
  return crypto.randomUUID();
}

interface PipelineParams {
  message: string;
  cloneId: string;
  conversationId?: string;
  visitorId?: string;
  mode?: string;
  history?: Array<{ role: "user" | "assistant"; content: string }>;
}

interface PipelineResult {
  content: string;
  confidence: number;
  sources: Array<{ chunkId: string; score: number }>;
  gapDetected: boolean;
  conversationId: string;
}

export async function runPipeline(params: PipelineParams): Promise<PipelineResult> {
  const clone = await db.query.clones.findFirst({
    where: eq(schema.clones.id, params.cloneId),
  });
  if (!clone) throw new Error("Clone not found");

  const cloneMode = await db.query.cloneModes.findFirst({
    where: and(
      eq(schema.cloneModes.cloneId, params.cloneId),
      eq(schema.cloneModes.mode, params.mode ?? "pedagogy")
    ),
  });

  const memories = await db.query.memories.findMany({
    where: eq(schema.memories.cloneId, params.cloneId),
  });

  const embedding = await generateEmbedding(params.message);
  const retrievedChunks = await searchSimilar(embedding, params.cloneId);

  const systemPrompt = buildSystemPrompt({
    cloneName: clone.name,
    personality: clone.personality,
    tone: clone.tone,
    systemPrompt: cloneMode?.systemPrompt ?? "Eres un asistente útil.",
    memories: memories.map((m) => ({ content: m.content })),
    mode: params.mode,
  });

  const { content, confidence } = await generateResponse({
    query: params.message,
    chunks: retrievedChunks.map((c) => c.content),
    systemPrompt,
    history: params.history,
  });

  const conversationId = params.conversationId;

  if (!conversationId) {
    const newConversationId = generateId();
    await db.insert(schema.conversations).values({
      id: newConversationId,
      cloneId: params.cloneId,
      visitorId: params.visitorId ?? null,
      mode: params.mode ?? "pedagogy",
    });
    params.conversationId = newConversationId;
  }

  const gapDetected = confidence < 0.7;

  if (gapDetected) {
    await db.insert(schema.analyticsGaps).values({
      id: generateId(),
      cloneId: params.cloneId,
      question: params.message,
      count: 1,
    });
  }

  return {
    content,
    confidence,
    sources: retrievedChunks.map((c) => ({ chunkId: c.id, score: c.score })),
    gapDetected,
    conversationId: params.conversationId!,
  };
}
