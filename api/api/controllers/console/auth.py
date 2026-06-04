"""Authentication blueprint — JWT-based login."""
from flask import Blueprint, request, jsonify
import jwt
import bcrypt
import psycopg2
import os
from datetime import datetime, timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/console/api/auth")


def _get_db_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "myownclone_postgres"),
        port=os.environ.get("DB_PORT", "5432"),
        user=os.environ.get("DB_USERNAME", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
        dbname=os.environ.get("DB_DATABASE", "myownclone"),
    )


def _get_secret_key():
    return os.environ.get("JWT_SECRET_KEY", "dev-secret-change-me")


def _verify_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, _get_secret_key(), algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

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
            return jsonify({"error": "Invalid credentials"}), 401

        account_id, db_email, db_password_hash, name, role, tenant_id = row

        if not db_password_hash:
            return jsonify({"error": "Account has no password set"}), 401

        if not bcrypt.checkpw(password.encode("utf-8"), db_password_hash.encode("utf-8")):
            return jsonify({"error": "Invalid credentials"}), 401

        payload = {
            "sub": account_id,
            "tenant_id": str(tenant_id) if tenant_id else "default",
            "role": role or "admin",
            "email": db_email,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(hours=24),
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
