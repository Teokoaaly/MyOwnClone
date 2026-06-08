# extensions/ext_database.py
"""SQLAlchemy database extension."""
from flask_sqlalchemy import SQLAlchemy

from api.base import TypeBase

db = SQLAlchemy(model_class=TypeBase)
