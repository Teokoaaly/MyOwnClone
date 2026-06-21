"""CLI: generate MODEL_SECRETS_KEY."""
from __future__ import annotations
import click
from flask.cli import with_appcontext

from api.libs.crypto import generate_master_key


def register_generate_master_key(app):
    """Register flask generate-master-key command."""

    @app.cli.command("generate-master-key")
    def generate_master_key_cmd():
        """Generate a new MODEL_SECRETS_KEY (256-bit, base64-encoded).

        Print the result to stdout for the operator to add to .env.
        """
        key = generate_master_key()
        click.echo("# Add this to api/.env as MODEL_SECRETS_KEY=<value>:")
        click.echo(f"MODEL_SECRETS_KEY={key}")
