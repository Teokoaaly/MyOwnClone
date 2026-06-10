# Auditoria — Auth, Autorizacion y Seguridad (TASK-360-02)

## Resumen
- **Estado:** Amarillo — Login funcional, JWT configurado, rate limiting presente, pero con varias vulnerabilidades menores y workarounds
- **Riesgo principal:** Proxy auth inyecta `'proxy-service'` como tenant_id no UUID; workaround de SQL raw para evitar enum faltante; CSRF cookie no configurada explicitamente
- **Veredicto prod:** Apto para MVP con servicios internos. Requiere hardening antes de exponer al publico sin restricciones

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| NextAuth v5 (JWT) | ✅ | ~85% | `src/lib/auth.ts` — 3 providers, JWT callbacks, sesion funcional |
| Login credentials | ✅ | Funcional | Login con email+password, bcrypt comparacion |
| Login Google OAuth | ✅ | Configurado | Provider Google en auth.ts, requiere AUTH_GOOGLE_ID/SECRET |
| Login magic link (Resend) | ✅ | Configurado | Provider Resend en auth.ts, requiere RESEND_API_KEY |
| Forgot/reset password | ✅ | Existe | `forgot-password/page.tsx`, `reset-password/page.tsx` |
| Rate limiting (backend) | ✅ | Funcional | `api/controllers/console/auth.py` — Redis + fallback memoria, 5 intentos/15min |
| CSRF | ✅ | Default NextAuth | Sin configuracion explicita, usa cookie por defecto |
| Service-to-service API key | ✅ | Funcional | `middleware.ts` — X-API-Key, `login.py` — proxy-service |
| Timing-safe compare | ✅ | Implementado | `login.py:84` — hmac.compare_digest para service tokens |
| Platform admin via env vars | ⚠️ | Configurado pero PASSWORD_HASH vacio | `.env.local` tiene PLATFORM_ADMIN_PASSWORD_HASH=_vacio_ |
| Roles RBAC | ⚠️ | Parcial | owner/admin/member/platform_admin definidos pero no todos verificados consistentemente |
| Public endpoints sin auth | ⚠️ | Revisar | Chat publico, bookings publicos sin proteccion |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| A02-001 | P0 | Platform admin env var PASSWORD_HASH vacio | Admin global no puede autenticarse via env vars (pero funciona via DB user) | `.env.local` linea 76-78 — comentario dice que bcrypt $ causa problemas con dotenv-expand | Usar comillas simples en `.env` o generar el hash via script y escaparlo |
| A02-002 | P0 | Proxy auth usa `'proxy-service'` como tenant_id UUID | Endpoints que filtran por tenant_id fallan con 500 si no tienen parche especifico | `login.py:59-60` — `g.tenant_id = 'proxy-service'` | Ya mitigado en analytics/inbox (commit 672262e); extender parche a clone, booking, stripe controllers |
| A02-003 | P1 | Workaround de SQL raw en auth.ts | Bypass del tipado de Drizzle ORM; cualquier cambio de schema puede romper la query | `auth.ts:60` — `db.execute(sql\`SELECT ... FROM ${schema.users} WHERE email = ${email}\`)` | Crear enum `user_role` en BD y restaurar uso de `db.query.users.findFirst()` |
| A02-004 | P1 | Roles no verificados consistentemente en frontend | El frontend usa el role del JWT pero no hay guards por ruta | `dashboard/layout.tsx` no verifica roles; solo admin layout verifica `isPlatformAdminSession` | Añadir middleware de autorizacion por rol en dashboard y admin |
| A02-005 | P1 | Sin proteccion CSRF explicita en API Routes | API Routes de Next.js no tienen CSRF validation (NextAuth si la tiene para login) | No hay token CSRF en `api/clone/sources/route.ts`, `api/bookings/route.ts` | Añadir middleware CSRF o usar header checks en API Routes mutantes |
| A02-006 | P2 | Public chat sin rate limiting | Endpoint de chat publico puede ser usado para spam sin restricciones | `middleware.ts` proxy a Flask, pero Flask no tiene rate limit en public chat | Añadir rate limiting por IP en el middleware proxy para rutas publicas |
| A02-007 | P2 | Secrets en texto plano en login.py | Hardcoded `'dev-api-key-for-proxy'` en codigo | `login.py:57` — si FLASK_ENV no es production, se permite clave hardcodeada | Ya mitigado parcialmente: solo en desarrollo. Aceptable para MVP pero documentar |
| A02-008 | P2 | Webhook Stripe sin verificacion de firma | Cualquiera puede llamar al webhook de Stripe si conoce la URL | `api/stripe/webhook/route.ts` — existe pero no se audito validacion de firma | Ver audit TASK-360-06 para cobertura completa |
| A02-009 | P3 | JWT sin refresh token | La sesion expira y no hay renovacion automatica | `auth.ts` session strategy JWT, sin `maxAge` configurado | Aceptable para MVP; anyadir refresh token en version futura |
| A02-010 | P3 | Sin logout centralizado | Cada provider maneja logout por separado | `SignOutButton.tsx` llama a `signOut()` de NextAuth | Funcional, pero no invalida el token del lado del servidor |

