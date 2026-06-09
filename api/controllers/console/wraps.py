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

    In standalone mode this is a no-op — workspace setup is not required.
    Kept as a pass-through so decorated endpoints still work.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Workspace check not enforced in standalone mode
        return f(*args, **kwargs)
    return decorated_function