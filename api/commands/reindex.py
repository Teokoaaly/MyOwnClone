"""Placeholder reindex CLI command."""

import click


@click.command("reindex")
def reindex_command():
    """Stub reindex command kept for app_factory CLI registration."""
    raise click.ClickException("reindex command is not implemented in standalone mode yet.")


__all__ = ["reindex_command"]
