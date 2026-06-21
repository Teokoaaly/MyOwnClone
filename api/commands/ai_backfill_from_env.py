"""Flask CLI command: ai-backfill-from-env

Reads API keys from environment variables (OPENAI_API_KEY, ANTHROPIC_API_KEY,
COHERE_API_KEY, OLLAMA_BASE_URL) and creates corresponding AIModel + AIModelAssignment
rows. Idempotent: skips models that already exist (key = provider+name+model_type).
"""
from __future__ import annotations

import os
import click
from flask.cli import with_appcontext
from sqlalchemy import select

from api.extensions import db
from api.models import AIModel, AIModelAssignment, AssignmentTask


# ─── Known provider / model combinations ───────────────────────────────────────

KNOWN_MODELS = [
    # OpenAI
    {
        "provider": "openai",
        "name": "gpt-4o-mini",
        "model_type": "chat",
        "input_cost_per_1k": 15,   # $0.15 / 1M input = $0.00015 / 1K = 0.015 cents... actually $0.15/1M = 0.015cents/1K
        "output_cost_per_1k": 60,   # $0.60/1M = 0.06 cents/1K
        "max_tokens": 128000,
        "task": "chat_primary",
    },
    {
        "provider": "openai",
        "name": "gpt-4o",
        "model_type": "chat",
        "input_cost_per_1k": 250,  # $2.50/1M = 0.25 cents/1K
        "output_cost_per_1k": 1000, # $10/1M = 1 cent/1K
        "max_tokens": 128000,
        "task": "chat_fallback",
    },
    {
        "provider": "openai",
        "name": "text-embedding-3-small",
        "model_type": "embedding",
        "input_cost_per_1k": 2,    # $0.02/1M tokens
        "output_cost_per_1k": 0,
        "max_tokens": 8191,
        "task": "embedding",
    },
    # Anthropic
    {
        "provider": "anthropic",
        "name": "claude-3-5-haiku",
        "model_type": "chat",
        "input_cost_per_1k": 75,   # $0.75/1M = 0.075 cents/1K
        "output_cost_per_1k": 300,  # $3/1M = 0.3 cents/1K
        "max_tokens": 200000,
        "task": "chat_primary",
    },
    {
        "provider": "anthropic",
        "name": "claude-3-5-sonnet",
        "model_type": "chat",
        "input_cost_per_1k": 300,  # $3/1M = 0.3 cents/1K
        "output_cost_per_1k": 1500, # $15/1M = 1.5 cents/1K
        "max_tokens": 200000,
        "task": "chat_fallback",
    },
    # Cohere
    {
        "provider": "cohere",
        "name": "rerank-english-v3.0",
        "model_type": "rerank",
        "input_cost_per_1k": 35,   # $0.35/1K
        "output_cost_per_1k": 0,
        "max_tokens": 4096,
        "task": "rerank",
    },
    # Ollama (local, free)
    {
        "provider": "ollama",
        "name": "llama3.2",
        "model_type": "chat",
        "input_cost_per_1k": 0,
        "output_cost_per_1k": 0,
        "max_tokens": 128000,
        "task": "chat_primary",
    },
]


def _env_key_for_model(provider: str) -> str | None:
    """Return the env var name that would supply the API key for this provider."""
    mapping = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "cohere": "COHERE_API_KEY",
    }
    return mapping.get(provider)


def _has_api_key(provider: str) -> bool:
    """Check if the provider's env var is set and non-empty."""
    env_var = _env_key_for_model(provider)
    if not env_var:
        return False
    key = os.environ.get(env_var, "").strip()
    return bool(key)


def _has_ollama() -> bool:
    """Check if OLLAMA_BASE_URL is set."""
    url = os.environ.get("OLLAMA_BASE_URL", "").strip()
    return bool(url)


