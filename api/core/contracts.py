"""Shared MyOwnClone API contracts.

The database has accumulated a few legacy Spanish/internal values. Public APIs
should expose the frontend contract while still accepting old rows until a
dedicated data migration can rewrite them.
"""

from __future__ import annotations

PLAN_KEYS = ("trial", "basic", "pro", "scale", "enterprise")
TENANT_STATUS_KEYS = ("trial", "active", "suspended", "cancelled")
SILO_KEYS = ("teach", "support", "sales")
CONVERSATION_MODE_KEYS = ("pedagogy", "support", "sales")

_PLAN_ALIASES = {
    "": "trial",
    "trial": "trial",
    "free": "trial",
    "gratis": "trial",
    "basic": "basic",
    "basico": "basic",
    "básico": "basic",
    "pro": "pro",
    "scale": "scale",
    "escala": "scale",
    "enterprise": "enterprise",
}

_TENANT_STATUS_ALIASES = {
    "": "trial",
    "trial": "trial",
    "trialing": "trial",
    "normal": "active",
    "active": "active",
    "suspended": "suspended",
    "banned": "suspended",
    "cancelled": "cancelled",
    "canceled": "cancelled",
}

_SILO_ALIASES = {
    "": "teach",
    "teach": "teach",
    "teaching": "teach",
    "learn": "teach",
    "pedagogy": "teach",
    "support": "support",
    "sales": "sales",
}

_CONVERSATION_MODE_ALIASES = {
    "": "pedagogy",
    "teach": "pedagogy",
    "teaching": "pedagogy",
    "learn": "pedagogy",
    "pedagogy": "pedagogy",
    "support": "support",
    "sales": "sales",
}

PLAN_PRICES_CENTS = {
    "trial": 0,
    "basic": 4900,
    "pro": 9900,
    "scale": 19900,
    "enterprise": 49900,
}


def _normalize(value: str | None, aliases: dict[str, str], fallback: str) -> str:
    return aliases.get((value or "").strip().lower(), fallback)


def normalize_plan(value: str | None) -> str:
    return _normalize(value, _PLAN_ALIASES, "trial")


def normalize_tenant_status(value: str | None) -> str:
    return _normalize(value, _TENANT_STATUS_ALIASES, "trial")


def normalize_silo(value: str | None) -> str:
    return _normalize(value, _SILO_ALIASES, "teach")


def normalize_conversation_mode(value: str | None) -> str:
    return _normalize(value, _CONVERSATION_MODE_ALIASES, "pedagogy")


def normalize_silo_list(values: list[str] | tuple[str, ...] | None) -> list[str]:
    normalized: list[str] = []
    for value in values or []:
        silo = normalize_silo(value)
        if silo not in normalized:
            normalized.append(silo)
    return normalized or ["teach"]
