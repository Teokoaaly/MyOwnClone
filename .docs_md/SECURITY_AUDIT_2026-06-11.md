# Informe de auditoria de seguridad - MyOwnClone

**Fecha:** 2026-06-11  
**Estado:** revisado y corregido contra el codigo actual  
**Alcance:** Frontend Next.js, Backend Flask, DB/tenancy, integraciones publicas  
**Nota metodologica:** este documento corrige una version previa que contenia algunos hallazgos sobredimensionados o imprecisos. Las rutas y evidencias de abajo se han contrastado con el workspace actual.

---

## Resumen ejecutivo

| Gravedad | Cantidad | Estado |
|---|---:|---|
| P0 / Critico | 4 | Requiere accion antes de produccion |
| P1 / Alto | 9 | Debe entrar en el hardening inicial |
| P2 / Medio | 10 | Riesgo controlable, pero acumulativo |
| P3 / Bajo | 7 | Limpieza y deuda tecnica |

**Veredicto:** no listo para produccion publica sin hardening.  

El proyecto tiene bases razonables: NextAuth con JWT, bcrypt, firma de Stripe webhook, login Flask con rate limiting, verificacion timing-safe en varios puntos y validacion de secretos en produccion. El riesgo principal no esta en una sola pieza, sino en la combinacion de proxy service-to-service, endpoints publicos de coste, falta de proteccion centralizada de rutas, ausencia de CSP y validaciones incompletas de input/tenant.

---

## Correcciones a la version anterior

- **No se puede afirmar que `api/.env` y `MyOwnClone/.env.local` esten commiteados.** `git ls-files api/.env MyOwnClone/.env.local` no los lista. Si fueron compartidos, subidos en otra rama o copiados a terceros, deben rotarse igualmente.
- **Si existe una capa edge-like en Next.js:** `MyOwnClone/src/proxy.ts`. No hay `src/middleware.ts`, pero en este repo el proxy intercepta rutas y API. El problema real es que no aplica proteccion centralizada de paginas privadas ni exige sesion antes de reenviar todas las API protegidas.
- **Si hay rate limiting en login Flask:** `api/controllers/console/auth.py` limita intentos fallidos por IP con Redis y fallback in-memory. El hallazgo correcto es que faltan limites en endpoints publicos/costosos y auth frontend.
- **`_check_service_token` no esta integrado en `login_required`.** La comparacion de `X-API-Key` usa `api_key in valid_keys`, no `hmac.compare_digest`.
- **El hardcoded `dev-api-key-for-proxy` esta limitado por entorno en Flask**, pero el frontend Next.js sigue usando fallback si falta `SERVICE_API_KEY`. En produccion, un misconfig puede abrir un bypass.
- **`crypto.randomUUID()` en Next.js no requiere import explicito** en el runtime moderno. No debe figurar como hallazgo.

---

## P0 - Criticos

### P0-01 - API service key con fallback conocido en el proxy

**Evidencia:** `MyOwnClone/src/proxy.ts:22`, `api/libs/login.py:60-67`  
**Impacto:** si `SERVICE_API_KEY` falta en Next.js, el proxy usa `"dev-api-key-for-proxy"`. Flask acepta esa clave fuera de `FLASK_ENV=production`. En despliegues mal etiquetados, staging expuesto o contenedores con entorno incorrecto, se puede convertir en bypass de autenticacion service-to-service.  
**Recomendacion:** eliminar el fallback del frontend y hacer fail-fast si falta `SERVICE_API_KEY`. En Flask, aceptar la clave dev solo cuando `FLASK_ENV=development` y `ALLOW_DEV_SERVICE_KEY=true`.

### P0-02 - Identidad y rol se confian desde headers reenviados por el proxy

**Evidencia:** `api/libs/login.py:68-78`  
**Impacto:** cuando `X-API-Key` es valido, el backend acepta `X-User-Id`, `X-Tenant-Id`, `X-User-Role` y `X-User-Email` como identidad efectiva. Si la service key se filtra o se acepta el fallback, se puede suplantar usuario, rol y tenant.  
**Recomendacion:** validar el usuario contra BD, verificar pertenencia al tenant y no aceptar `X-User-Role` como autoridad. Idealmente usar JWT firmado por Next.js para llamadas internas o token service-to-service con claims firmados y scope limitado.

