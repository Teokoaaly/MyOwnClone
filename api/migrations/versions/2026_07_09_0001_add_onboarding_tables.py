"""Add onboarding_status to accounts + onboarding_steps table.

Revision ID: 0001_onboarding
Revises: 2026_06_27_0001
Create Date: 2026-07-09
"""
from alembic import op
import sqlalchemy as sa

revision = "2026_07_09_0001_onboarding"
down_revision = "2026_06_27_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add onboarding_status to accounts
    op.add_column(
        "accounts",
        sa.Column(
            "onboarding_status",
            sa.String(30),
            server_default="not_started",
            nullable=False,
        ),
    )
    op.create_index(
        "ix_accounts_onboarding_status",
        "accounts",
        ["onboarding_status"],
    )

    # Create onboarding_steps table
    op.create_table(
        "onboarding_steps",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("account_id", sa.String(36), nullable=False, index=True),
        sa.Column("tour_id", sa.String(50), nullable=False, index=True),
        sa.Column("step_key", sa.String(50), nullable=False),
        sa.Column("completed_at", sa.DateTime, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.UniqueConstraint("account_id", "tour_id", "step_key", name="uq_onboarding_step"),
    )

    # Create onboarding_events table
    op.create_table(
        "onboarding_events",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("account_id", sa.String(36), nullable=False, index=True),
        sa.Column("event", sa.String(50), nullable=False, index=True),
        sa.Column("tour_id", sa.String(50), nullable=True),
        sa.Column("step_key", sa.String(50), nullable=True),
        sa.Column("properties", sa.JSON, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table("onboarding_events")
    op.drop_table("onboarding_steps")
    op.drop_index("ix_accounts_onboarding_status")
    op.drop_column("accounts", "onboarding_status")
