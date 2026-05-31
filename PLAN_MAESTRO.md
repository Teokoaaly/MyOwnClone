# Plan Maestro — MyOwnClone + VPS Deployment
**Fecha:** 2026-05-31
**Autor:** Hacchi (con auditoría de código completa)

---

## Estado Actual

| Componente | Estado | Ubicación |
|---|---|---|
| Next.js (frontend + API) | Código completo en GitHub v2 | github.com/Teokoaaly/MyOwnClone (branch v2) |
| Dify (backend AI) | Carpeta api/ en ~/replica/dify/ | Windows → por copiar |
| PostgreSQL + pgvector | Supabase Cloud (gestionado) | db.[PROJECT_REF].supabase.co |
| FreeLLMAPI (router IA) | Corriendo en VPS :3001 | 100.99.222.101 |
| VPS Ubuntu | 3.9GB RAM, 2 CPUs, 116GB disco | 100.99.222.101 |

---

## Hallazgos de Auditoría (29 Issues)

### 🔴 CRÍTICOS — No shippable

1. **RAG pipeline roto** — `src/lib/rag/*.ts` usa `@deprecated`, referencias a tablas inexistentes (`schema.memories`, `schema.conversations`). El contenido real está en Dify.

2. **Widget.js expone URL interna** — `src/app/widget.js/route.ts:3` usa fallback `replica.tudominio.com` si `NEXT_PUBLIC_APP_URL` no está configurado.

3. **CloneChat mismatch API** — `src/components/chat/CloneChat.tsx:55-59` envía `conversationId`/`mode` (camelCase), pero el server espera `conversation_id`/`silo` (snake_case).

4. **Chat route sin auth** — `src/app/api/clone/[slug]/chat/route.ts` es público, no valida `visitorEmail`/`visitorName`.

5. **Sin rate limiting** — el endpoint público de chat no tiene límites; quota check solo en rutas autenticadas.

6. **STT route sin auth** — `src/app/api/stt/route.ts` permite a cualquiera usar la key de OpenAI.

7. **Inbound email sin verificación** — `SENDGRID_INBOUND_WEBHOOK_SECRET` definido pero nunca usado para verificar webhooks.

### 🟠 HIGH

8. **Query params sin sanitizar** — `src/app/api/admin/[...path]/route.ts:9` reenvía search params del cliente directamente al backend.

9. **Plans route expone datos backend** — `src/app/api/clone/plans/route.ts` proxies sin filtrar.

10. **Dev credentials crea admins** — `src/lib/auth.ts:22-69` auto-crea usuarios con rol `platform_admin` en dev; si se activa en prod, cualquiera es admin.

11. **Storage usa Service Role Key** — `src/lib/storage.ts:4` usa admin key para todas las operaciones en vez de keys anónimas por usuario.

12. **Middleware solo reconoce subdominio `replica.`** — `src/middleware.ts:6` solo detecta tenants en `*.replica.com`, ignora `customDomain` en `cloneConfigs`.

### 🟡 MEDIUM

13. **Chunk decoder produce basura** — `src/lib/rag/ingest.ts:25-27` trata token IDs como bytes.

14. **Bookings POST devuelve redirect** — `src/app/api/bookings/route.ts:127-129` devuelve redirect pero el cliente espera JSON.

15. **Inbox list error 404 confuso** — sin clones, error sin mensaje claro.

16. **Clone config sin manejo de errores** — si Dify está caído, página muestra solo el slug sin error visible.

17. **Booking sin validación de inputs** — `visitorEmail` no es formato email, `date` no se valida.

18. **Stripe checkout sin tenant context** — reenvía sin `tenantId` en URL, depende de cookie.

### 🟢 LOW / CODE QUALITY

19. `@ts-nocheck` en `pipeline.ts` — archivo deprecated.
20. `@ts-expect-error` sin doc en `auth.ts`.
21. Naming inconsistente `cloneConfigs` vs `clones`.
22. Dashboard resumen oculta errores (muestra `--` sin indicar fallo).
23. Interfaz `ChatMessage` vs `Message` duplicada.
24. `PLATFORM_ADMIN_TOKEN` nunca verificado en admin routes.

### ⚪ INCOMPLETO (sin implementación)

25. Upload de sources (PDF, YouTube, web) — tabla existe, no endpoints.
26. Stripe webhook handler — secret en env, no existe `/api/webhooks/stripe`.
27. Analytics dashboard — proxies a Dify pero el shape no coincide con el frontend.
28. Catálogo de productos — página existe, sin UI de gestión.
29. Billing portal — página existe, sin rutas de gestión.

---

## VPS: Qué podemos montar

### Recursos VPS (100.99.222.101)
- **RAM:** 3.9GB total (~1.8GB disponible)
- **CPU:** 2 cores
- **Disco:** 116GB (41GB libre)
- **SO:** Ubuntu 24.04

### Lo que SÍ cabe en el VPS (sin Docker)

