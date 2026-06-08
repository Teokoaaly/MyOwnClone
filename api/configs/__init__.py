"""MyOwnClone configuration stub."""

class MyOwnCloneConfig:
    MAILGUN_API_KEY: str = ""
    FROM_EMAIL: str = "noreply@myownclone.com"
    SITE_URL: str = "http://localhost:5001"

myownclone_config = MyOwnCloneConfig()

__all__ = ['MyOwnCloneConfig', 'myownclone_config']
