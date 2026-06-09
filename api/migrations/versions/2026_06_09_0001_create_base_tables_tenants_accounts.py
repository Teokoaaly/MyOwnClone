"""create base tables: tenants and accounts

These are the root tables that all other MyOwnClone tables reference via FK.
Must run BEFORE the core tables migration (a1b2c3d4e5f6).

In standalone mode (without the Dify base platform), these tables do not exist
and must be created explicitly.

Revision ID: 0000000000a0
Revises:
Create Date: 2026-06-09 07:00:00.000000
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = '0000000000a0'
down_revision = None        # This is the new root of the migration chain
branch_labels = None
depends_on = None


def _is_pg(conn) -> bool:
    return conn.dialect.name == "postgresql"


def upgrade():
    conn = op.get_bind()
    is_postgres = _is_pg(conn)

    uuid_type = postgresql.UUID() if is_postgres else sa.String(36)

    # ─── tenants ──────────────────────────────────────────────────────────
    op.create_table(
        "tenants",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("slug", sa.String(100), unique=True, nullable=True),
        sa.Column("plan", sa.String(50), server_default=sa.text("'básico'"), nullable=False),
        sa.Column("status", sa.String(50), server_default=sa.text("'normal'"), nullable=False),
        sa.Column(
            "subscription_status",
            sa.String(50),
            server_default=sa.text("'inactive'"),
            nullable=False,
        ),
        sa.Column("stripe_customer_id", sa.String(255), nullable=True),
        sa.Column("stripe_subscription_id", sa.String(255), nullable=True),
        sa.Column("trial_ends_at", sa.DateTime(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
    )
    op.create_index("idx_tenants_slug", "tenants", ["slug"], unique=True)
    op.create_index("idx_tenants_status", "tenants", ["status"], unique=False)

    # ─── accounts ─────────────────────────────────────────────────────────
    op.create_table(
        "accounts",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column(
            "tenant_id",
            uuid_type,
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("password", sa.String(255), nullable=True),  # bcrypt hash
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("avatar", sa.String(500), nullable=True),
        sa.Column("role", sa.String(50), server_default=sa.text("'owner'"), nullable=False),
        sa.Column("status", sa.String(50), server_default=sa.text("'active'"), nullable=False),
        sa.Column(
            "is_platform_admin",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        sa.Column("last_login_at", sa.DateTime(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.current_timestamp(),
            nullable=False,
        ),
    )
    op.create_index("idx_accounts_email", "accounts", ["email"], unique=True)
    op.create_index("idx_accounts_tenant", "accounts", ["tenant_id"], unique=False)
    op.create_index("idx_accounts_platform_admin", "accounts", ["is_platform_admin"], unique=False)


def downgrade():
    op.drop_index("idx_accounts_platform_admin", table_name="accounts")
    op.drop_index("idx_accounts_tenant", table_name="accounts")
    op.drop_index("idx_accounts_email", table_name="accounts")
    op.drop_table("accounts")

    op.drop_index("idx_tenants_status", table_name="tenants")
    op.drop_index("idx_tenants_slug", table_name="tenants")
    op.drop_table("tenants")
