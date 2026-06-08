# ⚠️ DEPRECATED — RAG Module

**This module is deprecated. All RAG logic has been moved to the backend.**

## Why

The RAG (Retrieval-Augmented Generation) pipeline was originally implemented in the frontend for experimentation. It has been fully migrated to the backend API where it belongs, leveraging the base platform's `RetrievalService`.

## What's Here

This directory previously contained:
- `pipeline.ts` — Full RAG pipeline (marked `@ts-nocheck`)
- `retrieve.ts` — Vector similarity search
- `ingest.ts` — Chunking + embeddings  
- `generate.ts` — Anthropic response generation
- `index.ts` — Re-exports for all modules

## Migration

All functionality is now handled by the backend at `/console/api/myownclone/...` endpoints. The frontend should use the API routes under `/api/clone/` instead of calling these modules directly.

## Action Required

- Do NOT use `lib/rag/*` in new code
- Existing imports should be migrated to call `/api/clone/[...path]` routes
- This module will be removed in a future version

## Date Deprecated
2026-06-03
