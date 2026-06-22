# Evidence — M2: Cifrado AES-256-GCM (SecretCipher)

**Milestone:** M2
**Fecha QA:** 2026-06-21
**Resultado:** ✅ PASS
**Commit:** cd693a7 (feat(sisyphus): M2 — AES-256-GCM SecretCipher + CLI commands + security_checks)
**Rama:** feature/sisyphus-m1-data-layer (HEAD remoto verificado via GitHub API)

## Artefactos creados

| Archivo | Propósito |
|---------|-----------|
| `api/libs/crypto.py` | `SecretCipher` (AES-256-GCM via `cryptography.hazmat.primitives.ciphers.aead.AESGCM`) + `generate_master_key()` + `is_configured()` + errores tipados (`MasterKeyMissingError`, `MasterKeyInvalidError`, `CiphertextMalformedError`). Formato: `base64(12B nonce ‖ ciphertext ‖ 16B tag)`. Re-exporta `InvalidTag`. |
| `api/commands/crypto.py` | Click commands: `flask generate-master-key` (imprime base64-32 + warning a stderr) y stub `flask rotate-secrets-key --new <key>` (cuerpo completo en M12). |
| `api/app_factory.py` | Registra ambos comandos en `app.cli`. |
| `api/libs/security_checks.py` | Añade `MODEL_SECRETS_KEY` a `_REQUIRED_IN_PROD`. Fail-fast en producción si la master key falta. |
| `api/tests/test_crypto.py` | 26 tests: round-trip, nonce único por call (GCM critical), tampering→InvalidTag, malformed/short/non-base64 blobs, missing key, wrong-length key (6 tamaños parametrizados), non-base64 key, rotación A→B falla (mientras nuevas cifran OK), `generate_master_key` único + longitud correcta, `is_configured` (true/false/wrong-length), TypeError en no-str, integración con security_checks (SystemExit en prod sin key). |

## Verificación ejecutada (con resultado exacto)

```
$ .venv/bin/python -m pytest api/tests/test_crypto.py -v
============================== 26 passed in 0.81s ==============================

$ .venv/bin/python -m pytest tests/test_plan_completion.py::test_m2_crypto_secret_cipher_exists \
                          tests/test_plan_completion.py::test_m2_security_checks_requires_master_key -v
============================== 2 passed in 0.30s ==============================
# (M2 smoke contract: api.libs.crypto exists, AESGCM present, no Fernet, MODEL_SECRETS_KEY in _REQUIRED_IN_PROD)

$ .venv/bin/python -m pytest tests/ api/tests/ --ignore=tests/test_plan_completion.py
================== 148 passed, 1 failed in 18.13s ==================
# (1 fail preexistente: test_inbox_e2e necesita PG en localhost:5432, NO causado por M2)

$ python scripts/check-plan-progress.py
Sisyphus plan: Sistema de Modelos IA Configurables por Tarea (M0-M13)
  done:        2/15  ['M0', 'M1']   ← M2 se marca done en el close-out (siguiente commit)
  in_progress: 1        ['M2']
  pending:     12       [...]
[OK] progreso consistente.

$ click.testing.CliRunner on generate-master-key:
  exit_code: 0
  stdout:    base64-32 random key
  stderr:    "[!] Store this key in your secret manager NOW."
             "[!] Set MODEL_SECRETS_KEY=*** in the API environment."
             "[!] Losing it makes every ai_models.api_key_encrypted row unreadable."
```

## Guardrails verificados

