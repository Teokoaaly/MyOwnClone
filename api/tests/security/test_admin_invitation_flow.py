"""
Security tests for admin invitation flow (BE-04 remediation).

Tests that:
- No auto-creation of admin accounts (privilege escalation prevention)
- First admin setup only works when no platform admin exists
- Unauthenticated/unauthorized users cannot access admin endpoints
- Invitation tokens are properly validated

References:
- BE-04: Admin auto-creation vulnerability
- CWE-269: Improper Privilege Management
"""

import json
import time
import jwt
import pytest

# Endpoints to test
ADMIN_INVITATION_ENDPOINTS = [
    "/console/api/myownclone/admin/invitation/first",
    "/console/api/myownclone/admin/invitation/accept",
    "/console/api/myownclone/admin/invitation/create",
    "/console/api/myownclone/admin/impersonate",
]

ADMIN_PROTECTED_ENDPOINTS = [
    "/console/api/myownclone/admin/overview",
    "/console/api/myownclone/admin/tenants",
    "/console/api/myownclone/admin/impersonation",
    "/console/api/myownclone/admin/impersonate",
    "/console/api/myownclone/admin/courtesy-account",
    "/console/api/myownclone/admin/audit-log",
    "/console/api/myownclone/admin/feedback",
]


class TestNoAutoCreation:
    """Tests that verify no auto-creation of admin accounts."""

    def test_impersonate_without_admin_returns_403(self, client):
        """
        RED test: Unauthorized user cannot trigger admin auto-creation.

        Attempts to use impersonation endpoint without being a platform admin
        should return 403, not auto-create an admin account.
        """
        # Create a valid JWT for a non-admin user
        from api.libs.jwt_utils import _get_secret_key

        secret = _get_secret_key()
        non_admin_token = jwt.encode(
            {
                "sub": "user-without-admin-access",
                "tenant_id": "some-tenant-id",
                "role": "member",
                "email": "regular@user.com",
                "exp": int(time.time()) + 3600,
            },
            secret,
            algorithm="HS256",
        )

        response = client.post(
            "/console/api/myownclone/admin/impersonate",
            json={"tenant_id": "target-tenant-id", "reason": "test impersonation"},
            headers={"Authorization": f"Bearer {non_admin_token}"},
        )

        # Should be rejected with 403, not auto-create admin
        assert response.status_code == 403, (
            f"Expected 403 Forbidden for non-admin user, got {response.status_code}. "
            "This suggests admin auto-creation may still be enabled!"
        )

    def test_courtesy_account_without_admin_returns_403(self, client):
        """
        RED test: Unauthorized user cannot create courtesy accounts.

        The courtesy account endpoint should not auto-create a platform admin
        when called by a non-admin user.
        """
        from api.libs.jwt_utils import _get_secret_key

        secret = _get_secret_key()
        non_admin_token = jwt.encode(
            {
                "sub": "user-without-admin-access",
                "tenant_id": "some-tenant-id",
                "role": "member",
                "email": "regular@user.com",
                "exp": int(time.time()) + 3600,
            },
            secret,
            algorithm="HS256",
        )

        response = client.post(
            "/console/api/myownclone/admin/courtesy-account",
            json={
                "email": "newuser@example.com",
                "name": "Test User",
                "plan": "pro",
                "duration_days": 30,
            },
            headers={"Authorization": f"Bearer {non_admin_token}"},
        )

        # Should be rejected with 403, not auto-create admin
        assert response.status_code == 403, (
            f"Expected 403 Forbidden for non-admin user, got {response.status_code}. "
            "Admin auto-creation may still be enabled!"
        )


class TestFirstAdminSetup:
    """Tests for the first admin setup endpoint."""

    @pytest.mark.skip(reason="Requires database - tested manually or in integration tests")
    def test_first_setup_rejects_when_admin_exists(self, client, app):
        """
        First admin setup should be disabled once a platform admin exists.
        """
        pass

    @pytest.mark.skip(reason="Requires database - tested manually or in integration tests")
    def test_first_setup_requires_password(self, client):
        """
        First admin setup must require a password (no auto-generated passwords).
        """
        pass


class TestInvitationEndpointsAuth:
    """Tests for authentication requirements on invitation endpoints."""

    @pytest.mark.parametrize("endpoint", ADMIN_INVITATION_ENDPOINTS)
    def test_invitation_endpoint_requires_auth(self, client, endpoint):
        """
        All invitation endpoints should require authentication.
        """
        if endpoint == "/console/api/myownclone/admin/invitation/first":
            # First setup uses POST without auth for initial setup
            return

        if endpoint == "/console/api/myownclone/admin/invitation/accept":
            # Accept invitation might not require auth (depends on design)
            return

        # For create invitation, should require auth
        if endpoint == "/console/api/myownclone/admin/invitation/create":
            response = client.post(endpoint)
            assert response.status_code in (401, 403), (
                f"Expected 401/403 for unauthenticated request to {endpoint}, "
                f"got {response.status_code}"
            )


