# Auditoria — Integraciones externas (TASK-360-06)

## Resumen
- **Estado:** Amarillo — Stripe y SendGrid configurados con firma; Resend y Whereby funcionales; gaps en rate limiting publico y validacion de inputs
- **Riesgo principal:** Endpoint publico de chat sin rate limiting permite abuso de costos LLM; SendGrid webhook abierto si falta el secret; email templates con XSS
- **Veredicto prod:** Funcional con reservas. Requiere endurecimiento de seguridad en endpoints publicos y validacion de inputs antes de produccion real

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| Stripe webhook (Next.js) | ✅ | ~90% | `src/app/api/stripe/webhook/route.ts` — HMAC signature verificada, maneja 5 eventos |
| Stripe controller (Flask) | ✅ | ~80% | `api/controllers/console/myownclone/stripe_ctrl.py` — checkout, plans, billing portal |
| SendGrid inbound | ✅ | ~70% | `api/controllers/myownclone_public.py:62-123` — firma verificada con fallback abierto |
| Resend (email outbound) | ✅ | ~80% | `src/lib/email.ts` — sendEmail, booking confirmation, login verification |
| Whereby (video) | ✅ | ~75% | `src/lib/video.ts` — createMeeting, getMeeting, deleteMeeting |
| Email processor | ✅ | ~85% | `api/core/myownclone/email_processor.py` — parsing, HTML stripping, truncacion |
| Email AI | ✅ | ~70% | `api/core/myownclone/email_ai.py` — clasificacion y borrador con LLM |
| Anthropic/OpenAI | ✅ | ~75% | `api/core/model_manager.py` — ModelManager con fallback |
| Sentry/PostHog | ⚠️ | ~20% | Configurado en `.env.example` pero no verificada integracion real |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| INT-001 | P0 | Chat publico sin rate limiting | Abuso de costos LLM — cualquier persona puede generar consultas ilimitadas | `myownclone_public.py:155-256` — endpoint `/clones/<slug>/chat` sin CAPTCHA, API key ni rate limit por IP | Anadir rate limiting por IP (ej: 20 req/min), CAPTCHA o API key para chat publico |
| INT-002 | P1 | SendGrid webhook abierto si falta secret | Acepta emails no autenticados en produccion si `SENDGRID_INBOUND_WEBHOOK_SECRET` no esta configurado | `myownclone_public.py:41-55` — `_check_sendgrid_signature()` retorna `True` si secret no definido | Fail-closed: rechazar si secret no configurado en produccion (no solo warn) |
| INT-003 | P1 | Parse errors retornan HTTP 200 | SendGrid no reintenta webhooks fallidos — emails se pierden silenciosamente | `myownclone_public.py:92` — `return jsonify({"status": "parse_error"}), 200` | Cambiar a 500 para que SendGrid reintente |
| INT-004 | P1 | XSS en email templates | Inyeccion HTML en nombres de visitantes/enlaces de booking | `email.ts:33-39, 51-59` — `params.visitorName`, `params.cloneName`, `params.meetingUrl` interpolados directamente en HTML | Escapar HTML con funcion `escapeHtml()` antes de interpolacion |
| INT-005 | P1 | Sin validacion de URL en Stripe checkout | Open redirect a dominios arbitrarios via `success_url`/`cancel_url` | `stripe_ctrl.py:94-95` — URLs pasadas directamente a Stripe sin validacion de dominio | Validar que URLs pertenecen a dominios permitidos (whitelist) |
| INT-006 | P2 | Mensaje de error Stripe expuesto al cliente | Filtra detalles internos del servidor | `stripe_ctrl.py:108` — `str(e)` devuelto al cliente | Loggear internamente, devolver mensaje generico |
| INT-007 | P2 | Sin validacion de longitud en chat publico | Prompts muy largos incrementan costos LLM innecesariamente | `myownclone_public.py:177-178` — `message = data.get("message", "")` sin max length | Limitar a 4000 caracteres (igual que email processor) |
| INT-008 | P2 | Sin validacion de email en booking | Datos arbitrarios se insertan en DB | `myownclone_public.py:397-473` — `visitor_email` aceptado sin formato | Validar formato basico de email con regex |
| INT-009 | P2 | Whereby getMeeting/deleteMeeting sin check de respuesta | Errores se devuelven como datos validos | `video.ts:43-52` — no checkean `response.ok` | Anadir check `response.ok` y lanzar error en caso contrario |
| INT-010 | P2 | Proxy tenant ID bypass en inbox | Posible acceso cross-tenant si proxy IDs son adivinables | `inbox.py:216` — `if tenant_id and not tenant_id.startswith("proxy-"):` | Documentar riesgo; considerar validacion adicional para proxy users |
| INT-011 | P3 | Prompt injection via email contenido | Atacante puede manipular clasificacion LLM | `email_ai.py:29-43` — contenido de email inyectado directamente en prompts | Conocido de LLMs; mitigar con instrucciones de sistema mas robustas |
| INT-012 | P3 | Draft regeneration siempre clasifica como "consulta" | Inconsistencia logica en inbox | `inbox.py:204-206` — `classification = "consulta"` hardcodeado | Usar resultado real de `classify_email()` |

