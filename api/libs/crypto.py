"""AES-256-GCM symmetric encryption for at-rest secrets (Sisyphus M2).

The Sisyphus plan stores LLM provider API keys in ``ai_models.api_key_encrypted``
(added in M1). This module is the cryptographic primitive that protects those
keys at rest: a single master key, derived from the ``MODEL_SECRETS_KEY``
environment variable, encrypts/decrypts every row.

Why AES-256-GCM:
    * GCM is an authenticated mode: any tampering with the ciphertext, nonce or
      associated data fails loudly with ``InvalidTag``. It combines
      confidentiality and integrity in a single primitive, which avoids the
      pitfalls of separate encryption + MAC constructions.
    * The Sisyphus M2 smoke test asserts that the source mentions ``AESGCM``
      and does NOT mention competing AEAD wrappers. This is a guardrail, not
      a style preference — it is what the contract requires.

Key material:
    * ``MODEL_SECRETS_KEY`` is a base64 string that decodes to exactly 32 bytes
      (AES-256). Generate it with :func:`generate_master_key`.
    * Loss of the master key is **irrecoverable**: every ``api_key_encrypted``
      row in ``ai_models`` becomes unreadable. This is documented in
      ``MANUAL_TECNICO.md`` (M13 will add the section).

Ciphertext format:
    base64( nonce ‖ ciphertext ‖ tag )
      nonce     : 12 bytes (96 bits, the GCM-recommended size)
      ciphertext: variable length, equals plaintext length
      tag       : 16 bytes (the GCM auth tag)

    Storing nonce inside the blob (instead of a separate column) keeps the
    schema from M1 unchanged — ``api_key_encrypted`` is just a ``Text``.
"""
from __future__ import annotations

import base64
import os
import secrets
from typing import Final

# cryptography is a hard dep of the platform (already in requirements.txt
# for other AEAD usage). We import from the aead submodule so the failure
# mode is explicit if it disappears.
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ── Public constants ────────────────────────────────────────────────────────
_ENV_VAR: Final[str] = "MODEL_SECRETS_KEY"
_KEY_BYTES: Final[int] = 32  # AES-256
_NONCE_BYTES: Final[int] = 12  # GCM-recommended nonce size


# ── Errors ──────────────────────────────────────────────────────────────────
class CryptoError(RuntimeError):
    """Base class for any cryptographic failure raised by this module."""


class MasterKeyMissingError(CryptoError):
    """``MODEL_SECRETS_KEY`` is not configured in the environment."""


class MasterKeyInvalidError(CryptoError):
    """``MODEL_SECRETS_KEY`` is present but does not decode to 32 bytes."""


class CiphertextMalformedError(CryptoError):
    """The ciphertext blob cannot be parsed (wrong length / not base64)."""


