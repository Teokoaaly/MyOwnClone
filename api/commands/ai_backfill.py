"""Flask CLI command: backfill the AI model catalog from legacy env vars (M13).

Before the configurable-AI-by-task system (M1-M12) the provider/model for each
task was selected from environment variables (``OPENAI_API_KEY`` and friends).
``flask ai-backfill-from-env`` materializes those legacy env vars into the
DB-driven ``AIModel`` / ``AIModelAssignment`` catalog so an existing deployment
can migrate without manual data entry.

Design contract:

- Global rows only (``tenant_id IS NULL``); per-tenant overrides stay manual.
- Provider API keys are encrypted with :class:`api.libs.crypto.SecretCipher`
  (AES-256-GCM, M2 contract). Plaintext keys are never persisted.
- Idempotent and safe to re-run: an unchanged env produces zero new rows and
  zero updates; an active assignment that already points at the correct model
  is reused, not duplicated.
- ``embedding`` models record ``embedding_dimensions=1536`` (the project-wide
  vector size, see ``api/core/retrieval.py``).
- ``stt`` is only backfilled when the OpenAI key is present (the only provider
  with a speech-to-text model in the catalog).
"""

from __future__ import annotations

import os
from dataclasses import dataclass

import click
from sqlalchemy import select

from api.extensions.ext_database import db
from api.libs.crypto import SecretCipher
from api.libs.uuid_utils import uuidv7
from api.models.ai_models import (
    TASK_CAPABILITY,
    AICapability,
    AIModel,
    AIModelAssignment,
    AIProvider,
    AITask,
)

_EMBEDDING_DIMENSIONS = 1536

# Per-provider env var + default model ids. Only providers whose key is present
# in the environment are considered.
_PROVIDER_SPECS: dict[str, dict[str, str]] = {
    AIProvider.OPENAI.value: {
        "env": "OPENAI_API_KEY",
        "chat_model": "gpt-4o-mini",
        "embedding_model": "text-embedding-3-small",
        "stt_model": "whisper-1",
    },
    AIProvider.ANTHROPIC.value: {
        "env": "ANTHROPIC_API_KEY",
        "chat_model": "claude-3-5-sonnet-latest",
    },
    AIProvider.MINIMAX.value: {
        "env": "MINIMAX_API_KEY",
        "chat_model": "abab6.5s-chat",
    },
    AIProvider.TOGETHER.value: {
        "env": "TOGETHER_API_KEY",
        "chat_model": "meta-llama/Llama-3.1-8B-Instruct-Turbo",
        "embedding_model": "togethercomputer/m2-bert-80M-8k-retrieval",
    },
}

# Capability -> the _PROVIDER_SPECS key holding the model id for that capability.
_CAPABILITY_MODEL_KEY: dict[AICapability, str] = {
    AICapability.LLM: "chat_model",
    AICapability.EMBEDDING: "embedding_model",
    AICapability.STT: "stt_model",
}

# Capability -> ordered provider preference. The first provider that both has a
# key in the environment and defines a model for the capability wins.
_CAPABILITY_PRIORITY: dict[AICapability, list[str]] = {
    AICapability.LLM: [
        AIProvider.OPENAI.value,
        AIProvider.ANTHROPIC.value,
        AIProvider.MINIMAX.value,
        AIProvider.TOGETHER.value,
    ],
    AICapability.EMBEDDING: [
        AIProvider.OPENAI.value,
        AIProvider.TOGETHER.value,
    ],
    AICapability.STT: [
        AIProvider.OPENAI.value,
    ],
}


@dataclass(slots=True)
class BackfillResult:
    models_created: int = 0
    models_updated: int = 0
    assignments_created: int = 0
    assignments_reused: int = 0
    providers_detected: tuple[str, ...] = ()
    skipped_tasks: tuple[str, ...] = ()


def _detect_providers(env: dict[str, str]) -> dict[str, str]:
    """Return ``{provider: api_key}`` for every provider whose key is set."""
    detected: dict[str, str] = {}
    for provider, spec in _PROVIDER_SPECS.items():
        key = (env.get(spec["env"]) or "").strip()
        if key:
            detected[provider] = key
    return detected


def _resolve_provider_for_capability(
    capability: AICapability, detected: dict[str, str]
) -> str | None:
    """Pick the highest-priority detected provider that defines this capability."""
    model_key = _CAPABILITY_MODEL_KEY[capability]
    for provider in _CAPABILITY_PRIORITY.get(capability, []):
        if provider in detected and _PROVIDER_SPECS[provider].get(model_key):
            return provider
    return None


