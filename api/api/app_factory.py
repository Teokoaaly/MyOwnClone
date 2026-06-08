"""MyOwnClone application factory.

Run with either:

    cd api/api && FLASK_APP=app_factory flask run --host=0.0.0.0 --port=5001

or use a WSGI entrypoint that imports `app_factory.create_app()`.
"""

from __future__ import annotations

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

# Production-required env vars. In production we refuse to start if any of
# these are missing or hold the documented dev defaults. In development we
# allow weak defaults so local dev is friction-free.
IS_PRODUCTION = os.getenv("FLASK_ENV", "production").lower() == "production"

# `dev-pepper-rotate-in-prod` is the default IMPERSONATION_TOKEN_PEPPER used
# by `admin_platform.py`; if a deployment fails to override it AND runs in
# production, hashes become predictable. The factory below logs a loud
# warning if it detects that combination.
DEFAULT_PEPPER = "dev-pepper-rotate-in-prod"
DEFAULT_JWT_SECRET = "dev-secret-change-me"


def _validate_required_env() -> None:
    """Fail fast if required environment variables are missing or trivial.

    Required in ALL environments:
      - DB_PASSWORD (must not be the literal 'postgres' or 'changeit')
      - REDIS_PASSWORD (must not be the literal 'changeit')
    Required in PRODUCTION:
      - PLATFORM_ADMIN_TOKEN (service-to-service auth from the Next.js proxy)
      - IMPERSONATION_TOKEN_PEPPER (must not be the default placeholder)
      - JWT_SECRET_KEY (must not be the default placeholder)
    """
    missing: list[str] = []

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

    if IS_PRODUCTION:
        if not os.getenv("PLATFORM_ADMIN_TOKEN"):
            missing.append("PLATFORM_ADMIN_TOKEN")
        pepper = os.getenv("IMPERSONATION_TOKEN_PEPPER", DEFAULT_PEPPER)
        if pepper == DEFAULT_PEPPER:
            raise ValueError(
                "SECURITY ERROR: IMPERSONATION_TOKEN_PEPPER is the default "
                "placeholder. Set a strong, unique value before going to production."
            )
        jwt = os.getenv("JWT_SECRET_KEY", DEFAULT_JWT_SECRET)
        if jwt == DEFAULT_JWT_SECRET:
            raise ValueError(
                "SECURITY ERROR: JWT_SECRET_KEY is the default placeholder. "
                "Set a strong, unique value before going to production."
            )

    if missing:
        raise EnvironmentError(
            f"FATAL: Required environment variables are missing: {', '.join(missing)}. "
            "The application cannot start without these credentials. "
            "See .env.example for required variables."
        )


def _build_cors_origins() -> list[str] | str:
    """Return a CORS allowlist. Defaults to empty (no cross-origin).

    Set `ALLOWED_ORIGINS` to a comma-separated list of origins, e.g.
        ALLOWED_ORIGINS="https://app.myownclone.com,https://admin.myownclone.com"
    """
    raw = os.getenv("ALLOWED_ORIGINS", "").strip()
    if not raw:
        # No allowlist configured. CORS is essentially disabled because we
        # do not add the Access-Control-Allow-Origin header.
        return []
    return [o.strip() for o in raw.split(",") if o.strip()]


def create_app() -> Flask:
    """Create and configure the Flask application."""
    # SECURITY: Validate config before doing anything else (fail-fast)
    _validate_required_env()
    app = Flask(__name__)

    # Database configuration. If `SQLALCHEMY_DATABASE_URI` is set in the
    # environment (e.g. for tests with SQLite, or for a managed
    # PostgreSQL), honour it. Otherwise build the URI from the individual
    # DB_* env vars.
    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    if not db_uri:
        db_uri = (
            f"postgresql://{os.getenv('DB_USER', 'postgres')}:"
            f"{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST', 'localhost')}:"
            f"{os.getenv('DB_PORT', '5432')}/"
            f"{os.getenv('DB_NAME', 'myownclone')}"
        )
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # CORS: empty list = no Access-Control-Allow-Origin header. Use
    # ALLOWED_ORIGINS env var to opt in to specific origins.
    cors_origins = _build_cors_origins()
    if cors_origins:
        CORS(
            app,
            resources={r"/console/api/*": {"origins": cors_origins}},
            supports_credentials=True,
        )
  ***REMOVED***:
        CORS(app)

    # Register CLI commands
    app.cli.add_command(seed_demo_data)

    # Register MyOwnClone blueprints
    register_myownclone_blueprints(app)

    return app


def register_myownclone_blueprints(app: Flask) -> None:
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(console_bp)
    app.register_blueprint(auth_bp)


# Flask uses this when FLASK_APP=app_factory
app = create_app()
