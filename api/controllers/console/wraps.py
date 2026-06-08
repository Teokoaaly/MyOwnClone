# controllers/console/wraps.py
"""Decorators for console endpoint access control."""
from functools import wraps
from flask import request, g


def account_initialization_required(f):
    """Decorator ensuring account has been initialized.

    Returns a (dict, status) tuple instead of a flask Response so that
    flask-restx can serialize the body through its normal pipeline.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'account') or g.account is None:
            return {'error': 'Account not found'}, 404
        return f(*args, **kwargs)
    return decorated_function


def setup_required(f):
    """Decorator ensuring workspace setup is complete."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'workspace') or g.workspace is None:
            return {'error': 'Workspace not found'}, 404
        return f(*args, **kwargs)
    return decorated_function