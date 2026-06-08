"""Shared test fixtures for the MyOwnClone backend."""
import os
import sys
from pathlib import Path

# Add repo root to sys.path so 'import api.*' works
_repo_root = Path(__file__).resolve().parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

# Provide required env vars BEFORE any app imports
os.environ.setdefault("DB_PASSWORD", "test_password")
os.environ.setdefault("REDIS_PASSWORD", "test_password")
os.environ.setdefault("JWT_SECRET_KEY", "x" * 64)
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_USER", "postgres")
os.environ.setdefault("DB_NAME", "myownclone")
os.environ.setdefault("FLASK_ENV", "development")
os.environ.setdefault("WEAVIATE_API_KEY", "test-weaviate-key")


import pytest


@pytest.fixture
def app():
    """Create a Flask app instance for tests."""
    from api.app_factory import create_app
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture
def jwt_token(app):
    """Generate a valid JWT for the test user."""
    from api.controllers.console.auth import _get_secret_key
    import jwt as pyjwt
    payload = {
        "sub": "test-account-id",
        "tenant_id": "test-tenant",
        "role": "admin",
        "email": "admin@test.local",
    }
    return pyjwt.encode(payload, _get_secret_key(), algorithm="HS256")


@pytest.fixture
def auth_headers(jwt_token):
    """Authorization headers with a valid Bearer token."""
    return {"Authorization": f"Bearer {jwt_token}"}
