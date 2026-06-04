"""SQLAlchemy type stubs for migration files."""
from sqlalchemy import Text

LongText = Text
StringUUID = 'UUID'
AdjustedJSON = 'JSON'

__all__ = ['LongText', 'StringUUID', 'AdjustedJSON']
