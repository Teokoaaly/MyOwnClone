"""
MyOwnClone application factory.
Register all MyOwnClone blueprints here.
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from api.extensions import db
from api.models import (
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
from api.controllers.myownclone_public import myownclone_public_bp

# Import console blueprint
from api.controllers.console import bp as console_bp
from api.controllers.console.auth import auth_bp

# Import CLI commands
from api.commands.seed import seed_demo_data

migrate = Migrate()


def _validate_required_env():
    """Fail fast if required environment variables are missing.

    Security: DB_PASSWORD and REDIS_PASSWORD are OBLIGATORY.
    JWT_SECRET_KEY must be set to a strong value (no hardcoded fallback).
    API keys can be empty for development mode.
    """
    import secrets
    import warnings

    missing = []

    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        missing.append("DB_PASSWORD")
    elif db_password in ("postgres", "changeit"):
        raise ValueError(
            "SECURITY ERROR: DB_PASSWORD cannot be 'postgres' or 'changeit'. "
            "Set a strong password in environment variable."
        )

    redis_password = os.getenv("REDIS_PASSWORD")
    if not redis_password:
        missing.append("REDIS_PASSWORD")
    elif redis_password == "changeit":
        raise ValueError(
            "SECURITY ERROR: REDIS_PASSWORD cannot be 'changeit'. "
            "Set a strong password in environment variable."
        )

    jwt_secret = os.getenv("JWT_SECRET_KEY", "")
    if not jwt_secret or jwt_secret == "dev-secret-change-me":
        if os.getenv("FLASK_ENV") == "production":
            raise RuntimeError(
                "SECURITY ERROR: JWT_SECRET_KEY must be set to a strong value in production. "
                "Generate one with: python -c 'import secrets; print(secrets.token_urlsafe(64))'"
            )
        # Dev: auto-generate a random key so the app can start, but warn loudly.
        generated = secrets.token_urlsafe(32)
        os.environ["JWT_SECRET_KEY"] = generated
        warnings.warn(
            "WARNING: JWT_SECRET_KEY not set — using a randomly generated key for this session. "
            "Set JWT_SECRET_KEY explicitly for consistent token validation across restarts.",
            RuntimeWarning,
        )

    # IMPERSONATION_TOKEN_PEPPER — pepper for SHA-256 hashing of impersonation tokens
    impersonation_pepper = os.getenv("IMPERSONATION_TOKEN_PEPPER", "dev-pepper-rotate-in-prod")
    if impersonation_pepper in ("", "dev-pepper-rotate-in-prod"):
        if os.getenv("FLASK_ENV") == "production":
            raise RuntimeError(
                "SECURITY ERROR: IMPERSONATION_TOKEN_PEPPER must be set to a strong value in production. "
                "Generate one with: python -c 'import secrets; print(secrets.token_urlsafe(32))'"
            )
        generated = secrets.token_urlsafe(32)
        os.environ["IMPERSONATION_TOKEN_PEPPER"] = generated
        warnings.warn(
            "WARNING: IMPERSONATION_TOKEN_PEPPER not set — using a randomly generated key for this session. "
            "Set IMPERSONATION_TOKEN_PEPPER explicitly for consistent token validation across restarts.",
            RuntimeWarning,
        )

    if missing:
        raise EnvironmentError(
            f"FATAL: Required environment variables are missing: {', '.join(missing)}. "
            "The application cannot start without these credentials. "
            "See .env.example for required variables."
        )


def create_app():
    """Create and configure the Flask application."""
    # SECURITY: Validate config before doing anything else (fail-fast)
    _validate_required_env()
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('DB_USER', 'postgres')}:"
        f"{os.getenv('DB_PASSWORD')}@"  # No fallback - validated above
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
    # CORS — restrict to allowed origins in production
    allowed_origins = os.environ.get("ALLOWED_ORIGINS", "").split(",")
    if allowed_origins and allowed_origins[0]:
        CORS(app, origins=allowed_origins, supports_credentials=True)
  ***REMOVED***:
        CORS(app)  # dev fallback — en prod debe configurarse

    # Register CLI commands
    app.cli.add_command(seed_demo_data)

    # Register MyOwnClone blueprints
    register_myownclone_blueprints(app)

    return app


def register_myownclone_blueprints(app):
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(console_bp)
    app.register_blueprint(auth_bp)


# Flask uses this when FLASK_APP=app_factory
app = create_app()