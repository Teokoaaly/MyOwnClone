"""add embedding_outbox table for cross-store ingestion

Revision ID: d4e7f8a9b0c2
Revises: d4e7f8a9b0c1
Create Date: 2026-06-21 13:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'd4e7f8a9b0c2'
down_revision = 'd4e7f8a9b0c1'
branch_labels = None
depends_on = None


def upgrade():
    uuid_type = sa.String(36)

    op.create_table(
        "embedding_outbox",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", uuid_type, nullable=True),
        sa.Column("chunk_id", uuid_type, nullable=True),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("embedding", sa.JSON(), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=True, default=dict),
        sa.Column(
            "weaviate_class",
            sa.String(128),
            nullable=False,
            server_default=sa.text("'Chunk'"),
        ),
        sa.Column(
            "status",
            sa.String(16),
            nullable=False,
            server_default=sa.text("'pending'"),
        ),
        sa.Column(
            "attempts",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
        sa.Column("last_error", sa.Text(), nullable=True),
        sa.Column("next_retry_at", sa.DateTime(), nullable=True),
        sa.Column("synced_at", sa.DateTime(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_outbox_status_next_retry",
        "embedding_outbox",
        ["status", "next_retry_at"],
        unique=False,
    )
    op.create_index(
        "ix_outbox_tenant",
        "embedding_outbox",
        ["tenant_id"],
        unique=False,
    )


def downgrade():
    op.drop_index("ix_outbox_tenant", table_name="embedding_outbox")
    op.drop_index("ix_outbox_status_next_retry", table_name="embedding_outbox")
    op.drop_table("embedding_outbox")