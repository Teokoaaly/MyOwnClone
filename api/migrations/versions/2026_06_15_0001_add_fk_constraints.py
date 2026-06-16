"""add foreign key constraints to clone_id, tenant_id, meeting_type_id, conversation_id

These tables were created without FK constraints, but the related tables
(tenants, clone_configs, conversations, meeting_types) already exist.

Revision ID: c3d4e5f6a7d0
Revises: c3d4e5f6a7c1
Create Date: 2026-06-15 12:00:00.000000
"""
from alembic import op


revision = 'c3d4e5f6a7d0'
down_revision = 'c3d4e5f6a7c1'
branch_labels = None
depends_on = None


def upgrade():
    # clone_configs.tenant_id → tenants.id
    op.execute("""
        ALTER TABLE clone_configs
        ADD CONSTRAINT fk_clone_configs_tenant_id
        FOREIGN KEY (tenant_id) REFERENCES tenants(id) ON DELETE CASCADE
    """)

    # clone_mode_prompts.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE clone_mode_prompts
        ADD CONSTRAINT fk_clone_mode_prompts_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)

    # creator_memory.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE creator_memory
        ADD CONSTRAINT fk_creator_memory_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)

    # conversations.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE conversations
        ADD CONSTRAINT fk_conversations_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)

    # messages.conversation_id → conversations.id
    op.execute("""
        ALTER TABLE messages
        ADD CONSTRAINT fk_messages_conversation_id
        FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
    """)

    # meeting_types.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE meeting_types
        ADD CONSTRAINT fk_meeting_types_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)

    # availability.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE availability
        ADD CONSTRAINT fk_availability_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)

    # bookings.meeting_type_id → meeting_types.id
    op.execute("""
        ALTER TABLE bookings
        ADD CONSTRAINT fk_bookings_meeting_type_id
        FOREIGN KEY (meeting_type_id) REFERENCES meeting_types(id) ON DELETE CASCADE
    """)

    # products.clone_id → clone_configs.id
    op.execute("""
        ALTER TABLE products
        ADD CONSTRAINT fk_products_clone_id
        FOREIGN KEY (clone_id) REFERENCES clone_configs(id) ON DELETE CASCADE
    """)


def downgrade():
    op.execute("ALTER TABLE products DROP CONSTRAINT IF EXISTS fk_products_clone_id")
    op.execute("ALTER TABLE bookings DROP CONSTRAINT IF EXISTS fk_bookings_meeting_type_id")
    op.execute("ALTER TABLE availability DROP CONSTRAINT IF EXISTS fk_availability_clone_id")
    op.execute("ALTER TABLE meeting_types DROP CONSTRAINT IF EXISTS fk_meeting_types_clone_id")
    op.execute("ALTER TABLE messages DROP CONSTRAINT IF EXISTS fk_messages_conversation_id")
    op.execute("ALTER TABLE conversations DROP CONSTRAINT IF EXISTS fk_conversations_clone_id")
    op.execute("ALTER TABLE creator_memory DROP CONSTRAINT IF EXISTS fk_creator_memory_clone_id")
    op.execute("ALTER TABLE clone_mode_prompts DROP CONSTRAINT IF EXISTS fk_clone_mode_prompts_clone_id")
    op.execute("ALTER TABLE clone_configs DROP CONSTRAINT IF EXISTS fk_clone_configs_tenant_id")
