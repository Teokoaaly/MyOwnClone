"""
Pytest fixtures for MyOwnClone API security tests.

Environment variables are set BEFORE the app factory is imported
so that _validate_required_env() and _setup_dev_keys() pass cleanly.
"""
import os
import pytest
from typing import Dict, Any, Optional

# ═══════════════════════════════════════════════════════════════════════════════
# Environment setup — must happen BEFORE any api imports
# ═══════════════════════════════════════════════════════════════════════════════
os.environ.setdefault("FLASK_ENV", "testing")
os.environ.setdefault("DB_PASSWORD", "test-db-password-not-default")
os.environ.setdefault("REDIS_PASSWORD", "test-redis-password-not-default")
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_PORT", "5432")
os.environ.setdefault("DB_NAME", "myownclone_test")
os.environ.setdefault("JWT_SECRET_KEY", "test-jwt-secret-key-for-ci-smoke-tests-only")
os.environ.setdefault(
    "IMPERSONATION_TOKEN_PEPPER",
    "test-impersonation-pepper-for-ci-smoke-tests",
)
os.environ.setdefault("SECRET_KEY", "test-flask-secret-key-for-ci")


# ═══════════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════════

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
def create_attack_request(client):
    """
    Factory fixture that creates a function to send attack payloads to endpoints.

    Returns a callable that accepts:
        - method: HTTP method (GET, POST, PUT, DELETE, etc.)
        - endpoint: URL path
        - payload: Data to send (dict for form, string for raw body)
        - headers: Optional dict of additional headers
        - content_type: Optional content type (default: form-encoded)

    Returns a Flask test client response.
    """
    def _make_attack_request(
        method: str,
        endpoint: str,
        payload: Any = None,
        headers: Optional[Dict[str, str]] = None,
        content_type: str = "application/x-www-form-urlencoded",
    ):
        headers = headers or {}
        method = method.upper()

        if method == "GET":
            return client.get(endpoint, headers=headers)
        elif method == "POST":
            return client.post(
                endpoint, data=payload, headers=headers, content_type=content_type
            )
        elif method == "PUT":
            return client.put(
                endpoint, data=payload, headers=headers, content_type=content_type
            )
        elif method == "DELETE":
            return client.delete(endpoint, headers=headers)
        elif method == "PATCH":
            return client.patch(
                endpoint, data=payload, headers=headers, content_type=content_type
            )
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    return _make_attack_request


@pytest.fixture
def mock_jwt_token():
    """
    Returns a mock JWT token for testing authentication-related security checks.

    NOTE: This is an intentionally INVALID token for testing 401 responses.
    For tests that need a valid token, a real JWT must be generated with
    a valid secret key against a running database.
    """
    return "Bearer mock-jwt-token-for-security-testing"


@pytest.fixture
def rate_limit_headers():
    """
    Returns headers dict configured to test rate limiting behavior.

    Includes X-Forwarded-For to simulate various IP sources.
    """
    return {
        "X-Forwarded-For": "10.0.0.1",
        "X-Real-IP": "10.0.0.1",
        "User-Agent": "SecurityTestBot/1.0",
    }


@pytest.fixture
def authenticated_client(client, mock_jwt_token):
    """
    Returns a test client with valid-looking auth headers for testing
    authenticated endpoints that should reject unauthorized requests.
    """
    client.environ_base["HTTP_AUTHORIZATION"] = mock_jwt_token
    return client


@pytest.fixture
def admin_headers():
    """
    Headers for an admin authenticated user (mock).
    """
    return {"Authorization": "Bearer mock-admin-user-token"}


@pytest.fixture
def user_headers():
    """
    Headers for a normal (non-admin) authenticated user (mock).
    """
    return {"Authorization": "Bearer mock-normal-user-token"}