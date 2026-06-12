"""add missing tables: clone_feedback, sources, chunks, conversations, messages

These tables are declared in api/models but were never created by
Alembic migrations, causing 500 errors when endpoints query them.

Revision ID: c3d4e5f6a7b9
Revises: f6a7b8c9d0e1
Create Date: 2026-06-12 12:20:00.000000
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision = 'c3d4e5f6a7b9'
down_revision = 'f6a7b8c9d0e1'
branch_labels = None
depends_on = None


def _is_pg(conn) -> bool:
    return conn.dialect.name == "postgresql"


def upgrade():
    conn = op.get_bind()
    is_postgres = _is_pg(conn)
    uuid_type = sa.String(36)

    # ─── clone_feedback ──────────────────────────────────────────────
    op.create_table(
        'clone_feedback',
        sa.Column('id', uuid_type, primary_key=True, nullable=False),
        sa.Column('clone_id', uuid_type, sa.ForeignKey('clone_configs.id', ondelete='CASCADE'), nullable=False),
        sa.Column('tenant_id', uuid_type, sa.ForeignKey('tenants.id', ondelete='CASCADE'), nullable=False),
        sa.Column('visitor_id', sa.String(128), nullable=True),
        sa.Column('conversation_id', sa.String(128), nullable=True),
        sa.Column('message_id', sa.String(128), nullable=True),
        sa.Column('rating', sa.String(20), nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('category', sa.String(50), nullable=True),
        sa.Column('status', sa.String(20), server_default=sa.text("'new'"), nullable=False),
        sa.Column('extra_metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index('idx_clone_feedback_clone', 'clone_feedback', ['clone_id'])
    op.create_index('idx_clone_feedback_tenant', 'clone_feedback', ['tenant_id'])

    # ─── sources ─────────────────────────────────────────────────────
    op.create_table(
        'sources',
        sa.Column('id', sa.Text(), primary_key=True, nullable=False),
        sa.Column('clone_id', sa.Text(), nullable=False),
        sa.Column('type', sa.String(30), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column('url', sa.Text(), nullable=True),
        sa.Column('status', sa.String(30), server_default=sa.text("'uploading'"), nullable=False),
        sa.Column('metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index('idx_sources_clone', 'sources', ['clone_id'])
    op.create_index('idx_sources_status', 'sources', ['status'])

    # ─── chunks ──────────────────────────────────────────────────────
    op.create_table(
        'chunks',
        sa.Column('id', sa.Text(), primary_key=True, nullable=False),
        sa.Column('source_id', sa.Text(), sa.ForeignKey('sources.id', ondelete='CASCADE'), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('embedding', postgresql.ARRAY(sa.Float) if is_postgres else sa.JSON(), nullable=True),
        sa.Column('token_count', sa.Integer(), nullable=True),
        sa.Column('metadata', sa.JSON(), nullable=True),
    )
    op.create_index('idx_chunks_source', 'chunks', ['source_id'])

    # ─── conversations ──────────────────────────────────────────────
    op.create_table(
        'conversations',
        sa.Column('id', sa.Text(), primary_key=True, nullable=False),
        sa.Column('clone_id', sa.Text(), nullable=False),
        sa.Column('visitor_id', sa.Text(), nullable=True),
        sa.Column('mode', sa.String(30), server_default=sa.text("'pedagogy'"), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index('idx_conversations_clone', 'conversations', ['clone_id'])

    # ─── messages ───────────────────────────────────────────────────
    op.create_table(
        'messages',
        sa.Column('id', sa.Text(), primary_key=True, nullable=False),
        sa.Column('conversation_id', sa.Text(), sa.ForeignKey('conversations.id', ondelete='CASCADE'), nullable=False),
        sa.Column('role', sa.Text(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('confidence', sa.Text(), nullable=True),
        sa.Column('sources', sa.JSON(), nullable=True),
        sa.Column('feedback', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    op.create_index('idx_messages_conversation', 'messages', ['conversation_id'])


def downgrade():
    op.drop_index('idx_messages_conversation', table_name='messages')
    op.drop_table('messages')
    op.drop_index('idx_conversations_clone', table_name='conversations')
    op.drop_table('conversations')
    op.drop_index('idx_chunks_source', table_name='chunks')
    op.drop_table('chunks')
    op.drop_index('idx_sources_status', table_name='sources')
    op.drop_index('idx_sources_clone', table_name='sources')
    op.drop_table('sources')
    op.drop_index('idx_clone_feedback_tenant', table_name='clone_feedback')
    op.drop_index('idx_clone_feedback_clone', table_name='clone_feedback')
    op.drop_table('clone_feedback')
