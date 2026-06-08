"""Date/time utilities for MyOwnClone."""

from datetime import datetime, timezone


def naive_utc_now() -> datetime:
    """Return current UTC time as a naive datetime (no timezone info).

    PostgreSQL stores timestamps without timezone innaive format,
    so we normalize all times to UTC without tzinfo.
    """
    return datetime.now(timezone.utc).replace(tzinfo=None)