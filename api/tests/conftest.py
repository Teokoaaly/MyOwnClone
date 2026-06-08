"""
Pytest fixtures for MyOwnClone API tests.

Environment variables are set BEFORE the app factory is imported
so that _validate_required_env() and _setup_dev_keys() pass cleanly.
"""
import os
import pytest

# ═══════════════════════════════════════════════════════════════════════
# Environment setup — must happen BEFORE any api imports
# ═══════════════════════════════════════════════════════════════════════
os.environ.setdefault("FLASK_ENV", "testing")
os.environ.setdefault("DB_PASSWORD", "test-db-password-not-default")
os.environ.setdefault("REDIS_PASSWORD", "test-redis-password-not-default")
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_PORT", "5432")
os.environ.setdefault("DB_NAME", "myownclone_test")
# JWT_SECRET_KEY must be ≥32 chars (_get_secret_key() enforces this)
os.environ.setdefault(
    "JWT_SECRET_KEY",
    "test-jwt-secret-key-for-ci-smoke-tests-only",
)
os.environ.setdefault(
    "IMPERSONATION_TOKEN_PEPPER",
    "test-impersonation-pepper-for-ci-smoke-tests",
)
os.environ.setdefault("SECRET_KEY", "test-flask-secret-key-for-ci")


@pytest.fixture(scope="session")
def app():
    """Create Flask app for testing (session-scoped, one per test run)."""
    from api.app_factory import create_app

    _app = create_app()
    _app.config["TESTING"] = True
    return _app


@pytest.fixture
def client(app):
    """Flask test client — fresh per test function."""
    return app.test_client()


@pytest.fixture
def user_headers():
    """
    Headers for a normal (non-admin) authenticated user.

    NOTE: These are mock headers. The JWT token is intentionally invalid
    so that tests checking for 401 (no auth) work correctly.
    For tests that need a REAL authenticated non-admin user (expecting 403
    from _is_platform_admin), the DB must be seeded with a non-admin account
    and a valid JWT must be generated. That requires a running PostgreSQL
    instance — see CI pipeline (.github/workflows/ci.yml) for the full setup.
    """
    return {"Authorization": "Bearer mock-normal-user-token"}


@pytest.fixture
def admin_headers():
    """
    Headers for an admin authenticated user.

    NOTE: Same caveat as user_headers — this is a mock.
    For 200 responses, a real admin account + valid JWT + running DB is needed.
    """
    return {"Authorization": "Bearer mock-admin-user-token"}
