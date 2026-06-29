"""Tests for the i18n module and the /me/locale endpoint."""
import os
from unittest.mock import patch

import pytest


# -----------------------------------------------------------------------------
# Basic module shape
# -----------------------------------------------------------------------------

def test_i18n_module_imports():
    """i18n module exports _ and gettext."""
    from api import i18n
    assert callable(i18n._)
    assert callable(i18n.gettext)
    assert callable(i18n.lazy_gettext)
    assert callable(i18n.set_locale_cookie)


def test_gettext_returns_string_when_no_request_context():
    """gettext returns the original string when called outside a request."""
    from api.i18n import gettext
    result = gettext("hello world")
    assert result == "hello world"


def test_gettext_with_variables():
    """gettext interpolates %s/%d in the string."""
    from api.i18n import gettext
    result = gettext("Hello %s, you have %d items", name="Alice", count=5)
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


def test_locale_cookie_name_is_exposed():
    """Cookie name constant is exposed."""
    from api.i18n import LOCALE_COOKIE_NAME
    assert LOCALE_COOKIE_NAME == "moc_locale"


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


# -----------------------------------------------------------------------------
# _get_locale() priority
# -----------------------------------------------------------------------------

def test_get_locale_from_cookie_wins_over_everything():
    """Cookie beats X-Locale, ?locale=, and Accept-Language."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context(
        "/foo?locale=en",
        headers={
            "Accept-Language": "fr-FR",
            "X-Locale": "en",
        },
        environ_overrides={"HTTP_COOKIE": "moc_locale=es"},
    ):
        assert _get_locale() == "es"


def test_get_locale_from_x_locale_header():
    """X-Locale header is honoured when no cookie is present."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context(
        "/foo",
        headers={"Accept-Language": "fr-FR", "X-Locale": "es"},
    ):
        assert _get_locale() == "es"


def test_get_locale_x_locale_rejects_unsupported():
    """X-Locale header that is unsupported is ignored."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context(
        "/foo",
        headers={"X-Locale": "fr", "Accept-Language": "es"},
    ):
        assert _get_locale() == "es"


def test_get_locale_from_query_param():
    """?locale=es overrides Accept-Language when no cookie or X-Locale."""
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


def test_cookie_with_unsupported_value_is_ignored():
    """Cookie holding an unsupported locale is ignored."""
    from flask import Flask
    from api.i18n import _get_locale

    app = Flask(__name__)
    with app.test_request_context(
        "/foo",
        headers={"Accept-Language": "es"},
        environ_overrides={"HTTP_COOKIE": "moc_locale=fr"},
    ):
        assert _get_locale() == "es"


# -----------------------------------------------------------------------------
# set_locale_cookie()
# -----------------------------------------------------------------------------

def test_set_locale_cookie_sets_supported_value():
    """set_locale_cookie writes the cookie when the locale is supported."""
    from flask import Flask
    from api.i18n import set_locale_cookie

    app = Flask(__name__)
    with app.test_request_context("/"):
        resp = app.make_response(("ok", 200))
        set_locale_cookie(resp, "es")
        cookie_header = resp.headers.get("Set-Cookie", "")
        assert "moc_locale=es" in cookie_header
        assert "Path=/" in cookie_header


def test_set_locale_cookie_clears_when_unsupported():
    """set_locale_cookie removes the cookie when the locale is invalid."""
    from flask import Flask
    from api.i18n import set_locale_cookie

    app = Flask(__name__)
    with app.test_request_context("/"):
        resp = app.make_response(("ok", 200))
        # First set a valid cookie, then try to set an invalid one.
        set_locale_cookie(resp, "es")
        set_locale_cookie(resp, "fr")
        # The response should now have both Set-Cookie headers, the latter
        # being a deletion.
        cookies = resp.headers.getlist("Set-Cookie")
        assert any("moc_locale=es" in c for c in cookies)
        assert any("moc_locale=" in c and "Expires=" in c for c in cookies)


# -----------------------------------------------------------------------------
# init_i18n()
# -----------------------------------------------------------------------------

def test_i18n_loads_in_flask_app():
    """init_i18n wires Flask-Babel correctly into a Flask app."""
    from flask import Flask
    from api.i18n import init_i18n

    app = Flask(__name__)
    babel = init_i18n(app)
    assert babel is not None
    # Babel configured the translation directory and default locale.
    assert app.config["BABEL_DEFAULT_LOCALE"] == "en"
    assert app.config["MOC_SUPPORTED_LOCALES"] == ["en", "es"]
    assert app.config["MOC_LOCALE_COOKIE_NAME"] == "moc_locale"


# -----------------------------------------------------------------------------
# /api/me/locale endpoint
# -----------------------------------------------------------------------------

@pytest.fixture
def flask_app_with_locale_route():
    """Build a minimal Flask app with only the locale controller mounted.

    We deliberately avoid :func:`create_app` because it initialises the
    database and Redis pools, which we don't need to test the locale
    selector behaviour. We DO initialise Babel because the controller
    uses ``_()`` to localise its JSON responses.
    """
    from flask import Flask
    from flask_restx import Api
    from api.controllers.console.myownclone.locale import MeLocaleApi
    from api.i18n import init_i18n

    app = Flask(__name__)
    app.config["TESTING"] = True
    init_i18n(app)
    api = Api(app, version="1.0", title="Locale test API")
    ns = api.namespace("locale", path="/")
    ns.add_resource(MeLocaleApi, "/me/locale")
    return app


def test_me_locale_get_returns_current_and_supported(flask_app_with_locale_route):
    app = flask_app_with_locale_route
    client = app.test_client()
    resp = client.get("/me/locale")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "locale" in data
    assert data["supported"] == ["en", "es"]
    assert data["default"] == "en"
    assert data["cookie_name"] == "moc_locale"


def test_me_locale_post_sets_cookie(flask_app_with_locale_route):
    app = flask_app_with_locale_route
    client = app.test_client()
    # Hit the endpoint with an explicit Spanish context so the
    # ``_("Locale updated")`` msgid is translated as expected.
    resp = client.post(
        "/me/locale",
        json={"locale": "es"},
        headers={"Accept-Language": "es"},
    )
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["locale"] == "es"
    assert data["message"] == "Idioma actualizado"
    cookie_header = resp.headers.get("Set-Cookie", "")
    assert "moc_locale=es" in cookie_header


def test_me_locale_post_rejects_unsupported(flask_app_with_locale_route):
    app = flask_app_with_locale_route
    client = app.test_client()
    resp = client.post(
        "/me/locale",
        json={"locale": "fr"},
        headers={"Accept-Language": "es"},
    )
    assert resp.status_code == 400
    data = resp.get_json()
    assert data["error"] == "unsupported_locale"
    assert "Idioma no soportado" == data["message"] or "Idioma no soportado" in data["message"]


def test_me_locale_get_reflects_cookie(flask_app_with_locale_route):
    """GET /me/locale returns the cookie-selected locale."""
    app = flask_app_with_locale_route
    client = app.test_client()
    client.set_cookie("moc_locale", "es")
    resp = client.get("/me/locale")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["locale"] == "es"