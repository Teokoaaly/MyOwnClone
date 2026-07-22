"""add unique constraint on bookings (meeting_type_id, date, start_time)

Revision ID: 2026_07_14_0001
Revises: 2026_07_03_0001, 2026_07_09_0001_onboarding
Create Date: 2026-07-14

SECURITY (auditoria 2026-07-13 / P1.6 / H-12): the booking POST endpoints
used an application-level ``SELECT ... WHERE meeting_type_id AND date AND
start_time`` check, which has a classic TOCTOU race: two concurrent
requests can both pass the check and both INSERT, producing a double-booking.

This migration adds a partial unique index on
``(meeting_type_id, date, start_time)`` restricted to rows where both
``date`` and ``start_time`` are NOT NULL (legacy rows with no slot are
exempt). Any second INSERT now raises IntegrityError, which the
controller catches and returns as 409 Conflict.

Partial index rationale:
- ``date`` and ``start_time`` are nullable (legacy data without slot).
- A plain UNIQUE constraint treats each NULL as distinct, so legacy
  rows would not collide. A partial unique index on
  ``WHERE date IS NOT NULL AND start_time IS NOT NULL`` enforces the
  invariant for the only path that matters (the booking flow).
"""
import sqlalchemy as sa
from alembic import op


revision = "2026_07_14_0001"
down_revision = ("2026_07_03_0001", "2026_07_09_0001_onboarding")
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        "uq_bookings_meeting_slot",
        "bookings",
        ["meeting_type_id", "date", "start_time"],
        unique=True,
        postgresql_where=sa.text(
            "date IS NOT NULL AND start_time IS NOT NULL"
        ),
    )


def downgrade() -> None:
    op.drop_index("uq_bookings_meeting_slot", table_name="bookings")
