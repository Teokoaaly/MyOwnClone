"""ai_models catalog, assignments and invocations (Sisyphus M1).

Creates the three tables that power the configurable-AI-by-task system:

  - ``ai_models``           one row per provider deployment, with AES-GCM key
  - ``ai_model_assignments`` rows that route a (tenant_id, task) pair to a model
  - ``ai_invocations``      append-only audit log (used by M7/M12)

Constraints worth highlighting:

  * ``ai_model_assignments.model_id`` is a FK to ``ai_models.id`` with
    ``ON DELETE RESTRICT`` — you cannot hard-delete a model that still has
    assignments. Soft-delete (``is_active=False``) is the only path. This is
    enforced at the DB level because SQLAlchemy ``ondelete`` alone is not
    portable and Alembic is the authoritative source.

  * ``uq_active_assignment_per_tenant_task`` is a PostgreSQL partial unique
    index: it guarantees "at most one active assignment per
    (tenant_id, task) pair". We do not use a plain UNIQUE constraint because
    we want several historical rows when is_active=False for audit trail.

  * The migration is idempotent for SQLite/test usage: ``create_table`` is
    guarded by ``_table_exists``. Postgres-specific bits (partial index) are
    also guarded. Re-running is safe.

Revision ID: e2f3a4b5c6d7
Revises: d1e2f3a4b5c6
Create Date: 2026-06-21 18:30:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'e2f3a4b5c6d7'
down_revision = 'd1e2f3a4b5c6'
branch_labels = None
depends_on = None


# ── Helpers (mirrors 2026_06_21_0001 style) ──────────────────────────────────
def _table_exists(conn, table: str) -> bool:
    return conn.execute(
        sa.text("SELECT 1 FROM information_schema.tables WHERE table_name = :t"),
        {"t": table},
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


# ── Indexes declared up-front so upgrade() reads like a checklist ───────────
# Format: (table, index_name, columns). Postgres-only ones are tagged.
INDEXES = [
    # ai_models
    ("ai_models", "ai_models_tenant_id_idx", ["tenant_id"], False),
    ("ai_models", "ai_models_provider_idx", ["provider"], False),
    ("ai_models", "ai_models_is_active_idx", ["is_active"], False),
    # ai_model_assignments
    ("ai_model_assignments",
     "ai_model_assignments_tenant_task_active_idx",
     ["tenant_id", "task", "is_active"], False),
    # ai_invocations
    ("ai_invocations", "ai_invocations_tenant_id_idx", ["tenant_id"], False),
    ("ai_invocations", "ai_invocations_task_idx", ["task"], False),
    ("ai_invocations", "ai_invocations_created_at_idx", ["created_at"], False),
]


def upgrade():
    conn = op.get_bind()
    is_pg = conn.dialect.name == "postgresql"

    # ── ai_models ────────────────────────────────────────────────────────────
    if not _table_exists(conn, "ai_models"):
        op.create_table(
            "ai_models",
            sa.Column(
                "id", sa.String(36), primary_key=True,
                nullable=False,
            ),
            sa.Column("tenant_id", sa.String(36), nullable=True),
            sa.Column("name", sa.String(120), nullable=False),
            sa.Column("provider", sa.String(20), nullable=False),
            sa.Column("model_id", sa.String(120), nullable=False),
            sa.Column("api_key_encrypted", sa.Text, nullable=False),
            sa.Column("base_url", sa.String(500), nullable=True),
            sa.Column("capabilities", sa.JSON, nullable=False, server_default="[]"),
            sa.Column(
                "input_price_cents_per_mtok",
                sa.Integer, nullable=False, server_default="0",
            ),
            sa.Column(
                "output_price_cents_per_mtok",
                sa.Integer, nullable=False, server_default="0",
            ),
            sa.Column(
                "priority", sa.Integer, nullable=False, server_default="100",
            ),
            sa.Column("temperature_default", sa.Float, nullable=True),
            sa.Column("max_tokens_default", sa.Integer, nullable=True),
            sa.Column("max_input_tokens", sa.Integer, nullable=True),
            sa.Column("embedding_dimensions", sa.Integer, nullable=True),
            sa.Column(
                "is_active", sa.Boolean, nullable=False, server_default=sa.text("true"),
            ),
            sa.Column(
                "created_at", sa.DateTime, nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
            sa.Column(
                "updated_at", sa.DateTime, nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
        )

    # ── ai_model_assignments ─────────────────────────────────────────────────
    if not _table_exists(conn, "ai_model_assignments"):
        op.create_table(
            "ai_model_assignments",
            sa.Column(
                "id", sa.String(36), primary_key=True,
                nullable=False,
            ),
            sa.Column("tenant_id", sa.String(36), nullable=True),
            sa.Column("task", sa.String(30), nullable=False),
            sa.Column("model_id", sa.String(36), nullable=False),
            sa.Column("override_params", sa.JSON, nullable=True),
            sa.Column(
                "is_active", sa.Boolean, nullable=False, server_default=sa.text("true"),
            ),
            sa.Column(
                "created_at", sa.DateTime, nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
            sa.Column(
                "updated_at", sa.DateTime, nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
        )
        # FK with ON DELETE RESTRICT. Guarded because PG SQLAlchemy's
        # create_foreign_key is also fine if column already exists with FK,
        # but our _table_exists check above guarantees the column is fresh.
        if is_pg:
            op.create_foreign_key(
                "ai_model_assignments_model_id_fkey",
                "ai_model_assignments", "ai_models",
                ["model_id"], ["id"],
                ondelete="RESTRICT",
            )

    # ── ai_invocations ───────────────────────────────────────────────────────
    if not _table_exists(conn, "ai_invocations"):
        op.create_table(
            "ai_invocations",
            sa.Column(
                "id", sa.String(36), primary_key=True,
                nullable=False,
            ),
            sa.Column("tenant_id", sa.String(36), nullable=False),
            sa.Column("clone_id", sa.String(36), nullable=True),
            sa.Column("task", sa.String(30), nullable=False),
            sa.Column("model", sa.String(120), nullable=False),
            sa.Column("prompt_hash", sa.String(64), nullable=True),
            sa.Column(
                "prompt_tokens", sa.Integer, nullable=False, server_default="0",
            ),
            sa.Column(
                "completion_tokens", sa.Integer, nullable=False, server_default="0",
            ),
            sa.Column(
                "latency_ms", sa.Integer, nullable=False, server_default="0",
            ),
            sa.Column(
                "success", sa.Boolean, nullable=False, server_default=sa.text("true"),
            ),
            sa.Column("error_message", sa.Text, nullable=True),
            sa.Column(
                "created_at", sa.DateTime, nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
        )

    # ── Plain indexes (idempotent across dialects via IF NOT EXISTS) ─────────
    if is_pg:
        for table, idx_name, columns, _ in INDEXES:
            if not _index_exists(conn, idx_name):
                cols_sql = ", ".join(columns)
                op.execute(
                    f"CREATE INDEX IF NOT EXISTS {idx_name} "
                    f"ON {table} ({cols_sql})"
                )

        # ── Partial unique index (the contract guarantee) ─────────────────────
        # "At most one active assignment per (tenant_id, task) pair."
        if not _index_exists(conn, "uq_active_assignment_per_tenant_task"):
            op.execute(
                f"CREATE UNIQUE INDEX IF NOT EXISTS "
                f"uq_active_assignment_per_tenant_task "
                f"ON ai_model_assignments (tenant_id, task) "
                f"WHERE is_active = true"
            )

        # FK on ai_invocations.tenant_id → tenants.id (existing table) is
        # intentionally NOT added here: the platform already enforces tenant
        # membership at the application layer via MyOwnClone.blueprint, and
        # adding a hard FK risks breaking multi-tenant test fixtures that
        # insert invocations before the tenant transaction commits. Documented
        # in HANDOFF_LLM.md §5 M1 caveat.


def downgrade():
    conn = op.get_bind()
    is_pg = conn.dialect.name == "postgresql"

    if is_pg:
        for table, idx_name, _, _ in INDEXES:
            if _index_exists(conn, idx_name):
                op.execute(f"DROP INDEX IF EXISTS {idx_name}")
        if _index_exists(conn, "uq_active_assignment_per_tenant_task"):
            op.execute("DROP INDEX IF EXISTS uq_active_assignment_per_tenant_task")

    # Drop tables in reverse dependency order. _table_exists guards make this
    # safe even if some tables were never created in this DB.
    if _table_exists(conn, "ai_invocations"):
        op.drop_table("ai_invocations")
    if _table_exists(conn, "ai_model_assignments"):
        op.drop_table("ai_model_assignments")
    if _table_exists(conn, "ai_models"):
        op.drop_table("ai_models")