"""chunks.embedding: ARRAY -> vector(1024)

Revision ID: 2026_07_03_0001
Revises: 2026_06_27_0001
Create Date: 2026-07-03
"""
from alembic import op

revision = '2026_07_03_0001'
down_revision = '2026_06_27_0001'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("ALTER TABLE chunks ALTER COLUMN embedding TYPE vector(1024) USING embedding::vector(1024);")

def downgrade():
    op.execute("ALTER TABLE chunks ALTER COLUMN embedding TYPE double precision[] USING embedding::double precision[];")
