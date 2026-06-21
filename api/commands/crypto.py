"""Flask CLI commands for crypto key management (Sisyphus M2 + M12).

Two commands:

* ``flask generate-master-key`` — generate a fresh AES-256 key and print it
  base64-encoded. The operator is expected to copy the value into a secret
  manager (1Password, AWS Secrets Manager, vault, etc.) and never commit it.

* ``flask rotate-secrets-key --new <key>`` — STUB for M2. The full rotation
  body (re-encrypt every ``ai_models.api_key_encrypted`` row using a
  double-key window) is implemented in M12 (see plan §M12c).

Both commands follow the existing pattern in ``api/commands/seed.py`` and
``api/commands/reindex.py`` (Click command, registered in
``api.app_factory.create_app``).
"""
from __future__ import annotations

import sys

import click

from api.libs.crypto import generate_master_key


@click.command("generate-master-key")
def generate_master_key_command() -> None:
    """Print a fresh 32-byte AES master key, base64-encoded.

    The value goes into the ``MODEL_SECRETS_KEY`` environment variable. Treat
    it like a database root password: anyone holding it can decrypt every
    row of ``ai_models.api_key_encrypted``.

    Losing the key is IRRECOVERABLE — re-encryption is the only escape, and
    it requires the key. This is the single most important operational
    fact of the configurable-AI-by-task system.
    """
    key = generate_master_key()
    # Print to stdout (operator-friendly) but also flush a loud warning to
    # stderr so it shows up in journalctl / docker logs even if stdout is
    # redirected.
    click.echo(key)
    click.echo(
        "\n[!] Store this key in your secret manager NOW.",
        err=True,
    )
    click.echo(
        "[!] Set MODEL_SECRETS_KEY=<value> in the API environment.",
        err=True,
    )
    click.echo(
        "[!] Losing it makes every ai_models.api_key_encrypted row unreadable.",
        err=True,
    )


@click.command("rotate-secrets-key")
@click.option(
    "--new",
    "new_key_b64",
    required=True,
    help="New master key, base64-encoded (32 bytes). The OLD key must remain "
         "in MODEL_SECRETS_KEY during rotation so legacy rows still decrypt.",
)
def rotate_secrets_key_command_stub(new_key_b64: str) -> None:
    """STUB. Full implementation lands in M12 (audit + double-key rotation).

    For now this command validates the input shape and exits 0 with a notice
    pointing to M12. It does NOT mutate the database.
    """
    import base64
    try:
        raw = base64.b64decode(new_key_b64, validate=True)
    except (ValueError, Exception) as exc:
        click.echo(f"[FAIL] --new value is not valid base64: {exc}", err=True)
        sys.exit(2)
    if len(raw) != 32:
        click.echo(
            f"[FAIL] --new value decodes to {len(raw)} bytes, need 32.",
            err=True,
        )
        sys.exit(2)
    click.echo(
        "[stub] rotate-secrets-key is a no-op in M2. "
        "Full re-encryption is implemented in M12 (plan §M12c). "
        "Input shape validated: 32-byte base64 OK.",
    )


# Re-export under the name ``app_factory.create_app`` expects.
__all__ = ["generate_master_key_command", "rotate_secrets_key_command_stub"]