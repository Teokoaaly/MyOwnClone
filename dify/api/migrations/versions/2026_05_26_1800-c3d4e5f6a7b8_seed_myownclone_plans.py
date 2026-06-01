"""seed MyOwnClone default plans

Inserts the four standard plans (Básico, Pro, Escala, Enterprise) into myownclone_plans.

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-05-26 18:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = 'c3d4e5f6a7b8'
down_revision = 'b2c3d4e5f6a7'
branch_labels = None
depends_on = None

PLANS = [
    {
        "name": "Básico",
        "price_cents": 4900,
        "stripe_price_id": None,  # Fill after creating in Stripe dashboard
        "words_training_limit": 500000,
        "responses_month_limit": 2000,
        "modes_active": 1,
        "email_triage": False,
        "booking": False,
        "api_access": False,
        "multi_clone": False,
        "whitelabel": False,
    },
    {
        "name": "Pro",
        "price_cents": 9900,
        "stripe_price_id": None,
        "words_training_limit": 1000000,
        "responses_month_limit": 4000,
        "modes_active": 3,
        "email_triage": True,
        "booking": False,
        "api_access": False,
        "multi_clone": False,
        "whitelabel": False,
    },
    {
        "name": "Escala",
        "price_cents": 19900,
        "stripe_price_id": None,
        "words_training_limit": 5000000,
        "responses_month_limit": 20000,
        "modes_active": 3,
        "email_triage": True,
        "booking": True,
        "api_access": True,
        "multi_clone": False,
        "whitelabel": False,
    },
    {
        "name": "Enterprise",
        "price_cents": 49900,
        "stripe_price_id": None,
        "words_training_limit": 999999999,
        "responses_month_limit": 999999,
        "modes_active": 3,
        "email_triage": True,
        "booking": True,
        "api_access": True,
        "multi_clone": True,
        "whitelabel": True,
    },
]


def upgrade():
    table = sa.table(
        "myownclone_plans",
        sa.column("id", sa.String(36)),
        sa.column("name", sa.String(50)),
        sa.column("price_cents", sa.Integer()),
        sa.column("stripe_price_id", sa.String(100)),
        sa.column("words_training_limit", sa.BigInteger()),
        sa.column("responses_month_limit", sa.Integer()),
        sa.column("modes_active", sa.Integer()),
        sa.column("email_triage", sa.Boolean()),
        sa.column("booking", sa.Boolean()),
        sa.column("api_access", sa.Boolean()),
        sa.column("multi_clone", sa.Boolean()),
        sa.column("whitelabel", sa.Boolean()),
    )

    import uuid

    for plan in PLANS:
        op.execute(
            table.insert().values(
                id=str(uuid.uuid4()),
                **plan,
            )
        )


def downgrade():
    op.execute("DELETE FROM myownclone_plans")
