"""Authentication blueprint — JWT-based login with rate limiting."""
import time
from collections import defaultdict
from flask import Blueprint, request, jsonify
import jwt
import bcrypt
import psycopg2
import os
from datetime import datetime, timedelta, timezone

from api.libs.jwt_utils import _get_secret_key, _verify_token

auth_bp = Blueprint("auth", __name__, url_prefix="/console/api/auth")

# ── In-memory rate limiter ───────────────────────────────────────────────────
# Tracks failed login attempts per IP. 5 attempts → 15-minute ban.
# In production, replace with Redis-based rate limiting.
_rate_limit_store: dict[str, list[float]] = defaultdict(list)
_RATE_LIMIT_MAX_ATTEMPTS = 5
_RATE_LIMIT_WINDOW_SECONDS = 900  # 15 minutes
_RATE_LIMIT_BAN_SECONDS = 900  # 15 minutes


def _check_rate_limit(ip: str) -> bool:
    """Check if IP is rate-limited. Returns True if allowed, False if blocked."""
    now = time.time()
    attempts = _rate_limit_store[ip]
    # Prune old entries outside the window
    _rate_limit_store[ip] = [t for t in attempts if now - t < _RATE_LIMIT_WINDOW_SECONDS]

    if len(_rate_limit_store[ip]) >= _RATE_LIMIT_MAX_ATTEMPTS:
        return False  # Rate limited
    return True


def _record_attempt(ip: str) -> None:
    """Record a failed login attempt for the given IP."""
    _rate_limit_store[ip].append(time.time())


def _reset_rate_limit(ip: str) -> None:
    """Clear failed attempts for an IP on successful login."""
    _rate_limit_store.pop(ip, None)


def _get_db_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "myownclone_postgres"),
        port=os.environ.get("DB_PORT", "5432"),
        user=os.environ.get("DB_USERNAME", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
        dbname=os.environ.get("DB_DATABASE", "myownclone"),
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # ── Rate limiting by IP ──────────────────────────────────────────────────
    client_ip = request.remote_addr or "unknown"
    if not _check_rate_limit(client_ip):
        retry_after = _RATE_LIMIT_BAN_SECONDS
        return jsonify({
            "error": f"Demasiados intentos. Intenta de nuevo en {retry_after // 60} minutos.",
            "retry_after_seconds": retry_after,
        }), 429

    conn = _get_db_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, email, password, name, role, tenant_id FROM accounts WHERE email = %s",
            (email,),
        )
        row = cur.fetchone()
        cur.close()

        if not row:
            _record_attempt(client_ip)
            return jsonify({"error": "Invalid credentials"}), 401

        account_id, db_email, db_password_hash, name, role, tenant_id = row

        if not db_password_hash:
            _record_attempt(client_ip)
            return jsonify({"error": "Account has no password set"}), 401

        if not bcrypt.checkpw(password.encode("utf-8"), db_password_hash.encode("utf-8")):
            _record_attempt(client_ip)
            return jsonify({"error": "Invalid credentials"}), 401

        # Successful login — reset rate limit for this IP
        _reset_rate_limit(client_ip)

        now = datetime.now(timezone.utc)
        payload = {
            "sub": account_id,
            "tenant_id": str(tenant_id) if tenant_id else "default",
            "role": role or "admin",
            "email": db_email,
            "iat": now,
            "exp": now + timedelta(hours=24),
        }
        token = jwt.encode(payload, _get_secret_key(), algorithm="HS256")

        return jsonify({
            "token": token,
            "expires_in": 86400,
            "user": {"email": db_email, "name": name, "role": role},
        }), 200

    finally:
        conn.close()


@auth_bp.route("/verify", methods=["GET"])
def verify():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing token"}), 401

    payload = _verify_token(auth_header[7:])
    if not payload:
        return jsonify({"error": "Invalid or expired token"}), 401

    return jsonify({"valid": True, "user": payload.get("email"), "role": payload.get("role")}), 200


__all__ = ["auth_bp", "_verify_token"]
