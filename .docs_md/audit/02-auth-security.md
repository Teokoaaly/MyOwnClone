# Auditoria 100% - Auth, Seguridad y Proxy (2026-06-11)

## Resumen

- **Estado:** Amarillo/Rojo.
- **Riesgo principal:** el proxy es una pieza central, pero aun tiene configuracion hardcodeada y confianza fuerte en headers.
- **Veredicto:** viable en local, no suficiente para produccion sin cerrar env, CSRF/rate limit y ownership checks.

## Hallazgos

| ID | Prioridad | Hallazgo | Evidencia | Recomendacion |
|---|---|---|---|---|
| A11-001 | P1 | Backend URL hardcodeado en proxy. | `MyOwnClone/src/proxy.ts:5` | Usar `process.env.MYOWNCLONE_API_URL` con fallback solo dev. |
| A11-002 | P1 | Service key dev fallback existe fuera de production. | `proxy.ts`, `api/libs/login.py:67-77` | Documentar y limitar por `ALLOW_DEV_SERVICE_KEY` + localhost. |
| A11-003 | P1 | Backend confia en `X-User-*` si service key valida. | `api/libs/login.py:73-77` | Mantener firma fuerte, rotacion y auditoria de proxy. |
| A11-004 | P1 | API local `sources` no valida ownership de clone contra tenant. | `sources/route.ts:10-12`, `:32` | Resolver clone desde backend/tenant, no solo cookie. |
| A11-005 | P2 | Rate limit publico en memoria. | `api/controllers/myownclone_public.py:50`, `:86-99` | Redis/Upstash o limiter compartido. |
| A11-006 | P2 | CSRF en rutas mutantes Next no esta auditado como completo. | `src/app/api/**/route.ts` | Middleware/token CSRF para POST/PUT/DELETE con cookie auth. |

## Acciones

1. Proxy env-driven.
2. Ownership check unificado para cloneId.
3. Rate limit durable para chat/booking publico.
4. Documentar env vars obligatorias: `SERVICE_API_KEY`, `MYOWNCLONE_API_URL`, `NEXTAUTH_SECRET`, webhook secrets.
5. Tests de acceso cruzado tenant A/B.