| Servicio | RAM estimada | ¿En VPS? |
|---|---|---|
| Next.js (puro Node) | ~300-500MB | ✅ Sí |
| FreeLLMAPI (ya corriendo) | ~200-400MB | ✅ Ya está |
| PostgreSQL cliente (Drizzle) | ~50MB | ✅ Sí (conecta a Supabase cloud) |
| Cron jobs / scripts | ~50MB | ✅ Sí |
| Unbound/DNSCrypt | ~30MB | ✅ Sí |

### Lo que NO cabe (necesita servidor propio o cloud)

| Servicio | RAM mínima | Alternativa |
|---|---|---|
| Dify (Python/AI backend) | ~2-4GB | Mantener en Windows o renting |
| pgvector (vector DB) | ~1GB+ | Supabase Cloud (ya lo tienes) |
| Stripe webhook + processing | — | Código sí, necesita Dify primero |

### Arquitectura propuesta para VPS

```
                    ┌─────────────────────┐
                    │   VPS (3.9GB RAM)   │
                    │  Ubuntu 24.04       │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ FreeLLMAPI    │  │
                    │  │ :3001         │  │
                    │  └───────────────┘  │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ Next.js       │  │
                    │  │ (futuro)     │  │
                    │  │ :3000         │  │
                    │  └───────────────┘  │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ Cron scripts │  │
                    │  │ (UKH watcher)│  │
                    │  └───────────────┘  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Internet          │
                    │                     │
          ┌─────────▼─────────┐  ┌────────▼────────┐
          │  Supabase Cloud   │  │  Dify Backend  │
          │  (PostgreSQL +   │  │  (Windows o    │
          │   pgvector)      │  │   otro VPS)   │
          │  db.xxx.supabase │  │  :5001         │
          └──────────────────┘  └────────────────┘
```

---

## Plan de Implementación — 5 fases

### Fase 1: Fixes críticos de seguridad ✅ (prioridad inmediata)

**Archivos a modificar:**
- `src/app/api/stt/route.ts` — agregar auth check
- `src/app/api/inbound-email/route.ts` — agregar verificación de webhook
- `src/app/api/clone/[slug]/chat/route.ts` — rate limiting básico
- `src/lib/storage.ts` — usar anon key en vez de service role
- `src/lib/auth.ts` — proteger dev credentials provider

**Tiempo estimado:** 2-3 horas

### Fase 2: Fixes de bugs lógicos ✅ (funcionalidad básica)

**Archivos a modificar:**
- `src/components/chat/CloneChat.tsx` — corregir payload a snake_case
- `src/app/api/bookings/route.ts` — devolver JSON en vez de redirect
- `src/lib/rag/` — eliminar o documentar como deprecated abandonado

**Tiempo estimado:** 1-2 horas

### Fase 3: Completar features incompletas (v2 post-audit)

**Implementar:**
- `/api/webhooks/stripe/route.ts` — handler de eventos Stripe
- `/api/sources/route.ts` — upload de PDFs, YouTube, web content
- Rate limiting real en `/api/clone/[slug]/chat`

**Tiempo estimado:** 4-6 horas

### Fase 4: Migrar Dify a VPS o cloud

**Opciones evaluadas:**
1. **Mantener en Windows** (gratis, pero bloqueado cuando Win no está)
2. **Dify Cloud** (gratis tier, 3 bots)
3. **VPS separado** (1GB+ RAM, ~5€/mes)
4. **HuggingFace Spaces** (gratis, limitado)

**Recomendación:** Dify Cloud + VPS propio para Next.js

**Tiempo estimado:** 1 día

### Fase 5: Desplegar Next.js en VPS

**Pre-requisitos:**
- Dify funcionando (cloud o VPS)
- Dominio configurado (`replica.tudominio.com`)
- SSL con Let's Encrypt

**Pasos:**
1. `node -v` (necesita Node 20+)
2. `npm install pnpm -g`
3. `pnpm install` + `pnpm build`
4. `pm2 start npm -- start` (o systemd service)
5. Configurar Nginx como reverse proxy a :3000

**Tiempo estimado:** 3-4 horas

---

## Bugs encontrados por archivo

```
src/app/api/clone/[slug]/chat/route.ts     - sin auth, sin rate limit
src/app/api/stt/route.ts                   - sin auth
src/app/api/inbound-email/route.ts         - sin verificación webhook
src/app/api/bookings/route.ts              - redirect vs JSON
src/app/api/admin/[...path]/route.ts       - query params sin sanitizar
src/components/chat/CloneChat.tsx          - camelCase vs snake_case
src/lib/storage.ts                          - service role key
src/lib/auth.ts                             - dev credentials provider
src/middleware.ts                          - solo detecta subdominio replica.
src/lib/rag/ingest.ts                      - decoder basura
src/lib/rag/pipeline.ts                    - @ts-nocheck, referencias rotas
```

---

## Notas

- El frontend Next.js está completo y funciona sin Dify para las partes estáticas (login, registro, dashboard básico)
- El verdadero valor está en Dify como backend AI — sin él, el clone chat no responde
- FreeLLMAPI ya está corriendo en el VPS y puede ser usado como router inteligente para futuras integraciones
- La carpeta `dify/` en el Windows tiene el backend completo — hay que copiarlo para desplegarlo