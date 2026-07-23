"""
MyOwnClone application factory.
Register all MyOwnClone blueprints here.
"""
import logging
import os
import uuid
from datetime import datetime

from api.libs.security_checks import assert_production_secrets

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
# Import base models so Alembic/SQLAlchemy metadata includes them
from api.models.account import Account, Tenant  # noqa: F401 — needed for metadata

# Import public blueprint
from api.controllers.myownclone_public import myownclone_public_bp

# Import console blueprint
from api.controllers.console import bp as console_bp
from api.controllers.console.auth import auth_bp

# Import CLI commands
from api.commands.seed import seed_demo_data

from api.core.readiness import register_health_routes

# Import deploy blueprint
from api.controllers.deploy import deploy_bp

migrate = Migrate()

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - dotenv is optional in some runtimes
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"), override=False)


def _setup_dev_keys():
    """Generate random keys for development mode when not set."""
    import secrets
    import warnings

    jwt_secret = os.getenv("JWT_SECRET_KEY", "")
    if not jwt_secret or jwt_secret == "dev-secret-change-me":
        generated = secrets.token_urlsafe(32)
        os.environ["JWT_SECRET_KEY"] = generated
        warnings.warn(
            "WARNING: JWT_SECRET_KEY not set — using a randomly generated key for this session. "
            "Set JWT_SECRET_KEY explicitly for consistent token validation across restarts.",
            RuntimeWarning,
        )

    impersonation_pepper = os.getenv("IMPERSONATION_TOKEN_PEPPER", "dev-pepper-rotate-in-prod")
    if impersonation_pepper in ("", "dev-pepper-rotate-in-prod"):
        generated = secrets.token_urlsafe(32)
        os.environ["IMPERSONATION_TOKEN_PEPPER"] = generated
        warnings.warn(
            "WARNING: IMPERSONATION_TOKEN_PEPPER not set — using a randomly generated key for this session. "
            "Set IMPERSONATION_TOKEN_PEPPER explicitly for consistent token validation across restarts.",
            RuntimeWarning,
        )


def _parse_origins() -> list[str]:
    raw = os.getenv("ALLOWED_ORIGINS", "")
    origins = [o.strip() for o in raw.split(",") if o.strip()]
    if not origins:
        if os.getenv("FLASK_ENV", "production") == "development":
            # Sensible defaults only in dev
            return ["http://localhost:3000", "http://127.0.0.1:3000"]
        raise ValueError(
            "ALLOWED_ORIGINS environment variable must be set in production. "
            "Specify comma-separated origins, e.g., https://example.com,https://app.example.com"
        )
    return origins


def _database_uri() -> str:
    """Return the SQLAlchemy database URI.

    DATABASE_URL wins when provided so CI, staging, and hosted databases can
    supply a single connection string. Local Docker deployments can keep using
    the DB_* variables. The project standardizes on psycopg2-compatible
    postgresql:// URLs.
    """
    database_url = os.getenv("DATABASE_URL", "").strip()
    if database_url:
        if database_url.startswith("postgresql+psycopg://"):
            return "postgresql://" + database_url.removeprefix("postgresql+psycopg://")
        return database_url

    return (
        f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST', 'localhost')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'myownclone')}"
    )


def create_app():
    """Create and configure the Flask application."""
    # SECURITY: Validate config before doing anything else (fail-fast)
    assert_production_secrets()
    _setup_dev_keys()

    # T2.12: Sentry error tracking (solo si SENTRY_DSN está configurado)
    sentry_dsn = os.environ.get("SENTRY_DSN", "").strip()
    if sentry_dsn:
        try:
            import sentry_sdk
            from sentry_sdk.integrations.flask import FlaskIntegration
            from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
            from sentry_sdk.integrations.redis import RedisIntegration

            sentry_sdk.init(
                dsn=sentry_dsn,
                integrations=[
                    FlaskIntegration(),
                    SqlalchemyIntegration(),
                    RedisIntegration(),
                ],
                # Capturar 10% de transacciones para performance
                traces_sample_rate=float(os.environ.get("SENTRY_TRACES_SAMPLE_RATE", "0.1")),
                # Capturar errores de profiling 100% (es gratis)
                profiles_sample_rate=1.0,
                environment=os.environ.get("FLASK_ENV", "production"),
                release=f"myownclone-api@{os.environ.get('RELEASE_ID', 'dev')}",
            )
            logging.getLogger(__name__).info("Sentry inicializado: %s...", sentry_dsn[:30])
        except ImportError:
            logging.getLogger(__name__).warning(
                "SENTRY_DSN configurado pero sentry-sdk no instalado. "
                "Anade 'sentry-sdk[flask]>=2.0.0' a requirements.txt"
            )
        except Exception as exc:
            logging.getLogger(__name__).warning("Sentry init fallo (no-fatal): %s", exc)

    app = Flask(__name__)

    # Custom JSON encoder for UUID/datetime serialization
    from flask.json.provider import DefaultJSONProvider

    class CustomJSONProvider(DefaultJSONProvider):
        def default(self, obj):
            if isinstance(obj, uuid.UUID):
                return str(obj)
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    app.json = CustomJSONProvider(app)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = _database_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    # CORS — parsed origins with dev defaults, restrictive resources, headers, max_age (phase 0.3)
    CORS(
        app,
        resources={r"/*": {"origins": _parse_origins()}},
        supports_credentials=True,
        allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
        expose_headers=["X-Request-Id"],
        max_age=600,
    )

    # Register CLI commands (P1.10.04 / H-13).
    # Antes solo se registraba seed_demo_data; los demas comandos
    # (@click.command) estaban definidos pero inalcanzables via `flask ...`.
    app.cli.add_command(seed_demo_data)
    # Lazy imports to avoid loading heavy modules at app import time.
    from api.commands.crypto import (
        generate_master_key_command,
        refresh_cost_daily_rollup_command,
        rotate_secrets_key_command,
    )
    from api.commands.ai_backfill import ai_backfill_from_env_command
    from api.commands.reindex import reindex_command

    app.cli.add_command(generate_master_key_command)
    app.cli.add_command(rotate_secrets_key_command)
    app.cli.add_command(refresh_cost_daily_rollup_command)
    app.cli.add_command(ai_backfill_from_env_command)
    app.cli.add_command(reindex_command)

    # Register MyOwnClone blueprints
    register_myownclone_blueprints(app)
    register_health_routes(app)

    # T3.6: Prometheus metrics endpoint
    from api.core.metrics import register_metrics_endpoint
    register_metrics_endpoint(app)

    return app


def register_myownclone_blueprints(app):
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(console_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(deploy_bp)


# Flask uses this when FLASK_APP=app_factory
app = create_app()
