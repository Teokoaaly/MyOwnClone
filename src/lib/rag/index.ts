// @deprecated — RAG is handled by the Dify backend (api/core/clonify/retrieval.py).
// This module is kept for reference only. Do not use in new code.
export { chunkText, generateEmbeddings, generateEmbedding } from "./ingest";
export { searchSimilar } from "./retrieve";
export { buildSystemPrompt, generateResponse, extractConfidence } from "./generate";
export { runPipeline } from "./pipeline";
