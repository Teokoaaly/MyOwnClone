# Model secrets key management

`MODEL_SECRETS_KEY` is the single AES-256-GCM master key used to encrypt every
`ai_models.api_key_encrypted` value.

Operational rules:

- store the key outside the repository and outside the VPS checkout
- treat it like a database root password
- losing the key is irreversible for already-encrypted provider secrets
- rotate by re-encrypting rows first, then rolling the deployment forward

Recommended rotation flow:

1. Generate a new key with `flask generate-master-key`.
2. Keep the current key available to the API workers.
3. Run `flask rotate-secrets-key --new <base64>` against the target database.
4. Update the runtime secret to the new key.
5. Restart API workers.
6. Verify model resolution and provider connection checks.

Important caveat:

- requests that already resolved model credentials before rotation keep using
  that in-memory plaintext until they finish
- new requests after rotation must read secrets with the new key
- this is why the old key should remain available until the old workers are
  drained and replaced
