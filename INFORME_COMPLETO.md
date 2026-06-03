# INFORME: Clonify.com — Ingeniería Inversa Completa

**Fecha:** 2026-05-26  
**Método:** Extracción pasiva de RSC payloads (React Server Components) + análisis de bundles JS públicos  
**Alcance:** Admin panel, dashboard de creador, bundles cliente, i18n completo  
**Autenticación requerida:** NINGUNA — todas las rutas de admin sirven código antes del redirect

---

## RESUMEN EJECUTIVO

Clonify es una plataforma SaaS multi-tenant que permite a creadores/infoproductores entrenar clones de IA con su propio contenido. Stack: Next.js 14 (App Router + Turbopack + RSC) sobre Vercel serverless, PostgreSQL Neon, Anthropic Claude + OpenAI. El producto está en beta activa con clientes reales.

**Hallazgo crítico:** El 100% del código fuente del panel de administración multi-tenant y del dashboard de creador es accesible sin autenticación. La vulnerabilidad V1 (RSC payload pre-redirect) permite extraer la UI completa, lógica de negocio, estados, y diccionario i18n de ~230KB que documenta cada feature.

---

## 1. DATOS DE LA EMPRESA

| Campo | Valor |
|---|---|
| Producto | Clonify — AI clone platform |
| Empresa | Marea Kiss LLC (Wyoming, USA) |
| CEO/Founder | Eugenio José Oller de Torres (Euge Oller) |
| Dominio | myownclone.com (también clonefy.com — parking) |
| Fase | Beta activa |
| Competidor directo | Delfi (San Francisco, US) |
| Precio base | $99/mes — 1M palabras training, 4K respuestas |

---

## 2. STACK TECNOLÓGICO

### Infraestructura
| Capa | Tecnología | Detalle |
|---|---|---|
| Frontend | Next.js 14 | App Router, Turbopack, React Server Components |
| Hosting | Vercel | `x-vercel-id: iad1::iad1`, Edge Network |
| API Backend | Next.js Route Handlers | Serverless en Vercel |
| Base de datos | PostgreSQL serverless | Neon Inc. |
| Auth | NextAuth.js | JWT + cookies HttpOnly + OTP + Google OAuth |
| AI/LLM | Anthropic Claude + OpenAI | Embeddings + chat completions |
| Pagos | Stripe | Checkout, trials 30d, cupones 100% off |
| Email | SMTP/API | Inbound: *@myownclone.com, Outbound: propio |
| Monitoring | Sentry | DSN: `6b2d7ed6999454df87ccf844aa85ba70`, org: `4511315838173184` |
| Analytics | PostHog | `phc_tn48YvixjuzzdhbNFLzt9hD7TfwbH2AssUxG2gAiPWei` |
| Fuentes | Poppins + JetBrains Mono | woff2 |
| i18n | Soporte completo | `/es`, `/en` con locale routing |

### Arquitectura Serverless
```
┌──────────────────────────────────────────────────┐
│                    Vercel Edge                    │
│  ┌─────────────┐  ┌──────────┐  ┌────────────┐  │
│  │ app.myownclone  │  │api.myownclone│  │admin.myownclone│  │
│  │ (visitante)  │  │(dashboard)│  │ (platform) │  │
│  └─────────────┘  └──────────┘  └────────────┘  │
│         │               │              │          │
│         └───────────────┼──────────────┘          │
│                         │                         │
│              Neon PostgreSQL (serverless)          │
│              Stripe • Anthropic • OpenAI           │
└──────────────────────────────────────────────────┘
```

---

## 3. ARQUITECTURA DE LA APLICACIÓN

### 3.1 Dashboard del Creador (36 secciones)

| Sección | Descripción |
|---|---|
| AdminClon | Gestión del clon: identidad, personalidad, publicación |
| AdminCerebro | Brain: memorias, firmas, plantillas de respuesta |
| AdminInbox | Triage de emails: clon propone drafts, humano aprueba/envía |
| AdminRecordings | Grabaciones de reuniones con transcripción |
| AdminReuniones | Booking: disponibilidad, tipos de reunión, integraciones |
| AdminBiblioteca | Contenido: cursos, vídeos, PDFs, YouTube, entrevistas AI |
| AdminFacturas | Facturación y planes |
| AdminPlan | Gestión de suscripción (Pro/Scale/Enterprise) |
| AdminIdentidad | Perfil del creador |
| AdminEstilo | Personalización visual del clon |
| AdminProductos | Productos que el clon puede recomendar |
| AdminContactos | CRM/contactos |
| AdminConversaciones | Historial de chats con el clon |
| AdminAprendizajes | Insights: preguntas frecuentes, gaps de conocimiento |
| AdminAgenda | Calendario |
| AdminLlamada | Videollamada integrada |
| AdminUso | Consumo: palabras, respuestas, costes |
| AdminResumen | Dashboard principal |
| AdminMeetingTypes | Tipos de reunión (duración, precio, descripción) |
| AdminAvailability | Horarios disponibles |
| AdminQuotaBanner | Banner de cuota/uso |
| AdminPlaceholder | Estados vacíos |
| AdminShell | Layout/navegación |
| AdminTenantSlug | Configuración de subdominio |

