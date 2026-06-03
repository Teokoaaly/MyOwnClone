# PROMPT MAESTRO — Clonify: Clon de IA para Infoproductores
# Entrega este prompt completo a cualquier IA (ChatGPT, Claude, etc.)
# para que entienda el proyecto y pueda ejecutarlo.

---

## CONTEXTO

Has analizado Clonify.com (mayo 2026), una plataforma SaaS que permite a infoproductores crear clones de IA entrenados con su propio contenido. Se extrajeron 2.6MB de código fuente sin autenticación mediante una vulnerabilidad de RSC payloads pre-redirect en Next.js.

Tu misión: construir una versión propia de este producto para venderlo a infoproductores hispanohablantes.

---

## STACK TECNOLÓGICO (a replicar)

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 14 App Router + TypeScript + Tailwind |
| Hosting | Vercel (o Coolify en VPS propio) |
| DB | PostgreSQL serverless (Neon/Supabase) + pgvector |
| Auth | NextAuth.js + OTP email + Google OAuth |
| LLM | Anthropic Claude (principal) + OpenAI (embeddings) |
| Embeddings | OpenAI text-embedding-3-small |
| Pagos | Stripe Checkout + webhooks |
| Email inbound | SendGrid Inbound Parse o CloudMailin |
| Video | Daily.co o Whereby |
| TTS/STT | Whisper + Edge TTS |

---

## ARQUITECTURA DEL CLON (RAG Pipeline)

```
Contenido → Transcripción → Chunking → Embeddings → Vector DB (pgvector)
                                                          ↓
Usuario pregunta → Retrieval → System prompt (modo) → LLM
                                                          ↓
                                            ¿Confianza > umbral?
                                            Sí → Responde
                                            No → "No tengo conocimiento" + notifica al creador
```

3 modos por clon:
1. Pedagogía: enseña con el contenido del creador
2. Ventas: recomienda productos (insistente o tranquilo)
3. Soporte: resuelve dudas, escala a humano

Contexto por URL: parámetro `?context=clase-4` activa retrieval específico.

---

## FUNCIONALIDADES A CONSTRUIR (por orden)

### Fase 1: Auth + Multi-tenant (semana 1)
- NextAuth.js + OTP email + Google OAuth
- Slugs únicos → [slug].midominio.com
- Cookies HttpOnly + SameSite strict

### Fase 2: Vector DB + RAG básico (semana 1-2)
- pgvector en PostgreSQL (misma DB)
- OpenAI text-embedding-3-small → embeddings
- Chunking: 500-1000 tokens con solapamiento
- Un solo modo al principio (pedagogía)
- System prompt: "Responde solo con el conocimiento proporcionado. Si no tienes suficiente información, di 'No tengo conocimiento sobre eso'"

### Fase 3: Chat UI pública (semana 2)
- Subdominio o widget embebible
- Notas de voz (MediaRecorder API → Whisper)
- Historial de conversación

### Fase 4: Dashboard creador (semana 2-3)
- Subir contenido: YouTube, vídeos, PDFs, texto
- Brain: CRUD de memorias, firmas, plantillas
- Analíticas básicas: preguntas frecuentes, gaps

### Fase 5: Inbox/Triage (semana 3-4)
- SendGrid Inbound Parse → webhook → PostgreSQL
- Clon lee email → genera draft → creador revisa
- Estados: pendiente, enviado, descartado
- Aprendizaje automático: guarda plantillas al enviar

### Fase 6: Stripe (semana 4)
- Planes: Pro/Scale/Enterprise
- Checkout + Customer Portal
- Trial 14-30 días con tarjeta
- Cortesías sin tarjeta (admin)
- Webhooks: subscription.created/updated/deleted

### Fase 7: Booking + Video (semana 5)
- CRUD de tipos de reunión + disponibilidad
- Página pública de reserva con selector fecha/hora
- Daily.co o Whereby para videollamada
- Grabación + transcripción (Whisper)

