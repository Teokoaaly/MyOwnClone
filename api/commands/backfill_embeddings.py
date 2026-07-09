"""Backfill embeddings for chunks that don't have them.

Run on VPS:
    cd /opt/myownclone/releases/20260703190910-landing-cleanup-restore
    python3 -c "from api.commands.backfill_embeddings import run; run()"
"""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def run() -> None:
    """Find all chunks without embeddings and generate them."""
    import os
    os.environ.setdefault("FLASK_APP", "api.app_factory")

    from api.app_factory import create_app
    app = create_app()

    with app.app_context():
        from sqlalchemy import select, func
        from api.extensions.ext_database import db
        from api.models.knowledge import Chunk

        total = db.session.execute(select(func.count(Chunk.id))).scalar() or 0
        with_emb = db.session.execute(
            select(func.count(Chunk.id)).where(Chunk.embedding.isnot(None))
        ).scalar() or 0
        pending = total - with_emb

        print(f"Chunks: {total} total, {with_emb} with embedding, {pending} pending")

        if pending == 0:
            print("All chunks already have embeddings. Nothing to do.")
            return

        # Get chunks without embeddings
        chunks = db.session.execute(
            select(Chunk).where(Chunk.embedding.is_(None))
        ).scalars().all()

        print(f"Found {len(chunks)} chunks to embed")

        from api.core.embeddings import EmbeddingService
        embedder = EmbeddingService()

        embedded = 0
        failed = 0
        for chunk in chunks:
            try:
                text = chunk.content or ""
                if not text.strip():
                    print(f"  Skipping chunk {chunk.id}: empty content")
                    failed += 1
                    continue

                vectors = embedder.embed_texts([text])
                if vectors and vectors[0]:
                    chunk.embedding = vectors[0]
                    db.session.commit()
                    embedded += 1
                    print(f"  Embedded chunk {chunk.id}: {len(text)} chars -> {len(vectors[0])}d")
                else:
                    print(f"  Failed chunk {chunk.id}: empty vector")
                    failed += 1
            except Exception as exc:
                db.session.rollback()
                print(f"  Error chunk {chunk.id}: {exc}")
                failed += 1

        print(f"\nDone: {embedded} embedded, {failed} failed")

        # Verify
        new_with_emb = db.session.execute(
            select(func.count(Chunk.id)).where(Chunk.embedding.isnot(None))
        ).scalar() or 0
        print(f"Final: {new_with_emb}/{total} chunks with embeddings")


if __name__ == "__main__":
    run()
