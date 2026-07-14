"""Authentication blueprint — JWT-based login with rate limiting."""
import logging
import time
from collections import defaultdict
from flask import Blueprint, request, jsonify
import jwt
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from sqlalchemy import select, text
from sqlalchemy.exc import ProgrammingError

from api.extensions.ext_database import db
from api.libs.jwt_utils import _get_secret_key, _verify_token
from api.models.account import Account

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

# P2 (H-02): list of trusted proxy IPs/CIDRs that may set X-Forwarded-For.
# Empty by default (operator must opt-in via TRUSTED_PROXIES env var, comma-separated).
# This prevents client-side header spoofing of X-Forwarded-For for rate-limit bucketing.
import ipaddress as _ipaddress
_TRUSTED_PROXIES: list = []
_trusted_proxies_loaded = False


def _load_trusted_proxies() -> None:
    global _TRUSTED_PROXIES, _trusted_proxies_loaded
    if _trusted_proxies_loaded:
        return
    _trusted_proxies_loaded = True
    raw = os.environ.get("TRUSTED_PROXIES", "")
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            _TRUSTED_PROXIES.append(_ipaddress.ip_network(token, strict=False))
        except ValueError:
            # Allow bare IPs in addition to CIDRs.
            try:
                _TRUSTED_PROXIES.append(_ipaddress.ip_address(token))
            except ValueError:
                logger.warning("TRUSTED_PROXIES: ignoring invalid entry %r", token)


def _client_ip(req) -> str:
    """Best-effort client IP extraction.

    P2 (H-02): prefer ``X-Forwarded-For`` ONLY if the immediate peer
    (request.remote_addr) is in TRUSTED_PROXIES. Otherwise fall back to
    remote_addr to prevent attackers from spoofing a different bucket per
    attempt (bypassing the per-IP rate limit).
    """
    _load_trusted_proxies()
    remote = req.remote_addr or "unknown"
    if _TRUSTED_PROXIES:
        try:
            remote_ip = _ipaddress.ip_address(remote)
        except ValueError:
            return remote
        trusted = any(
            remote_ip in net for net in _TRUSTED_PROXIES
        )
        if trusted:
            xff = req.headers.get("X-Forwarded-For", "")
            if xff:
                # First entry is the original client.
                client = xff.split(",", 1)[0].strip()
                if client:
                    return client
    return remote


def _prune_memory_fallback(now: float) -> None:
    """P2 (H-02): periodically evict IPs whose entire window has expired.

    Without this, an attacker that spams distinct IPs would grow
    ``_memory_fallback`` unbounded (memory leak). Called opportunistically
    from ``_check_rate_limit`` at most once every 60s.
    """
    global _last_memory_prune
    if now - _last_memory_prune < _MEMORY_PRUNE_INTERVAL:
        return
    _last_memory_prune = now
    cutoff = now - _RATE_LIMIT_WINDOW_SECONDS
    stale = [ip for ip, ts_list in _memory_fallback.items() if not ts_list or max(ts_list) < cutoff]
    for ip in stale:
        _memory_fallback.pop(ip, None)


_last_memory_prune = 0.0
_MEMORY_PRUNE_INTERVAL = 60.0


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
        client = redis.Redis(
            host=host,
            port=port,
            password=password or None,
            socket_connect_timeout=1.0,
            socket_timeout=1.0,
        )
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
    _prune_memory_fallback(now)
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


def _lookup_account_via_sqlalchemy(email: str):
    """Look up an account row using the Flask-SQLAlchemy session.

    P1.10 (H-10): the previous implementation opened a raw psycopg2
    connection per login attempt, bypassing the Flask-SQLAlchemy pool and
    connection reuse. Under brute-force this is a DoS amplifier (one
    fresh TCP connection per attempt) and prevents the application from
    using the session lifecycle (transactions, rollback on error, etc.).

    This helper returns a dict-like row with the canonical field names
    (``password_hash`` aliasing ``Account.password``), or ``None`` if the
    row is missing or the lookup fails. The legacy ``users`` table is
    still consulted as a fallback for tenants not yet migrated.
    """
    # 1. Canonical: accounts (Alembic-managed).
    try:
        acct = db.session.execute(
            select(Account).where(Account.email == email)
        ).scalar_one_or_none()
        if acct is not None:
            return {
                "id": str(acct.id),
                "email": acct.email,
                "password_hash": acct.password,
                "name": acct.name,
                "role": acct.role,
                "tenant_id": str(acct.tenant_id) if acct.tenant_id else None,
            }
    except ProgrammingError:
        logger.info("'accounts' lookup failed - will try legacy 'users'")
    except Exception:
        logger.exception("'accounts' lookup failed - will try legacy 'users'")

    # 2. Legacy fallback: users (Drizzle/NextAuth schema).
    try:
        row = db.session.execute(
            text(
                "SELECT id, email, password_hash, name, role, tenant_id "
                "FROM users WHERE email = :email"
            ),
            {"email": email},
        ).first()
        if row is None:
            return None
        return {
            "id": str(row[0]),
            "email": row[1],
            "password_hash": row[2],
            "name": row[3],
            "role": row[4],
            "tenant_id": str(row[5]) if row[5] else None,
        }
    except ProgrammingError:
        # 'users' table missing too — treat as no account.
        return None
    except Exception:
        logger.exception("Legacy 'users' fallback failed")
        return None


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # ── Rate limiting by IP ──────────────────────────────────────────────────
    client_ip = _client_ip(request)
    if not _check_rate_limit(client_ip):
        retry_after = _RATE_LIMIT_BAN_SECONDS
        return jsonify({
            "error": f"Demasiados intentos. Intenta de nuevo en {retry_after // 60} minutos.",
            "retry_after_seconds": retry_after,
        }), 429

    # P1.10 (H-10): use the Flask-SQLAlchemy session instead of a raw
    # psycopg2 connection. The session is connection-pooled, transaction-
    # safe, and avoids the per-login TCP handshake DoS amplifier.
    row = _lookup_account_via_sqlalchemy(email)

    if not row:
        _record_attempt(client_ip)
        return jsonify({"error": "Invalid credentials"}), 401

    account_id = row["id"]
    db_email = row["email"]
    db_password_hash = row["password_hash"]
    name = row["name"]
    role = row["role"]
    tenant_id = row["tenant_id"]

    if not db_password_hash:
        _record_attempt(client_ip)
        return jsonify({"error": "Account has no password set"}), 401

    try:
        if not bcrypt.checkpw(password.encode("utf-8"), db_password_hash.encode("utf-8")):
            _record_attempt(client_ip)
            return jsonify({"error": "Invalid credentials"}), 401
    except ValueError:
        # bcrypt.checkpw raises ValueError if the stored hash is not a valid
        # bcrypt string (legacy md5 / argon2 / plain text). Treat as bad
        # credentials instead of leaking the exception as a 500.
        logger.warning(
            "Stored password hash for %s is not a valid bcrypt hash", email,
        )
        _record_attempt(client_ip)
        return jsonify({"error": "Invalid credentials"}), 401

    # Successful login — reset rate limit for this IP
    _reset_rate_limit(client_ip)

    now = datetime.now(timezone.utc)
    payload = {
        "sub": account_id,
        "tenant_id": tenant_id or "default",
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
