"""add MyOwnClone columns to existing tables — DISABLED for standalone mode

Dify base tables (documents, messages) do not exist in standalone MyOwnClone.
Migration 1 already created all MyOwnClone tables directly.

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-05-26 16:48:00.000000
"""
from alembic import op
import sqlalchemy as sa

revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None

def upgrade():
    pass

def downgrade():
    pass
