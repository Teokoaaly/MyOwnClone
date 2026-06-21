"""Tests for the AES-256-GCM cipher (Sisyphus M2).

Five scenarios from the HANDOFF_LLM §5 M2 contract:

  1. Round-trip: encrypt → decrypt == plaintext.
  2. Tampering: any byte change in the blob → InvalidTag.
  3. Missing key: empty ``MODEL_SECRETS_KEY`` → MasterKeyMissingError.
  4. Wrong length: base64 that decodes to != 32 bytes → MasterKeyInvalidError.
  5. Rotation: A encrypts, B decrypts → InvalidTag (same outcome as tampering).

Plus a few guard tests around the security_checks module so the smoke test
in ``tests/test_plan_completion.py::test_m2_security_checks_requires_master_key``
is doubly covered.

These tests are unit-level: they do not need a Flask app context, do not
talk to the DB, and never read real secrets. Every test sets its own
``MODEL_SECRETS_KEY`` via ``monkeypatch.setenv`` and restores the previous
value via the ``env_clean`` fixture.
"""
from __future__ import annotations

import base64

import pytest

from api.libs.crypto import (
    CiphertextMalformedError,
    MasterKeyInvalidError,
    MasterKeyMissingError,
    SecretCipher,
    generate_master_key,
    is_configured,
)
from cryptography.exceptions import InvalidTag


# ── Fixtures ────────────────────────────────────────────────────────────────
@pytest.fixture
def env_clean(monkeypatch):
    """Strip ``MODEL_SECRETS_KEY`` from the environment for the test."""
    monkeypatch.delenv("MODEL_SECRETS_KEY", raising=False)
    return monkeypatch


def _b64(nbytes: int) -> str:
    return base64.b64encode(b"k" * nbytes).decode("ascii")


