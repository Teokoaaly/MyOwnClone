"""add audit_log table

Revision ID: 2026_07_14_0002
Revises: 2026_07_14_0001
Create Date: 2026-07-14

P1.2 (auditoria 2026-07-13, C-16): the audit_log table was previously
created via runtime DDL in ``api.middleware.audit_trail._ensure_table``,
which had a race condition on cold start (multiple workers checking at
once) and bypassed Alembic migrations.

This migration creates the table via the proper Alembic path. The
runtime DDL call is removed in the same audit block; the existing
``log_audit_action`` function is now wired into the state-changing
endpoints (admin platform operations).
"""
from alembic import op
import sqlalchemy as sa


revision = "2026_07_14_0002"
down_revision = "2026_07_14_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "audit_log",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "timestamp",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.current_timestamp(),
        ),
        sa.Column("user_id", sa.String(36), nullable=True),
        sa.Column("tenant_id", sa.String(36), nullable=True),
        sa.Column("action", sa.String(100), nullable=False),
        sa.Column("resource_type", sa.String(50), nullable=True),
        sa.Column("resource_id", sa.String(36), nullable=True),
        sa.Column("details", sa.JSON, nullable=True),
        sa.Column("ip_address", sa.String(45), nullable=True),
        sa.Column("user_agent", sa.String(255), nullable=True),
    )
    op.create_index(
        "ix_audit_log_user_id",
        "audit_log",
        ["user_id"],
    )
    op.create_index(
        "ix_audit_log_tenant_id",
        "audit_log",
        ["tenant_id"],
    )
    op.create_index(
        "ix_audit_log_action",
        "audit_log",
        ["action"],
    )
    op.create_index(
        "ix_audit_log_timestamp",
        "audit_log",
        ["timestamp"],
    )


def downgrade() -> None:
    op.drop_index("ix_audit_log_timestamp", table_name="audit_log")
    op.drop_index("ix_audit_log_action", table_name="audit_log")
    op.drop_index("ix_audit_log_tenant_id", table_name="audit_log")
    op.drop_index("ix_audit_log_user_id", table_name="audit_log")
    op.drop_table("audit_log")
