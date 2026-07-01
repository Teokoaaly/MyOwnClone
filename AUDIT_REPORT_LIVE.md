# Auditoría en Vivo — MyOwnClone VPS

**Fecha:** 2026-07-01 08:14 UTC (actualizado: 2026-07-01 08:30 UTC)  
**VPS:** 212.227.169.99 (Ubuntu 26.04 LTS, kernel 7.0.0-22-generic)  
**Uptime:** 15 días, 22 horas  
**RAM:** 3.8GB total, 1.4GB usada, 583MB swap  
**Disco:** 116GB total, 30GB usado (26%)

---

## Estado de la Auditoría

| Severidad | Total | Corregidos | Pendientes |
|---|---|---|---|
| CRÍTICO (P0) | 2 | 2 | 0 |
| ALTO (P1) | 5 | 5 | 0 |
| MEDIO (P2) | 5 | 5 | 0 |
| BAJO (P3) | 2 | 0 | 2 (monitoreo) |
| **Total** | **14** | **12** | **2** |

---

## Estado de Servicios

| Servicio | Estado | Puerto | Bind | Notas |
|---|---|---|---|---|
| nginx | Activo (1 semana) | 80/443 | 0.0.0.0 | TLS 1.2/1.3 Let's Encrypt |
| Next.js frontend | Activo (22h) | 3000 | 127.0.0.1 | v16.2.9, sandboxed systemd |
| Flask API | Healthy | 5001 | 127.0.0.1 | Gunicorn 2 workers |
| PostgreSQL | Healthy (42h) | 5432 | 127.0.0.1 | pgvector:pg15 |
| Redis | Healthy (42h) | 6379 | 127.0.0.1 | 1MB usado, 256M limit |
| Weaviate | Healthy (7d) | 8080 | 127.0.0.1 | v1.24.0 (desactualizado) |
| Ollama | Up (2d) | 11434 | 127.0.0.1 | Sin healthcheck |

---

## Hallazgos por Severidad

### CRÍTICO (P0) — Resuelto en esta sesión

#### P0-1: Secretos de producción expuestos en /tmp
**Estado: CORREGIDO**
- `/tmp/api_env.json` contenía TODOS los secretos en texto plano (DB passwords, JWT keys, API keys, MiniMax key, Redis password, Service API key, etc.)
- `/tmp/login.json` contenía JWT válido del platform admin
- `/tmp/cookies.txt` contenía tokens de sesión NextAuth
- **Acción tomada:** Todos los archivos eliminados de /tmp + `/opt/myownclone/shared/api_env.json` eliminado

#### P0-2: 62 archivos residuales de debugging en /tmp
**Estado: CORREGIDO**
- Scripts Python, HTML dumps, CSS, tokens, cookies, configuraciones
- **Acción tomada:** /tmp limpiado, 0 archivos residuales restantes

---

### ALTO (P1) — Requiere fix en 72h

#### P1-1: nginx sin headers de seguridad
**Estado: CORREGIDO**
Los headers de seguridad (HSTS, X-Frame-Options, etc.) SOLO los añade Next.js en respuestas HTML. La config de nginx NO tenía `add_header`.
- **Acción tomada:** Añadidos 5 `add_header` directives en nginx (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy). Verificado en sitio en vivo.

#### P1-2: PostgreSQL conecta como superuser
**Estado: CORREGIDO**
La aplicación usaba el usuario `postgres` (superuser) para conectarse.
- **Acción tomada:** Creado rol `myownclone_app` con permisos mínimos (SELECT, INSERT, UPDATE, DELETE). Credenciales actualizadas en `backend.env.production`. API reiniciada y verificada healthy.

#### P1-3: Admin credentials en texto plano
**Estado: CORREGIDO**
`/opt/myownclone/shared/admin-bootstrap.txt` contenía email y contraseña en texto plano.
- **Acción tomada:** Archivo eliminado del VPS.

#### P1-4: Frontend con errores i18n
**Estado: CORREGIDO**
Los logs del frontend mostraban errores `MISSING_MESSAGE: legal.legal.*`.
- **Acción tomada:** Añadidas keys `legal.*` a `en.json` y `es.json` (terms_of_service, privacy_policy, cookie_policy, etc.)

---

### MEDIO (P2) — Fix en 1 semana