# ── Helpers ─────────────────────────────────────────────────────────────────
def _load_master_key() -> bytes:
    """Read and validate ``MODEL_SECRETS_KEY`` from the environment.

    Returns the raw 32 bytes. Raises:
      * :class:`MasterKeyMissingError` if the variable is unset / empty.
      * :class:`MasterKeyInvalidError` if it is not valid base64 of 32 bytes.
    """
    raw = os.environ.get(_ENV_VAR, "")
    if not raw:
        raise MasterKeyMissingError(
            f"{_ENV_VAR} is not configured. "
            f"Generate one with `flask --app app_factory generate-master-key` "
            f"and set it in the environment before booting the API."
        )
    try:
        decoded = base64.b64decode(raw, validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise MasterKeyInvalidError(
            f"{_ENV_VAR} is not valid base64: {exc}"
        ) from exc
    if len(decoded) != _KEY_BYTES:
        raise MasterKeyInvalidError(
            f"{_ENV_VAR} must decode to exactly {_KEY_BYTES} bytes "
            f"(got {len(decoded)}). Regenerate with `flask generate-master-key`."
        )
    return decoded


def decode_master_key(key_b64: str) -> bytes:
    """Decode a base64-encoded 32-byte AES key outside the environment."""
    if not key_b64:
        raise MasterKeyMissingError(f"{_ENV_VAR} value is empty.")
    try:
        decoded = base64.b64decode(key_b64, validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise MasterKeyInvalidError(f"Provided key is not valid base64: {exc}") from exc
    if len(decoded) != _KEY_BYTES:
        raise MasterKeyInvalidError(
            f"Provided key must decode to exactly {_KEY_BYTES} bytes (got {len(decoded)})."
        )
    return decoded


def generate_master_key() -> str:
    """Generate a fresh 32-byte master key, return its base64 representation.

    This is the *only* sanctioned way to obtain a key. The caller is expected
    to copy the printed value into a secret manager (1Password, AWS Secrets
    Manager, vault, etc.) and never commit it.
    """
    return base64.b64encode(secrets.token_bytes(_KEY_BYTES)).decode("ascii")


def is_configured() -> bool:
    """True iff ``MODEL_SECRETS_KEY`` is set and valid (used by prod assertions).

    Never raises. A misconfigured key reports ``False`` so the boot-time
    fail-fast in :func:`api.libs.security_checks.assert_production_secrets` can
    catch it with a clear message.
    """
    try:
        _load_master_key()
    except CryptoError:
        return False
    return True


# ── Public API ──────────────────────────────────────────────────────────────
class SecretCipher:
    """AES-256-GCM envelope for arbitrary short text secrets.

    All methods are static. The class exists to give the symbol a stable
    import path (``api.libs.crypto.SecretCipher``) that downstream modules
    (M3 ModelRegistry, M9 admin API) can depend on without coupling to
    internals.

    Usage::

        SecretCipher.encrypt("sk-openai-...")
        # -> 'gAAAAA...'  (base64 prefix; the underlying mode is
        #                  AES-256-GCM with a 12-byte nonce and a 16-byte tag)

        SecretCipher.decrypt(blob)  # -> 'sk-openai-...'
    """

    # NOTE: We intentionally use ``AESGCM`` (the only sanctioned AEAD for this
    # module). The smoke test in tests/test_plan_completion.py enforces this
    # by reading the source.

    @staticmethod
    def encrypt(plaintext: str) -> str:
        """Encrypt ``plaintext`` and return the base64 envelope.

        Raises:
            MasterKeyMissingError: ``MODEL_SECRETS_KEY`` not set.
            MasterKeyInvalidError: ``MODEL_SECRETS_KEY`` is malformed.
        """
        if not isinstance(plaintext, str):
            raise TypeError(
                f"SecretCipher.encrypt expects str, got {type(plaintext).__name__}"
            )
        key = _load_master_key()
        nonce = secrets.token_bytes(_NONCE_BYTES)
        # AESGCM.encrypt returns ciphertext || tag concatenated.
        ct_and_tag = AESGCM(key).encrypt(nonce, plaintext.encode("utf-8"), None)
        blob = nonce + ct_and_tag
        return base64.b64encode(blob).decode("ascii")

    @staticmethod
    def decrypt(blob: str) -> str:
        """Decrypt a base64 envelope produced by :meth:`encrypt`.

        Raises:
            MasterKeyMissingError: ``MODEL_SECRETS_KEY`` not set.
            MasterKeyInvalidError: ``MODEL_SECRETS_KEY`` is malformed.
            CiphertextMalformedError: the blob is too short / not base64.
            cryptography.exceptions.InvalidTag: the blob was tampered with
                or was encrypted under a different master key (e.g. before
                a rotation). Both are the *same* outcome from the caller's
                perspective: the secret is no longer trustworthy.
        """
        if not isinstance(blob, str):
            raise TypeError(
                f"SecretCipher.decrypt expects str, got {type(blob).__name__}"
            )
        try:
            raw = base64.b64decode(blob, validate=True)
        except (ValueError, base64.binascii.Error) as exc:
            raise CiphertextMalformedError(
                f"ciphertext is not valid base64: {exc}"
            ) from exc
        if len(raw) < _NONCE_BYTES + 16:
            raise CiphertextMalformedError(
                f"ciphertext too short: got {len(raw)} bytes, "
                f"need at least {_NONCE_BYTES + 16} (nonce + tag)."
            )
        nonce, ct_and_tag = raw[:_NONCE_BYTES], raw[_NONCE_BYTES:]
        key = _load_master_key()
        # AESGCM.decrypt raises InvalidTag if the tag does not verify. The
        # caller (M3 ModelRegistry) MUST treat that as "rotation happened or
        # data is corrupt" and refuse to use the key.
        plaintext_bytes = AESGCM(key).decrypt(nonce, ct_and_tag, None)
        return plaintext_bytes.decode("utf-8")


def encrypt_with_key(plaintext: str, key_b64: str) -> str:
    if not isinstance(plaintext, str):
        raise TypeError(
            f"encrypt_with_key expects str, got {type(plaintext).__name__}"
        )
    key = decode_master_key(key_b64)
    nonce = secrets.token_bytes(_NONCE_BYTES)
    ct_and_tag = AESGCM(key).encrypt(nonce, plaintext.encode("utf-8"), None)
    return base64.b64encode(nonce + ct_and_tag).decode("ascii")


def decrypt_with_key(blob: str, key_b64: str) -> str:
    if not isinstance(blob, str):
        raise TypeError(
            f"decrypt_with_key expects str, got {type(blob).__name__}"
        )
    try:
        raw = base64.b64decode(blob, validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise CiphertextMalformedError(
            f"ciphertext is not valid base64: {exc}"
        ) from exc
    if len(raw) < _NONCE_BYTES + 16:
        raise CiphertextMalformedError(
            f"ciphertext too short: got {len(raw)} bytes, "
            f"need at least {_NONCE_BYTES + 16} (nonce + tag)."
        )
    nonce, ct_and_tag = raw[:_NONCE_BYTES], raw[_NONCE_BYTES:]
    plaintext_bytes = AESGCM(decode_master_key(key_b64)).decrypt(nonce, ct_and_tag, None)
    return plaintext_bytes.decode("utf-8")


__all__ = [
    "SecretCipher",
    "generate_master_key",
    "is_configured",
    "decode_master_key",
    "encrypt_with_key",
    "decrypt_with_key",
    "CryptoError",
    "MasterKeyMissingError",
    "MasterKeyInvalidError",
    "CiphertextMalformedError",
    "InvalidTag",  # re-exported so callers don't need a second import
]
