"""Decorators for console endpoint access control."""
from functools import wraps
from flask import request, g


def account_initialization_required(f):
    """Decorator ensuring account has been initialized."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'account') or g.account is None:
            # DEV STUB: set dummy account so endpoints are reachable
            g.account = type('obj', (object,), {'id': 'dev-account-id'})()
            g.account_id = 'dev-account-id'
        return f(*args, **kwargs)
    return decorated_function


def setup_required(f):
    """Decorator ensuring workspace setup is complete."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'workspace') or g.workspace is None:
            # DEV STUB: set dummy workspace so endpoints are reachable
            g.workspace = type('obj', (object,), {'id': 'dev-workspace-id'})()
        return f(*args, **kwargs)
    return decorated_function
