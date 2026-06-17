"""Authentication blueprint — JWT-based login with rate limiting."""
import logging
import time
from collections import defaultdict
from flask import Blueprint, request, jsonify
import jwt
import bcrypt
import psycopg2
import os
from datetime import datetime, timedelta, timezone

from api.libs.jwt_utils import _get_secret_key, _verify_token

logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth", __name__, url_prefix="/console/api/auth")

# ── Rate limiter (Redis with in-memory fallback) ────────────────────────────
# Tracks failed login attempts per IP. 5 attempts → 15-minute ban.
# In production, configure REDIS_HOST/REDIS_PASSWORD so attempts persist
# across worker processes and restarts. In dev, falls back to a per-process
# in-memory store.
_RATE_LIMIT_MAX_ATTEMPTS = 5
_RATE_LIMIT_WINDOW_SECONDS = 900  # 15 minutes
_RATE_LIMIT_BAN_SECONDS = 900  # 15 minutes
_RATE_LIMIT_KEY_PREFIX = "myownclone:login_attempts:"

_memory_fallback: dict[str, list[float]] = defaultdict(list)
_redis_client = None
_redis_checked = False


def _get_redis():
    """Lazy-init a Redis client. Returns None if Redis is not configured or
    unreachable; callers must fall back to the in-memory store."""
    global _redis_client, _redis_checked
    if _redis_checked:
        return _redis_client
    _redis_checked = True
    host = os.environ.get("REDIS_HOST")
    password = os.environ.get("REDIS_PASSWORD")
    port = int(os.environ.get("REDIS_PORT", "6379"))
    if not host:
        return None
    try:
        import redis
        redis_kwargs = dict(
            host=host,
            port=port,
            password=password or None,
            socket_connect_timeout=1.0,
            socket_timeout=1.0,
        )
        if os.environ.get("REDIS_TLS", "").lower() == "true":
            redis_kwargs["ssl"] = True
            redis_kwargs["ssl_cert_reqs"] = None  # self-signed cert on internal network
        client = redis.Redis(**redis_kwargs)
        client.ping()
        _redis_client = client
        logger.info("Rate limiter: connected to Redis at %s:%s", host, port)
    except Exception as exc:
        logger.warning(
            "Rate limiter: Redis unavailable (%s). Falling back to in-memory store.",
            exc,
        )
        _redis_client = None
    return _redis_client


def _check_rate_limit(ip: str) -> bool:
    """Check if IP is rate-limited. Returns True if allowed, False if blocked.

    This only inspects the counter; it does not increment. Call
    _record_attempt after a failed auth to register the failure.
    """
    client = _get_redis()
    key = f"{_RATE_LIMIT_KEY_PREFIX}{ip}"

    if client is not None:
        try:
            count = client.get(key)
            current = int(count) if count is not None else 0
            return current < _RATE_LIMIT_MAX_ATTEMPTS
        except Exception as exc:
            logger.warning("Rate limiter Redis read failed (%s); using memory", exc)

    now = time.time()
    attempts = _memory_fallback[ip]
    _memory_fallback[ip] = [t for t in attempts if now - t < _RATE_LIMIT_WINDOW_SECONDS]
    return len(_memory_fallback[ip]) < _RATE_LIMIT_MAX_ATTEMPTS


def _record_attempt(ip: str) -> None:
    """Record a failed login attempt for the given IP."""
    client = _get_redis()
    key = f"{_RATE_LIMIT_KEY_PREFIX}{ip}"
    if client is not None:
        try:
            count = client.incr(key)
            if count == 1:
                client.expire(key, _RATE_LIMIT_WINDOW_SECONDS)
            return
        except Exception as exc:
            logger.warning("Rate limiter Redis incr failed (%s); using memory", exc)
    _memory_fallback[ip].append(time.time())


def _reset_rate_limit(ip: str) -> None:
    """Clear failed attempts for an IP on successful login."""
    client = _get_redis()
    key = f"{_RATE_LIMIT_KEY_PREFIX}{ip}"
    if client is not None:
        try:
            client.delete(key)
            return
        except Exception as exc:
            logger.warning("Rate limiter Redis reset failed (%s)", exc)
    _memory_fallback.pop(ip, None)


def _get_db_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "myownclone_postgres"),
        port=os.environ.get("DB_PORT", "5432"),
        user=os.environ.get("DB_USER") or os.environ.get("DB_USERNAME", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
        dbname=os.environ.get("DB_NAME") or os.environ.get("DB_DATABASE", "myownclone"),
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
        # 'accounts' (Alembic) es la tabla canonica de usuarios.
        # 'users' (Drizzle/NextAuth) es legacy y se conserva como fallback
        # para tenants que aun no han migrado.
        try:
            cur.execute(
                "SELECT id, email, password AS password_hash, name, role, tenant_id "
                "FROM accounts WHERE email = %s",
                (email,),
            )
            row = cur.fetchone()
        except psycopg2.errors.UndefinedTable:
            logger.info("'accounts' table missing - will try legacy 'users'")
            row = None
        except Exception:
            logger.exception("'accounts' lookup failed - will try legacy 'users'")
            row = None

        if not row:
            # Fallback: legacy 'users' table (Drizzle/NextAuth).
            try:
                cur.execute(
                    "SELECT id, email, password_hash, name, role, tenant_id FROM users WHERE email = %s",
                    (email,),
                )
                row = cur.fetchone()
            except psycopg2.errors.UndefinedTable:
                row = None
            except Exception:
                logger.exception("Legacy 'users' fallback failed")
                row = None

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