### P0-03 - Escalada a platform admin por cuentas `proxy-*`

**Evidencia:** `api/controllers/console/myownclone/admin_platform.py:306-309`  
**Impacto:** `_is_platform_admin()` considera admin cualquier `account_id` que empiece por `proxy-`. El `login_required` actual usa `proxy-service` por defecto si no llega `X-User-Id`, por lo que una llamada service-to-service valida puede convertirse en platform admin. Combinado con P0-01/P0-02, es un bypass administrativo.  
**Recomendacion:** eliminar el prefijo `proxy-*` como criterio de admin. Separar service account de user account y autorizar endpoints admin solo con rol real `platform_admin` consultado en BD o con un token admin dedicado.

### P0-04 - Chat publico sin rate limiting ni limite de coste

**Evidencia:** `api/controllers/myownclone_public.py:155-256` y `:258-296`  
**Impacto:** `/api/myownclone/public/clones/<slug>/chat` y `/chat-simple` aceptan mensajes publicos y disparan retrieval + LLM sin rate limit, CAPTCHA, longitud maxima fuerte ni cuota por clone/IP. Permite abuso de costes y degradacion del servicio.  
**Recomendacion:** rate limit por IP + clone, max length de mensaje, timeout de LLM, tracking de coste y respuesta 429. Para clones privados, exigir token/widget key.

---

## P1 - Altos

### P1-01 - STT API publica consume OpenAI sin autenticacion

**Evidencia:** `MyOwnClone/src/app/api/stt/route.ts:3-31`  
**Impacto:** cualquier cliente puede subir audio y consumir `OPENAI_API_KEY`. No hay sesion, limite de tamano, MIME allowlist ni rate limit.  
**Recomendacion:** exigir `auth()`, validar `audio/*` permitido, limitar bytes y aplicar rate limit por usuario/IP.

### P1-02 - Bookings API local expone lectura y escritura sin auth suficiente

**Evidencia:** `MyOwnClone/src/app/api/bookings/route.ts:7-130`  
**Impacto:** `GET` permite leer reservas de un `cloneId` arbitrario. `POST` crea reservas con input minimo y sin rate limit/CAPTCHA.  
**Recomendacion:** `GET` solo para owner/admin del clone. Para booking publico, mover a endpoint por slug con validacion de disponibilidad, email, CAPTCHA/rate limit y antifraude basico.

### P1-03 - XSS potencial en chat por `dangerouslySetInnerHTML`

**Evidencia:** `MyOwnClone/src/components/chat/MessageBubble.tsx:38-60`, `:88`  
**Impacto:** el contenido del asistente se transforma a HTML y se sanitiza con regex. Esta estrategia es fragil frente a vectores como `javascript:` en enlaces futuros, SVG/event handlers sin comillas o HTML inesperado del LLM.  
**Recomendacion:** evitar HTML y renderizar markdown seguro con `react-markdown` + `rehype-sanitize`, o usar DOMPurify configurado. Mantener usuarios como texto.

### P1-04 - Sin cabeceras de seguridad en Next.js

**Evidencia:** `MyOwnClone/next.config.ts:4-7`  
**Impacto:** no hay CSP, HSTS, X-Frame-Options/frame-ancestors, X-Content-Type-Options ni Referrer-Policy configuradas. Aumenta el impacto de XSS/clickjacking.  
**Recomendacion:** anadir `headers()` en `next.config.ts` con CSP incremental, `frame-ancestors`, `nosniff`, HSTS en produccion y politica de referrer.

### P1-05 - CSRF token generado pero no verificado

**Evidencia:** `MyOwnClone/src/app/api/csrf/route.ts:1-13`; no hay verificacion centralizada en mutaciones.  
**Impacto:** se emite cookie/token, pero POST/PUT/DELETE no lo validan. Si una ruta usa cookies de sesion y no tiene controles adicionales, queda expuesta a CSRF.  
**Recomendacion:** implementar helper/middleware de verificacion para mutaciones o eliminar el endpoint si se decide confiar exclusivamente en SameSite + tokens bearer.

### P1-06 - Inputs de booking/email interpolados en HTML

