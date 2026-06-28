"""create system_settings table

Revision ID: 2026_06_27_0001
Revises: f3a4b5c6d7e8
Create Date: 2026-06-27 00:00:00.000000

"""
import sqlalchemy as sa
from alembic import op


revision = "2026_06_27_0001"
down_revision = "f3a4b5c6d7e8"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "system_settings",
        sa.Column("key", sa.String(64), primary_key=True),
        sa.Column("value", sa.Text, nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime,
            server_default=sa.func.now(),
        ),
    )
    op.execute(
        "INSERT INTO system_settings (key, value) VALUES "
        "('maintenance_mode', 'false')"
    )


def downgrade():
    op.execute("DELETE FROM system_settings WHERE key = 'maintenance_mode'")
    op.drop_table("system_settings")
