"""Real SQLAlchemy type aliases for MyOwnClone models.

`StringList` is dialect-aware: native `ARRAY(String)` on PostgreSQL, plain
`JSON` on SQLite/MySQL so the same model works in unit tests and CI.
`LongText` is a portable alias for `Text` (no length limit).
"""
from __future__ import annotations

from sqlalchemy import JSON, String, Text
from sqlalchemy.types import TypeDecorator

__all__ = ["LongText", "StringList"]


LongText = Text


class StringList(TypeDecorator):
    """Stores a list of strings transparently across dialects.

    On PostgreSQL uses `ARRAY(String)`, which preserves indexing and the
    `unnest` operator. On other dialects (SQLite, MySQL) it falls back to
    `JSON` so the model is portable for tests.
    """

    impl = JSON
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            from sqlalchemy.dialects.postgresql import ARRAY
            return dialect.type_descriptor(ARRAY(String()))
        return dialect.type_descriptor(JSON())

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if dialect.name == "postgresql":
            return list(value) if value is not None else None
        import json
        return json.dumps(list(value) if value else [])

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            import json
            try:
                return json.loads(value)
            except (TypeError, ValueError):
                return []
        return list(value) if value else []
