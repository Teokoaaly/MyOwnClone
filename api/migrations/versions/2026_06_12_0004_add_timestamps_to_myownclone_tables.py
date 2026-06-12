"""add created_at/updated_at to all MyOwnClone tables missing them

Some tables in this migration (clone_configs, clone_mode_prompts,
creator_memory, email_inbound, email_templates, meeting_types,
availability, bookings, products, cost_tracking, analytics_questions,
analytics_gaps, impersonation_log, impersonation_tokens, myownclone_plans)
are mapped from DefaultFieldsDCMixin which declares created_at/updated_at
columns. The original core tables migration (a1b2c3d4e5f6) defined a
_timestamps() helper but it was not consistently invoked, so the
columns are missing from the live database. This migration adds them
with safe defaults so ORM queries that reference these columns succeed.

Revision ID: c3d4e5f6a7c0
Revises: c3d4e5f6a7b9
Create Date: 2026-06-12 12:30:00.000000
"""
import sqlalchemy as sa
from alembic import op


revision = 'c3d4e5f6a7c0'
down_revision = 'c3d4e5f6a7b9'
branch_labels = None
depends_on = None


# Tables that use DefaultFieldsDCMixin and therefore expect created_at/updated_at.
# Listed explicitly so we can drop the columns on downgrade.
TIMESTAMPED_TABLES = [
    'clone_configs',
    'clone_mode_prompts',
    'creator_memory',
    'email_inbound',
    'email_templates',
    'meeting_types',
    'availability',
    'bookings',
    'products',
    'cost_tracking',
    'analytics_questions',
    'analytics_gaps',
    'impersonation_log',
    'impersonation_tokens',
    'myownclone_plans',
    'admin_audit_log',
]


def upgrade():
    for table in TIMESTAMPED_TABLES:
        # Check if columns already exist (idempotent for partial migrations)
        conn = op.get_bind()
        inspector = sa.inspect(conn)
        existing = {c['name'] for c in inspector.get_columns(table)} if inspector.has_table(table) else set()

        if 'created_at' not in existing:
            op.execute(
                f"ALTER TABLE {table} ADD COLUMN created_at TIMESTAMP "
                f"DEFAULT CURRENT_TIMESTAMP NOT NULL"
            )
        if 'updated_at' not in existing:
            op.execute(
                f"ALTER TABLE {table} ADD COLUMN updated_at TIMESTAMP "
                f"DEFAULT CURRENT_TIMESTAMP NOT NULL"
            )


def downgrade():
    for table in TIMESTAMPED_TABLES:
        op.execute(f"ALTER TABLE {table} DROP COLUMN IF EXISTS created_at")
        op.execute(f"ALTER TABLE {table} DROP COLUMN IF EXISTS updated_at")
