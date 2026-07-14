# Evidencia — Fases P1 + P2 Auditoría VPS 2026-07-13

> **Rama:** `fix/p1-backend-robustez-infra` (desde `fix/p0-backend-crashes-and-idor`)
> **Base:** commit `05a57b0` (P0 docs)
> **HEAD:** `5c99f33`
> **Frontend:** NO tocado (restricción del humano confirmada)
> **Modo:** L2 backend/infra (respetado AGENTS.md, sin push)

---

## Resumen ejecutivo

| Bloque | Commit | Hallazgos | Tests | Estado |
|--------|--------|-----------|-------|--------|
| P1.10.04 H-13 CLI commands | `e309cf9` | H-13 | 0 (cierra `test_m13_backfill_command_exists`) | ✅ |
| P1.10.01 H-08 email format-string | `5ab614f` | H-08 | 5 | ✅ |
| P1.10.02 H-09 platform guard | — | H-09 | 1 | ✅ (commitió en `260481a` con P2.4) |
| P1.6 H-12 booking unique constraint | `cf7249e` | H-12 | 3 | ✅ |
| P1.10 H-10 psycopg2 → SQLAlchemy | `32afd0a` | H-10 | 8 | ✅ |
| P2.4 datetime.utcnow deprecated | `260481a` | Deprecation cleanup | 0 (verificación visual) | ✅ |
| P2 H-02 rate-limit memory + XFF | `d189508` | H-02 | 4 | ✅ |
| P2.8.07 avatar makedirs + ext sanitization | `5c99f33` | MEDIUM | 0 (verificación visual) | ✅ |
| **Docs** | (siguiente) | — | — | ⏳ |

**Suite:** 403 passed, 13 failed (todos pre-existentes), **0 regresiones**.

---

## Detalle por bloque

### P1.10.04 — CLI commands (H-13)
- **Antes:** solo `seed_demo_data` registrado en `app.cli`; los demás `@click.command` (`generate-master-key`, `rotate-secrets-key`, `refresh-cost-daily-rollup`, `ai-backfill-from-env`, `reindex`) inalcanzables vía `flask ...`.
- **Después:** los 5 comandos registrados en `app_factory.py:230-242` con lazy imports.
- **Cierra test pre-existente:** `tests/test_plan_completion.py::test_m13_backfill_command_exists`.

### P1.10.01 — Email format-string injection (H-08)
- **Antes:** `subject_tpl.format(**kwargs)` sobre valores atacante-controlables (clone_name, lead_email, etc.).
- **Después:** `_escape_format_injection()` duplica `{` y `}` en valores caller-supplied; whitelist `_SAFE_EMAIL_TEMPLATE_KEYS` + warning para keys inesperadas.
- **Tests:** 5 en `test_p1_email_format_injection.py`.

### P1.10.02 — Platform guard en monitoring (H-09)
- **Antes:** `_check_os` abría `/proc/stat` sin guard; en win32 o macOS lanzaba OSError.
- **Después:** guard explícito `platform.system() != "Linux"` → ServiceHealth `status="unknown"` con detalle de plataforma (no 500).
- **Tests:** 1 en `test_p1_platform_guard.py`.

### P1.6 — Booking unique constraint (H-12, TOCTOU)
- **Migración** `2026_07_14_0001_add_booking_unique_constraint.py`: partial unique index `uq_bookings_meeting_slot` sobre `(meeting_type_id, date, start_time)` WHERE ambos NOT NULL.
- **Ambos endpoints** (`myownclone_public.create_booking_public` + `booking.BookingsApi.post`): `try/except IntegrityError → 409` para convertir la race en error de cliente, no 500.
- **Tests:** 3 en `test_p1_booking_unique_constraint.py` (migración + 2 handlers).

### P1.10 — Auth sin psycopg2 crudo (H-10)
- **Antes:** `_get_db_conn` abría conexión psycopg2 cruda por cada login → DoS amplifier.
- **Después:** `_lookup_account_via_sqlalchemy(email)` usa `db.session` con modelo `Account`; mantiene fallback a tabla legacy `users` (Drizzle/NextAuth). Maneja `ProgrammingError` y errores genéricos sin 500 leak.
- **Bonus:** `bcrypt.checkpw ValueError` (hash legacy no-bcrypt) → 401, no 500.
- **Tests:** 8 en `test_p1_auth_psycopg2_removal.py` (3 source-level + 3 helper + 2 endpoint behavior).

### P2.4 — datetime.utcnow deprecated
- **Antes:** `datetime.utcnow()` emite DeprecationWarning en Py 3.12+.
- **Después:** `_naive_utc_now()` = `datetime.now(timezone.utc).replace(tzinfo=None)` (consistente con columnas DateTime naive existentes).
- **Archivos:** `api/core/ai_audit.py`, `api/core/security_types.py`, `api/models/system_settings.py`.

