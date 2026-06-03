"""
MyOwnClone application factory.
Register all MyOwnClone blueprints here.
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from extensions import db
from models import (
    Availability,
    Booking,
    CloneConfig,
    CloneModePrompt,
    CloneSilo,
    CreatorMemory,
    CreatorMemoryType,
    EmailInbound,
    EmailTemplate,
    MeetingType_,
    Product,
)

# Import public blueprint
from controllers.myownclone_public import myownclone_public_bp

# Import console blueprint
from controllers.console import bp as console_bp

# Import CLI commands
from commands.seed import seed_demo_data

migrate = Migrate()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('DB_USER', 'postgres')}:"
        f"{os.getenv('DB_PASSWORD', 'postgres')}@"
        f"{os.getenv('DB_HOST', 'localhost')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'myownclone')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register CLI commands
    app.cli.add_command(seed_demo_data)

    # Register MyOwnClone blueprints
    register_myownclone_blueprints(app)

    return app


def register_myownclone_blueprints(app):
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(console_bp)


# Flask uses this when FLASK_APP=app_factory
app = create_app()