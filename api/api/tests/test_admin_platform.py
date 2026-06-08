"""Smoke tests for the platform-admin endpoints.

Each test verifies the auth contract and (where the fixture allows) the
response shape. Tests run against an in-memory SQLite DB; no PostgreSQL
is required.

Markers:
    admin — tests that exercise /console/api/myownclone/admin/*
"""

from __future__ import annotations

import json


# ---------------------------------------------------------------------------
# Auth contract: every admin endpoint must reject unauthenticated requests
# ---------------------------------------------------------------------------


def test_overview_requires_auth(client):
    """No auth header → 401."""
    resp = client.get("/console/api/myownclone/admin/overview")
    assert resp.status_code == 401, resp.data
    payload = resp.get_json()
    assert payload["error"] == "Unauthorized — missing Bearer token"


def test_overview_rejects_non_admin_user(client, user_token):
    """A non-admin Bearer JWT must be rejected (DB role lookup returns
    nothing in the in-memory fixture, so the controller falls back to the
    DB lookup path which finds no row → not platform_admin). The actual
    status code is either 401 (no session resolved) or 403 (session
    resolved but role wrong); we accept either as "rejected"."""
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=user_token
    )
    assert resp.status_code in (401, 403), resp.data


def test_overview_accepts_service_token(client, admin_headers):
    """The X-Admin-Token service path grants access regardless of DB rows."""
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=admin_headers
    )
    # The service-token path in login.py sets g.account_role="platform_admin"
    # and returns 200 immediately. The query may return zeros / empty, but
    # the contract is satisfied.
    assert resp.status_code == 200, resp.data
    payload = resp.get_json()
    # Required keys in the overview response.
    for key in (
        "total_tenants",
        "active_tenants",
        "total_clones",
        "mrr_cents",
        "mrr_display",
        "total_costs_cents",
        "total_costs_display",
        "margin_cents",
        "margin_display",
        "plan_breakdown",
        "generated_at",
    ):
        assert key in payload, f"missing {key} in overview response"


def test_overview_admin_jwt_with_platform_admin_role(client, admin_token):
    """A Bearer JWT whose `role` claim is platform_admin must also work
    via the g.account_role fast path."""
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=admin_token
    )
    assert resp.status_code == 200, resp.data


# ---------------------------------------------------------------------------
# Plan breakdown shape: 5 canonical plans, all defaulted to 0
# ---------------------------------------------------------------------------


def test_overview_plan_breakdown_has_canonical_plans(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=admin_headers
    )
    assert resp.status_code == 200
    breakdown = resp.get_json()["plan_breakdown"]
    for plan in ("trial", "basic", "pro", "scale", "enterprise"):
        assert plan in breakdown, f"missing plan {plan!r} in breakdown"
        assert breakdown[plan] == 0


# ---------------------------------------------------------------------------
# Tenants: paginated list
# ---------------------------------------------------------------------------


def test_tenants_requires_auth(client):
    resp = client.get("/console/api/myownclone/admin/tenants")
    assert resp.status_code == 401


def test_tenants_empty_db_returns_paginated_shape(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/tenants", headers=admin_headers
    )
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["items"] == []
    assert payload["pagination"] == {
        "page": 1,
        "limit": 20,
        "total": 0,
        "pages": 0,
    }


def test_tenants_limit_clamped_to_50(client, admin_headers):
    """The controller caps `limit` at 50 even if the client asks for 999."""
    resp = client.get(
        "/console/api/myownclone/admin/tenants?limit=999",
        headers=admin_headers,
    )
    assert resp.status_code == 200
    assert resp.get_json()["pagination"]["limit"] == 50


def test_tenants_invalid_status_filter_is_ignored(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/tenants?status=bogus",
        headers=admin_headers,
    )
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Tenant detail: 404 for unknown tenant
# ---------------------------------------------------------------------------


