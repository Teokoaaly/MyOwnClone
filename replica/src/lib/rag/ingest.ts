import { encode } from "gpt-tokenizer";
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

interface ChunkResult {
  content: string;
  tokenCount: number;
  metadata: { position: number };
}

export function chunkText(
  text: string,
  maxTokens: number = 800,
  overlap: number = 100
): ChunkResult[] {
  const tokens = encode(text);
  const chunks: ChunkResult[] = [];
  let position = 0;

  for (let i = 0; i < tokens.length; i += maxTokens - overlap) {
    const chunkTokens = tokens.slice(i, i + maxTokens);
    const content = new TextDecoder().decode(
      new Uint8Array(chunkTokens.flatMap((t) => [t]))
    );
    chunks.push({
      content,
      tokenCount: chunkTokens.length,
      metadata: { position: position++ },
    });
  }

  return chunks;
}

export async function generateEmbeddings(
  chunks: string[]
): Promise<number[][]> {
  const embeddings: number[][] = [];

  for (let i = 0; i < chunks.length; i += 20) {
    const batch = chunks.slice(i, i + 20);
    const response = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: batch,
    });
    embeddings.push(...response.data.map((d) => d.embedding));
  }

  return embeddings;
}

export async function generateEmbedding(text: string): Promise<number[]> {
  const response = await openai.embeddings.create({
    model: "text-embedding-3-small",
    input: text,
  });
  return response.data[0].embedding;
}
