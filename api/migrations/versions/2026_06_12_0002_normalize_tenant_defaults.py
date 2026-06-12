"""normalize tenant plan/status defaults

Revision ID: f6a7b8c9d0e1
Revises: b1c2d3e4f5a6
Create Date: 2026-06-12
"""

from alembic import op
import sqlalchemy as sa


revision = "f6a7b8c9d0e1"
down_revision = "b1c2d3e4f5a6"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "tenants",
        "plan",
        existing_type=sa.String(length=50),
        server_default=sa.text("'trial'"),
        existing_nullable=False,
    )
    op.alter_column(
        "tenants",
        "status",
        existing_type=sa.String(length=50),
        server_default=sa.text("'trial'"),
        existing_nullable=False,
    )


def downgrade():
    op.alter_column(
        "tenants",
        "plan",
        existing_type=sa.String(length=50),
        server_default=sa.text("'básico'"),
        existing_nullable=False,
    )
    op.alter_column(
        "tenants",
        "status",
        existing_type=sa.String(length=50),
        server_default=sa.text("'normal'"),
        existing_nullable=False,
    )
