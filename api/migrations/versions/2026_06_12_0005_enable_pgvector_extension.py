"""enable pgvector extension

Revision ID: c3d4e5f6a7c1
Revises: c3d4e5f6a7c0
Create Date: 2026-06-12 13:10:00.000000
"""
from alembic import op


revision = 'c3d4e5f6a7c1'
down_revision = 'c3d4e5f6a7c0'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    if conn.dialect.name == "postgresql":
        op.execute("CREATE EXTENSION IF NOT EXISTS vector")


def downgrade():
    # Do not drop the extension automatically: other tables or applications in
    # the database may depend on it.
    pass
