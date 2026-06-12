"""UUID utilities for MyOwnClone."""

import secrets
import time
import uuid


def uuidv7() -> str:
    """Generate a UUIDv7 string.

    UUIDv7 provides time-ordered IDs suitable for database indexes.
    Format: timestamp (48 bits) + random (80 bits) = 128 bits.
    """
    native_uuid7 = getattr(uuid, "uuid7", None)
    if native_uuid7 is not None:
        return str(native_uuid7())

    timestamp_ms = int(time.time_ns() // 1_000_000) & ((1 << 48) - 1)
    rand_a = secrets.randbits(12)
    rand_b = secrets.randbits(62)

    value = (timestamp_ms << 80) | (0x7 << 76) | (rand_a << 64) | (0b10 << 62) | rand_b
    return str(uuid.UUID(int=value))
