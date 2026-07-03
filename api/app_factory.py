"""
MyOwnClone application factory.
Register all MyOwnClone blueprints here.
"""
import os
import uuid
from datetime import datetime, timezone

from api.libs.security_checks import assert_production_secrets

from flask import Flask, jsonify
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


def _redis_ready() -> tuple[bool, str | None]:
    host = os.getenv("REDIS_HOST", "").strip()
    if not host:
        return True, "not_configured"

    try:
        import redis

        # Soporte TLS: si REDIS_TLS=true, conectar con SSL.
        # Por defecto asume TLS cuando el puerto es 6380.
        redis_tls = os.getenv("REDIS_TLS", "false").strip().lower() == "true"
        redis_port = int(os.getenv("REDIS_PORT", "6379"))
        if not redis_tls and redis_port == 6380:
            redis_tls = True  # puerto 6380 implica TLS en este stack

        client_kwargs = {
            "host": host,
            "port": redis_port,
            "password": os.getenv("REDIS_PASSWORD") or None,
            "socket_connect_timeout": 1.0,
            "socket_timeout": 1.0,
        }
        if redis_tls:
            client_kwargs["ssl"] = True
            client_kwargs["ssl_certfile"] = "/etc/redis/tls/redis.crt"
            client_kwargs["ssl_keyfile"] = "/etc/redis/tls/redis.key"
            client_kwargs["ssl_ca_certs"] = "/etc/redis/tls/ca.crt"
            # Cert fue generado con otro hostname; en la red Docker solo usamos 'redis'
            client_kwargs["ssl_check_hostname"] = False

        client = redis.Redis(**client_kwargs)
        client.ping()
        return True, None
    except Exception as exc:  # pragma: no cover - exact client failures vary
        return False, str(exc)


def create_app():
    """Create and configure the Flask application."""
    # SECURITY: Validate config before doing anything else (fail-fast)
    assert_production_secrets()
    _setup_dev_keys()
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

    # Register CLI commands
    app.cli.add_command(seed_demo_data)

    # Register MyOwnClone blueprints
    register_myownclone_blueprints(app)
    register_health_routes(app)

    return app


def register_health_routes(app):
    """Register liveness/readiness endpoints used by Docker and probes."""

    @app.get("/healthz")
    def healthz():
        """Chequeo detallado: DB + Redis + Ollama. Devuelve 503 si algo falla."""
        import os
        import requests

        checks: dict[str, str] = {}
        all_ok = True

        # 1. Database
        try:
            from sqlalchemy import text
            db.session.execute(text("SELECT 1"))
            checks["database"] = "ok"
        except Exception as exc:
            db.session.rollback()
            checks["database"] = f"error: {exc}"
            all_ok = False

        # 2. Redis
        redis_ok, redis_error = _redis_ready()
        if redis_ok:
            checks["redis"] = redis_error or "ok"
        else:
            checks["redis"] = f"error: {redis_error}"
            all_ok = False

        # 3. Ollama (si está configurado como embedding local)
        ollama_url = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
        try:
            resp = requests.get(f"{ollama_url}/api/tags", timeout=2)
            if resp.status_code == 200:
                checks["ollama"] = "ok"
            else:
                checks["ollama"] = f"error: HTTP {resp.status_code}"
                all_ok = False
        except Exception as exc:
            checks["ollama"] = f"unreachable: {exc}"
            # Ollama no es crítico si hay fallback, no degrada a 503
            # pero se reporta para visibilidad

        payload_status = "ready" if all_ok else "degraded"
        http_status = 200 if all_ok else 503
        return jsonify({"status": payload_status, "checks": checks}), http_status

    @app.get("/readyz")
    def readyz():
        """Liveness simple: solo verifica que la app responde. Para Docker healthcheck."""
        return jsonify({"status": "ready"}), 200


def register_myownclone_blueprints(app):
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(console_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(deploy_bp)


# Flask uses this when FLASK_APP=app_factory
app = create_app()
