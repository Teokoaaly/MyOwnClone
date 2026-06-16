# controllers/console/wraps.py
"""Decorators for console endpoint access control."""
from functools import wraps
from flask import request, g


def account_initialization_required(f):
    """Decorator ensuring account has been initialized.

    In standalone mode, 'login_required' sets g.account_id from the JWT.
    This decorator checks that the JWT-based account context is present.
    Returns a (dict, status) tuple instead of a flask Response so that
    flask-restx can serialize the body through its normal pipeline.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'account_id') or g.account_id is None:
            return {'error': 'Account not found'}, 404
        return f(*args, **kwargs)
    return decorated_function


def setup_required(f):
    """Decorator ensuring workspace setup is complete.

    Checks that at least one platform admin exists in the system.
    Returns 403 if setup has not been completed.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from api.extensions.ext_database import db
        from sqlalchemy import select
        from api.models.account import Account

        # Check if any platform admin exists
        admin_exists = db.session.execute(
            select(Account.id).where(Account.is_platform_admin == True).limit(1)
        ).scalar_one_or_none() is not None

        if not admin_exists:
            return {'error': 'Platform setup not complete'}, 403

        return f(*args, **kwargs)
    return decorated_function