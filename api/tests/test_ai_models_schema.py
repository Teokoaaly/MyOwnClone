"""Schema tests for the ai_models catalog (Sisyphus M1).

These tests are INTENTIONALLY DB-light: they introspect SQLAlchemy table
metadata so they pass even when PostgreSQL is not running locally. The
partial-unique-index guarantee is verified by reading the migration source
itself — the migration is the only place where the partial index can be
expressed in PostgreSQL syntax.

For full migration smoke tests (DB up + DB down + partial unique violation)
see the QA scenarios documented in ``.sisyphus/evidence/task-M1-data-layer.md``
(they require a live PG instance and are not part of CI yet).
"""
from __future__ import annotations

import importlib
import re
from pathlib import Path

import pytest


# ─── Models load cleanly and re-export the contract ────────────────────────
def test_models_module_imports() -> None:
    """api.models.ai_models must import without side effects."""
    mod = importlib.import_module("api.models.ai_models")
    assert mod is not None


def test_models_module_exposes_contract_symbols() -> None:
    """Every symbol referenced by HANDOFF_LLM §5 M1 must exist."""
    mod = importlib.import_module("api.models.ai_models")
    for name in ("AIModel", "AIModelAssignment", "AIInvocation",
                 "AIProvider", "AICapability", "AITask", "TASK_CAPABILITY"):
        assert hasattr(mod, name), f"missing symbol: {name}"


def test_models_package_reexports_ai_models() -> None:
    """api.models.__init__ must re-export AIModel/AIModelAssignment/AIInvocation."""
    pkg = importlib.import_module("api.models")
    for name in ("AIModel", "AIModelAssignment", "AIInvocation"):
        assert hasattr(pkg, name), f"api.models missing re-export: {name}"


# ─── Enums have the agreed-upon values ─────────────────────────────────────
def test_ai_provider_enum_values() -> None:
    """The 6 agreed-upon providers are present (HANDOFF_LLM §7 guardrail)."""
    mod = importlib.import_module("api.models.ai_models")
    expected = {"openai", "anthropic", "minimax", "together",
                "openai_compatible", "local"}
    actual = {p.value for p in mod.AIProvider}
    assert actual == expected, f"providers drifted: {actual}"


def test_ai_task_enum_values() -> None:
    """The 5 routed tasks are present."""
    mod = importlib.import_module("api.models.ai_models")
    expected = {"chat", "embedding", "email_classification",
                "email_draft", "stt"}
    actual = {t.value for t in mod.AITask}
    assert actual == expected, f"tasks drifted: {actual}"


def test_task_capability_map_is_total() -> None:
    """Every task has exactly one capability."""
    mod = importlib.import_module("api.models.ai_models")
    assert set(mod.TASK_CAPABILITY.keys()) == set(mod.AITask)
    for task, cap in mod.TASK_CAPABILITY.items():
        assert isinstance(cap, mod.AICapability)


# ─── Schema-level contracts (DB-light via SQLAlchemy metadata) ─────────────
def test_ai_model_table_name_and_required_columns() -> None:
    mod = importlib.import_module("api.models.ai_models")
    table = mod.AIModel.__table__
    assert table.name == "ai_models"
    required = {
        "id", "tenant_id", "name", "provider", "model_id",
        "api_key_encrypted", "base_url", "capabilities",
        "input_price_cents_per_mtok", "output_price_cents_per_mtok",
        "priority", "is_active", "created_at", "updated_at",
    }
    actual = set(table.columns.keys())
    missing = required - actual
    assert not missing, f"ai_models missing columns: {missing}"


def test_ai_model_api_key_is_text_not_string() -> None:
    """Encrypted keys can be long; String(N) would truncate. Use Text."""
    from sqlalchemy import Text
    mod = importlib.import_module("api.models.ai_models")
    col = mod.AIModel.__table__.columns["api_key_encrypted"]
    assert isinstance(col.type, Text), (
        f"api_key_encrypted must be Text (got {type(col.type).__name__})"
    )


