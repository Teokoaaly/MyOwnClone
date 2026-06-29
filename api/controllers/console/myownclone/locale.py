"""Locale (language) endpoints for the manual selector.

These endpoints are public (no login required) so any visitor can pick
their language without signing in. The chosen locale is persisted in a
cookie (``moc_locale``) and honoured by Flask-Babel on every subsequent
request via :func:`api.i18n._get_locale`.

Endpoints:
- ``GET  /console/api/myownclone/me/locale`` returns the current locale
  plus the list of supported locales.
- ``POST /console/api/myownclone/me/locale`` accepts ``{"locale": "es"}``
  and sets the cookie. Unknown values are rejected.
"""
import logging

from flask import current_app, jsonify, request
from flask_restx import Resource

from api.controllers.console import console_ns
from api.i18n import (
    DEFAULT_LOCALE,
    LOCALE_COOKIE_NAME,
    SUPPORTED_LOCALES,
    _ as _flask_gettext,
    set_locale_cookie,
)

logger = logging.getLogger(__name__)


def _resolve_current_locale() -> str:
    """Return the locale Flask-Babel will pick for the current request."""
    # Import lazily to avoid import cycles during app boot.
    from api.i18n import _get_locale
    try:
        return _get_locale()
    except Exception:
        logger.exception("Failed to resolve current locale; using default")
        return DEFAULT_LOCALE


@console_ns.route("/myownclone/me/locale")
class MeLocaleApi(Resource):
    """Read and update the visitor's locale preference."""

    def get(self):
        """Return the current and supported locales."""
        try:
            current = _resolve_current_locale()
        except Exception:
            current = DEFAULT_LOCALE
        return {
            "locale": current,
            "supported": list(SUPPORTED_LOCALES),
            "default": DEFAULT_LOCALE,
            "cookie_name": LOCALE_COOKIE_NAME,
        }, 200

    def post(self):
        """Persist the visitor's chosen locale in a cookie."""
        payload = request.get_json(silent=True) or {}
        requested = (payload.get("locale") or "").strip().lower()
        if requested not in SUPPORTED_LOCALES:
            resp = jsonify({
                "error": "unsupported_locale",
                "message": _flask_gettext("Unsupported locale"),
                "supported": list(SUPPORTED_LOCALES),
            })
            resp.status_code = 400
            return resp
        # Echo the canonical list and what was set so the front-end can sync.
        resp = jsonify({
            "locale": requested,
            "supported": list(SUPPORTED_LOCALES),
            "default": DEFAULT_LOCALE,
            "message": _flask_gettext("Locale updated"),
        })
        resp.status_code = 200
        set_locale_cookie(resp, requested)
        return resp