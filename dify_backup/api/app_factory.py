"""
MyOwnClone application factory.
Register all MyOwnClone blueprints here.
"""
from dify.api.controllers.myownclone_public import myownclone_public_bp

def register_myownclone_blueprints(app):
    """Register all MyOwnClone blueprints with the Flask app."""
    app.register_blueprint(myownclone_public_bp)