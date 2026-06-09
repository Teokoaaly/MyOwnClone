"""Type aliases for MyOwnClone models."""
from sqlalchemy import Text

# LongText is just Text - postgres-specific TEXT type
LongText = Text

__all__ = ["LongText"]