### P2 H-02 — Rate-limit memory leak + XFF spoofing
- **Antes:**
  - `_memory_fallback: dict[str, list[float]]` crecía sin límite ante IP spray.
  - `client_ip = request.remote_addr or "unknown"` → detrás de nginx todos los atacantes comparten bucket, o si nginx reenvía X-Forwarded-For sin stripping, el cliente lo spoofea.
- **Después:**
  - `_client_ip(req)`: prefiere `X-Forwarded-For` SOLO si el peer inmediato está en `TRUSTED_PROXIES` (env var, comma-separated CIDRs/IPs). Por defecto vacío → usa `remote_addr`.
  - `_prune_memory_fallback(now)`: eviction oportunista cada 60s de IPs cuyo timestamp máximo está fuera de la ventana. Previene memory leak.
- **Tests:** 4 en `test_p2_rate_limit_hardening.py`.

### P2.8.07 — Avatar upload makedirs + ext sanitization
- **Antes:** extensión del archivo = `file.filename.rsplit('.', 1)[-1]` (cliente-controlable); un `shellcode.php` enviado como `image/png` quedaba guardado como `<uuid>.php`. Sin `os.makedirs`, deploys frescos lanzaban `FileNotFoundError`.
- **Después:**
  - Mapeo `content_type → extension` (allowlist). El nombre del archivo cliente se IGNORA.
  - `os.makedirs(avatars_dir, exist_ok=True)` antes de save.
  - `AVATARS_DIR` configurable por env (default `/opt/myownclone/shared/avatars`).

---

## Archivos modificados (rama P1+P2 vs P0)

```
 api/controllers/console/auth.py                    |  93 ++++-
 api/controllers/console/myownclone/booking.py      |   7 +-
 api/controllers/console/myownclone/clone.py        |  19 +-
 api/controllers/myownclone_public.py               |   8 +-
 api/core/ai_audit.py                              |   7 +-
 api/core/email_service.py                         |  35 +-
 api/core/monitoring.py                            |   9 +-
 api/core/security_types.py                        |   9 +-
 api/models/system_settings.py                     |   7 +-
 api/migrations/versions/2026_07_14_0001_add_booking_unique_constraint.py | 41 +++
 api/tests/test_p1_auth_psycopg2_removal.py        | 134 ++++
 api/tests/test_p1_booking_unique_constraint.py     |  72 +++
 api/tests/test_p1_email_format_injection.py        |  88 +++
 api/tests/test_p1_platform_guard.py               |  30 +
 api/tests/test_p2_rate_limit_hardening.py         |  82 +++
```

**Tests nuevos:** 5 archivos, 21 tests.

---

## Suite evolution

| Snapshot | Pass | Fail pre-existentes | Notas |
|----------|------|---------------------|-------|
| Baseline (P0 inicial) | 107 | 3 (root tests) | sin api/tests |
| P0 base | 310 | 16 | base limpia tras fix `test_memories_in_chat.py` |
| P0 done | 381 | 14 | cerró 2 health + 1 file |
| P1.10.04 | 382 | 13 | cerró `test_m13_backfill_command_exists` |
| P1.10.01 + P1.6 + P1.10 + P2 | 403 | 13 | sin regresiones |

---

## Pendiente fuera de P1+P2

- **P0.4 voice (C-12):** requiere decisión humana (cambio contrato API o nuevo modelo DB).
- **P0.1 rotación física SERVICE_API_KEY en VPS:** runbook en `.omo/evidence/p0-auditoria-2026-07-13.md`.
- **P1.5 retrieval vector search:** pgvector `<=>` operator (refactor mayor, no incluido en este pase).
- **P1.4 FKs migration:** requiere pre-migration cleanup de huérfanos (siguiente pase coordinado con ventana de mantenimiento).
- **13 fallos pre-existentes restantes** (embeddings guard, inbox e2e, model registry legacy, runtime integration) — planificados en fases siguientes.

---

## Cómo reproducir la verificación

```bash
cd "C:\Users\haxth3\Documents\MyOwnClone-admin-vps-exec"
git checkout fix/p1-backend-robustez-infra

# Tests P1+P2 específicos
python -m pytest api/tests/test_p1_auth_psycopg2_removal.py \
                 api/tests/test_p1_booking_unique_constraint.py \
                 api/tests/test_p1_email_format_injection.py \
                 api/tests/test_p1_platform_guard.py \
                 api/tests/test_p2_rate_limit_hardening.py \
                 --override-ini="addopts=" -v

# Suite completa (403 passed, 13 pre-existing failed)
python -m pytest api/tests/ tests/ --override-ini="addopts=" -q --tb=no

# Confirmar que no queda datetime.utcnow real
grep -rn "datetime\.utcnow" api/ | grep -v "P2.4:"
# (debe estar vacio)
```

---

**Fecha:** 2026-07-14
**Próximo paso:** revisión humana + decisión push/deploy acumulado de P0 + P1 + P2.
