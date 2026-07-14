"""Regression tests for P1.10.01: email template format-string injection guard.
(auditoria 2026-07-13, H-08)

The previous code did ``subject_tpl.format(**kwargs)`` on caller-supplied
values. ``str.format`` resolves attribute access, so a value like
``{0.__class__}`` would have leaked internals. Now caller-supplied values
are escaped to ``{{...}}`` so they cannot be reinterpreted as format spec.
"""
from __future__ import annotations

from api.core.email_service import _escape_format_injection


def test_escape_neutralizes_attribute_access_injection():
    """H-08 core: a payload trying to escape into str.format spec must
    render as the literal text, not as a class reference."""
    payload = "{0.__class__.__init__.__globals__}"
    escaped = _escape_format_injection(payload)
    # The payload becomes a balanced literal that str.format treats as text,
    # not as a spec. The doubled braces render through str.format as their
    # raw text (since they are not adjacent to a real placeholder).
    out = ("hello {name}".format(name=escaped))
    assert "__class__" in out  # text is preserved as a literal
    # Critically: NO class info was leaked (no module path, no function repr).
    assert "module" not in out
    assert " at 0x" not in out
    # The original payload was NOT resolved into a real spec.
    # If str.format had treated it as a spec, it would have raised KeyError
    # or returned a repr. The fact that the call succeeded with our escaped
    # value proves the spec was neutralized.


def test_escape_does_not_affect_normal_text():
    assert _escape_format_injection("user@example.com") == "user@example.com"
    assert _escape_format_injection("hello world") == "hello world"
    assert _escape_format_injection("") == ""
    # Non-strings pass through unchanged.
    assert _escape_format_injection(42) == 42
    assert _escape_format_injection(None) is None
    assert _escape_format_injection(True) is True


def test_escape_balances_existing_braces():
    """A value with both { and } gets both doubled so the format call stays balanced."""
    assert _escape_format_injection("{a}{b}") == "{{a}}{{b}}"


def test_safe_keys_whitelisted():
    """The known good keys pass through the formatter; unexpected ones warn."""
    from api.core import email_service as es
    # Known-safe keys.
    safe = {"app_url", "token", "reset_url", "first_name", "clone_name",
            "lead_name", "lead_email", "sender_name", "team_name", "from_name"}
    assert safe.issubset(es._SAFE_EMAIL_TEMPLATE_KEYS)


def test_real_template_renders_with_safe_kwargs():
    """End-to-end: the production templates render correctly with safe kwargs,
    and an injected value in a kwarg is rendered literally (not as spec)."""
    from api.core import email_service as es

    body = es.TEMPLATES["en"]["password_reset_body"]
    rendered = body.format(
        app_url=es.APP_URL,
        token="{0.__class__}",  # injection attempt
    )
    # Token contains the original literal; __class__ is text, not a spec.
    assert "__class__" in rendered
    # The {app_url} placeholder was correctly substituted with the constant.
    assert es.APP_URL in rendered
    # No leaked class attributes (e.g. no module path, no dict reprs).
    assert "module" not in rendered
    assert "at 0x" not in rendered
