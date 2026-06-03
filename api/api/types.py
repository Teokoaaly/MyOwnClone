"""Custom types for MyOwnClone SQLAlchemy models."""

from sqlalchemy import Text
from sqlalchemy.types import TypeDecorator


class LongText(TypeDecorator):
    """A TEXT column that maps to Python str.

    Used for fields that may contain very long text content
    (descriptions, system prompts, email bodies, etc.).
    """

    impl = Text
    cache_ok = True

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        return value