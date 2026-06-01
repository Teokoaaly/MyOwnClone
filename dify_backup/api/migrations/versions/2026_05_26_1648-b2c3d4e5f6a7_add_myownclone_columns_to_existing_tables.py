"""add MyOwnClone columns to existing Dify tables — documents, messages, tenants, accounts

Adds silo/context/speaker metadata on documents, silo/context on messages,
slug/plan/subscription fields on tenants, and role on accounts.

These are additive columns only; no existing Dify behaviour is altered.

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-05-26 16:48:00.000000

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

import models.types


# revision identifiers, used by Alembic.
revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade():
    # ─── documents ───────────────────────────────────────────────────────
    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('silo', sa.String(20), nullable=True)
        )
        batch_op.add_column(
            sa.Column('context_id', sa.String(255), nullable=True)
        )
        batch_op.add_column(
            sa.Column('speaker', sa.String(100), nullable=True)
        )
        batch_op.add_column(
            sa.Column('source_metadata', models.types.AdjustedJSON(), nullable=True)
        )
        batch_op.add_column(
            sa.Column(
                'clone_config_id',
                models.types.StringUUID(),
                nullable=True,
            )
        )

    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.create_index(
            'idx_documents_silo',
            ['tenant_id', 'silo'],
            unique=False,
        )
        batch_op.create_index(
            'idx_documents_context',
            ['tenant_id', 'silo', 'context_id'],
            unique=False,
        )

    # ─── messages ────────────────────────────────────────────────────────
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('silo', sa.String(20), nullable=True)
        )
        batch_op.add_column(
            sa.Column('context_id', sa.String(255), nullable=True)
        )
        batch_op.add_column(
            sa.Column('confidence_score', sa.Float(), nullable=True)
        )
        batch_op.add_column(
            sa.Column('sources', models.types.AdjustedJSON(), nullable=True)
        )

    # ─── tenants ─────────────────────────────────────────────────────────
    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('slug', sa.String(100), unique=True, nullable=True)
        )
        batch_op.add_column(
            sa.Column('plan', sa.String(20), server_default=sa.text("'básico'"), nullable=True)
        )
        batch_op.add_column(
            sa.Column('custom_domain', sa.String(255), nullable=True)
        )
        batch_op.add_column(
            sa.Column('subscription_status', sa.String(20), server_default=sa.text("'trial'"), nullable=True)
        )
        batch_op.add_column(
            sa.Column('stripe_customer_id', sa.String(100), nullable=True)
        )
        batch_op.add_column(
            sa.Column('stripe_subscription_id', sa.String(100), nullable=True)
        )

    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.create_index(
            'idx_tenants_slug',
            ['slug'],
            unique=False,
        )

    # ─── accounts ────────────────────────────────────────────────────────
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('role', sa.String(20), server_default=sa.text("'member'"), nullable=True)
        )


def downgrade():
    # ─── accounts ────────────────────────────────────────────────────────
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ─── tenants ─────────────────────────────────────────────────────────
    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.drop_index('idx_tenants_slug')

    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.drop_column('stripe_subscription_id')
        batch_op.drop_column('stripe_customer_id')
        batch_op.drop_column('subscription_status')
        batch_op.drop_column('custom_domain')
        batch_op.drop_column('plan')
        batch_op.drop_column('slug')

    # ─── messages ────────────────────────────────────────────────────────
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('sources')
        batch_op.drop_column('confidence_score')
        batch_op.drop_column('context_id')
        batch_op.drop_column('silo')

    # ─── documents ───────────────────────────────────────────────────────
    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.drop_index('idx_documents_context')
        batch_op.drop_index('idx_documents_silo')

    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.drop_column('clone_config_id')
        batch_op.drop_column('source_metadata')
        batch_op.drop_column('speaker')
        batch_op.drop_column('context_id')
        batch_op.drop_column('silo')
