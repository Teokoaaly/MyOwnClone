"""Standardized error response helpers for consistent API error format.

All API errors should follow this structure:
    {"error": {"code": "error_code", "message": "Human-readable message"}}

Usage:
    from api.libs.error_helpers import error_response
    return error_response("not_found", "Clone not found", 404)
    return error_response("unauthorized", "Missing auth", 401)
"""

from __future__ import annotations

from flask import jsonify


def error_response(code: str, message: str, status: int = 400) -> tuple:
    """Return a standardized error response.

    Args:
        code: Machine-readable error code (e.g., "not_found", "unauthorized")
        message: Human-readable error message
        status: HTTP status code

    Returns:
        Tuple of (response, status_code) for Flask
    """
    return jsonify({
        "error": {
            "code": code,
            "message": message,
        }
    }), status


def not_found(message: str = "Resource not found") -> tuple:
    return error_response("not_found", message, 404)


def unauthorized(message: str = "Authentication required") -> tuple:
    return error_response("unauthorized", message, 401)


def forbidden(message: str = "Access denied") -> tuple:
    return error_response("forbidden", message, 403)


def bad_request(message: str = "Invalid request") -> tuple:
    return error_response("bad_request", message, 400)


def rate_limited(retry_after: int | None = None) -> tuple:
    payload = {"error": {"code": "rate_limited", "message": "Too many requests"}}
    if retry_after:
        payload["retry_after"] = retry_after
    return jsonify(payload), 429


def server_error(message: str = "Internal server error") -> tuple:
    return error_response("server_error", message, 500)
