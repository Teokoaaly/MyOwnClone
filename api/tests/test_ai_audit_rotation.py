from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

from api.commands.crypto import rotate_secrets_key
from api.core.ai_audit import build_cost_daily_rollup_rows, refresh_cost_daily_rollup
from api.libs.crypto import decrypt_with_key, encrypt_with_key, generate_master_key


def test_rotate_secrets_key_reencrypts_rows(monkeypatch):
    old_key = generate_master_key()
    new_key = generate_master_key()
    row = SimpleNamespace(api_key_encrypted=encrypt_with_key("sk-live", old_key))
    committed = {"value": False}

    monkeypatch.setattr(
        "api.commands.crypto.db.session.execute",
        lambda stmt: SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: [row])),
    )
    monkeypatch.setattr(
        "api.commands.crypto.db.session.commit",
        lambda: committed.__setitem__("value", True),
    )

    result = rotate_secrets_key(new_key_b64=new_key, old_key_b64=old_key)

    assert result.scanned == 1
    assert result.rotated == 1
    assert committed["value"] is True
    assert decrypt_with_key(row.api_key_encrypted, new_key) == "sk-live"


def test_rotate_secrets_key_supports_dry_run(monkeypatch):
    old_key = generate_master_key()
    new_key = generate_master_key()
    original = encrypt_with_key("sk-dry", old_key)
    row = SimpleNamespace(api_key_encrypted=original)

    monkeypatch.setattr(
        "api.commands.crypto.db.session.execute",
        lambda stmt: SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: [row])),
    )
    monkeypatch.setattr(
        "api.commands.crypto.db.session.commit",
        lambda: (_ for _ in ()).throw(AssertionError("commit should not run")),
    )

    result = rotate_secrets_key(new_key_b64=new_key, old_key_b64=old_key, dry_run=True)

    assert result.scanned == 1
    assert result.rotated == 1
    assert row.api_key_encrypted == original


def test_build_cost_daily_rollup_rows_groups_by_day_task_model():
    invocations = [
        SimpleNamespace(
            tenant_id="tenant-1",
            created_at=datetime(2026, 6, 23, 8, 0, 0),
            task="chat",
            model="gpt-4o-mini",
            prompt_tokens=10,
            completion_tokens=5,
            success=True,
        ),
        SimpleNamespace(
            tenant_id="tenant-1",
            created_at=datetime(2026, 6, 23, 9, 0, 0),
            task="chat",
            model="gpt-4o-mini",
            prompt_tokens=20,
            completion_tokens=15,
            success=False,
        ),
    ]

    rows = build_cost_daily_rollup_rows(invocations)

    assert len(rows) == 1
    assert rows[0].invocations == 2
    assert rows[0].prompt_tokens == 30
    assert rows[0].completion_tokens == 20
    assert rows[0].success_count == 1
    assert rows[0].error_count == 1


def test_refresh_cost_daily_rollup_replaces_recent_window(monkeypatch):
    invocations = [
        SimpleNamespace(
            tenant_id="tenant-1",
            created_at=datetime(2026, 6, 23, 8, 0, 0),
            task="chat",
            model="gpt-4o-mini",
            prompt_tokens=10,
            completion_tokens=5,
            success=True,
        )
    ]
    deleted = []
    added = []
    committed = {"value": False}

    monkeypatch.setattr(
        "api.core.ai_audit.db.session.execute",
        lambda stmt: (
            deleted.append(stmt) or SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: invocations))
        ),
    )
    monkeypatch.setattr(
        "api.core.ai_audit.db.session.add",
        lambda row: added.append(row),
    )
    monkeypatch.setattr(
        "api.core.ai_audit.db.session.commit",
        lambda: committed.__setitem__("value", True),
    )

    count = refresh_cost_daily_rollup(days=30)

    assert count == 1
    assert len(added) == 1
    assert added[0].tenant_id == "tenant-1"
    assert added[0].invocations == 1
    assert committed["value"] is True
