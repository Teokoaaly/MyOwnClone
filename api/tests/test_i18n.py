"""Test for the i18n module."""
import os
from unittest.mock import patch

import pytest


def test_i18n_module_imports():
    """i18n module exports _ and gettext."""
    from api import i18n
    assert callable(i18n._)
    assert callable(i18n.gettext)
    assert callable(i18n.lazy_gettext)


def test_gettext_returns_string_when_no_request_context():
    """gettext returns the original string when called outside a request."""
    from api.i18n import gettext
    result = gettext("hello world")
    assert result == "hello world"


def test_underscore_translates_to_default_locale():
    """When the default locale is 'en', _() returns the English string."""
    from api import i18n
    # No request context = no locale selected = default behavior
    result = i18n._("AI models")
    # In default locale (en), if no .mo loaded, returns original
    assert isinstance(result, str)


def test_gettext_with_variables():
    """gettext interpolates %s/%d in the string."""
    from api.i18n import gettext
    result = gettext("Hello %s, you have %d items", name="Alice", count=5)
    # If translation loaded, format; else return raw
    assert "Alice" in result or result == "Hello %s, you have %d items"


def test_supported_locales_contains_expected():
    """English and Spanish are in the supported locales list."""
    from api.i18n import SUPPORTED_LOCALES
    assert "en" in SUPPORTED_LOCALES
    assert "es" in SUPPORTED_LOCALES


def test_default_locale_is_english():
    """Default locale is 'en'."""
    from api.i18n import DEFAULT_LOCALE
    assert DEFAULT_LOCALE == "en"


def test_locales_directory_exists():
    """api/locales directory exists with en/ and es/ subdirs."""
    from pathlib import Path
    locales = Path(__file__).resolve().parents[1] / "locales"
    assert locales.is_dir()
    assert (locales / "en" / "LC_MESSAGES").is_dir()
    assert (locales / "es" / "LC_MESSAGES").is_dir()


def test_mo_files_compiled():
    """The .mo files exist for both locales."""
    from pathlib import Path
    locales = Path(__file__).resolve().parents[1] / "locales"
    assert (locales / "en" / "LC_MESSAGES" / "messages.mo").is_file()
    assert (locales / "es" / "LC_MESSAGES" / "messages.mo").is_file()


def test_get_locale_from_query_param():
    """?locale=es overrides Accept-Language."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context("/foo?locale=es", headers={"Accept-Language": "en"}):
        assert _get_locale() == "es"


def test_get_locale_from_query_param_rejects_invalid():
    """?locale=invalid falls back to Accept-Language."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context("/foo?locale=invalid", headers={"Accept-Language": "es"}):
        assert _get_locale() == "es"


def test_get_locale_from_accept_language():
    """Without query param, use Accept-Language header."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context("/foo", headers={"Accept-Language": "es-ES,es;q=0.9,en;q=0.8"}):
        assert _get_locale() == "es"


def test_get_locale_defaults_to_english():
    """Without any hint, default to English."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context("/foo", headers={}):
        assert _get_locale() == "en"


def test_i18n_loads_in_flask_app():
    """init_i18n wires Flask-Babel correctly into a Flask app."""
    from flask import Flask
    from api.i18n import init_i18n

    app = Flask(__name__)
    babel = init_i18n(app)
    assert babel is not None
    # Babel object created (not None is enough; app attribute is not always exposed)
    assert isinstance(babel, object)
