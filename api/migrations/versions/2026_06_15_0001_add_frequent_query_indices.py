"""add frequent query column indices

Add indices on columns frequently used in WHERE/JOIN clauses:
- clone_configs.tenant_id
- conversations.clone_id
- messages.conversation_id
- bookings.meeting_type_id

Revision ID: c3d4e5f6a7c2
Revises: c3d4e5f6a7c1
Create Date: 2026-06-15 10:00:00.000000

"""
from alembic import op


revision = 'c3d4e5f6a7c2'
down_revision = 'c3d4e5f6a7c1'
branch_labels = None
depends_on = None


def upgrade():
    # clone_configs.tenant_id - frequently filtered in multi-tenant queries
    op.create_index('idx_clone_configs_tenant_id', 'clone_configs', ['tenant_id'], unique=False)

    # conversations.clone_id - used for JOINs and WHERE filtering
    op.create_index('idx_conversations_clone_id', 'conversations', ['clone_id'], unique=False)

    # messages.conversation_id - used for JOINs to fetch conversation messages
    op.create_index('idx_messages_conversation_id', 'messages', ['conversation_id'], unique=False)

    # bookings.meeting_type_id - used for JOINs with meeting_types
    op.create_index('idx_bookings_meeting_type_id', 'bookings', ['meeting_type_id'], unique=False)


def downgrade():
    op.drop_index('idx_clone_configs_tenant_id', 'clone_configs')
    op.drop_index('idx_conversations_clone_id', 'conversations')
    op.drop_index('idx_messages_conversation_id', 'messages')
    op.drop_index('idx_bookings_meeting_type_id', 'bookings')
