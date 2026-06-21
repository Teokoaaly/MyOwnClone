"""add response_feedback table and model_quality_scores view

Revision ID: f6a9b0c1d2e
Revises: e5f8a9b0c1d2
Create Date: 2026-06-21 16:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'f6a9b0c1d2e'
down_revision = 'e5f8a9b0c1d2'
branch_labels = None
depends_on = None


def upgrade():
    uuid_type = sa.String(36)

    # ─── response_feedback table ───────────────────────────────────────────────
    op.create_table(
        "response_feedback",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column(
            "invocation_id",
            uuid_type,
            nullable=True,
            # FK is optional, will be added after ai_invocations exists
        ),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("implicit_signal", sa.Integer(), nullable=True),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_response_feedback_tenant",
        "response_feedback",
        ["tenant_id"],
        unique=False,
    )
    op.create_index(
        "ix_response_feedback_invocation",
        "response_feedback",
        ["invocation_id"],
        unique=False,
    )

    # ─── model_quality_scores view ────────────────────────────────────────────
    # Refreshed every 5 minutes via cron or scheduled task
    # Used by SmartRouter (M15) for quality-based routing
    op.execute("""
        CREATE MATERIALIZED VIEW IF NOT EXISTS model_quality_scores AS
        SELECT
            ai.model_id,
            COUNT(*) AS feedback_count,
            AVG(CASE WHEN rf.rating > 0 THEN 1.0 ELSE 0.0 END) AS avg_quality_score,
            MIN(rf.created_at) AS first_feedback_at,
            MAX(rf.created_at) AS last_feedback_at
        FROM response_feedback rf
        JOIN ai_invocations ai ON ai.id = rf.invocation_id
        WHERE rf.created_at >= CURRENT_DATE - INTERVAL '30 days'
        GROUP BY ai.model_id
    """)

    # UNIQUE INDEX for CONCURRENTLY refresh
    op.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS ix_model_quality_scores_concurrent
        ON model_quality_scores (model_id)
    """)


def downgrade():
    op.execute("DROP MATERIALIZED VIEW IF EXISTS model_quality_scores")
    op.drop_index("ix_response_feedback_invocation", table_name="response_feedback")
    op.drop_index("ix_response_feedback_tenant", table_name="response_feedback")
    op.drop_table("response_feedback")