def test_assignment_table_uses_fk_with_restrict() -> None:
    """AIModelAssignment.model_id must FK to ai_models.id with RESTRICT."""
    mod = importlib.import_module("api.models.ai_models")
    table = mod.AIModelAssignment.__table__
    assert table.name == "ai_model_assignments"
    fks = list(table.foreign_keys)
    assert len(fks) == 1, f"expected 1 FK, got {len(fks)}"
    fk = fks[0]
    assert fk.column.table.name == "ai_models"
    assert fk.column.name == "id"
    assert fk.ondelete == "RESTRICT", (
        f"FK ondelete must be RESTRICT (got {fk.ondelete!r})"
    )


def test_invocation_table_required_columns() -> None:
    mod = importlib.import_module("api.models.ai_models")
    table = mod.AIInvocation.__table__
    assert table.name == "ai_invocations"
    required = {
        "id", "tenant_id", "task", "model",
        "prompt_tokens", "completion_tokens", "latency_ms",
        "success", "created_at",
    }
    actual = set(table.columns.keys())
    missing = required - actual
    assert not missing, f"ai_invocations missing columns: {missing}"


# ─── Migration-level guarantee (read the file) ─────────────────────────────
# The partial unique index on (tenant_id, task) WHERE is_active=true cannot be
# expressed portably in SQLAlchemy. The migration is the only authoritative
# source — verify it directly so a future agent cannot "fix" the model file
# in a way that breaks the contract.
import ast


@pytest.fixture(scope="module")
def m1_migration_source() -> str:
    repo = Path(__file__).resolve().parents[2]
    path = repo / "api" / "migrations" / "versions" / (
        "2026_06_21_0002_ai_models_catalog.py"
    )
    assert path.exists(), f"migration not found: {path}"
    return path.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def m1_migration_sql_strings(m1_migration_source: str) -> list[str]:
    """Extract every string literal from the migration source.

    Using AST is more robust than regex against quoted/concatenated/f-string SQL.
    """
    tree = ast.parse(m1_migration_source)
    strings: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            strings.append(node.value)
        elif isinstance(node, ast.JoinedStr):  # f-string concatenation
            for value in node.values:
                if isinstance(value, ast.Constant) and isinstance(value.value, str):
                    strings.append(value.value)
    return strings


def _string_contains_create_unique_partial_index(s: str) -> bool:
    """True iff ``s`` is one of the literal SQL fragments that, concatenated,
    build the partial unique index DDL. We check the fragments individually
    to remain agnostic to how the migration joins them."""
    fragments = (
        "CREATE UNIQUE INDEX IF NOT EXISTS",
        "uq_active_assignment_per_tenant_task",
        "ON ai_model_assignments (tenant_id, task)",
        "WHERE is_active = true",
    )
    if all(f in s for f in fragments):
        return True
    # Also accept a single fully-formed SQL string.
    return (
        "CREATE UNIQUE INDEX" in s
        and "uq_active_assignment_per_tenant_task" in s
        and "ON ai_model_assignments (tenant_id, task)" in s
        and "WHERE is_active = true" in s
    )


def test_migration_declares_partial_unique_index(
    m1_migration_sql_strings: list[str],
) -> None:
    found = [
        s for s in m1_migration_sql_strings
        if _string_contains_create_unique_partial_index(s)
    ]
    assert found, (
        "migration MUST declare the partial unique index "
        "uq_active_assignment_per_tenant_task (tenant_id, task) WHERE is_active=true"
    )


def test_migration_links_to_head_revision(m1_migration_source: str) -> None:
    """down_revision must chain from the current head d1e2f3a4b5c6."""
    assert re.search(
        r"^down_revision\s*=\s*['\"]d1e2f3a4b5c6['\"]",
        m1_migration_source,
        re.MULTILINE,
    ), "down_revision must be 'd1e2f3a4b5c6' (current head)"


def test_migration_fk_uses_restrict(m1_migration_source: str) -> None:
    """AIModelAssignment.model_id FK must use ondelete=RESTRICT."""
    assert "ondelete" in m1_migration_source and "RESTRICT" in m1_migration_source


def test_migration_has_no_seed_data(m1_migration_source: str) -> None:
    """Backfill command (M13) owns seeding, NOT the migration."""
    for forbidden in ("INSERT INTO ai_models", "INSERT INTO ai_model_assignments"):
        assert forbidden.lower() not in m1_migration_source.lower(), (
            f"migration must NOT seed data ({forbidden}) — backfill is M13"
        )