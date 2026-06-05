"""add admin_audit_log table

Records every sensitive platform-admin action (impersonations, tenant plan
or status changes, courtesy signups) so the platform has full traceability.

Revision ID: b1c2d3e4f5a6
Revises: a1b2c3d4e5f7
Create Date: 2026-06-04 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

revision = 'b1c2d3e4f5a6'
down_revision = 'a1b2c3d4e5f7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'admin_audit_log',
        sa.Column('id', sa.String(36), primary_key=True, nullable=False),
        sa.Column('actor_id', sa.String(36), nullable=False),
        sa.Column('action', sa.String(50), nullable=False),
        sa.Column('target_type', sa.String(50), nullable=True),
        sa.Column('target_id', sa.String(36), nullable=True),
        sa.Column('reason', sa.Text(), nullable=True),
        sa.Column('metadata_json', sa.Text(), nullable=True),
        sa.Column('ip_address', sa.String(64), nullable=True),
        sa.Column('user_agent', sa.String(500), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index('idx_admin_audit_actor', 'admin_audit_log', ['actor_id'], unique=False)
    op.create_index('idx_admin_audit_action', 'admin_audit_log', ['action'], unique=False)
    op.create_index('idx_admin_audit_target', 'admin_audit_log', ['target_type', 'target_id'], unique=False)
    op.create_index('idx_admin_audit_created', 'admin_audit_log', ['created_at'], unique=False)


def downgrade():
    op.drop_index('idx_admin_audit_created', table_name='admin_audit_log')
    op.drop_index('idx_admin_audit_target', table_name='admin_audit_log')
    op.drop_index('idx_admin_audit_action', table_name='admin_audit_log')
    op.drop_index('idx_admin_audit_actor', table_name='admin_audit_log')
    op.drop_table('admin_audit_log')