def backfill_from_env(
    *,
    session=None,
    env: dict[str, str] | None = None,
    dry_run: bool = False,
) -> BackfillResult:
    """Create/update global ``AIModel`` and ``AIModelAssignment`` rows from env.

    Args:
        session: SQLAlchemy session. Defaults to ``db.session`` (injectable for
            tests so no live database is required).
        env: Environment mapping. Defaults to ``os.environ``.
        dry_run: When True, compute counts without adding rows or committing.
    """
    session = session if session is not None else db.session
    env = env if env is not None else dict(os.environ)

    detected = _detect_providers(env)
    result = BackfillResult(providers_detected=tuple(sorted(detected)))
    if not detected:
        return result

    existing_models = list(
        session.execute(
            select(AIModel).where(AIModel.tenant_id.is_(None))
        ).scalars().all()
    )
    existing_assignments = list(
        session.execute(
            select(AIModelAssignment).where(
                AIModelAssignment.tenant_id.is_(None),
                AIModelAssignment.is_active.is_(True),
            )
        ).scalars().all()
    )

    models_by_key: dict[tuple[str, str], AIModel] = {
        (m.provider, m.model_id): m for m in existing_models
    }
    active_assignment_by_task: dict[str, AIModelAssignment] = {
        a.task: a for a in existing_assignments
    }

    def _ensure_model(provider: str, model_id: str, capability: AICapability) -> str:
        """Return the AIModel.id for (provider, model_id), creating/updating it."""
        cap_value = capability.value
        dims = _EMBEDDING_DIMENSIONS if capability is AICapability.EMBEDDING else None
        key = (provider, model_id)
        existing = models_by_key.get(key)

        if existing is None:
            new_id = str(uuidv7())
            model = AIModel(
                id=new_id,
                tenant_id=None,
                name=f"{provider}/{model_id}",
                provider=provider,
                model_id=model_id,
                api_key_encrypted=SecretCipher.encrypt(detected[provider]),
                capabilities=[cap_value],
                embedding_dimensions=dims,
                is_active=True,
            )
            models_by_key[key] = model
            if not dry_run:
                session.add(model)
            result.models_created += 1
            return new_id

        # Existing row: update only when something actually changed so re-runs
        # are idempotent (no spurious models_updated bumps).
        changed = False
        capabilities = list(existing.capabilities or [])
        if cap_value not in capabilities:
            capabilities.append(cap_value)
            existing.capabilities = capabilities
            changed = True
        if dims is not None and existing.embedding_dimensions != dims:
            existing.embedding_dimensions = dims
            changed = True
        if not _key_matches(existing.api_key_encrypted, detected[provider]):
            existing.api_key_encrypted = SecretCipher.encrypt(detected[provider])
            changed = True
        if changed:
            result.models_updated += 1
        return existing.id

    for task in AITask:
        capability = TASK_CAPABILITY[task]
        provider = _resolve_provider_for_capability(capability, detected)
        if provider is None:
            result.skipped_tasks += (task.value,)
            continue
        model_id = _PROVIDER_SPECS[provider][_CAPABILITY_MODEL_KEY[capability]]
        target_model_pk = _ensure_model(provider, model_id, capability)

        current = active_assignment_by_task.get(task.value)
        if current is not None and current.model_id == target_model_pk:
            result.assignments_reused += 1
            continue

        if current is not None:
            # Repoint: deactivate the stale active assignment to preserve the
            # "one active assignment per (tenant, task)" invariant.
            current.is_active = False

        assignment = AIModelAssignment(
            id=str(uuidv7()),
            tenant_id=None,
            task=task.value,
            model_id=target_model_pk,
            is_active=True,
        )
        active_assignment_by_task[task.value] = assignment
        if not dry_run:
            session.add(assignment)
        result.assignments_created += 1

    if not dry_run:
        session.commit()
    return result


def _key_matches(encrypted_blob: str, plaintext: str) -> bool:
    """True iff ``encrypted_blob`` decrypts to ``plaintext`` under the master key.

    A decryption failure (wrong/rotated master key, malformed blob) is treated
    as a mismatch so the row is re-encrypted with the current key.
    """
    try:
        return SecretCipher.decrypt(encrypted_blob) == plaintext
    except Exception:
        return False


@click.command("ai-backfill-from-env")
@click.option(
    "--dry-run",
    is_flag=True,
    help="Report what would change without writing to the database.",
)
def ai_backfill_from_env_command(dry_run: bool) -> None:
    """Backfill AIModel/AIModelAssignment rows from legacy provider env vars."""
    result = backfill_from_env(dry_run=dry_run)
    mode = "dry-run" if dry_run else "applied"
    click.echo(
        "[OK] ai-backfill-from-env "
        f"{mode}: providers={','.join(result.providers_detected) or '(none)'} "
        f"models_created={result.models_created} "
        f"models_updated={result.models_updated} "
        f"assignments_created={result.assignments_created} "
        f"assignments_reused={result.assignments_reused}"
    )
    if result.skipped_tasks:
        click.echo(
            f"[!] skipped tasks (no provider key): {','.join(result.skipped_tasks)}",
            err=True,
        )
    if not result.providers_detected:
        click.echo(
            "[!] No provider env vars detected "
            "(OPENAI_API_KEY/ANTHROPIC_API_KEY/MINIMAX_API_KEY/TOGETHER_API_KEY).",
            err=True,
        )


__all__ = [
    "BackfillResult",
    "backfill_from_env",
    "ai_backfill_from_env_command",
]
