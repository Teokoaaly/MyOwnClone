"""add MyOwnClone core tables — clone_configs, knowledge_silos, email_inbound, meetings, etc.

Creates the 14 new tables that form the MyOwnClone data layer on top of Dify:
clone_configs, clone_mode_prompts, creator_memory, email_inbound, email_templates,
meeting_types, availability, bookings, products, cost_tracking, analytics_questions,
analytics_gaps, impersonation_log, plans.

Every MyOwnClone table is scoped to a Dify tenant so the multi-tenant boundary is preserved
without touching Dify's core models.

Revision ID: a1b2c3d4e5f6
Revises: 97e2e1a644e8
Create Date: 2026-05-26 16:45:00.000000

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

import models.types


def _is_pg(conn):
    return conn.dialect.name == "postgresql"


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '97e2e1a644e8'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    is_postgres = _is_pg(conn)

    # ─── plans ───────────────────────────────────────────────────────────
    op.create_table(
        'myownclone_plans',
        _uuid('id', is_postgres, pk=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price_cents', sa.Integer(), nullable=False),
        sa.Column('stripe_price_id', sa.String(100), nullable=True),
        sa.Column('words_training_limit', sa.BigInteger(), server_default=sa.text('500000'), nullable=False),
        sa.Column('responses_month_limit', sa.Integer(), server_default=sa.text('2000'), nullable=False),
        sa.Column('modes_active', sa.Integer(), server_default=sa.text('1'), nullable=False),
        sa.Column('email_triage', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('booking', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('api_access', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('multi_clone', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('whitelabel', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    )

    # ─── clone_configs ───────────────────────────────────────────────────
    op.create_table(
        'clone_configs',
        _uuid('id', is_postgres, pk=True),
        _tenant_fk('tenant_id', is_postgres),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(100), unique=True, nullable=False),
        sa.Column('description', models.types.LongText(), nullable=True),
        sa.Column('avatar_url', sa.String(500), nullable=True),
        sa.Column('personality_tone', sa.String(50), nullable=True),
        sa.Column('language', sa.String(10), server_default=sa.text("'es'"), nullable=False),
        sa.Column(
            'active_modes',
            _array_col(postgresql, is_postgres, sa.String(20)),
            server_default=sa.text("'{teach}'") if is_postgres else None,
            nullable=True,
        ),
        sa.Column('is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
        _timestamps(),
    )
    _create_index('idx_clone_configs_slug', 'clone_configs', ['slug'], is_postgres)
    _create_index('idx_clone_configs_tenant', 'clone_configs', ['tenant_id'], is_postgres)

    # ─── clone_mode_prompts ──────────────────────────────────────────────
    op.create_table(
        'clone_mode_prompts',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('mode', sa.String(20), nullable=False),
        sa.Column('system_prompt', models.types.LongText(), nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
        _timestamps(),
    )
    _create_index('idx_mode_prompts_clone', 'clone_mode_prompts', ['clone_id', 'mode'], is_postgres)

    # ─── creator_memory ──────────────────────────────────────────────────
    op.create_table(
        'creator_memory',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('type', sa.String(20), nullable=False),
        sa.Column('content', models.types.LongText(), nullable=False),
        sa.Column('trigger_condition', models.types.LongText(), nullable=True),
        sa.Column('priority', sa.Integer(), server_default=sa.text('0'), nullable=False),
        _timestamps(),
    )
    _create_index('idx_creator_memory_clone_type', 'creator_memory', ['clone_id', 'type'], is_postgres)

    # ─── email_inbound ───────────────────────────────────────────────────
    op.create_table(
        'email_inbound',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('from_email', sa.String(255), nullable=True),
        sa.Column('from_name', sa.String(255), nullable=True),
        sa.Column('subject', sa.String(500), nullable=True),
        sa.Column('body_text', models.types.LongText(), nullable=True),
        sa.Column('body_html', models.types.LongText(), nullable=True),
        sa.Column('draft_reply', models.types.LongText(), nullable=True),
        sa.Column('status', sa.String(20), server_default=sa.text("'pending'"), nullable=False),
        sa.Column(
            'labels',
            _array_col(postgresql, is_postgres, sa.String(50)),
            server_default=sa.text("'{}'") if is_postgres else None,
            nullable=True,
        ),
        sa.Column('classification', sa.String(50), nullable=True),
        sa.Column('thread_id', sa.String(500), nullable=True),
        sa.Column('received_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('responded_at', sa.DateTime(), nullable=True),
    )
    _create_index('idx_email_inbound_clone_status', 'email_inbound', ['clone_id', 'status'], is_postgres)

    # ─── email_templates ─────────────────────────────────────────────────
    op.create_table(
        'email_templates',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('subject', sa.String(500), nullable=True),
        sa.Column('body', models.types.LongText(), nullable=True),
        sa.Column(
            'trigger_keywords',
            _array_col(postgresql, is_postgres, sa.String(100)),
            server_default=sa.text("'{}'") if is_postgres else None,
            nullable=True,
        ),
        _timestamps(),
    )

    # ─── meeting_types ───────────────────────────────────────────────────
    op.create_table(
        'meeting_types',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('duration_minutes', sa.Integer(), server_default=sa.text('30'), nullable=False),
        sa.Column('price_cents', sa.Integer(), server_default=sa.text('0'), nullable=False),
        sa.Column('description', models.types.LongText(), nullable=True),
        sa.Column('color', sa.String(7), server_default=sa.text("'#6366f1'"), nullable=False),
        sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    )

    # ─── availability ────────────────────────────────────────────────────
    op.create_table(
        'availability',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('day_of_week', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.Time(), nullable=False),
        sa.Column('end_time', sa.Time(), nullable=False),
        sa.Column('buffer_minutes', sa.Integer(), server_default=sa.text('15'), nullable=False),
    )
    _create_index('idx_availability_clone_dow', 'availability', ['clone_id', 'day_of_week'], is_postgres)

    # ─── bookings ────────────────────────────────────────────────────────
    op.create_table(
        'bookings',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('meeting_type_id', 'meeting_types', is_postgres, ondelete='CASCADE'),
        sa.Column('visitor_name', sa.String(255), nullable=True),
        sa.Column('visitor_email', sa.String(255), nullable=True),
        sa.Column('date', sa.Date(), nullable=True),
        sa.Column('start_time', sa.Time(), nullable=True),
        sa.Column('end_time', sa.Time(), nullable=True),
        sa.Column('status', sa.String(20), server_default=sa.text("'confirmed'"), nullable=False),
        sa.Column('meeting_url', sa.String(500), nullable=True),
        sa.Column('recording_url', sa.String(500), nullable=True),
        sa.Column('transcript', models.types.LongText(), nullable=True),
        sa.Column('notes', models.types.LongText(), nullable=True),
        _timestamps(),
    )
    _create_index('idx_bookings_meeting_date', 'bookings', ['meeting_type_id', 'date'], is_postgres)

    # ─── products ────────────────────────────────────────────────────────
    op.create_table(
        'products',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', models.types.LongText(), nullable=True),
        sa.Column('price_cents', sa.Integer(), nullable=True),
        sa.Column('url', sa.String(500), nullable=True),
        sa.Column('image_url', sa.String(500), nullable=True),
        sa.Column('priority', sa.Integer(), server_default=sa.text('0'), nullable=False),
        sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    )
    _create_index('idx_products_clone_active', 'products', ['clone_id', 'active'], is_postgres)

    # ─── cost_tracking ───────────────────────────────────────────────────
    op.create_table(
        'cost_tracking',
        _uuid('id', is_postgres, pk=True),
        _tenant_fk('tenant_id', is_postgres),
        sa.Column('category', sa.String(20), nullable=False),
        sa.Column('operation', sa.String(100), nullable=True),
        sa.Column('model', sa.String(50), nullable=True),
        sa.Column('tokens_in', sa.Integer(), server_default=sa.text('0'), nullable=False),
        sa.Column('tokens_out', sa.Integer(), server_default=sa.text('0'), nullable=False),
        sa.Column('cost_cents', sa.Integer(), server_default=sa.text('0'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    _create_index(
        'idx_cost_tracking_tenant_category_ts',
        'cost_tracking',
        ['tenant_id', 'category', 'created_at'],
        is_postgres,
    )

    # ─── analytics_questions ─────────────────────────────────────────────
    op.create_table(
        'analytics_questions',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('question', models.types.LongText(), nullable=True),
        sa.Column('count', sa.Integer(), server_default=sa.text('1'), nullable=False),
        sa.Column('last_asked_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    _create_index('idx_analytics_q_clone', 'analytics_questions', ['clone_id'], is_postgres)

    # ─── analytics_gaps ──────────────────────────────────────────────────
    op.create_table(
        'analytics_gaps',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk('clone_id', 'clone_configs', is_postgres, ondelete='CASCADE'),
        sa.Column('question', models.types.LongText(), nullable=True),
        sa.Column('count', sa.Integer(), server_default=sa.text('1'), nullable=False),
        sa.Column('suggested_source', sa.String(500), nullable=True),
        sa.Column('status', sa.String(20), server_default=sa.text("'open'"), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    )
    _create_index('idx_analytics_gaps_clone', 'analytics_gaps', ['clone_id', 'status'], is_postgres)

    # ─── impersonation_log ───────────────────────────────────────────────
    _uuid_fk_account = (
        sa.Column(
            'admin_id',
            postgresql.UUID(),
            sa.ForeignKey('accounts.id', ondelete='CASCADE'),
            nullable=False,
        )
        if is_postgres
        else sa.Column(
            'admin_id',
            models.types.StringUUID(),
            sa.ForeignKey('accounts.id', ondelete='CASCADE'),
            nullable=False,
        )
    )
    _uuid_fk_tenant = _tenant_fk('tenant_id', is_postgres)
    op.create_table(
        'impersonation_log',
        _uuid('id', is_postgres, pk=True),
        _uuid_fk_account,
        _uuid_fk_tenant,
        sa.Column('reason', models.types.LongText(), nullable=True),
        sa.Column('started_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('ended_at', sa.DateTime(), nullable=True),
    )
    _create_index('idx_impersonation_admin', 'impersonation_log', ['admin_id'], is_postgres)
    _create_index('idx_impersonation_tenant', 'impersonation_log', ['tenant_id'], is_postgres)


def downgrade():
    op.drop_table('impersonation_log')
    op.drop_table('analytics_gaps')
    op.drop_table('analytics_questions')
    op.drop_table('cost_tracking')
    op.drop_table('products')
    op.drop_table('bookings')
    op.drop_table('availability')
    op.drop_table('meeting_types')
    op.drop_table('email_templates')
    op.drop_table('email_inbound')
    op.drop_table('creator_memory')
    op.drop_table('clone_mode_prompts')
    op.drop_table('clone_configs')
    op.drop_table('myownclone_plans')


# ─── helpers ────────────────────────────────────────────────────────────────


def _uuid(col_name: str, is_postgres: bool, *, pk: bool = False) -> sa.Column:
    if is_postgres:
        return sa.Column(
            col_name,
            postgresql.UUID(),
            server_default=sa.text('uuid_generate_v4()') if pk else None,
            primary_key=pk,
            nullable=False,
        )
    return sa.Column(col_name, models.types.StringUUID(), primary_key=pk, nullable=False)


def _uuid_fk(col_name: str, target_table: str, is_postgres: bool, *, ondelete: str = 'CASCADE') -> sa.Column:
    if is_postgres:
        return sa.Column(
            col_name,
            postgresql.UUID(),
            sa.ForeignKey(f'{target_table}.id', ondelete=ondelete),
            nullable=False,
        )
    return sa.Column(
        col_name,
        models.types.StringUUID(),
        sa.ForeignKey(f'{target_table}.id', ondelete=ondelete),
        nullable=False,
    )


def _tenant_fk(col_name: str, is_postgres: bool) -> sa.Column:
    return _uuid_fk(col_name, 'tenants', is_postgres, ondelete='CASCADE')


def _timestamps() -> list[sa.Column]:
    return [
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False),
    ]


def _array_col(pg_dialect, is_postgres: bool, item_type):
    if is_postgres:
        return pg_dialect.ARRAY(item_type)
    return sa.JSON()


def _create_index(name: str, table: str, columns: list[str], is_postgres: bool) -> None:
    if is_postgres:
        op.create_index(name, table, columns, unique=False)
    else:
        op.create_index(name, table, columns, unique=False)
