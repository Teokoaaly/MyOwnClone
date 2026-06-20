"""align schema with drizzle: enums, indexes, and clone_mode_prompts.temperature

This migration reconciles the Alembic-owned schema with what the Drizzle
schema (MyOwnClone/src/lib/db/schema) already declares, closing the drift
documented in SCHEMA_OWNERSHIP.md. It also adds the temperature column
needed by FASE 3 of the standard RAG pipeline (per-mode LLM temperature).

Changes (all additive, idempotent):
  1. Create PG enums already declared by Drizzle but missing at the DB level:
       - clone_feedback_rating (up, down)
       - cost_category (clone_response, content_ingestion, platform_ops)
       - inbound_email_status (pending, sent, discarded, spam)
  2. Add missing indexes that Drizzle declares:
       - cost_tracking (tenant_id, category, created_at)
       - email_inbound (clone_id, status)
       - clone_configs (tenant_id), (is_active)
       - clone_mode_prompts (clone_id)
       - email_templates (clone_id)
       - impersonation_tokens (admin_id), (tenant_id)
       - clone_feedback (clone_id)
       - chunks (source_id), embedding ivfflat already exists from pgvector ext
  3. Add clone_mode_prompts.temperature NUMERIC(3,2) DEFAULT 0.30 NOT NULL
     (used by FASE 3 to let teach/support/sales have different creativity).

Safety:
  - Uses IF NOT EXISTS everywhere so re-running is safe.
  - Enums are only created; existing String columns are NOT converted
    automatically to avoid data loss. Existing rows keep their string values.
    A separate data migration can normalize values if needed.

Revision ID: d1e2f3a4b5c6
Revises: c3d4e5f6a7c1
Create Date: 2026-06-21 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'd1e2f3a4b5c6'
down_revision = 'c3d4e5f6a7c1'
branch_labels = None
depends_on = None


# ── Enums to ensure exist ────────────────────────────────────────────────────
ENUMS = [
    ("clone_feedback_rating", ["up", "down"]),
    ("cost_category", ["clone_response", "content_ingestion", "platform_ops"]),
    ("inbound_email_status", ["pending", "sent", "discarded", "spam"]),
]


# ── Indexes to ensure exist (table, index_name, column_expression) ──────────
# Using raw SQL with CREATE INDEX IF NOT EXISTS so we can express composite and
# expression indexes uniformly.
INDEXES = [
    ("cost_tracking", "cost_tracking_tenant_category_ts_idx",
     "(tenant_id, category, created_at)"),
    ("email_inbound", "email_inbound_clone_status_idx",
     "(clone_id, status)"),
    ("clone_configs", "clone_configs_tenant_id_idx", "(tenant_id)"),
    ("clone_configs", "clone_configs_is_active_idx", "(is_active)"),
    ("clone_mode_prompts", "clone_mode_prompts_clone_id_idx", "(clone_id)"),
    ("email_templates", "email_templates_clone_id_idx", "(clone_id)"),
    ("impersonation_tokens", "impersonation_tokens_admin_id_idx", "(admin_id)"),
    ("impersonation_tokens", "impersonation_tokens_tenant_id_idx", "(tenant_id)"),
    ("clone_feedback", "clone_feedback_clone_id_idx", "(clone_id)"),
    ("sources", "sources_clone_id_idx", "(clone_id)"),
    ("sources", "sources_status_idx", "(status)"),
    ("chunks", "chunks_source_id_idx", "(source_id)"),
]


def _enum_exists(conn, name: str) -> bool:
    return conn.execute(
        sa.text("SELECT 1 FROM pg_type WHERE typname = :n"),
        {"n": name},
    ).scalar() == 1


def _index_exists(conn, index_name: str) -> bool:
    return conn.execute(
        sa.text("SELECT 1 FROM pg_indexes WHERE indexname = :n"),
        {"n": index_name},
    ).scalar() == 1


def _column_exists(conn, table: str, column: str) -> bool:
    return conn.execute(
        sa.text(
            "SELECT 1 FROM information_schema.columns "
            "WHERE table_name = :t AND column_name = :c"
        ),
        {"t": table, "c": column},
    ).scalar() == 1


def upgrade():
    conn = op.get_bind()
    is_pg = conn.dialect.name == "postgresql"

    if not is_pg:
        # SQLite/test fallback: skip enum/index creation that needs PG syntax.
        # Only the temperature column (portable) is applied below.
        pass
    else:
        # 1. Enums
        for enum_name, values in ENUMS:
            if not _enum_exists(conn, enum_name):
                values_sql = ", ".join(f"'{v}'" for v in values)
                op.execute(f"CREATE TYPE {enum_name} AS ENUM ({values_sql})")

        # 2. Indexes (idempotent)
        for table, idx_name, expr in INDEXES:
            if not _index_exists(conn, idx_name):
                # IF NOT EXISTS is supported in PG 9.5+
                op.execute(
                    f"CREATE INDEX IF NOT EXISTS {idx_name} ON {table} {expr}"
                )

    # 3. clone_mode_prompts.temperature (portable across dialects)
    if not _column_exists(conn, "clone_mode_prompts", "temperature"):
        op.add_column(
            "clone_mode_prompts",
            sa.Column(
                "temperature",
                sa.Numeric(3, 2),
                server_default=sa.text("0.30"),
                nullable=False,
            ),
        )


def downgrade():
    conn = op.get_bind()

    if _column_exists(conn, "clone_mode_prompts", "temperature"):
        op.drop_column("clone_mode_prompts", "temperature")

    if conn.dialect.name == "postgresql":
        for table, idx_name, _ in INDEXES:
            if _index_exists(conn, idx_name):
                op.execute(f"DROP INDEX IF EXISTS {idx_name}")
        # We intentionally do NOT drop the enums: they may be referenced by
        # Drizzle-managed rows or future migrations. Dropping a PG enum that
        # is in use fails loudly, which is safer than a silent cascade.