# ── 1. Round-trip ───────────────────────────────────────────────────────────
def test_encrypt_decrypt_roundtrip(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    plain = "sk-openai-***REDACTED***-EXAMPLE"
    blob = SecretCipher.encrypt(plain)
    assert isinstance(blob, str)
    assert blob != plain, "ciphertext must differ from plaintext"
    # GCM prefix should be base64 of (12-byte nonce + ciphertext + 16-byte tag).
    # The base64 length must round-trip exactly.
    decoded = base64.b64decode(blob, validate=True)
    assert len(decoded) >= 12 + 16, "blob too short to contain nonce + tag"
    assert SecretCipher.decrypt(blob) == plain


def test_each_encryption_uses_a_fresh_nonce(env_clean):
    """Two encryptions of the same plaintext MUST yield different ciphertexts.

    Without a fresh nonce per call, AES-GCM catastrophically breaks (reuse
    leaks XOR of plaintexts). This is a non-negotiable invariant.
    """
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    a = SecretCipher.encrypt("same plaintext")
    b = SecretCipher.encrypt("same plaintext")
    assert a != b, "GCM nonce must be unique per encrypt() call"


# ── 2. Tampering ────────────────────────────────────────────────────────────
def test_tampered_ciphertext_raises_invalid_tag(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    blob = SecretCipher.encrypt("payload")
    tampered = blob[:-4] + "XXXX"
    with pytest.raises(InvalidTag):
        SecretCipher.decrypt(tampered)


def test_short_ciphertext_rejected(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    # base64 of 10 bytes — below the 12 (nonce) + 16 (tag) minimum.
    too_short = base64.b64encode(b"x" * 10).decode()
    with pytest.raises(CiphertextMalformedError):
        SecretCipher.decrypt(too_short)


def test_non_base64_ciphertext_rejected(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    with pytest.raises(CiphertextMalformedError):
        SecretCipher.decrypt("@@@not-base64@@@")


# ── 3. Missing key ──────────────────────────────────────────────────────────
def test_encrypt_without_key_raises_missing(env_clean):
    # env_clean already removed MODEL_SECRETS_KEY
    with pytest.raises(MasterKeyMissingError):
        SecretCipher.encrypt("anything")


def test_decrypt_without_key_raises_missing(env_clean):
    # Use a known-valid blob from another key just to get past base64 parse;
    # the key check happens after that and is what we are testing.
    blob = base64.b64encode(b"n" * 32).decode()  # valid b64, too short though
    # Make it long enough to pass the malformed check.
    blob = base64.b64encode(b"n" * 64).decode()
    with pytest.raises(MasterKeyMissingError):
        SecretCipher.decrypt(blob)


def test_empty_string_key_raises_missing(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", "")
    with pytest.raises(MasterKeyMissingError):
        SecretCipher.encrypt("x")


# ── 4. Wrong length ─────────────────────────────────────────────────────────
@pytest.mark.parametrize("nbytes", [16, 24, 31, 33, 48, 64])
def test_wrong_length_key_raises_invalid(env_clean, nbytes: int):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(nbytes))
    with pytest.raises(MasterKeyInvalidError):
        SecretCipher.encrypt("x")


def test_non_base64_key_raises_invalid(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", "not-valid-base64-!!!")
    with pytest.raises(MasterKeyInvalidError):
        SecretCipher.encrypt("x")


# ── 5. Rotation (A encrypts, B decrypts → fail) ────────────────────────────
def test_rotation_fails_to_decrypt_old_ciphertext(env_clean):
    key_a = base64.b64encode(b"A" * 32).decode()
    key_b = base64.b64encode(b"B" * 32).decode()

    env_clean.setenv("MODEL_SECRETS_KEY", key_a)
    blob_under_a = SecretCipher.encrypt("top secret")

    # Operator rotates by replacing the env var.
    env_clean.setenv("MODEL_SECRETS_KEY", key_b)
    with pytest.raises(InvalidTag):
        SecretCipher.decrypt(blob_under_a)


def test_after_rotation_new_encryptions_decrypt(env_clean):
    """The new key MUST work for new data (sanity check after rotation)."""
    key_a = base64.b64encode(b"A" * 32).decode()
    key_b = base64.b64encode(b"B" * 32).decode()

    env_clean.setenv("MODEL_SECRETS_KEY", key_a)
    blob_a = SecretCipher.encrypt("old")

    env_clean.setenv("MODEL_SECRETS_KEY", key_b)
    blob_b = SecretCipher.encrypt("new")
    assert SecretCipher.decrypt(blob_b) == "new"
    with pytest.raises(InvalidTag):
        SecretCipher.decrypt(blob_a)


# ── Helpers ────────────────────────────────────────────────────────────────
def test_generate_master_key_returns_valid_32_bytes():
    """A freshly generated key MUST decode to exactly 32 bytes."""
    k = generate_master_key()
    assert isinstance(k, str)
    assert len(base64.b64decode(k, validate=True)) == 32


def test_generate_master_key_returns_unique_values():
    """Two calls MUST return different keys."""
    a = generate_master_key()
    b = generate_master_key()
    assert a != b


def test_is_configured_true_when_valid(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    assert is_configured() is True


def test_is_configured_false_when_missing(env_clean):
    assert is_configured() is False


def test_is_configured_false_when_wrong_length(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(16))
    assert is_configured() is False


# ── Type safety ────────────────────────────────────────────────────────────
def test_encrypt_rejects_non_string(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    with pytest.raises(TypeError):
        SecretCipher.encrypt(b"bytes-not-str")  # type: ignore[arg-type]


def test_decrypt_rejects_non_string(env_clean):
    env_clean.setenv("MODEL_SECRETS_KEY", _b64(32))
    with pytest.raises(TypeError):
        SecretCipher.decrypt(b"bytes-not-str")  # type: ignore[arg-type]


# ── security_checks integration ─────────────────────────────────────────────
def test_security_checks_requires_master_key_in_prod(monkeypatch):
    """Smoke test M2 contract: security_checks._REQUIRED_IN_PROD contains MODEL_SECRETS_KEY."""
    from api.libs import security_checks
    assert "MODEL_SECRETS_KEY" in list(security_checks._REQUIRED_IN_PROD)


def test_security_checks_aborts_in_prod_without_key(monkeypatch):
    """Without MODEL_SECRETS_KEY in prod, assert_production_secrets must fail loudly."""
    from api.libs import security_checks
    monkeypatch.setattr(security_checks, "_is_production", lambda: True)
    monkeypatch.delenv("MODEL_SECRETS_KEY", raising=False)
    monkeypatch.delenv("JWT_SECRET_KEY", raising=False)
    monkeypatch.delenv("IMPERSONATION_TOKEN_PEPPER", raising=False)
    monkeypatch.delenv("ALLOWED_ORIGINS", raising=False)
    monkeypatch.delenv("REDIS_PASSWORD", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DB_HOST", raising=False)
    monkeypatch.delenv("DB_USER", raising=False)
    monkeypatch.delenv("DB_NAME", raising=False)
    monkeypatch.setenv("DB_PASSWORD", "test-db-password-not-default")
    with pytest.raises(SystemExit) as excinfo:
        security_checks.assert_production_secrets()
    # Exit code is 1 per the module.
    assert excinfo.value.code == 1