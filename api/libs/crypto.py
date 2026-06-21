"""AES-GCM encryption/decryption for model secrets."""
from __future__ import annotations
import os
import base64
from typing import Optional

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


MASTER_KEY_ENV = "MODEL_SECRETS_KEY"


def get_master_key() -> bytes:
    """Get master key from env var. Returns 32 bytes (256 bits).

    Raises RuntimeError if not set.
    """
    key_b64 = os.environ.get(MASTER_KEY_ENV)
    if not key_b64:
        raise RuntimeError(
            f"{MASTER_KEY_ENV} env var not set. "
            f"Generate with `flask generate-master-key`."
        )
    try:
        key = base64.b64decode(key_b64)
    except Exception as exc:
        raise RuntimeError(f"{MASTER_KEY_ENV} is not valid base64: {exc}") from exc
    if len(key) != 32:
        raise RuntimeError(
            f"{MASTER_KEY_ENV} must decode to 32 bytes (256 bits), got {len(key)}"
        )
    return key


def generate_master_key() -> str:
    """Generate a new random 256-bit master key. Returns base64 string.

    Print result to stdout (no logging, no printing to stderr) for the
    operator to copy to .env.
    """
    key = AESGCM.generate_key(bit_length=256)
    return base64.b64encode(key).decode("ascii")


class SecretCipher:
    """AES-GCM cipher for short secrets (API keys, tokens)."""

    NONCE_SIZE = 12  # 96 bits, standard for GCM
    KEY_SIZE = 32  # 256 bits

    def __init__(self, master_key: Optional[bytes] = None):
        if master_key is None:
            master_key = get_master_key()
        if len(master_key) != self.KEY_SIZE:
            raise ValueError(
                f"Master key must be {self.KEY_SIZE} bytes, got {len(master_key)}"
            )
        self._aesgcm = AESGCM(master_key)

    def encrypt(self, plaintext: str, associated_data: bytes = b"") -> bytes:
        """Encrypt plaintext. Returns nonce (12 bytes) + ciphertext + tag (16 bytes).

        `associated_data` is bound to the ciphertext (e.g. the model_id) so
        that an attacker can't swap ciphertexts between rows.
        """
        if not isinstance(plaintext, str):
            raise TypeError("plaintext must be str")
        nonce = os.urandom(self.NONCE_SIZE)
        ct = self._aesgcm.encrypt(
            nonce, plaintext.encode("utf-8"), associated_data or None
        )
        return nonce + ct

    def decrypt(self, blob: bytes, associated_data: bytes = b"") -> str:
        """Decrypt blob produced by `encrypt`. Returns plaintext.

        Raises cryptography.exceptions.InvalidTag if the blob is tampered.
        """
        if not isinstance(blob, (bytes, bytearray)):
            raise TypeError("blob must be bytes")
        if len(blob) < self.NONCE_SIZE + 16:
            raise ValueError("blob too short")
        nonce = bytes(blob[:self.NONCE_SIZE])
        ct = bytes(blob[self.NONCE_SIZE:])
        pt = self._aesgcm.decrypt(nonce, ct, associated_data or None)
        return pt.decode("utf-8")

    def encrypt_to_b64(self, plaintext: str, associated_data: bytes = b"") -> str:
        """Convenience: encrypt and return base64 string (for DB column)."""
        return base64.b64encode(self.encrypt(plaintext, associated_data)).decode("ascii")

    def decrypt_from_b64(self, blob_b64: str, associated_data: bytes = b"") -> str:
        """Convenience: decrypt from base64 string."""
        return self.decrypt(base64.b64decode(blob_b64), associated_data)
