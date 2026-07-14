"""Regression tests for P1.10.06: monitoring non-blocking + remove ollama
embedding probe (auditoria 2026-07-13).

Covers:
- _check_ollama no longer makes an embedding request (only /api/tags).
- The proc.cpu_percent call uses interval=None (non-blocking).
"""
from __future__ import annotations

import inspect

from api.core import monitoring


def test_check_ollama_does_not_call_api_embed():
    """The embedding test was removed to avoid wasted GPU on each poll.

    The check is on the EXECUTABLE source (docstrings stripped) so that the
    audit reference ("/api/embed with...") in the docstring does not match.
    """
    import ast
    import textwrap

    src = textwrap.dedent(inspect.getsource(monitoring.ServerMonitor._check_ollama))
    # Strip the docstring so comments/audit notes do not trigger the assertion.
    tree = ast.parse(src)
    func_def = tree.body[0]
    if (func_def.body and isinstance(func_def.body[0], ast.Expr)
            and isinstance(func_def.body[0].value, ast.Constant)
            and isinstance(func_def.body[0].value.value, str)):
        func_def.body.pop(0)
        src = ast.unparse(func_def)

    assert "/api/embed" not in src, (
        "monitoring._check_ollama must not POST to /api/embed (was wasting GPU per probe)"
    )
    assert "/api/tags" in src, (
        "_check_ollama must still call /api/tags to know which models are loaded"
    )
    assert "mxbai-embed-large" not in src, (
        "Embedding model name should not be hardcoded here"
    )


def test_check_process_uses_non_blocking_cpu_percent():
    """psutil.Process.cpu_percent must be called with interval=None (no 100ms sleep)."""
    # The psutil block lives inside _check_api_health; grep the whole module.
    src = inspect.getsource(monitoring)
    # Allow interval=None OR interval=0 (both non-blocking on modern psutil).
    assert "cpu_percent(interval=None)" in src or "cpu_percent(interval=0)" in src, (
        "process.cpu_percent must use non-blocking interval"
    )
    assert "cpu_percent(interval=0.1)" not in src, (
        "The old blocking 100ms interval is still present"
    )
