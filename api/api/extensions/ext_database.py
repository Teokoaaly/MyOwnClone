# extensions/ext_database.py
"""SQLAlchemy database extension.

`db` uses `TypeBase` (defined in `api.base`) as its declarative model class
so every model declared in `api.models.*` ends up in the same metadata that
alembic and `db.create_all()` see. The default `flask_sqlalchemy.SQLAlchemy`
uses its own internal `DeclarativeBase`, which would not see the MyOwnClone
models and leave the schema half-built.
"""
from flask_sqlalchemy import SQLAlchemy

from api.base import TypeBase

db = SQLAlchemy(model_class=TypeBase)