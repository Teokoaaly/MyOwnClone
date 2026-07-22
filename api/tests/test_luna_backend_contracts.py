from __future__ import annotations

import ast
import inspect
from pathlib import Path


def _migration_revisions() -> dict[str, str | tuple[str, ...] | None]:
    versions_dir = Path(__file__).resolve().parents[1] / "migrations" / "versions"
    revisions: dict[str, str | tuple[str, ...] | None] = {}
    for path in versions_dir.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        values = {
            node.targets[0].id: ast.literal_eval(node.value)
            for node in tree.body
            if isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id in {"revision", "down_revision"}
        }
        if "revision" in values:
            revisions[values["revision"]] = values.get("down_revision")
    return revisions


def test_alembic_graph_has_one_head_and_no_missing_parent() -> None:
    revisions = _migration_revisions()
    parents = {
        parent
        for value in revisions.values()
        if value is not None
        for parent in (value if isinstance(value, tuple) else (value,))
    }

    assert parents <= revisions.keys()
    assert revisions.keys() - parents == {"2026_07_14_0002"}


def test_alembic_tracks_flask_and_typebase_metadata() -> None:
    env_path = Path(__file__).resolve().parents[1] / "migrations" / "env.py"
    source = env_path.read_text(encoding="utf-8")

    assert "from api.base import TypeBase" in source
    assert "TypeBase.metadata" in source


def test_admin_tenant_detail_exposes_canonical_methods_and_shape() -> None:
    from api.controllers.console.myownclone import admin_platform
    from api.controllers.console.myownclone.admin_platform import AdminTenantDetailApi

    source = inspect.getsource(admin_platform)
    assert hasattr(AdminTenantDetailApi, "get")
    assert hasattr(AdminTenantDetailApi, "patch")
    assert '"tenant":' in source
    assert '"usage":' in source
    assert '"clones":' in source


def test_admin_overview_exposes_generation_timestamp() -> None:
    from api.controllers.console.myownclone.admin_platform import AdminOverviewApi

    assert '"generated_at":' in inspect.getsource(AdminOverviewApi)