**Evidencia:** `MyOwnClone/src/app/api/bookings/route.ts:46-53`, `MyOwnClone/src/lib/email.ts:35`  
**Impacto:** `visitorName`, `cloneName` y `meetingUrl` se insertan en HTML de email. Puede permitir HTML injection/phishing dentro del correo.  
**Recomendacion:** escapar HTML antes de interpolar o usar templates que autoescapen. Validar URL de meeting antes de incluirla.

### P1-07 - SendGrid inbound queda abierto si falta secreto

**Evidencia:** `api/controllers/myownclone_public.py:34-54`  
**Impacto:** si `SENDGRID_INBOUND_WEBHOOK_SECRET` no esta configurado, `/inbound-email` acepta requests no autenticados. Esto es util en dev, peligroso en produccion o staging expuesto.  
**Recomendacion:** fail-fast en produccion si falta el secreto. Registrar metrica/alerta si se usa modo abierto.

### P1-08 - Falta validacion de uploads

**Evidencia:** `MyOwnClone/src/app/api/stt/route.ts:4-21`, `MyOwnClone/src/app/api/clone/sources/route.ts:70-124`  
**Impacto:** cargas sin limite fuerte de tamano, MIME, extension ni escaneo pueden agotar memoria, generar costes o introducir contenido malicioso para pipelines posteriores.  
**Recomendacion:** limites por `Content-Length`, allowlist MIME, tamano maximo por plan, streaming si aplica y estados de ingestion seguros.

### P1-09 - Fallo runtime en impersonacion por import ausente

**Evidencia:** `api/controllers/console/myownclone/admin_platform.py:178` usa `secrets.token_urlsafe(32)` pero el archivo no importa `secrets`.  
**Impacto:** el endpoint `/myownclone/admin/impersonate` puede devolver 500. Es disponibilidad/operacion, pero afecta un flujo sensible de admin.  
**Recomendacion:** importar `secrets` y cubrir con test de smoke del endpoint.

---

## P2 - Medios

| ID | Hallazgo | Evidencia | Recomendacion |
|---|---|---|---|
| P2-01 | Comparacion de service key no usa timing-safe | `api/libs/login.py:60-67`, `_check_service_token` en `:83-98` | Usar `hmac.compare_digest` para cada key esperada. |
| P2-02 | `DEPLOY_SECRET` tambien autentica como service key general | `api/libs/login.py:60-63` | Separar secretos por scope: deploy no debe servir para APIs de usuario/admin. |
| P2-03 | `subprocess.run(..., shell=True)` | `api/controllers/deploy.py:33-35` | Usar lista de args y timeout; mantener allowlist de comandos. |
| P2-04 | Errores internos se devuelven al cliente | `MyOwnClone/src/app/api/clone/sources/route.ts:48,133` | Log interno + error generico externo. |
| P2-05 | Hostname tenant slug se reinyecta sin autorizacion visible | `MyOwnClone/src/proxy.ts:142-150` | Resolver slug contra tenant real y validar acceso donde aplique. |
| P2-06 | Reset token via query param | `MyOwnClone/src/app/api/auth/forgot-password/route.ts:47` | Reducir TTL, `Referrer-Policy`, pagina intermedia que cambie token por cookie httpOnly. |
| P2-07 | Token de impersonacion visible en UI | `MyOwnClone/src/components/admin/ImpersonateButton.tsx:70-75` | Mostrar una sola vez, minimizar exposicion en DOM y auditar accesos. |
| P2-08 | SQL raw en auth | `MyOwnClone/src/lib/auth.ts:63-65` | Aceptable por parametrizacion Drizzle, pero documentar y no copiar fuera de helpers. |
| P2-09 | Tests de tenant scoping skipped | `api/tests/test_tenant_scoping.py:94` | Desbloquear fixtures y convertir en test obligatorio. |
| P2-10 | Public booking Flask tambien sin rate limit | `api/controllers/myownclone_public.py:323-395` | Rate limit por IP/clone/email y validacion de email/date. |

---

## P3 - Bajos / deuda

