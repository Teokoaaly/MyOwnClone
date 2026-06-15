"""fix plan pricing to match landing page

Aligns the myownclone_plans table with the landing page pricing:
  Free     $0.00  (was Básico $49.00)
  Pro      $64.90 (was $99.00)
  Enterprise $100  (was $499.00)
  Escala → removed

Revision ID: c3d4e6f7a8b9
Revises: c3d4e5f6a7b8
Create Date: 2026-06-15 13:40:00.000000
"""

from alembic import op

revision = 'c3d4e6f7a8b9'
down_revision = 'c3d4e5f6a7b8'
branch_labels = None
depends_on = None


def upgrade():
    # Rename Básico → Free, set price to 0
    op.execute("""
        UPDATE myownclone_plans
        SET name = 'Free', price_cents = 0,
            words_training_limit = 100000,
            responses_month_limit = 500
        WHERE name = 'Básico'
    """)

    # Fix Pro price: 9900 → 6490
    op.execute("""
        UPDATE myownclone_plans
        SET price_cents = 6490
        WHERE name = 'Pro'
    """)

    # Fix Enterprise price: 49900 → 10000
    op.execute("""
        UPDATE myownclone_plans
        SET price_cents = 10000
        WHERE name = 'Enterprise'
    """)

    # Remove Escala
    op.execute("DELETE FROM myownclone_plans WHERE name = 'Escala'")


def downgrade():
    # Revert Free → Básico
    op.execute("""
        UPDATE myownclone_plans
        SET name = 'Básico', price_cents = 4900,
            words_training_limit = 500000,
            responses_month_limit = 2000
        WHERE name = 'Free'
    """)

    # Revert Pro price
    op.execute("""
        UPDATE myownclone_plans
        SET price_cents = 9900
        WHERE name = 'Pro'
    """)

    # Revert Enterprise price
    op.execute("""
        UPDATE myownclone_plans
        SET price_cents = 49900
        WHERE name = 'Enterprise'
    """)

    # Re-insert Escala
    import uuid
    op.execute(f"""
        INSERT INTO myownclone_plans (id, name, price_cents, words_training_limit,
            responses_month_limit, modes_active, email_triage, booking, api_access,
            multi_clone, whitelabel)
        VALUES ('{uuid.uuid4()}', 'Escala', 19900, 5000000, 20000, 3,
            true, true, true, false, false)
    """)