def test_tenant_detail_404_for_unknown_id(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/tenants/does-not-exist",
        headers=admin_headers,
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"] == "tenant_not_found"


def test_tenant_patch_requires_at_least_one_field(client, admin_headers):
    resp = client.patch(
        "/console/api/myownclone/admin/tenants/does-not-exist",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps({}),
    )
    # 404 (tenant not found) wins over 400 (no fields) per the controller
    # order. Either way the request is rejected.
    assert resp.status_code in (400, 404), resp.data


# ---------------------------------------------------------------------------
# Impersonation: reason validation
# ---------------------------------------------------------------------------


def test_impersonate_rejects_short_reason(client, admin_headers):
    resp = client.post(
        "/console/api/myownclone/admin/impersonate",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps({"tenant_id": "t1", "reason": "short"}),
    )
    # Either 400 (Pydantic validation: min_length=10) or 404 (tenant not
    # found) if the validator passes; we want to know the request did NOT
    # succeed silently.
    assert resp.status_code in (400, 404), resp.data


def test_impersonate_404_for_unknown_tenant(client, admin_headers):
    resp = client.post(
        "/console/api/myownclone/admin/impersonate",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps(
            {
                "tenant_id": "does-not-exist",
                "reason": "Reason text longer than 10 chars",
            }
        ),
    )
    assert resp.status_code == 404
    assert resp.get_json()["error"] == "tenant_not_found"


def test_impersonate_stop_without_token_400(client, admin_headers):
    resp = client.post(
        "/console/api/myownclone/admin/impersonate/stop",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps({}),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"] == "no_token"


# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------


def test_audit_log_requires_auth(client):
    resp = client.get("/console/api/myownclone/admin/audit-log")
    assert resp.status_code == 401


def test_audit_log_empty_returns_paginated_shape(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/audit-log", headers=admin_headers
    )
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["items"] == []
    assert payload["pagination"]["total"] == 0


# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------


def test_feedback_requires_auth(client):
    resp = client.get("/console/api/myownclone/admin/feedback")
    assert resp.status_code == 401


def test_feedback_empty_returns_paginated_shape(client, admin_headers):
    resp = client.get(
        "/console/api/myownclone/admin/feedback", headers=admin_headers
    )
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["items"] == []
    assert payload["pagination"]["total"] == 0


# ---------------------------------------------------------------------------
# Courtesy signup
# ---------------------------------------------------------------------------


def test_courtesy_requires_auth(client):
    resp = client.post(
        "/console/api/myownclone/admin/courtesy",
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "email": "test@example.com",
                "name": "Test",
                "plan": "pro",
                "duration_days": 30,
            }
        ),
    )
    assert resp.status_code == 401


def test_courtesy_validates_email_shape(client, admin_headers):
    resp = client.post(
        "/console/api/myownclone/admin/courtesy",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps(
            {
                "email": "not-an-email",
                "name": "Test",
                "plan": "pro",
                "duration_days": 30,
            }
        ),
    )
    assert resp.status_code == 400
    assert resp.get_json()["error"] == "invalid_payload"


# ---------------------------------------------------------------------------
# Courtesy signup — additional validation tests
# ---------------------------------------------------------------------------


def test_courtesy_accepts_valid_payload(client, admin_headers):
    """Happy path: a complete valid payload returns 201 with the echoed
    fields. The actual tenant-creation side-effect is out of scope here —
    the controller is allowed to return 201 with a 'status: created' body."""
    resp = client.post(
        "/console/api/myownclone/admin/courtesy",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps(
            {
                "email": "newuser@example.com",
                "name": "New User",
                "plan": "pro",
                "duration_days": 30,
            }
        ),
    )
    assert resp.status_code == 201, resp.data
    body = resp.get_json()
    assert body["email"] == "newuser@example.com"
    assert body["name"] == "New User"
    assert body["plan"] == "pro"
    assert body["duration_days"] == 30
    assert body["status"] == "created"


def test_courtesy_rejects_invalid_plan(client, admin_headers):
    """A plan not in the canonical 5 must be rejected with 400."""
    resp = client.post(
        "/console/api/myownclone/admin/courtesy",
        headers={**admin_headers, "Content-Type": "application/json"},
        data=json.dumps(
            {
                "email": "u@example.com",
                "name": "U",
                "plan": "platinum",  # not in allowed set
                "duration_days": 30,
            }
        ),
    )
    assert resp.status_code == 400, resp.data
    assert resp.get_json()["error"] == "invalid_payload"


def test_courtesy_rejects_out_of_range_duration(client, admin_headers):
    """duration_days must be 1-365. 0 and999 must both be rejected."""
    for bad in (0, 999, -1):
        resp = client.post(
            "/console/api/myownclone/admin/courtesy",
            headers={**admin_headers, "Content-Type": "application/json"},
            data=json.dumps(
                {
                    "email": "u@example.com",
                    "name": "U",
                    "plan": "pro",
                    "duration_days": bad,
                }
            ),
        )
        assert resp.status_code == 400, (bad, resp.data)
        assert resp.get_json()["error"] == "invalid_payload"


def test_courtesy_rejects_non_admin(client, user_token):
    """A Bearer JWT with role=member must NOT create a courtesy tenant."""
    resp = client.post(
        "/console/api/myownclone/admin/courtesy",
        headers={**user_token, "Content-Type": "application/json"},
        data=json.dumps(
            {
                "email": "u@example.com",
                "name": "U",
                "plan": "pro",
                "duration_days": 30,
            }
        ),
    )
    assert resp.status_code == 403, resp.data


# ---------------------------------------------------------------------------
# Admin role resolution — verify g.account_role fast path works
# ---------------------------------------------------------------------------


def test_admin_jwt_with_platform_admin_role_returns_200(client, admin_token):
    """Regression test: _is_platform_admin must check g.account_role before
    doing a DB lookup, so a JWT with role=platform_admin grants access even
    if the in-memory DB has no matching Account row."""
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=admin_token
    )
    assert resp.status_code == 200, resp.data


def test_member_jwt_is_rejected(client, user_token):
    """A Bearer JWT with role=member must be rejected. Either 401 or 403
    is acceptable per the auth contract."""
    resp = client.get(
        "/console/api/myownclone/admin/overview", headers=user_token
    )
    assert resp.status_code in (401, 403), resp.data
