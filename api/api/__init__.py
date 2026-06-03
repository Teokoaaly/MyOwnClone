# Re-export app from app_factory for FLASK_APP compatibility
# This allows `flask run` to work when FLASK_APP=app_factory
from app_factory import app, create_app

__all__ = ["app", "create_app"]