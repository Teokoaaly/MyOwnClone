from alembic import op


revision = "2026_07_23_0001"
down_revision = "2026_07_14_0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    if connection.dialect.name != "postgresql":
        return

    op.execute(
        """
        WITH ranked AS (
            SELECT assignment.id,
                   ROW_NUMBER() OVER (
                       PARTITION BY assignment.task
                       ORDER BY CASE WHEN model.is_active THEN 0 ELSE 1 END,
                                model.priority ASC,
                                assignment.created_at ASC,
                                assignment.id ASC
                   ) AS row_number
            FROM ai_model_assignments AS assignment
            JOIN ai_models AS model ON model.id = assignment.model_id
            WHERE assignment.tenant_id IS NULL
              AND assignment.is_active = true
        )
        UPDATE ai_model_assignments AS assignment
        SET is_active = false,
            updated_at = NOW()
        FROM ranked
        WHERE assignment.id = ranked.id
          AND ranked.row_number > 1
        """
    )
    op.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS uq_active_global_assignment_per_task
        ON ai_model_assignments (task)
        WHERE tenant_id IS NULL AND is_active = true
        """
    )


def downgrade() -> None:
    connection = op.get_bind()
    if connection.dialect.name == "postgresql":
        op.execute("DROP INDEX IF EXISTS uq_active_global_assignment_per_task")