## Matriz de interconexion

### Flujo: Autenticacion

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | LoginForm | `login/login-form.tsx` | ✅ Funcional | Sin i18n, texto hardcodeado |
| Frontend | NextAuth route | `api/auth/[...nextauth]/route.ts` | ✅ Funcional | — |
| Auth Lib | JWT authorize | `lib/auth.ts` | ✅ Funcional | Workaround SQL raw |
| Auth Lib | Platform admin | `lib/platform-admin.ts` | ⚠️ PASSWORD_HASH vacio | Depende de env vars |
| Middleware | Proxy + tenant | `middleware.ts` | ✅ Funcional | — |
| Backend | Login decorator | `api/libs/login.py` | ✅ Funcional | proxy-service no UUID |
| Backend | JWT utils | `api/libs/jwt_utils.py` | ✅ Funcional | — |
| Backend | Auth blueprint | `api/controllers/console/auth.py` | ✅ Funcional | Rate limiting Redis |
| Backend | Security checks | `api/libs/security_checks.py` | ✅ Funcional | Fail-fast en produccion |
| DB | Users table | `schema/users.ts` | ⚠️ Parcial | Enum user_role no existe |

### Roles y acceso por ruta

| Ruta | Rol requerido | Verificado? | Metodo |
|---|---|---|---|
| `/resumen` (dashboard) | Cualquier sesion | ✅ | `auth()` en layout |
| `/admin/*` | platform_admin | ✅ | `isPlatformAdminSession()` |
| `/biblioteca` | Cualquier sesion | ✅ | Dashboard layout check |
| `/api/clone/sources` | Sesion | ✅ | `auth()` en route handler |
| `/api/admin/*` | Sesion + proxy | ✅ | Backend `login_required` |
| `/api/public/*` | No | ✅ (intencional) | — |
| Chat public `/{slug}` | No | ✅ (intencional) | — |

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| A02-A | P0 | Configurar PLATFORM_ADMIN_PASSWORD_HASH con hash escapado | Agent Security | 0.3d | — |
| A02-B | P0 | Extender parche proxy-service a clone, booking, stripe controllers | Agent Backend | 0.5d | — |
| A02-C | P1 | Crear enum user_role en BD y restaurar Drizzle ORM en auth.ts | Agent DB | 0.5d | D01-G |
| A02-D | P1 | Añadir guard de roles por ruta en dashboard layout | Agent Frontend | 0.5d | — |
| A02-E | P1 | Implementar CSRF protection en API Routes mutantes | Agent Frontend | 1d | — |
| A02-F | P2 | Añadir rate limiting por IP en middleware para chat publico | Agent Frontend | 0.5d | — |
| A02-G | P2 | Verificar firma de webhook Stripe | Agent Backend | 0.5d | — |
| A02-H | P3 | Documentar JWT maxAge y refresh token como mejora futura | Agent Security | 0.3d | — |

## Open Questions

1. **Platform admin PASSWORD_HASH**: Se usa comillas simples en `.env` o se mueve a una configuracion por script? La documentacion actual recomienda generarlo con `node -e '...'` pero el $ del hash rompe dotenv.
2. **Proxy UUID**: Hay 6 controllers que podrian tener el mismo problema que analytics/inbox. Se extiende el parche a todos o se redisenia la autenticacion proxy para resolver el tenant_id real?
3. **CSRF**: Las API Routes de Next.js necesitan CSRF? NextAuth lo maneja para login, pero las rutas custom como `/api/clone/sources` POST no tienen proteccion.
4. **Rate limiting en public chat**: Se implementa en el middleware de Next.js (edge) o en Flask? Edge es mas escalable pero mas limitado en estado.