def _model_exists(provider: str, name: str, model_type: str) -> bool:
    """Check if a model with this provider+name+model_type already exists."""
    return db.session.execute(
        select(AIModel).where(
            AIModel.provider == provider,
            AIModel.name == name,
            AIModel.model_type == model_type,
        )
    ).scalar_one_or_none() is not None


def _assignment_exists(model_id: str, task: str, tenant_id: str | None = None) -> bool:
    """Check if an assignment already exists for this model+task (optionally tenant-scoped)."""
    query = select(AIModelAssignment).where(
        AIModelAssignment.model_id == model_id,
        AIModelAssignment.task == task,
    )
    if tenant_id is None:
        query = query.where(AIModelAssignment.tenant_id.is_(None))
  ***REMOVED***:
        query = query.where(AIModelAssignment.tenant_id == tenant_id)
    return db.session.execute(query).scalar_one_or_none() is not None


@click.command("ai-backfill-from-env")
@with_appcontext
def ai_backfill_from_env():
    """Read API keys from environment and create AIModel + AIModelAssignment rows.

    Idempotent: skips models that already exist (key = provider+name+model_type).

    Supported providers:
      - OPENAI_API_KEY  → openai/gpt-4o-mini (chat_primary), openai/gpt-4o (chat_fallback),
                          openai/text-embedding-3-small (embedding)
      - ANTHROPIC_API_KEY → anthropic/claude-3-5-haiku (chat_primary),
                             anthropic/claude-3-5-sonnet (chat_fallback)
      - COHERE_API_KEY  → cohere/rerank-english-v3.0 (rerank)
      - OLLAMA_BASE_URL → ollama/llama3.2 (chat_primary, free)

    Usage:
      flask ai-backfill-from-env
    """
    click.echo("=== AI Model Backfill from Environment ===\n")

    created_models = []
    skipped_models = []
    created_assignments = []

    for model_spec in KNOWN_MODELS:
        provider = model_spec["provider"]
        name = model_spec["name"]
        model_type = model_spec["model_type"]
        task = model_spec["task"]

        # Check if env var is set for this provider
        if provider == "ollama":
            has_key = _has_ollama()
      ***REMOVED***:
            has_key = _has_api_key(provider)

        if not has_key:
            click.echo(f"  ⏭ Skipping {provider}/{name} — no API key configured")
            skipped_models.append(f"{provider}/{name}")
            continue

        # Check if model already exists
        if _model_exists(provider, name, model_type):
            click.echo(f"  ✓ {provider}/{name} already exists, skipping")
            skipped_models.append(f"{provider}/{name}")
            continue

        # Create the model
        model = AIModel(
            provider=provider,
            name=name,
            model_type=model_type,
            input_cost_per_1k=model_spec.get("input_cost_per_1k", 0),
            output_cost_per_1k=model_spec.get("output_cost_per_1k", 0),
            max_tokens=model_spec.get("max_tokens"),
            is_active=True,
        )
        db.session.add(model)
        db.session.flush()  # get the ID
        click.echo(f"  + Created AIModel: {provider}/{name} (id={model.id})")
        created_models.append(f"{provider}/{name}")

        # Create global assignment for this model+task
        if not _assignment_exists(str(model.id), task):
            assignment = AIModelAssignment(
                tenant_id=None,  # global
                model_id=str(model.id),
                task=task,
                label=f"{name} ({task})",
                priority=0,
                is_active=True,
            )
            db.session.add(assignment)
            db.session.flush()
            click.echo(f"    └── Created AIModelAssignment: task={task} (global)")
            created_assignments.append(f"{provider}/{name} → {task}")
      ***REMOVED***:
            click.echo(f"    └── Assignment for task={task} already exists")

    db.session.commit()

    click.echo(f"\n=== Summary ===")
    click.echo(f"  Models created:  {len(created_models)}")
    click.echo(f"  Models skipped:   {len(skipped_models)}")
    click.echo(f"  Assignments created: {len(created_assignments)}")

    if created_models:
        click.echo(f"\nCreated models: {', '.join(created_models)}")
