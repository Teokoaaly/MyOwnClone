"""add custom_domain to clone_configs

Revision ID: d4e5f6a7b8c9
Revises: 2026_05_26_1800-c3d4e5f6a7b8
Create Date: 2026-05-27 12:00:00.000000

"""
import sqlalchemy as sa
from alembic import op

revision = 'd4e5f6a7b8c9'
down_revision = '2026_05_26_1800-c3d4e5f6a7b8'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('clone_configs', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('custom_domain', sa.String(255), nullable=True)
        )


def downgrade():
    with op.batch_alter_table('clone_configs', schema=None) as batch_op:
        batch_op.drop_column('custom_domain')