### Fase 8: Admin plataforma (semana 6)
- Listado de tenants con costes y uso
- Suplantación con audit log
- MRR dashboard

---

## DASHBOARD DEL CREADOR (36 secciones a construir)

Gestión del clon: AdminClon, AdminIdentidad, AdminEstilo, AdminProposito
Contenido: AdminBiblioteca, AdminCerebro, AdminRecordings
Comunicación: AdminInbox, AdminConversaciones, AdminContactos
Ventas: AdminProductos, AdminFacturas, AdminPlan
Reuniones: AdminAgenda, AdminReuniones, AdminMeetingTypes, AdminAvailability, AdminLlamada
Analíticas: AdminResumen, AdminAprendizajes, AdminUso

---

## PLANES Y PRECIOS

| Plan | Precio | Incluye |
|------|--------|---------|
| Básico | 49€/mes | 500K palabras training, 2K respuestas, 1 modo |
| Pro | 99€/mes | 1M palabras, 4K respuestas, 3 modos, email triage |
| Escala | 199€/mes | 5M palabras, 20K respuestas, booking + video, API |
| Enterprise | 499€/mes | Ilimitado, multi-clon, whitelabel, prioridad |

Trial 14 días con tarjeta. Cortesías sin tarjeta para early adopters.

---

## PITCH DE VENTA (30 segundos)

"Imagina un empleado que nunca duerme, conoce todo tu contenido al dedillo, y atiende a tus clientes como lo harías tú. Eso es lo que construimos: un clon de IA entrenado con tus vídeos, PDFs y cursos. Responde dudas, recomienda tus productos y gestiona tus emails. Desde 49€ al mes."

---

## CLIENTES OBJETIVO

1. Infoproductores — Creadores de cursos, coaches, consultores
2. SaaS B2B — Soporte y onboarding
3. Agencias — Atención a leads, calificación
4. Ecommerce — Recomendador de productos
5. Abogados/gestores — Consultas frecuentes

---

## ARGUMENTOS DE VENTA

- "Atiende mientras duermes" — Tus alumnos preguntan a las 3AM. El clon responde.
- "Multiplica ventas sin multiplicar equipo" — El clon recomienda en cada conversación.
- "Tu bandeja organizada" — El clon lee emails, propone respuestas en tu tono.
- "Nunca alucina" — Si no sabe, lo dice y te avisa. No inventa.
- "Habla tu idioma" — Español nativo, con tu estilo y personalidad.

---

## OBJECIONES Y RESPUESTAS

"Mis clientes quieren hablar conmigo" → "El clon no te reemplaza, filtra. Tú solo atiendes lo que necesita tu toque personal."
"No quiero que diga algo mal" → "Nunca alucina. Si no tiene confianza, deriva a humano y te avisa."
"Es muy caro" → "Una venta de tu curso de 500€ paga 5 meses de Pro. ¿Cuántas ventas pierdes mientras duermes?"
"Ya tengo un chatbot" → "Esto no es un chatbot genérico. Habla con tu conocimiento, tu tono, tu personalidad."

---

## NOMBRES PARA EL PRODUCTO

- TuVoz AI — "Tu conocimiento, tu voz, 24/7"
- AlterEgo — "El tú que nunca duerme"
- ClonIA — "Tu clon inteligente"
- Réplica — "Multiplícate"

---

## ESTRATEGIA DE CAPTACIÓN

| Canal | Acción |
|-------|--------|
| Comunidades infoproductores | Hotmart, Teachable, Gumroad — demo gratuita |
| LinkedIn | Casos de uso reales |
| Partners | Agencias — comisión por referido |
| Email frío | Infoproductores >1000 alumnos |

---

## COMPETENCIA DE REFERENCIA

Clonify.com — Euge Oller, $99/mes, Next.js + Vercel + Neon + Anthropic
Delfi — competidor US, más genérico
Dify (github.com/langgenius/dify) — 142K ⭐, open source, base técnica pero sin capa de negocio
