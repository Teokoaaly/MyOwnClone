"""add ai_models and ai_model_assignments catalog

Revision ID: d4e7f8a9b0c1
Revises: c3d4e6f7a8b9
Create Date: 2026-06-21 00:01:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'd4e7f8a9b0c1'
down_revision = 'c3d4e6f7a8b9'
branch_labels = None
depends_on = None


def upgrade():
    uuid_type = sa.String(36)

    # ─── ai_models ───────────────────────────────────────────────────────────
    op.create_table(
        "ai_models",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("provider", sa.String(50), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column(
            "model_type",
            sa.String(30),
            server_default=sa.text("'chat'"),
            nullable=False,
        ),
        sa.Column("capabilities", sa.JSON, nullable=True),
        sa.Column("config", sa.JSON, nullable=True),
        sa.Column(
            "input_cost_per_1k",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "output_cost_per_1k",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column("max_tokens", sa.Integer(), nullable=True),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(36), nullable=True),
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
    op.create_index("idx_ai_models_provider", "ai_models", ["provider"], unique=False)
    op.create_index("idx_ai_models_model_type", "ai_models", ["model_type"], unique=False)
    op.create_index("idx_ai_models_is_active", "ai_models", ["is_active"], unique=False)

    # ─── ai_model_assignments ──────────────────────────────────────────────
    op.create_table(
        "ai_model_assignments",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("tenant_id", sa.String(36), nullable=True),
        sa.Column(
            "model_id",
            uuid_type,
            sa.ForeignKey("ai_models.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("label", sa.String(100), nullable=True),
        sa.Column("task", sa.String(30), nullable=False),
        sa.Column(
            "priority",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(36), nullable=True),
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
    op.create_index("idx_ai_model_assignments_tenant", "ai_model_assignments", ["tenant_id"], unique=False)
    op.create_index("idx_ai_model_assignments_task", "ai_model_assignments", ["task"], unique=False)
    # Unique constraint: only one active assignment per tenant+task
    op.create_index(
        "idx_ai_model_assignments_tenant_task",
        "ai_model_assignments",
        ["tenant_id", "task"],
        unique=False,
    )


def downgrade():
    op.drop_index("idx_ai_model_assignments_tenant_task", table_name="ai_model_assignments")
    op.drop_index("idx_ai_model_assignments_task", table_name="ai_model_assignments")
    op.drop_index("idx_ai_model_assignments_tenant", table_name="ai_model_assignments")
    op.drop_table("ai_model_assignments")

    op.drop_index("idx_ai_models_is_active", table_name="ai_models")
    op.drop_index("idx_ai_models_model_type", table_name="ai_models")
    op.drop_index("idx_ai_models_provider", table_name="ai_models")
    op.drop_table("ai_models")