### 3.2 Admin de Plataforma (8 secciones)

| Sección | Descripción |
|---|---|
| AdminPlatformTenants | Gestión de tenants: buscar, filtrar, ver costes, suplantar |
| AdminPlatformResumen | MRR, costes plataforma, margen, gráficas |
| AdminPlatformInbox | Bandeja global de *@myownclone.com |
| AdminPlatformSpam | Gestión de dominios bloqueados |
| AdminPlatformFeedback | Errores y sugerencias de usuarios |
| AdminPlatformFaqs | FAQs de plataforma |
| AdminImpersonationBanner | Banner rojo durante suplantación (30min + audit log) |

### 3.3 Público / Visitante

| Sección | Descripción |
|---|---|
| PublicBooking | Página de reserva (calendario, slots, formulario) |
| PublicRecording | Grabación compartida + chat con el clon contextual |
| MyBooking | Página post-reserva (confirmación, cancelar, ICS) |
| MeetingRoom | Sala de videollamada en Clonify |
| VoiceCall | Notas de voz (MediaRecorder API + transcripción) |
| FeedbackWidget | Widget flotante de feedback |
| InstantMeeting | Reunión instantánea |

---

## 4. FLUJO DEL CLON (RAG Pipeline)

```
                 ┌──────────────────┐
                 │   CONTENIDO      │
                 │ YouTube, vídeos  │
                 │ PDFs, texto, web │
                 │ Entrevistas AI   │
                 └────────┬─────────┘
                          │
                    Transcripción
                    Chunking
                    Embeddings (OpenAI)
                          │
                 ┌────────▼─────────┐
                 │   VECTOR DB      │
                 │  (Neon pgvector) │
                 └────────┬─────────┘
                          │
    ┌─────────────────────┼─────────────────────┐
    │                     │                     │
    ▼                     ▼                     ▼
Pedagogía              Soporte              Ventas
(System prompt)    (System prompt)    (System prompt)
    │                     │                     │
    └─────────────────────┼─────────────────────┘
                          │
              ┌───────────▼───────────┐
              │  ¿Confianza > umbral? │
              └───────────┬───────────┘
                    │           │
                    Sí          No
                    │           │
                    ▼           ▼
              Responde    "No tengo conocimiento"
                          → Notifica al creador
                          → Sugiere rellenar gap
```

### Modos del clon:
1. **Pedagogía** — enseña con el contenido del creador
2. **Ventas** — recomienda productos (insistente o tranquilo)
3. **Soporte** — resuelve dudas, escala a humano si no sabe

### Instancias por contexto:
Cada URL del clon puede llevar un parámetro de contexto (clase, vídeo, landing) que activa un retrieval específico.

---

## 5. FUNCIONALIDADES DETALLADAS

### 5.1 Triage / Inbox (Killer Feature)
- El clon lee emails entrantes (*@myownclone.com o dominio personalizado)
- Propone drafts de respuesta en la voz del creador
- El creador revisa, edita y envía (o descarta)
- Aprende de cada interacción (memorias, plantillas, firmas)
- Sistema de etiquetas para clasificar tickets

### 5.2 Brain (Memorias + Firmas + Plantillas)
- **Memorias**: fragmentos de conocimiento inyectados en el prompt del clon
- **Firmas**: cierre de emails configurable
- **Plantillas**: respuestas reusables con condición "cuándo usar"
- Todo se puede crear/editar/borrar desde el panel

### 5.3 Ingresión de Contenido
- YouTube: pegar URL, transcripción automática
- Cursos: subir vídeos a carpetas por módulos
- PDFs, texto, web
- Entrevistas AI: un agente entrevista al creador para extraer su conocimiento
- Speaker separation: en entrevistas reales, separa al creador del entrevistador

### 5.4 Booking + Videollamada
- Tipos de reunión configurables (duración, precio, descripción)
- Página pública de reserva con selector de fecha/hora
- Videollamada integrada en Clonify (no Zoom/Meet)
- Grabación automática con transcripción
- Chat post-reunión con el clon (sabe lo que se dijo)

### 5.5 Analytics / Insights
- Preguntas más frecuentes
- Gaps de conocimiento (lo que el clon no supo responder)
- Análisis de avatar de audiencia
- Costes desglosados: respuestas del clon vs ingesta vs ops

