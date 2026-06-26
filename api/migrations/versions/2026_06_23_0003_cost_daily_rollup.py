"""add cost_daily_rollup for AI runtime reporting

Revision ID: f3a4b5c6d7e8
Revises: e2f3a4b5c6d7
Create Date: 2026-06-23 11:50:00.000000
"""

from alembic import op
import sqlalchemy as sa


revision = "f3a4b5c6d7e8"
down_revision = "e2f3a4b5c6d7"
branch_labels = None
depends_on = None


def _table_exists(conn, table: str) -> bool:
    if conn.dialect.name == "sqlite":
        return conn.execute(
            sa.text("SELECT 1 FROM sqlite_master WHERE type='table' AND name = :t"),
            {"t": table},
        ).scalar() == 1
    return conn.execute(
        sa.text("SELECT 1 FROM information_schema.tables WHERE table_name = :t"),
        {"t": table},
    ).scalar() == 1


def upgrade():
    conn = op.get_bind()
    if _table_exists(conn, "cost_daily_rollup"):
        return

    op.create_table(
        "cost_daily_rollup",
        sa.Column("id", sa.String(36), primary_key=True, nullable=False),
        sa.Column("tenant_id", sa.String(36), nullable=False),
        sa.Column("day", sa.Date, nullable=False),
        sa.Column("task", sa.String(30), nullable=False),
        sa.Column("model", sa.String(120), nullable=False),
        sa.Column("invocations", sa.Integer, nullable=False, server_default="0"),
        sa.Column("prompt_tokens", sa.Integer, nullable=False, server_default="0"),
        sa.Column("completion_tokens", sa.Integer, nullable=False, server_default="0"),
        sa.Column("success_count", sa.Integer, nullable=False, server_default="0"),
        sa.Column("error_count", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
    )
    op.create_index("cost_daily_rollup_tenant_day_idx", "cost_daily_rollup", ["tenant_id", "day"])
    op.create_index("cost_daily_rollup_task_idx", "cost_daily_rollup", ["task"])


def downgrade():
    conn = op.get_bind()
    if not _table_exists(conn, "cost_daily_rollup"):
        return
    op.drop_index("cost_daily_rollup_task_idx", table_name="cost_daily_rollup")
    op.drop_index("cost_daily_rollup_tenant_day_idx", table_name="cost_daily_rollup")
    op.drop_table("cost_daily_rollup")
