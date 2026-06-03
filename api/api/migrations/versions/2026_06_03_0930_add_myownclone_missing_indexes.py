"""add MyOwnClone missing indexes

Revision ID: a1b2c3d4e5f7
Revises: e5f6a7b8c9d0
Create Date: 2026-06-03 09:30:00.000000

"""
from alembic import op

revision = 'a1b2c3d4e5f7'
down_revision = 'e5f6a7b8c9d0'
branch_labels = None
depends_on = None


def upgrade():
    # email_templates.clone_id
    op.create_index('idx_email_templates_clone_id', 'email_templates', ['clone_id'], unique=False)

    # meeting_types.clone_id
    op.create_index('idx_meeting_types_clone_id', 'meeting_types', ['clone_id'], unique=False)

    # clone_feedback.clone_id
    op.create_index('idx_clone_feedback_clone_id', 'clone_feedback', ['clone_id'], unique=False)


def downgrade():
    op.drop_index('idx_email_templates_clone_id', 'email_templates')
    op.drop_index('idx_meeting_types_clone_id', 'meeting_types')
    op.drop_index('idx_clone_feedback_clone_id', 'clone_feedback')