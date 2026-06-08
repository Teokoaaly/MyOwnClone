"""Decorators for console endpoint access control.

`account_initialization_required` and `setup_required` are convenience gates
that historically defaulted to permissive stubs in development. They now
fail closed (401) in any environment. Development convenience (auto-fill a
dummy account/workspace) is gated behind the explicit `FLASK_ENV=development`
env var so production deployments cannot accidentally ship with the stubs
on.

If you need a real "is this account set up" check, replace the body of
`account_initialization_required` with a DB query against `accounts` and
`tenants`. The current body is a fail-closed guard that surfaces the bug
instead of hiding it.
"""

from __future__ import annotations

import os
from functools import wraps

from flask import g, jsonify

# A real production deployment must set FLASK_ENV=production (or leave it
# unset, since `development` is opt-in here). Treat the absence of the env
# var as production.
IS_DEVELOPMENT = os.getenv("FLASK_ENV", "production").lower() == "development"


def account_initialization_required(f):
    """Block requests with no `account_id` on `g`.

    Returns 401 `account_not_initialized` in production.
    In development, fills a dummy account_id so local exploration is easy.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        account_id = getattr(g, "account_id", None)
        if account_id:
            return f(*args, **kwargs)

        if IS_DEVELOPMENT:
            g.account_id = "dev-account-id"
            g.account = type("obj", (object,), {"id": "dev-account-id"})()
            return f(*args, **kwargs)

        return (
            jsonify(
                {
                    "error": "account_not_initialized",
                    "message": "No account context on request. Did login_required run?",
                }
            ),
            401,
        )

    return decorated_function


def setup_required(f):
    """Block requests with no `workspace` context on `g`.

    Returns 401 `workspace_not_initialized` in production.
    In development, fills a dummy workspace so local exploration is easy.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        workspace = getattr(g, "workspace", None)
        if workspace is not None:
            return f(*args, **kwargs)

        if IS_DEVELOPMENT:
            g.workspace = type("obj", (object,), {"id": "dev-workspace-id"})()
            return f(*args, **kwargs)

        return (
            jsonify(
                {
                    "error": "workspace_not_initialized",
                    "message": "No workspace context on request.",
                }
            ),
            401,
        )

    return decorated_function


__all__ = ["account_initialization_required", "setup_required"]
