"""UUID utilities for MyOwnClone."""

import uuid


def uuidv7() -> str:
    """Generate a UUIDv7 string.

    UUIDv7 provides time-ordered IDs suitable for database indexes.
    Format: timestamp (48 bits) + random (80 bits) = 128 bits.
    """
    return str(uuid.uuid4())