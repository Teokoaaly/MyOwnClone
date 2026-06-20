"""Text chunking for RAG ingestion.

Single canonical implementation shared by:
  - api/commands/reindex.py (--rechunk flag)
  - api/core/ingestion_pipeline.py (FASE 2)
  - (legacy) MyOwnClone/src/app/api/clone/sources/route.ts:chunkText

Parameters mirror the Next.js chunker so that chunks produced before the
backend pipeline existed remain compatible.

CHUNK_SIZE   = 1200 characters   (MAX_CHUNK_CHARS in route.ts)
CHUNK_OVERLAP = 160 characters   (CHUNK_OVERLAP_CHARS in route.ts)

The chunker prefers to cut at sentence or paragraph boundaries that fall
near the hard limit, to avoid splitting ideas mid-sentence.
"""

from __future__ import annotations

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 160


def chunk_text(
    text: str,
    *,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> list[str]:
    """Split `text` into overlapping chunks, preferring natural boundaries."""
    normalized = (
        text.replace("\r\n", "\n")
        .replace("\n{3,}", "\n\n")
        .strip()
    )
    if not normalized:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(normalized):
        end = min(start + chunk_size, len(normalized))

        if end < len(normalized):
            # Try to break at the latest sentence or paragraph near `end`.
            sentence_break = normalized.rfind(".", start + int(chunk_size * 0.55), end)
            paragraph_break = normalized.rfind("\n\n", start + int(chunk_size * 0.55), end)
            break_at = max(sentence_break, paragraph_break)
            if break_at > start:
                end = break_at + 1

        chunk = normalized[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(normalized):
            break
        # Move forward, leaving `overlap` characters of context.
        start = max(end - overlap, start + 1)

    return chunks


def count_words(text: str) -> int:
    return len([w for w in text.split() if w])
