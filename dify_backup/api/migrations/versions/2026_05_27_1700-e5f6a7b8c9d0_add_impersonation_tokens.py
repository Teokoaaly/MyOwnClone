"""add impersonation_tokens table

Revision ID: e5f6a7b8c9d0
Revises: 2026_05_27_1200-d4e5f6a7b8c9
Create Date: 2026-05-27 17:00:00.000000

"""
import sqlalchemy as sa
from alembic import op

revision = 'e5f6a7b8c9d0'
down_revision = '2026_05_27_1200-d4e5f6a7b8c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'impersonation_tokens',
        sa.Column('id', sa.String(36), primary_key=True, nullable=False),
        sa.Column('token', sa.String(128), unique=True, nullable=False),
        sa.Column('admin_id', sa.String(36), nullable=False),
        sa.Column('tenant_id', sa.String(36), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )


def downgrade():
    op.drop_table('impersonation_tokens')
