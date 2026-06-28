"""Internationalization (i18n) setup for the MyOwnClone backend.

This module wires Flask-Babel into the Flask app, exposes the
translation callable `_()`, and provides a helper to pick the locale
for each request (from the `Accept-Language` header, the `locale`
query parameter, or a user-preference cookie).

Usage in application code:

    from api.i18n import _

    @app.route("/")
    def index():
        flash(_("Welcome to MyOwnClone"))
        return render_template("index.html")

Translation workflow:

    # 1. Mark translatable strings with _() or gettext()
    # 2. Extract to .pot:
    #      pybabel extract -F api/babel.cfg -o api/locales/messages.pot api/
    # 3. Create or update a locale (e.g. Spanish):
    #      pybabel init -i api/locales/messages.pot -d api/locales -l es
    #      # or update existing:
    #      pybabel update -i api/locales/messages.pot -d api/locales -l es
    # 4. Edit api/locales/es/LC_MESSAGES/messages.po
    # 5. Compile:
    #      pybabel compile -d api/locales
"""
import os
from typing import Any, Optional

from flask import Flask, g, request
from flask_babel import Babel, gettext as _flask_gettext

# Default locale
DEFAULT_LOCALE = "en"
# Supported locales (must have a .mo file compiled in api/locales/<lang>/LC_MESSAGES)
SUPPORTED_LOCALES = ["en", "es"]


def _get_locale() -> str:
    """Pick the best locale for the current request.

    Priority:
    1. ?locale= query parameter (for testing)
    2. X-Locale header (set by Next.js proxy or nginx)
    3. Session-stored preference (g.locale, set by login flow)
    4. Accept-Language header
    5. DEFAULT_LOCALE
    """
    # 0. X-Locale header (set by Next.js proxy via nginx, or directly)
    x_locale = request.headers.get("X-Locale", "").strip()
    if x_locale and x_locale in SUPPORTED_LOCALES:
        return x_locale

    # 1. Query parameter
    forced = request.args.get("locale")
    if forced and forced in SUPPORTED_LOCALES:
        return forced

    # 2. Session-stored preference (g.locale is set by /auth/login)
    g_locale = getattr(g, "locale", None)
    if g_locale and g_locale in SUPPORTED_LOCALES:
        return g_locale

    # 3. Accept-Language header
    if request.accept_languages:
        best = request.accept_languages.best_match(SUPPORTED_LOCALES)
        if best:
            return best

    return DEFAULT_LOCALE


def init_i18n(app: Flask) -> Babel:
    """Initialize Flask-Babel on the given Flask app.

    Returns the Babel instance so it can be extended in tests if needed.
    """
    # Tell Flask-Babel where to find compiled .mo files.
    import os
    locales_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "locales"
    )
    app.config.setdefault("BABEL_TRANSLATION_DIRECTORIES", locales_path)
    app.config.setdefault("BABEL_DEFAULT_LOCALE", DEFAULT_LOCALE)
    babel = Babel(app, locale_selector=_get_locale)
    return babel


def _(s: str) -> str:
    """Shorthand for gettext / Flask-Babel's translation.

    Importable as `from api.i18n import _` for use in application code.
    The function picks the current request's locale from Flask's request
    context automatically.
    """
    return _flask_gettext(s)


def gettext(s: str, **variables: Any) -> str:
    """Translate and interpolate a string with the current locale."""
    msg = _(s)
    if variables:
        try:
            return msg % variables
        except (KeyError, TypeError):
            return msg
    return msg


def lazy_gettext(s: str):
    """Lazy translation (returns a marker evaluated at request time)."""
    from flask_babel import lazy_gettext as _lazy
    return _lazy(s)
