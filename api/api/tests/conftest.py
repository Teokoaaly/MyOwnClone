"""Test fixtures for MyOwnClone backend.

Run with:

    cd api/api && pytest

The conftest adds the package root to `sys.path` so tests can use the
package's own import style. The Flask app is built with an in-memory
SQLite database so no PostgreSQL is required for the smoke tests.
"""
from __future__ import annotations

import os
import sys

# Make the live package importable. `api/api/` is the package root; tests
# import from it directly.
_HERE = os.path.dirname(os.path.abspath(__file__))
_PKG_ROOT = os.path.abspath(os.path.join(_HERE, ".."))
if _PKG_ROOT not in sys.path:
    sys.path.insert(0, _PKG_ROOT)

# IMPORTANT: these env vars must be set BEFORE the app factory is imported,
# because the factory validates them at import time and refuses to start
# without them. We set safe test defaults here.
os.environ.setdefault("DB_PASSWORD", "test-db-password-not-real")
os.environ.setdefault("REDIS_PASSWORD", "test-redis-password-not-real")
os.environ.setdefault("FLASK_ENV", "development")
os.environ.setdefault("PLATFORM_ADMIN_TOKEN", "test-platform-admin-token")
os.environ.setdefault("IMPERSONATION_TOKEN_PEPPER", "test-pepper-not-real")
os.environ.setdefault("JWT_SECRET_KEY", "test-jwt-secret-not-real")
# Use a SQLite URI for tests. We override the URI the factory would build
# from env vars so the smoke tests can run without a PostgreSQL server.
# Using a file-based DB to avoid in-memory connection issues.
os.environ.setdefault(
    "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
)

import pytest

from app_factory import create_app
from extensions import db

# Ensure all models are imported so db.create_all() finds their tables.
# Without this, Base.metadata may not contain the model tables when
# SQLAlchemy tries to create them (especially with SQLite in-memory).
import api.models
import api.models.account
import api.models.analytics
import api.models.clone
import api.models.email
import api.models.meeting
import api.models.myownclone


@pytest.fixture()
def app():
    """Build a Flask app bound to a file-based SQLite database for tests."""
    # Set the URI BEFORE create_app so the engine is created with the right URI
    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    flask_app = create_app()
    flask_app.config["TESTING"] = True

    with flask_app.app_context():
        # Import all models to register them with Base.metadata
        import api.models.account
        import api.models.analytics
        import api.models.clone
        import api.models.email
        import api.models.meeting
        import api.models.myownclone

        # Debug: check tables in Base.metadata
        from api.base import Base
        print(f"Tables in Base.metadata: {list(Base.metadata.tables.keys())}")

        # Create tables using Base.metadata directly, catching unsupported type errors
        # (SQLite doesn't support ARRAY type used in clone/email models)
        from sqlalchemy.exc import UnsupportedCompilationError
        for table_name, table in Base.metadata.tables.items():
            try:
                table.create(db.engine, checkfirst=True)
                print(f"Created table: {table_name}")
            except UnsupportedCompilationError as e:
                print(f"Skipped table {table_name} (unsupported type): {e}")
            except Exception as e:
                print(f"Error creating table {table_name}: {e}")

        # Check if tables were created
        import sqlite3
        conn = sqlite3.connect('instance/test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"Tables in database: {[t[0] for t in tables]}")
        conn.close()

        yield flask_app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """A Flask test client."""
    return app.test_client()


@pytest.fixture()
def admin_headers():
    """Headers carrying the service-to-service admin token."""
    return {"X-Admin-Token": "test-platform-admin-token"}


@pytest.fixture()
def user_token(app):
    """Mint a JWT for a fake non-admin account."""
    import time
    from datetime import datetime, timedelta
    import jwt

    payload = {
        "sub": "test-user-id",
        "tenant_id": "test-tenant-id",
        "role": "member",
        "email": "user@example.com",
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(payload, "test-jwt-secret-not-real", algorithm="HS256")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture()
def admin_token(app):
    """Mint a JWT for a fake platform-admin account.

    Note: with the in-memory SQLite fixture the Account/Tenant tables are
    empty, so the role is taken from the JWT claim (the `g.account_role`
    fast path in `admin_platform._is_platform_admin`)."""
    import jwt
    from datetime import datetime, timedelta

    payload = {
        "sub": "test-admin-id",
        "tenant_id": "platform",
        "role": "platform_admin",
        "email": "admin@example.com",
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(payload, "test-jwt-secret-not-real", algorithm="HS256")
    return {"Authorization": f"Bearer {token}"}
