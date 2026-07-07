"""add Sisyphus M10-M20 tables + ai_invocations cost columns

Revision ID: s1sy5phus_m10_m20
Revises: c3d4e5f6a7b8
Create Date: 2026-07-07 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 's1sy5phus_m10_m20'
down_revision = 'c3d4e5f6a7b8'
branch_labels = None
depends_on = None


def upgrade():
    uuid_type = sa.String(36)

    op.add_column("ai_invocations", sa.Column("cost_cents", sa.Integer(), nullable=False, server_default=sa.text("0")))
    op.add_column("ai_invocations", sa.Column("response_hash", sa.String(64), nullable=True))

    op.create_table("embedding_outbox",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("chunk_id", uuid_type, nullable=True),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("embedding", sa.JSON(), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=True),
        sa.Column("weaviate_class", sa.String(128), nullable=False, server_default=sa.text("'Chunk'")),
        sa.Column("status", sa.String(16), nullable=False, server_default=sa.text("'pending'")),
        sa.Column("attempts", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.Column("last_error", sa.Text(), nullable=True),
        sa.Column("next_retry_at", sa.DateTime(), nullable=True),
        sa.Column("synced_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index("ix_outbox_status_next_retry", "embedding_outbox", ["status", "next_retry_at"])
    op.create_index("ix_outbox_tenant", "embedding_outbox", ["tenant_id"])

    op.create_table("response_feedback",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("invocation_id", uuid_type, nullable=True),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("implicit_signal", sa.Integer(), nullable=True),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index("ix_response_feedback_tenant", "response_feedback", ["tenant_id"])
    op.create_index("ix_response_feedback_invocation", "response_feedback", ["invocation_id"])

    op.create_table("routing_log",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("task", sa.String(30), nullable=False),
        sa.Column("selected_model_id", uuid_type, nullable=True),
        sa.Column("fallback_used", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("route_reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index("ix_routing_log_tenant", "routing_log", ["tenant_id"])
    op.create_index("ix_routing_log_task", "routing_log", ["task"])

    op.create_table("moderation_log",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("content_hash", sa.String(64), nullable=False),
        sa.Column("flagged", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("categories", sa.JSON(), nullable=True),
        sa.Column("score", sa.Float(), nullable=True),
        sa.Column("action", sa.String(16), nullable=False, server_default=sa.text("'allow'")),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index("ix_moderation_log_tenant", "moderation_log", ["tenant_id"])
    op.create_index("ix_moderation_log_flagged", "moderation_log", ["flagged"])


def downgrade():
    op.drop_index("ix_moderation_log_flagged", table_name="moderation_log")
    op.drop_index("ix_moderation_log_tenant", table_name="moderation_log")
    op.drop_table("moderation_log")
    op.drop_index("ix_routing_log_task", table_name="routing_log")
    op.drop_index("ix_routing_log_tenant", table_name="routing_log")
    op.drop_table("routing_log")
    op.drop_index("ix_response_feedback_invocation", table_name="response_feedback")
    op.drop_index("ix_response_feedback_tenant", table_name="response_feedback")
    op.drop_table("response_feedback")
    op.drop_index("ix_outbox_tenant", table_name="embedding_outbox")
    op.drop_index("ix_outbox_status_next_retry", table_name="embedding_outbox")
    op.drop_table("embedding_outbox")
    op.drop_column("ai_invocations", "response_hash")
    op.drop_column("ai_invocations", "cost_cents")
