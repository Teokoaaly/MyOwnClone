"""Flask CLI command to re-embed all chunks using the active EmbeddingService.

Use after switching EMBEDDING_PROVIDER (e.g. lexical → openai) so that
existing chunks get real semantic vectors.

Usage:
    flask --app app_factory reindex                  # all tenants
    flask --app app_factory reindex --tenant <id>    # one tenant
    flask --app app_factory reindex --clone <id>     # one clone
    flask --app app_factory reindex --dry-run        # report only, no writes

⚠️ ALWAYS back up the database before running this in production:
    bash ops/backup_postgres.sh

The command is idempotent: re-running it just re-embeds the same chunks.
"""

import logging

import click
from sqlalchemy import select

from api.commands.seed import seed_demo_data  # noqa: F401 — re-exported for app.cli
from api.extensions.ext_database import db
from api.core.embeddings import EmbeddingService, EMBEDDING_DIMENSIONS
from api.core.chunking import chunk_text
from api.models.account import Tenant
from api.models.clone import CloneConfig
from api.models.knowledge import Chunk, Source

logger = logging.getLogger(__name__)


@click.command("reindex")
@click.option("--tenant", "tenant_id", default=None, help="Restrict to one tenant id")
@click.option("--clone", "clone_id", default=None, help="Restrict to one clone id")
@click.option("--dry-run", is_flag=True, default=False, help="Report counts without writing")
@click.option(
    "--rechunk", is_flag=True, default=False,
    help="Re-split source content into new chunks before embedding (slower, "
         "needed only if chunking parameters changed)",
)
def reindex_command(tenant_id: str | None, clone_id: str | None, dry_run: bool, rechunk: bool):
    """Re-embed all chunks with the active EmbeddingService."""
    click.echo(f"Active embedding provider: {EmbeddingService().provider}")
    click.echo(f"Active embedding model:   {EmbeddingService().model}")
    if dry_run:
        click.echo("DRY RUN: no writes will be performed.")

    # Build the source/chunk query.
    source_filters = [Source.status == "ready"]
    if clone_id:
        source_filters.append(Source.clone_id == clone_id)
    elif tenant_id:
        clone_ids_subq = (
            select(CloneConfig.id).where(CloneConfig.tenant_id == tenant_id)
        )
        source_filters.append(Source.clone_id.in_(clone_ids_subq))

    sources = db.session.execute(
        select(Source).where(*source_filters).order_by(Source.created_at)
    ).scalars().all()

    if not sources:
        click.echo("No 'ready' sources found. Nothing to reindex.")
        return

    click.echo(f"Found {len(sources)} source(s) to reindex.")
    if dry_run:
        return

    total_chunks = 0
    total_tokens = 0
    failures = 0

    for source in sources:
        # Resolve tenant_id for cost tracking.
        clone = db.session.execute(
            select(CloneConfig).where(CloneConfig.id == source.clone_id)
        ).scalar_one_or_none()
        tenant = clone.tenant_id if clone else tenant_id

        if rechunk:
            # Delete existing chunks and re-split from source text.
            # NOTE: source text is not stored as a column; the original content
            # lives only in the chunks. We concatenate existing chunk content
            # as a best-effort reconstruction. For sources ingested via the
            # new pipeline (FASE 2), the raw text is cached in metadata.
            existing_contents = [
                row[0]
                for row in db.session.execute(
                    select(Chunk.content)
                    .where(Chunk.source_id == source.id)
                    .order_by(Chunk.id)
                ).all()
            ]
            raw_text = "\n\n".join(c for c in existing_contents if c)
            if not raw_text.strip():
                click.echo(f"  ↳ source {source.id}: no text to rechunk, skipping")
                continue
            db.session.execute(
                Chunk.__table__.delete().where(Chunk.source_id == source.id)
            )
            new_chunks = chunk_text(raw_text)
            chunk_rows = [
                Chunk(
                    source_id=source.id,
                    content=txt,
                    chunk_metadata={
                        "position": idx,
                        "silo": (source.source_metadata or {}).get("silo", "teach"),
                    },
                )
                for idx, txt in enumerate(new_chunks)
            ]
            texts_to_embed = new_chunks
            chunk_objs = chunk_rows
        else:
            # Keep existing chunks; just refresh their embeddings.
            chunk_objs = list(
                db.session.execute(
                    select(Chunk).where(Chunk.source_id == source.id)
                ).scalars().all()
            )
            texts_to_embed = [c.content or "" for c in chunk_objs]

        if not texts_to_embed:
            click.echo(f"  ↳ source {source.id}: no chunks, skipping")
            continue

        try:
            embed_service = EmbeddingService(tenant_id=tenant)
            result = embed_service.embed_texts(texts_to_embed)

            if len(result.vectors) != len(chunk_objs):
                logger.error(
                    "Embedding count mismatch for source %s: %d vs %d chunks",
                    source.id, len(result.vectors), len(chunk_objs),
                )
                failures += 1
                continue

            for chunk_obj, vector in zip(chunk_objs, result.vectors):
                chunk_obj.embedding = vector

            if rechunk:
                db.session.add_all(chunk_objs)

            db.session.commit()
            total_chunks += len(chunk_objs)
            total_tokens += result.tokens_used
            click.echo(
                f"  ↳ source {source.id} ({source.title[:40]}): "
                f"{len(chunk_objs)} chunks via {result.provider}, "
                f"{result.tokens_used} tokens"
            )
        except Exception:
            db.session.rollback()
            failures += 1
            logger.exception("Failed to reindex source %s", source.id)

    click.echo("")
    click.echo(f"Done. Chunks re-embedded: {total_chunks}")
    click.echo(f"Embedding tokens used:    {total_tokens}")
    click.echo(f"Failures:                 {failures}")
    if total_tokens:
        from api.core.pricing import estimate_embedding_cost_cents
        cost = estimate_embedding_cost_cents(
            model=EmbeddingService().model, tokens=total_tokens
        )
        click.echo(f"Estimated cost:          ${cost / 100:.4f} USD")