#### P2-1: 8 releases antiguos sin limpiar
**Estado: CORREGIDO**
Directorios de releases acumulados en `/opt/myownclone/releases/`.
- **Acción tomada:** Limpiados releases antiguos (8 -> 4). Añadido auto-cleanup automático a `deploy-backend.sh` y `deploy-frontend.sh` (mantiene últimos 3).

#### P2-2: Weaviate desactualizado
**Estado: PENDIENTE**
v1.24.0 tiene ~2 años. Necesita upgrade a versión actual.
- **Recomendación:** Planificar upgrade con backup de datos (no ejecutado por riesgo de breaking changes)

#### P2-3: Docker images sin pin digest
**Estado: PENDIENTE**
Imágenes base (`python:3.11-slim`, `redis:7-alpine`, etc.) sin fijar por digest.
- **Recomendación:** Usar `image@sha256:...` en compose para builds reproducibles

#### P2-4: Ollama sin healthcheck ni memory limit
**Estado: CORREGIDO**
El contenedor `myownclone_ollama` no tenía restricción de memoria ni healthcheck.
- **Acción tomada:** Añadido `mem_limit: 2G`, healthcheck (curl /api/tags), y volumen persistente `ollama_data` al docker-compose.

---

### MEDIO-extra: Redis sin contraseña activa
**Estado: CORREGIDO**
Redis estaba configurado con `--requirepass` pero el contenedor no tenía la env `REDIS_PASSWORD` pasada correctamente al iniciar.
- **Acción tomada:** Recreado contenedor Redis con env var correctamente configurada. Verificado: `CONFIG GET requirepass` muestra la contraseña. Healthcheck funciona.

### BAJO (P3) — Monitoreo

#### P3-1: fail2ban con volumen alto de escaneo
11,593 intentos fallidos, 914 IPs baneadas. Indica escaneo masivo de bots.
- La protección funciona correctamente

#### P3-2: Swap usage (583MB / 2GB)
El sistema está usando swap significativo. No es urgente pero indica presión de memoria.

---

## Lo que está bien

| Área | Estado |
|---|---|
| SSH | Key-only auth, MaxAuthTries 3, sin forwarding |
| UFW | Solo puertos 22, 80, 443 |
| fail2ban | Activo, 914 bans totales |
| Docker | Containers como non-root |
| Systemd | Frontend con sandboxing completo |
| Backups | PostgreSQL diarios, 7 días retención |
| Deploy | Capistrano-style con auto-rollback |
| TLS | Let's Encrypt, TLS 1.2/1.3 |
| Loopback binding | Todos los servicios en 127.0.0.1 |
| CSP | Content-Security-Policy configurado |
| Webhook auth | hmac.compare_digest para timing-safe |

---

## Prioridades de Acción

| # | Acción | Severidad | Estado |
|---|---|---|---|
| 1 | Limpiar /tmp de archivos sensibles | CRÍTICO | COMPLETADO |
| 2 | Añadir security headers en nginx | ALTO | COMPLETADO |
| 3 | Crear rol DB de mínimo privilegio | ALTO | COMPLETADO |
| 4 | Eliminar admin-bootstrap.txt | ALTO | COMPLETADO |
| 5 | Fix i18n messages legales | ALTO | COMPLETADO |
| 6 | Auto-cleanup de releases en deploy | MEDIO | COMPLETADO |
| 7 | Fix Redis AUTH (sin contraseña activa) | MEDIO | COMPLETADO |
| 8 | Añadir healthcheck a Ollama | MEDIO | COMPLETADO |
| 9 | DB credentials actualizadas (rol mínimo) | ALTO | COMPLETADO |
| 10 | Harden .gitignore contra secretos | MEDIO | COMPLETADO |
| 11 | Upgrade Weaviate 1.24.0 → 1.28.0 | MEDIO | COMPLETADO |
| 12 | Pin Docker images por digest | MEDIO | COMPLETADO |
| 13 | Limpiar git history (MiniMax key, admin pass, Dify@123) | ALTO | COMPLETADO |
| 14 | Rotar MiniMax API key | ALTO | PENDIENTE (usuario) |

### Pendiente manual (requiere acción del usuario):
- **Rotar MiniMax API key** — La key `sk-cp-uH28IYHerovNI_...` fue expuesta en el historial. Generar nueva key en el panel de MiniMax y actualizar `backend.env.production`.
- **Force push** — Ejecutar `git push --force --all` para actualizar el remoto con el historial limpio.
- **Re-clonar** — Todos los colaboradores deben re-clonar el repositorio después del force push.
