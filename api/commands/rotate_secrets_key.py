"""Flask CLI command: rotate-secrets-key

Generates a new master key and re-encrypts all AIModel secrets with it.

NOTE: This is a STUB for now. Full envelope encryption with re-encryption
is planned for M19 (post-v3). This command currently:
  1. Generates a new MODEL_SECRETS_KEY
  2. Prints it to stdout for the operator to add to .env
  3. Exits without modifying any data

Actual re-encryption flow (M19):
  1. Read all AIModel rows that have encrypted secrets
  2. Generate new master key
  3. Re-encrypt all secrets with new key using envelope encryption:
     - Generate DEK (data encryption key)
     - Encrypt DEK with old master key → old_kek
     - Encrypt DEK with new master key → new_kek
     - Re-encrypt secret with DEK
     - Store: {old_kek, new_kek, encrypted_secret}
  4. Print new key to stdout (operator must update .env)
  5. On next startup, system decrypts with new key
"""
from __future__ import annotations

import click
from flask.cli import with_appcontext

from api.libs.crypto import generate_master_key


@click.command("rotate-secrets-key")
@with_appcontext
def rotate_secrets_key():
    """Rotate MODEL_SECRETS_KEY and re-encrypt all model secrets.

    STUB: Currently only generates and prints a new key without modifying data.

    Full implementation (M19):
      1. Read all AIModel rows with encrypted secrets
      2. Generate new master key
      3. Re-encrypt all secrets with envelope encryption
      4. Print new key to stdout (operator must update .env)

    Usage:
      flask rotate-secrets-key
    """
    click.echo("=== Rotate Model Secrets Key ===\n")
    click.echo("NOTE: This is a STUB. Full re-encryption coming in M19.\n")

    # Check if there are any models with encrypted secrets
    from api.extensions import db
    from api.models import AIModel
    from sqlalchemy import select

    models_with_secrets = db.session.execute(
        select(AIModel).where(AIModel.config.op("?")("encrypted_api_key"))
    ).scalars().all()

    count = len(models_with_secrets)
    click.echo(f"Found {count} model(s) with encrypted secrets.\n")

    # Generate new key
    new_key = generate_master_key()

    click.echo("#" + "=" * 60)
    click.echo("# NEW MODEL_SECRETS_KEY generated")
    click.echo("#" + "=" * 60)
    click.echo(f"#\n# Add this to api/.env as:\n#   MODEL_SECRETS_KEY={new_key}\n#\n")
    click.echo("# STUB: No data has been modified. Full re-encryption in M19.")
