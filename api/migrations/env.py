import logging
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# ── Portable path setup ─────────────────────────────────────────────────────
# Makes `api` package importable from any working directory (local dev + Docker)
_api_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _api_root not in sys.path:
    sys.path.insert(0, _api_root)

# Load .env before creating the app so credentials are available
try:
    from dotenv import load_dotenv
    _env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(_env_file, override=False)
except ImportError:
    pass  # python-dotenv not installed; rely on environment variables

from api.app_factory import create_app
from api.base import TypeBase

app = create_app()
config = context.config
config.set_main_option("sqlalchemy.url", app.config["SQLALCHEMY_DATABASE_URI"])

target_metadata = (
    app.extensions["sqlalchemy"].metadata,
    TypeBase.metadata,
)

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
