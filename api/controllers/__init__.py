from flask import Blueprint
from flask_restx import Api, Namespace

bp = Blueprint("console", __name__, url_prefix="/console/api")

api = Api(
    bp,
    version="1.0",
    title="Console API",
    description="Console management APIs for app configuration, monitoring, and administration",
)

console_ns = Namespace("console", description="Console management API operations", path="/")

# Import myownclone controllers
from .console.myownclone import admin_platform as myownclone_admin, analytics as myownclone_analytics, booking as myownclone_booking, clone as myownclone_clone, creator_memory as myownclone_creator_memory, feedback as myownclone_feedback, inbox as myownclone_inbox, stripe_ctrl as myownclone_stripe
from . import myownclone_public as myownclone_public

api.add_namespace(console_ns)

__all__ = [
    "api",
    "bp",
    "console_ns",
    "myownclone_admin",
    "myownclone_analytics",
    "myownclone_booking",
    "myownclone_clone",
    "myownclone_creator_memory",
    "myownclone_feedback",
    "myownclone_inbox",
    "myownclone_public",
    "myownclone_stripe",
]