1. `moc_active_clone_id` es cookie accesible a JS; revisar si debe ser `HttpOnly` segun uso real (`MyOwnClone/src/lib/clone-resolver.ts`).
2. Variables de entorno duplicadas o historicas: `AUTH_SECRET`/`NEXTAUTH_SECRET`, admin envs y service keys.
3. `run_dev.py` usa debug para local; documentar que nunca debe usarse en produccion.
4. Widget JS sin SRI ni versionado fuerte (`MyOwnClone/src/app/widget.js/route.ts`).
5. Whereby fetch sin timeout/AbortController (`MyOwnClone/src/lib/video.ts`).
6. Seeds/logs pueden exponer credenciales demo si se ejecutan en entornos compartidos (`api/commands/seed.py`).
7. Mezcla de castellano/ingles en errores puede dificultar observabilidad y UX de seguridad.

---

## Cosas bien implementadas

- Login Flask con rate limiting por IP, Redis y fallback in-memory (`api/controllers/console/auth.py`).
- NextAuth con estrategia JWT y bcrypt para passwords (`MyOwnClone/src/lib/auth.ts`).
- Firma Stripe webhook con `stripe.webhooks.constructEvent()` (`MyOwnClone/src/app/api/stripe/webhook/route.ts`).
- `assert_production_secrets()` y generacion segura de secretos dev (`api/app_factory.py`, `api/libs/security_checks.py`).
- SendGrid inbound usa `hmac.compare_digest` cuando hay secreto configurado (`api/controllers/myownclone_public.py`).
- Tokens de impersonacion se almacenan hasheados con pepper (`api/controllers/console/myownclone/admin_platform.py`).
- Escape de wildcards LIKE en busqueda admin (`api/controllers/console/myownclone/admin_platform.py`).
- Consultas Drizzle/SQLAlchemy mayoritariamente parametrizadas.

---

## Plan de remediacion priorizado

### Antes de produccion

1. Eliminar fallback `dev-api-key-for-proxy` del proxy y hacer fail-fast de `SERVICE_API_KEY`.
2. Quitar admin por prefijo `proxy-*`; separar service account de platform admin.
3. Validar identidad/tenant en backend en vez de confiar ciegamente en headers.
4. Rate limit + max length en chat publico, STT y bookings.
5. Exigir auth en STT y en `GET /api/bookings`.
6. Anadir CSP/cabeceras de seguridad.
7. Sustituir sanitizacion regex del chat por renderer seguro.
8. Escapar HTML en emails.
9. Configurar/fail-fast `SENDGRID_INBOUND_WEBHOOK_SECRET` en produccion.
10. Corregir import `secrets` en impersonacion y activar test.

### Hardening siguiente

11. Verificacion CSRF real o retirar el endpoint de token si no se usa.
12. Validacion de uploads por tamano/MIME y limites por plan.
13. Separar `DEPLOY_SECRET` de `SERVICE_API_KEY`.
14. Usar comparacion timing-safe para service keys.
15. No devolver `error.message` en APIs.
16. Rehabilitar tests de tenant scoping.
17. Revisar reset tokens en URL y politica de referrer.
18. Timeouts en integraciones externas.

---

## Nota sobre secretos locales

Existen `api/.env` y `MyOwnClone/.env.local` en el workspace local, pero no estan trackeados por `git ls-files` en esta revision. Aun asi:

- si esos ficheros se compartieron, copiaron a chats, subieron a otra rama/remoto o aparecen en logs, rotar claves;
- mantener `.env*` sensibles fuera de git;
- usar `.env.example` sin valores reales;
- considerar `git-secrets`, `gitleaks` o trufflehog en CI.

---

## Archivos verificados

- `MyOwnClone/src/proxy.ts`
- `MyOwnClone/next.config.ts`
- `MyOwnClone/src/lib/auth.ts`
- `MyOwnClone/src/components/chat/MessageBubble.tsx`
- `MyOwnClone/src/app/api/stt/route.ts`
- `MyOwnClone/src/app/api/bookings/route.ts`
- `MyOwnClone/src/app/api/clone/sources/route.ts`
- `MyOwnClone/src/app/api/csrf/route.ts`
- `MyOwnClone/src/lib/email.ts`
- `api/libs/login.py`
- `api/controllers/console/auth.py`
- `api/controllers/console/myownclone/admin_platform.py`
- `api/controllers/myownclone_public.py`
- `api/controllers/deploy.py`
- `api/tests/test_tenant_scoping.py`

