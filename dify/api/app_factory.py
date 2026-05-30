"""Flask application factory for Dify.

This file registers all blueprints including clonify_public_bp.
Place in dify/api/ alongside app.py or __init__.py.
"""

from flask import Flask
from flask_compress import Compress

from configs import dify_config
from extensions.ext_database import db
from extensions.ext_login import login_manager
from extensions.ext_mail import mail
from extensions.ext_migrate import migrate
from extensions.ext_redis import redis_client
from extensions.ext_storage import storage

# Import all controllers to ensure blueprints are registered
# This must happen before app factory to allow route decorators to be evaluated


def create_app():
    """Application factory pattern used by Dify."""
    app = Flask(__name__)
    app.config.from_object(dify_config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    storage.init_app(app)
    Compress.init_app(app)

    # Register blueprints
    from controllers import bp as console_bp
    from controllers.console import api as console_api

    app.register_blueprint(console_bp)

    # ── CLONIFY PUBLIC BLUEPRINT (FIX BUG #1) ──────────────────────────────
    # Los endpoints públicos /api/clonify/public/* devolvían 404
    # porque clonify_public_bp nunca fue registrado.
    from controllers import clonify_public as clonify_public_module
    app.register_blueprint(clonify_public_module.clonify_public_bp)
    # ─────────────────────────────────────────────────────────────────────────

    # Register API namespaces (Flask-RESTX)
    console_api.init_app(app)

    with app.app_context():
        db.create_all()

    return app