### 5.6 Admin de Plataforma
- **Resumen**: MRR desglosado por plan, costes plataforma, margen, gráficas temporales
- **Tenants**: listado con búsqueda, filtros por plan/estado, ordenación por coste/uso
- **Suplantación**: login como cualquier tenant con motivo + audit log + timeout 30min
- **Inbox global**: todos los emails que llegan a *@myownclone.com
- **Concesión de planes**: invitaciones con cortesía (sin tarjeta) o trial Stripe
- **Feedback**: errores y sugerencias con screenshots

---

## 6. ENDPOINTS API DESCUBIERTOS

| Endpoint | Método | Auth |
|---|---|---|
| `/api/admin/clon/sources/activity` | GET | Cookie (sin CSRF) |
| `/api/me/tenants` | GET | Cookie |
| `/api/me/tenants/switch` | POST | Cookie (sin CSRF) |
| `/api/auth/logout` | POST | Cookie |
| `/api/admin/platform/impersonate/stop` | POST | Cookie (sin CSRF) |
| `/api/admin/feedback` | POST | Cookie |

El resto de endpoints usan Server Actions (Next.js) → no expuestos como fetch explícito.

---

## 7. VULNERABILIDADES CONFIRMADAS

| # | Vulnerabilidad | Severidad | Evidencia |
|---|---|---|---|
| V1 | Fuga masiva código admin sin auth | **CRÍTICA** | 2.6MB extraídos de 10 rutas |
| V2 | Sentry DSN + org ID expuestos | **CRÍTICA** | En meta tags HTML |
| V3 | Sin cabeceras de seguridad | ALTA | Sin CSP, X-Frame, X-Content-Type |
| V4 | CORS wildcard en login/registro | ALTA | `Access-Control-Allow-Origin: *` |
| V5 | Sin protección CSRF en API admin | ALTA | Sin X-CSRF-Token en POST |
| V8 | Sin rate limiting | MEDIA | 10 peticiones/3s → 200 OK |

### Mecanismo de V1:
```
GET /admin → Next.js detecta !auth → NEXT_REDIRECT /login
PERO antes del redirect, el RSC payload ya se ha serializado
y enviado al cliente (266KB de HTML con toda la UI del admin)
```

---

## 8. PLANES Y PRECIOS

| Plan | Precio | Detalles |
|---|---|---|
| Pro | $99/mes | 1M palabras, 4K respuestas |
| Scale | Superior | Más capacidad |
| Enterprise | Personalizado | Custom |

- Trial 30 días con Stripe (tarjeta obligatoria)
- Cortesías sin tarjeta (concedidas manualmente por admin)
- MRR tracking y gestión de pagos fallidos

---

## 9. EQUIPO Y CONTEXTO

- **Euge Oller** — CEO, creador también de Emprenda Aprendiendo y Leader Sumaris
- **Javi** — advisor, recomendó "haz 10 veces menos" (focus en MVP)
- **Hai** — advisor, recomendó centrarse en el clon primero
- **Josías** — early user/beta tester
- Euge descubrió Delfi (competidor US) y decidió construir una versión mejor orientada a negocios online
- YC RFS #3: "Company Brain" — centralizar conocimiento de empresa es la visión final

---

## 10. ARCHIVOS EXTRAÍDOS

Todo en `/home/haxth3/myownclone_source/`:

```
admin*.html              6 páginas del admin (264KB c/u)
api_*.html                4 páginas del dashboard (260KB c/u)
*_rsc_*.txt               86 payloads RSC serializados
rsc_payload_6.txt         229KB — diccionario i18n completo
js_bundles/               24 bundles JS minificados
admin_full.html           HTML completo inicial
admin_inbox.html          Bandeja admin completa
```

---

## 11. RECOMENDACIONES PARA CLONACIÓN

### MVP viable con estas tecnologías:

| Componente | Tech Stack Propuesto |
|---|---|
| Frontend | Next.js 14 App Router + TypeScript + Tailwind |
| Hosting | Vercel (o Coolify en VPS propio) |
| DB | PostgreSQL (Neon o Supabase) |
| Auth | NextAuth.js + OTP + OAuth |
| Vector DB | pgvector (misma DB) o Pinecone |
| LLM | Anthropic Claude + OpenAI |
| Embeddings | OpenAI text-embedding-3-small |
| Email inbound | SendGrid Inbound Parse o CloudMailin |
| Pagos | Stripe Checkout |
| Booking | Cal.com API o custom con Daily/Whereby |
| TTS/STT | Whisper + ElevenLabs/Edge TTS |

### Orden de construcción:
1. Auth + multi-tenant (slugs, subdominios)
2. Vector DB + RAG básico (un solo modo)
3. Chat UI pública
4. Dashboard creador (contenido, brain, analíticas)
5. Inbox/triage de emails
6. Stripe + planes
7. Booking + videollamada
8. Admin platform (tenants, impersonation, MRR)
