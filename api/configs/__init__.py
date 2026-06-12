"""MyOwnClone configuration — reads from environment variables."""

import os


class MyOwnCloneConfig:
    """Application configuration backed by environment variables.

    All attributes are resolved lazily from ``os.environ`` so that env
    vars set after module import (e.g. via dotenv) are picked up
    correctly.
    """

    @property
    def STRIPE_SECRET_KEY(self) -> str:
        return os.environ.get("STRIPE_SECRET_KEY", "")

    @property
    def MAILGUN_API_KEY(self) -> str:
        return os.environ.get("MAILGUN_API_KEY", "")

    @property
    def FROM_EMAIL(self) -> str:
        return os.environ.get("FROM_EMAIL", "noreply@myownclone.com")

    @property
    def SITE_URL(self) -> str:
        return (
            os.environ.get("MYOWNCLONE_SITE_URL")
            or os.environ.get("NEXTAUTH_URL")
            or os.environ.get("PUBLIC_APP_URL")
            or "http://localhost:5001"
        )

    @property
    def SENDGRID_INBOUND_WEBHOOK_SECRET(self) -> str:
        return os.environ.get("SENDGRID_INBOUND_WEBHOOK_SECRET", "")

    @property
    def ANTHROPIC_API_KEY(self) -> str:
        return os.environ.get("ANTHROPIC_API_KEY", "")

    @property
    def OPENAI_API_KEY(self) -> str:
        return os.environ.get("OPENAI_API_KEY", "")


myownclone_config = MyOwnCloneConfig()

__all__ = ["MyOwnCloneConfig", "myownclone_config"]