## Matriz de interconexion

### Flujo: Stripe billing

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Facturacion page | `facturacion/page.tsx` | ✅ Funcional | — |
| API Route | Stripe webhook | `api/stripe/webhook/route.ts` | ✅ HMAC verificado | tenant_id no validado como UUID |
| Backend | Stripe controller | `stripe_ctrl.py` | ✅ Auth + checkout | Open redirect en URLs |
| Backend | Plans endpoint | `stripe_ctrl.py` | ✅ Funcional | — |
| DB | Tenants (plan/status) | `schema/tenants.ts` | ✅ subscriptionStatus | — |

### Flujo: Email inbound (SendGrid)

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Webhook | SendGrid inbound | `myownclone_public.py:62-123` | ⚠️ Condicional | Abierto si falta secret; parse error retorna 200 |
| Parser | Email processor | `email_processor.py` | ✅ Funcional | HTML stripping basico (aceptable) |
| AI | Email AI | `email_ai.py` | ✅ Funcional | Prompt injection; JSON parsing fragil |
| DB | Emails | `schema/emails.ts` | ✅ Funcional | — |

### Flujo: Email outbound (Resend)

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Lib | email.ts | `src/lib/email.ts` | ✅ Funcional | XSS en templates |
| Templates | Booking/verify | `email.ts:33-59` | ⚠️ Vulnerable | Sin escape HTML |
| Config | Resend API key | `.env.example` | ✅ Documentado | — |

### Flujo: Video (Whereby)

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Lib | video.ts | `src/lib/video.ts` | ⚠️ Parcial | getMeeting/deleteMeeting sin check respuesta |
| Config | WHEREBY_API_KEY | `.env.example` | ✅ Documentado | — |

### Flujo: Chat publico (LLM)

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Endpoint | Chat SSE | `myownclone_public.py:155-256` | ⚠️ Sin rate limit | Sin CAPTCHA/API key, sin max length |
| Pipeline | RAG retrieval | `api/core/retrieval.py` | ✅ Funcional | — |
| LLM | ModelManager | `api/core/model_manager.py` | ✅ Funcional | Sin fallback robusto |

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-601 | P0 | Anadir rate limiting a chat publico (20 req/min por IP) | Agent Backend (360-04) | 1 dia | — |
| T-602 | P1 | SendGrid webhook: fail-closed si falta secret | Agent Backend (360-04) | 0.5 dias | — |
| T-603 | P1 | SendGrid parse error: retornar 500 en vez de 200 | Agent Backend (360-04) | 0.5 dias | — |
| T-604 | P1 | Escapar HTML en email templates (escapeHtml) | Agent Frontend (360-03) | 0.5 dias | — |
| T-605 | P1 | Validar dominio en success_url/cancel_url de Stripe | Agent Backend (360-04) | 0.5 dias | — |
| T-606 | P2 | Limitar longitud de mensaje en chat publico a 4000 chars | Agent Backend (360-04) | 0.5 dias | — |
| T-607 | P2 | Validar formato de email en endpoint de booking | Agent Backend (360-04) | 0.5 dias | — |
| T-608 | P2 | Anadir check response.ok a Whereby getMeeting/deleteMeeting | Agent Frontend (360-03) | 0.5 dias | — |
| T-609 | P2 | Loggear error Stripe internamente, devolver mensaje generico | Agent Backend (360-04) | 0.5 dias | — |
| T-610 | P3 | Usar classify_email() real en draft regeneration | Agent Backend (360-04) | 0.5 dias | — |

## Open Questions

1. **Chat publico**: Se requiere autenticacion para chatear con un clon, o es intencionalmente publico? Si es publico, el rate limiting es critico.
2. **SendGrid fallback**: El fallback abierto es para desarrollo local. En produccion, se garantiza que `SENDGRID_INBOUND_WEBHOOK_SECRET` este configurado?
3. **Prompt injection**: Se quiere mitigar con sanitizacion de input o con instruccions de sistema mas robustas?
4. **Whereby**: Se usa activamente? Si no, considerar eliminar la integracion para reducir superficie de ataque.
