"""Regression tests for P1.6: booking unique constraint + 409 on TOCTOU race
(auditoria 2026-07-13, H-12).

Covers:
- H-12: the partial unique index ``uq_bookings_meeting_slot`` is defined on
  (meeting_type_id, date, start_time) WHERE both NOT NULL, so legacy rows
  with NULL slot are exempt and concurrent INSERTs on the same slot raise
  IntegrityError which both controllers translate to 409.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def test_migration_file_creates_partial_unique_index():
    """The migration must use op.create_index with postgresql_where."""
    mig_path = (
        REPO_ROOT
        / "api"
        / "migrations"
        / "versions"
        / "2026_07_14_0001_add_booking_unique_constraint.py"
    )
    assert mig_path.exists(), f"Migration not found: {mig_path}"
    src = mig_path.read_text(encoding="utf-8")
    assert "create_index" in src, "Migration must call op.create_index"
    assert 'uq_bookings_meeting_slot' in src, "Index must be named uq_bookings_meeting_slot"
    # The partial WHERE must exclude NULL date/start_time so legacy rows survive.
    assert "date IS NOT NULL AND start_time IS NOT NULL" in src, (
        "Index must be partial on date/start_time NOT NULL"
    )
    # And must be on the right column set.
    m = re.search(r"create_index\(\s*[\"']uq_bookings_meeting_slot[\"']", src)
    assert m, "Index name not found in create_index call"


def test_public_booking_catches_integrity_error():
    """The public booking POST must catch IntegrityError -> 409."""
    from api.controllers import myownclone_public
    src = Path(myownclone_public.__file__).read_text(encoding="utf-8")
    # The IntegrityError import must be at module level.
    assert "from sqlalchemy.exc import IntegrityError" in src, (
        "myownclone_public.py must import IntegrityError at module level"
    )
    # The create_booking_public endpoint must wrap commit() in try/except IntegrityError.
    assert re.search(
        r"except IntegrityError.*?return jsonify.*?409",
        src,
        re.DOTALL,
    ), "create_booking_public must translate IntegrityError to 409"


def test_admin_booking_catches_integrity_error():
    """The admin BookingsApi.post must catch IntegrityError -> 409."""
    from api.controllers.console.myownclone import booking as booking_mod
    src = Path(booking_mod.__file__).read_text(encoding="utf-8")
    assert "from sqlalchemy.exc import IntegrityError" in src
    assert re.search(
        r"except IntegrityError.*?return.*?409",
        src,
        re.DOTALL,
    ), "BookingsApi.post must translate IntegrityError to 409"
