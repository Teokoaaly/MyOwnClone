"""Flask CLI commands for key management and AI audit rollups."""

from __future__ import annotations

import os
from dataclasses import dataclass

import click
from sqlalchemy import select

from api.core.ai_audit import refresh_cost_daily_rollup
from api.extensions.ext_database import db
from api.libs.crypto import (
    CiphertextMalformedError,
    InvalidTag,
    MasterKeyInvalidError,
    MasterKeyMissingError,
    SecretCipher,
    decode_master_key,
    decrypt_with_key,
    encrypt_with_key,
    generate_master_key,
)
from api.models.ai_models import AIModel


@dataclass(slots=True)
class RotationResult:
    scanned: int
    rotated: int
    skipped: int


def rotate_secrets_key(
    *,
    new_key_b64: str,
    old_key_b64: str | None = None,
    dry_run: bool = False,
) -> RotationResult:
    old_key_b64 = old_key_b64 or os.environ.get("MODEL_SECRETS_KEY", "")
    decode_master_key(old_key_b64)
    decode_master_key(new_key_b64)

    rows = db.session.execute(select(AIModel)).scalars().all()
    rotated = 0
    skipped = 0

    for row in rows:
        plaintext = decrypt_with_key(row.api_key_encrypted, old_key_b64)
        candidate = encrypt_with_key(plaintext, new_key_b64)
        if row.api_key_encrypted == candidate:
            skipped += 1
            continue
        rotated += 1
        if not dry_run:
            row.api_key_encrypted = candidate

    if not dry_run:
        db.session.commit()
    return RotationResult(scanned=len(rows), rotated=rotated, skipped=skipped)


@click.command("generate-master-key")
def generate_master_key_command() -> None:
    key = generate_master_key()
    click.echo(key)
    click.echo("\n[!] Store this key in your secret manager NOW.", err=True)
    click.echo("[!] Set MODEL_SECRETS_KEY=<value> in the API environment.", err=True)
    click.echo("[!] Losing it makes every ai_models.api_key_encrypted row unreadable.", err=True)


@click.command("rotate-secrets-key")
@click.option("--new", "new_key_b64", required=True, help="New master key, base64-encoded.")
@click.option("--old", "old_key_b64", required=False, help="Old master key override. Defaults to MODEL_SECRETS_KEY.")
@click.option("--dry-run", is_flag=True, help="Validate and count rows without mutating the database.")
def rotate_secrets_key_command(new_key_b64: str, old_key_b64: str | None, dry_run: bool) -> None:
    try:
        result = rotate_secrets_key(
            new_key_b64=new_key_b64,
            old_key_b64=old_key_b64,
            dry_run=dry_run,
        )
    except (MasterKeyMissingError, MasterKeyInvalidError, CiphertextMalformedError, InvalidTag) as exc:
        click.echo(f"[FAIL] {exc}", err=True)
        raise SystemExit(2) from exc

    mode = "dry-run" if dry_run else "applied"
    click.echo(
        f"[OK] rotation {mode}: scanned={result.scanned} rotated={result.rotated} skipped={result.skipped}"
    )
    click.echo(
        "[!] Keep the old key available for already-running workers until the deployment rolls forward.",
        err=True,
    )


@click.command("refresh-cost-daily-rollup")
@click.option("--days", default=30, show_default=True, type=int, help="How many recent days to recompute.")
def refresh_cost_daily_rollup_command(days: int) -> None:
    rows = refresh_cost_daily_rollup(days=days)
    click.echo(f"[OK] cost_daily_rollup refreshed: {rows} row(s)")


__all__ = [
    "generate_master_key_command",
    "rotate_secrets_key_command",
    "refresh_cost_daily_rollup_command",
    "rotate_secrets_key",
]
