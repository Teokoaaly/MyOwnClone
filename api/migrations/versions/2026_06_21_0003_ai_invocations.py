"""add ai_invocations table and cost_daily_rollup materialized view

Revision ID: e5f8a9b0c1d2
Revises: d4e7f8a9b0c2
Create Date: 2026-06-21 15:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'e5f8a9b0c1d2'
down_revision = 'd4e7f8a9b0c2'
branch_labels = None
depends_on = None


def upgrade():
    uuid_type = sa.String(36)

    # ─── ai_invocations table ─────────────────────────────────────────────────
    op.create_table(
        "ai_invocations",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("model_id", uuid_type, nullable=True),
        sa.Column("task", sa.String(30), nullable=False),
        sa.Column("prompt_hash", sa.String(64), nullable=False),
        sa.Column("response_hash", sa.String(64), nullable=False),
        sa.Column(
            "tokens_in",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "tokens_out",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "cost_cents",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "latency_ms",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column(
            "success",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_ai_invocations_tenant",
        "ai_invocations",
        ["tenant_id"],
        unique=False,
    )
    op.create_index(
        "ix_ai_invocations_task",
        "ai_invocations",
        ["task"],
        unique=False,
    )
    op.create_index(
        "ix_ai_invocations_created",
        "ai_invocations",
        ["created_at"],
        unique=False,
    )

    # ─── cost_daily_rollup materialized view ───────────────────────────────────
    # Requires UNIQUE INDEX for CONCURRENTLY refresh
    op.execute("""
        CREATE MATERIALIZED VIEW IF NOT EXISTS cost_daily_rollup AS
        SELECT
            tenant_id,
            model_id,
            task,
            DATE(created_at) AS rollup_date,
            SUM(tokens_in) AS total_tokens_in,
            SUM(tokens_out) AS total_tokens_out,
            SUM(cost_cents) AS total_cost_cents,
            COUNT(*) AS invocation_count,
            AVG(latency_ms)::INTEGER AS avg_latency_ms,
            BOOL_AND(success) AS all_succeeded
        FROM ai_invocations
        WHERE created_at >= CURRENT_DATE - INTERVAL '90 days'
        GROUP BY
            tenant_id,
            model_id,
            task,
            DATE(created_at)
    """)

    # UNIQUE INDEX required for CONCURRENTLY refresh
    op.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS ix_cost_daily_rollup_concurrent
        ON cost_daily_rollup (tenant_id, model_id, task, rollup_date)
    """)


def downgrade():
    op.execute("DROP MATERIALIZED VIEW IF EXISTS cost_daily_rollup")
    op.drop_index("ix_ai_invocations_created", table_name="ai_invocations")
    op.drop_index("ix_ai_invocations_task", table_name="ai_invocations")
    op.drop_index("ix_ai_invocations_tenant", table_name="ai_invocations")
    op.drop_table("ai_invocations")