1. **NO Fernet.** El módulo `api/libs/crypto.py` no contiene la palabra "Fernet" en ninguna parte (ni docstring ni comentarios). Verificado por `tests/test_plan_completion.py::test_m2_crypto_secret_cipher_exists` que lee el fuente.
2. **AESGCM sí.** Misma verificación, busca `"AESGCM"` en el archivo.
3. **Fresh nonce per call.** Test dedicado `test_each_encryption_uses_a_fresh_nonce` confirma que dos cifrados del mismo plaintext producen ciphertexts distintos — invariante crítico de GCM (reuse de nonce = leak del XOR de plaintexts).
4. **Master key de 32 bytes exacta.** Test parametrizado con 6 tamaños incorrectos (16, 24, 31, 33, 48, 64) confirma rechazo claro con `MasterKeyInvalidError`.
5. **Fail-fast en producción.** `test_security_checks_aborts_in_prod_without_key` confirma `SystemExit(1)` si `MODEL_SECRETS_KEY` falta y `FLASK_ENV != development`.

## Decisiones explícitas (fuera del scope)

1. **`rotate-secrets-key` queda como stub.** La rotación real (re-cifrar cada `ai_models.api_key_encrypted` bajo doble-clave: vieja descifra, nueva cifra) es M12c según el plan. El stub valida solo la forma del input (32 bytes base64) y referencia M12. Esto evita un cambio que requeriría doble-key window antes de tiempo.
2. **No documento el módulo `Fernet` para nada.** Inicialmente el docstring explicaba el contraste Fernet-vs-GCM. Lo reescribí porque el smoke test rechaza la palabra "Fernet" en el fuente (incluso en comentarios). La justificación se mantiene sin nombrar la alternativa.
3. **Errores tipados separados** (`MasterKeyMissingError`, `MasterKeyInvalidError`, `CiphertextMalformedError`, todos heredan de `CryptoError`) para que M3 (ModelRegistry) pueda distinguir "no está configurado" (fallo recoverable pidiendo al operador) de "blob corrupto" (datos perdidos) sin tener que parsear strings de error.
4. **`MODEL_SECRETS_KEY` en `_REQUIRED_IN_PROD`, no en `_INSECURE_DEFAULTS`.** No hay un "default inseguro" — el valor ausente es el problema. Esto hace que `assert_production_secrets` aborte con `SystemExit(1)` y mensaje claro en vez de aceptar un valor vacío.

## Bloqueos que quedan para M3+

- **M3 (ModelRegistry)** ahora puede import `SecretCipher` y descifrar `api_models.api_key_encrypted`. Verá `MasterKeyMissingError` si la env var no está seteada en runtime — debe decidir entre reintentar, fallback al legacy env `_detect_provider` (especificado en el plan), o propagar el error.
- **M9 (API admin)** podrá crear modelos con `SecretCipher.encrypt(api_key)` y nunca devolver la key descifrada en responses GET.
- **M12 (rotación doble-clave)** implementará `rotate-secrets-key` usando la firma ya validada en el stub.

## Estado del push

```
$ git push origin feature/sisyphus-m1-data-layer
To https://github.com/Teokoaaly/MyOwnClone.git
   d8f5e24..cd693a7  feature/sisyphus-m1-data-layer -> feature/sisyphus-m1-data-layer

$ curl https://api.github.com/repos/Teokoaaly/MyOwnClone/branches/feature/sisyphus-m1-data-layer
remote HEAD: cd693a7 ✓
```

## Próximo hito

**M4a — ProviderAdapter interface + ProviderRegistry.** Va ANTES que M3 (ModelRegistry) por la regla del plan: el registry despacha contra la interfaz, no contra implementaciones concretas. Entregables:
- `api/core/providers/base.py` con ABC `ProviderAdapter` (invoke, invoke_stream, test_connection) + dataclasses `GenerationParams`, `ModelReply`, `ModelUsage`, `ModelInvocationError` (movidas desde `model_manager.py` y re-exportadas para back-compat).
- `api/core/providers/registry.py` con `ProviderRegistry` + decorador `@register("openai")`.
- `api/tests/test_provider_registry.py` (registro, lookup, idempotencia).

**Pendiente de decisión humana:**
- ¿Resolver SSH del VPS para validar despliegues o seguir sin él?
- ¿El usuario revoca el PAT de GitHub que se usó en este push (recomendado)?
- ¿Pushear la rama con un PR #5 hacia master?