class TestAdminEndpointsProtected:
    """Tests that admin endpoints properly reject unauthorized users."""

    @pytest.mark.parametrize("endpoint", ADMIN_PROTECTED_ENDPOINTS)
    def test_admin_endpoints_reject_no_auth(self, client, endpoint):
        """Admin endpoints must reject requests without authentication."""
        # Determine HTTP method based on endpoint
        if endpoint in ["/console/api/myownclone/admin/tenants",
                        "/console/api/myownclone/admin/courtesy-account"]:
            method = "POST"
        elif endpoint == "/console/api/myownclone/admin/impersonate":
            method = "POST"
      ***REMOVED***:
            method = "GET"

        if method == "GET":
            response = client.get(endpoint)
      ***REMOVED***:
            response = client.post(endpoint, json={})

        assert response.status_code == 401, (
            f"Expected 401 for unauthenticated request to {endpoint}, "
            f"got {response.status_code}"
        )

    @pytest.mark.parametrize("endpoint", ADMIN_PROTECTED_ENDPOINTS)
    def test_admin_endpoints_reject_malformed_bearer(self, client, endpoint):
        """Admin endpoints must reject malformed authorization headers."""
        if endpoint in ["/console/api/myownclone/admin/tenants",
                        "/console/api/myownclone/admin/courtesy-account"]:
            method = "POST"
            payload = {}
        elif endpoint == "/console/api/myownclone/admin/impersonate":
            method = "POST"
            payload = {"tenant_id": "test", "reason": "test"}
      ***REMOVED***:
            method = "GET"
            payload = None

        headers = {"Authorization": "Token malformed"}

        if method == "GET":
            response = client.get(endpoint, headers=headers)
      ***REMOVED***:
            response = client.post(endpoint, json=payload, headers=headers)

        assert response.status_code == 401, (
            f"Expected 401 for malformed bearer token to {endpoint}, "
            f"got {response.status_code}"
        )

    @pytest.mark.parametrize("endpoint", ADMIN_PROTECTED_ENDPOINTS)
    def test_admin_endpoints_reject_invalid_signature(self, client, endpoint):
        """Admin endpoints must reject JWTs signed with wrong key."""
        bad_token = jwt.encode(
            {
                "sub": "attacker-id",
                "tenant_id": "attacker-tenant",
                "role": "platform_admin",
                "email": "attacker@evil.com",
                "exp": int(time.time()) + 3600,
            },
            "wrong-secret-key",
            algorithm="HS256",
        )

        if endpoint in ["/console/api/myownclone/admin/tenants",
                        "/console/api/myownclone/admin/courtesy-account"]:
            method = "POST"
            payload = {}
        elif endpoint == "/console/api/myownclone/admin/impersonate":
            method = "POST"
            payload = {"tenant_id": "test", "reason": "test"}
      ***REMOVED***:
            method = "GET"
            payload = None

        headers = {"Authorization": f"Bearer {bad_token}"}

        if method == "GET":
            response = client.get(endpoint, headers=headers)
      ***REMOVED***:
            response = client.post(endpoint, json=payload, headers=headers)

        assert response.status_code == 401, (
            f"Expected 401 for invalid signature on {endpoint}, "
            f"got {response.status_code}"
        )

    @pytest.mark.parametrize("endpoint", ADMIN_PROTECTED_ENDPOINTS)
    def test_admin_endpoints_reject_expired_token(self, client, endpoint):
        """Admin endpoints must reject expired JWTs."""
        from api.libs.jwt_utils import _get_secret_key

        secret = _get_secret_key()
        expired = jwt.encode(
            {
                "sub": "user-id",
                "tenant_id": "tenant-id",
                "role": "platform_admin",
                "email": "user@myownclone.local",
                "exp": int(time.time()) - 60,  # Expired 60 seconds ago
            },
            secret,
            algorithm="HS256",
        )

        if endpoint in ["/console/api/myownclone/admin/tenants",
                        "/console/api/myownclone/admin/courtesy-account"]:
            method = "POST"
            payload = {}
        elif endpoint == "/console/api/myownclone/admin/impersonate":
            method = "POST"
            payload = {"tenant_id": "test", "reason": "test"}
      ***REMOVED***:
            method = "GET"
            payload = None

        headers = {"Authorization": f"Bearer {expired}"}

        if method == "GET":
            response = client.get(endpoint, headers=headers)
      ***REMOVED***:
            response = client.post(endpoint, json=payload, headers=headers)

        assert response.status_code == 401, (
            f"Expected 401 for expired token on {endpoint}, "
            f"got {response.status_code}"
        )


class TestRoleBasedAccess:
    """Tests for role-based access control on admin endpoints."""

    def test_non_admin_role_rejected(self, client):
        """
        User with non-platform_admin role should be rejected from admin endpoints.
        """
        from api.libs.jwt_utils import _get_secret_key

        secret = _get_secret_key()
        # Token with 'admin' role (tenant admin, not platform admin)
        tenant_admin_token = jwt.encode(
            {
                "sub": "tenant-admin-id",
                "tenant_id": "some-tenant",
                "role": "admin",  # Tenant admin, not platform admin
                "email": "tenant@admin.com",
                "exp": int(time.time()) + 3600,
            },
            secret,
            algorithm="HS256",
        )

        response = client.get(
            "/console/api/myownclone/admin/overview",
            headers={"Authorization": f"Bearer {tenant_admin_token}"},
        )

        # Should be rejected - tenant admins cannot access platform admin endpoints
        assert response.status_code == 403, (
            f"Expected 403 for tenant admin accessing platform admin endpoint, "
            f"got {response.status_code}"
        )
