---
id: thread-myownclone-vs-myclone-is
type: thread
updated: 2026-10-23
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[myownclone]]", "[[myownclone-vs-delfi]]", "[[ai-clones-market]]"]
---

# Thread — MyOwnClone vs MyClone.is

Síntesis del material atomizado el 2026-10-22. Fuentes: 10 documentos OSINT en `raw/articles/` (Mayo–Junio 2026), atomizados en 107 notas de `2-atoms/`.

## Tesis del thread

MyClone.is es el competidor más dangerous y el más documentado del mapa. No compite por ser el clon más parecido a una persona famous: compite por **operationalizar** la clonificación — 227 endpoints REST, versionado de prompts, workflows, Stripe Connect para el creador, observabilidad Langfuse, voz con tres proveedores y dominios propios. Our product tiene la arquitectura más limpia (tres silos explícitos, modos, memorias) pero **apenas expone superficie de API**: es un back-office RSC-first sin contrato público.

Esto invierte la lectura del mapa de competencia heredado (`[[2026-1022-solo-personify-compite-de-verdad]]`): el mapa de mayo decía "solo Personify compite de verdad" y no mencionaba MyClone.is. Ese atom ahora lleva la fricción correspondiente.

## Ejes de comparación

| Eje | MyClone.is (verificado) | MyOwnClone (verificado en código) | Átomos |
|---|---|---|---|
| Superficie API | 227 endpoints, OpenAPI v1/v2, envoltura `{data, error}` | RSC + Server Actions; sin REST público | [[2026-1022-myclone-api-superficie-227-endpoints]], [[2026-1022-mutaciones-rsc-sin-api-rest]], [[2026-1022-api-privada-sin-documentacion]] |
| Versionado de prompts | Objetos `PromptVersion` con `change_summary`, `created_by`, timeline y diff | `CloneModePrompt` es un único campo sobrescribible; sin historial | [[2026-1022-myclone-prompt-versioning]], [[2026-1022-gap-prompt-versioning-clonemodeprompt]] |
| Memoria / modos | Los modos no aparecen en su API | Tres silos (knowledge/terms/personality) + modos + memorias | [[2026-1022-myclone-carece-modos-memories-ni-visitors]], [[2026-1022-arquitectura-rac-tres-modos-por-clon]], [[2026-1022-modulo-brain-cerebro-memorias-plantillas]] |
| Workflows | `Workflow` con ciclo de vida, `output_template`, scoring de leads | Cero: solo chat libre | [[2026-1022-myclone-workflows-beta-dominio]], [[2026-1022-gap-workflows-myownclone]] |
| Monetización del creador | Stripe Connect | El creador no cobra; solo planes de plataforma | [[2026-1022-myclone-stripe-connect-monetizacion]], [[2026-1022-gap-monetizacion-creador-stripe-connect]] |
| Voz | 3 orígenes × 2 proveedores (Cartesia/ElevenLabs) + LiveKit | Sin voz; LiveKit también ausente | [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]], [[2026-1022-myclone-voice-clone]], [[2026-1022-gap-voz-en-vivo-myownclone]] |
| Observabilidad | Langfuse + evals + tracking de tokens | Ninguna | [[2026-1022-myclone-langfuse-observabilidad]], [[2026-1022-gap-observabilidad-prompts-langfuse]] |
| Captura de leads | `/personas/{id}/visitors` + `capture-lead` | No existe tabla de visitantes; solo `Feedback` con rating | [[2026-1022-myownclone-ventajas-sobre-myclone]], [[2026-1022-gap-lead-capture-visitors]] |
| Streaming | SSE + LiveKit | SSE sobre Dify RAG, sin historial en el prompt | [[2026-1022-myclone-chat-streaming-sse]], [[2026-1022-pipeline-chat-actual-myownclone]] |
| Dominios propios | Custom domains + whitelabel | Campo `custom_domain` existe pero inactivo | [[2026-1022-myclone-custom-domains-whitelabel]], [[2026-1022-gap-custom-domains-campo-inactivo]] |

## El gap estructural de our platform

El handoff de junio documenta que nuestro producto son **dos repos independientes** (Flask/SQLAlchemy en 5001 + Next.js/Drizzle en 3000) donde el frontend escribe Drizzle directamente y bypasea Flask, con dos sistemas de auth desconectados y cuatro bugs de drift de schema. Eso no es una nota de OSINT del competidor: es una descripción de our own code, verificada contra `api/api/models/clone.py`. Es el hallazgo más accionable de todo el lote y no aparece en ninguna nota legacy.

Ver [[2026-1022-myownclone-dos-repos-flask-nextjs]], [[2026-1022-auth-flask-nextauth-desconectados]], [[2026-1022-drift-schema-drizzle-sqlalchemy]], [[2026-1022-bug-enum-modos-teach-vs-pedagogy]].

## Lo que ya tenemos y no se está comparando

La tabla de ejes arrima a MyClone.is en casi todo. Pero el material atomizado hoy contiene capacidades propias de MyOwnClone que la comparación no captura, porque no tienen equivalente en la API del competidor:

- **Inbox triage con propuestas de IA** — [[2026-1022-inbox-triage-propuestas-ia]]: el "Triage Mode" no envía correos, genera *propuestas* que el humano acepta (borrador de respuesta, propuestas de memoria, plantilla reutilizable, label de auto-clasificación por intención), con historial de hilo, notas de voz transcritas y salida "procesar sin respuesta". Es una postura explícita: la IA propone, el humano manda.
- **Memorias y firmas del creator** — [[2026-1022-modulo-brain-cerebro-memorias-plantillas]]: CRUD de memorias + firma de email + plantillas + dominios de spam + dominio inbound. El competidor no expone nada equivalente.
- **Reuniones completas** — [[2026-1022-modulo-reuniones-booking-video]]: booking público con timezone automático, videollamada, grabación con transcripción, ICS para Google/Outlook/Office 365/Apple y burbuja del clon en las páginas de grabación.
- **Desglose de costes pagador explícito** — [[2026-1022-costes-por-categoria-tenant]]: `categoryCloneResponses` y `categoryIngestion` al tenant, `categoryPlatformOps` a la plataforma. Frente a la "transparencia de uso" del competidor, esto es una política de costes, no un contador.
- **Soporte escalable a humano** — [[2026-1022-soporte-al-cliente-separado-y-escalado]], con retrieval por silo separado y auto-email del ticket.
- **Aviso de gaps al creador** — [[2026-1022-clon-avisar-al-creador-de-gaps]] y [[2026-1022-dashboard-de-insights]]: el clon no solo admite lo que no sabe, lo reporta a quien puede rellenarlo.

El eje honesto del gap no es "MyClone.is tiene más endpoints". Es que **su API es la superficie del competidor, y la nuestra es cero** — así que cualquier comparación por superficie siempre va a perder. La comparación honesta es por capacidad de producto, y en varios ejes vamos por delante. Ver [[myownclone-platform-architecture]] para la anatomía de esa ausencia de API y [[myownclone-strategy-and-vision]] para qué capabilities existen en la visión del founder.

## La superficie de producto del competidor que la tabla no recogía

La tabla de ejes compara API, monetización, voz y widget en abstracto. El material atomizado el 2026-10-22 permite bajar un nivel y ver **cómo está construido** el producto del competidor, y ese nivel cambia la lectura de varias filas.

**El widget es un embed de script externo, no un iframe.** Se distribuye como `https://app.myclone.is/embed/myclone-embed.js` con un objeto de configuración (`mode`, `expertUsername`, `personaName`, `widgetToken`, `position`, `primaryColor`, `bubbleText`, `enableVoice`, `welcomeMessage`, `layout`) e idempotencia de carga. Soporta **tres modos**: `bubble` (default, botón flotante que abre modal), `inline` y `fullpage`. En el plan Free **solo hay `bubble`**: `inline` y `fullpage` exigen Pro+, igual que el `widgetToken` ([[2026-1022-myclone-widget-embed-modos]]). La personalización llega a un nivel de guía de marca: hex por defecto (`#f59e0b` primario, `#fff4eb` fondo), tamaños fijos (modal 420×700, overlay 900×820, radio 16px, burbuja 60px), tres estilos (`guide`/`minimal`/`classic`), toggles de avatar, AI branding y "modo simple" sin animaciones — con **vista previa en vivo** en el panel, que es la fricción de integración que se elimina ([[2026-1022-myclone-widget-personalizacion]]).

Y el token no es una credencial opaca de un solo uso: usa prefijo `wgt_`, es **rotable** (`DELETE /users/me/widget-tokens/{token_id}`) y guarda `name`, `description`, `is_active` y `last_used_at` — es decir, **rastreable por uso**. Y el widget se sirve bajo el dominio propio del creator.

**El transporte es de dos canales, no uno.** El widget habla por **Socket.IO sobre WebSocket** con heartbeat de 25 s, reconexión con backoff exponencial y eventos `message`, `voice` (audio binario), `typing`, `presence` y `notification`, con doble fallback: polling cada 5 s si cae el WebSocket, y servicio desde el mismo dominio si cae el CDN ([[2026-1022-myclone-widget-comunicacion-websocket]]). El texto, en cambio, va por **SSE** (`POST /personas/username/{username}/stream-chat`, patrón Vercel AI SDK) y el audio en tiempo real por **LiveKit**. El OpenAPI no contiene ningún endpoint de socket, lo que apoya la hipótesis de dos canales y deja en el aire la afirmación de que el texto va por Socket.IO.

**El consumo se expone con contadores y fecha de reset.** `GET /tier/usage` devuelve los límites del plan Free con `reset_date` explícito y desglosados por categoría (`raw_text`, `documents`, `multimedia`, `youtube`, `voice`, `text`, `personas`). Los límites verificados: **2 personas** (1 activa), 5 textos raw (50 MB), 3 documentos (150 MB), 3 multimedia (500 MB / 1 h), **500 mensajes de texto al mes**, **10 minutos de voz al mes**, **0 API tokens** (Pro+), solo modo `bubble` y 0 transcripciones de YouTube ([[2026-1022-myclone-limites-plan-free]]). Es un freemium cuyo consumo real (500 mensajes + 10 min de voz) **se agota en minutos** si el embed está en producción: empuja a Pro casi de inmediato, contra un plan más barato propio de 99 €/mes ([[2026-1022-precio-99-mensual]]).

Y aquí está el detalle de modelo de negocio que la tabla no recogía: **`GET /tier/plans` es público, pero `GET,POST /tier/plans` y `PUT,DELETE /tier/plans/{tier_id}` requieren auth** — es decir, **el creator puede crear, editar y borrar planes dentro de su cuenta**. MyClone.is no solo cobra por plan: habilita al creator a revender su clon como producto ([[2026-1022-myclone-tier-plans-usage-api]]). Es el mismo modelo de "marketplace de planes" que documenta [[multi-tenant-saas]], y encaja con su Stripe Connect. La matriz por tier explica además una rareza: `pro` permite 10 dominios propios y `business`, con 30 personas, también — **el límite de dominios no escala con el tamaño del plan**, lo que sugiere que el dominio personalizado es un add-on y no un escalón de precio.

**La ingesta es un pipeline asíncrono con jobs y auditoría.** Los fuentes soportados son siete: LinkedIn, Twitter/X, Website, Documents (PDF, DOCX, XLSX, PPTX), Text, Audio (≤10 MB) y Video (≤200 MB, tope total 500 MB), con la ingesta de YouTube reservada a Pro+ ([[2026-1022-myclone-knowledge-library-fuentes]]). El pipeline expone `POST /scraping/{linkedin,twitter,website}`, `auto-onboard`, `bulk-onboard`, más `GET /scraping/status/{user_id}` y `GET /scraping/audit/{job_id}`; la expertización se muestra en vivo por SSE con `expert-status-stream`; y YouTube tiene subsistema propio en `/voice-processing/*` con reindexado de embeddings ([[2026-1022-myclone-scraping-ingestion-pipeline]]). **`auto-onboard` + `bulk-onboard` es el atajo de mayor apalancamiento**: una sola llamada construye el clon completo desde un username — precisamente el gap de activación más caro del producto propio, donde el onboarding es caso por caso.

**La identidad del clon se parametriza con diez variables, no con un prompt.** La plantilla por defecto ("Expert Digital Persona System Instructions") usa `{name}`, `{role}`, `{company}`, `{description}`, `{introduction}`, `{area_of_expertise}`, `{chat_objective}`, `{thinking_style}`, `{objective_response}` y `{example_responses}`, con un marco de 5 fases (Assessment → Information Gathering → Solution Reasoning → Recommendation Delivery → Experience Integration), límites de alcance, estilo de comunicación y la instrucción **"NO markdown formatting in responses"** ([[2026-1022-myclone-prompt-template-sistema]]). El handoff cuantifica el gap contra nuestro modelo de datos: `CloneConfig` solo tiene `name`, `description`, `personality_tone` y `language` — **faltan `role`, `company`, `introduction`, `area_of_expertise` y `chat_objective` como campos separados** ([[2026-1022-gap-campos-cloneconfig-vs-variables-myclone]]). La consecuencia es precisa: el bloqueo no es el prompt, es que la identidad vive en un prompt monolítico, y sin campos estructurados **no se puede generar una plantilla parametrizada ni versionarla por variables**. La recomendación del handoff es explícita —no copiar el prompt tal cual sino versionar antes que replicar las variables—, y la sintaxis (`{{variable}}` de doble llave frente a `{name}` de una llave) es una normalización barata.

**El acceso al clon se separa de su identidad y se controla por persona.** El clon se consume por **username público + token de sesión**, no por UUID — es lo que permite que un widget embebido en cualquier web solo necesite el username del creator. El control de acceso por persona (`check-access`, `request-access`, `verify-access`, `PATCH /personas/{id}/access-control`) es la primitiva que luego activa monetización y workflows, y los **dominios de email permitidos por creator con verificación** son un mecanismo anti-abuso fino: restringen a qué dominio puede registrarse un visitante para que nadie reclame la identidad de un creator ([[2026-1022-myclone-access-control-por-persona]]). Y el login devuelve un JWT cuyo payload lleva `{sub, email, fullname, account_type: "creator"}` **en claro** — el token es autocontenido y portable, pero auditable por cualquier log del lado cliente ([[2026-1022-myclone-auth-jwt-account-type-creator]]).

El stack, para cerrar: frontend **Next.js 13+ (App Router) + Astro v5.16.11 en la landing**, hosting en **Vercel**, NextAuth.js, Sentry, PostHog y GTM; backend de dominio **Python + Uvicorn sobre AWS** (54.208.x.x / 3.86.x.x, certificado Amazon RSA 2048 M01), con servicios internos por prefijo de ruta — Voyage (`/embeddings/*`), Langfuse, Cartesia, ElevenLabs, LiveKit, Stripe Connect y **Vercel AI SDK** como motor del streaming ([[2026-1022-myclone-stack-tecnologico]]). Es una app **híbrida**: frontend JS en Vercel, backend en AWS autoalojado. Y el dashboard tiene **doce secciones con ruta propia** — Overview, Personas, Knowledge Library, Voice Clone, Conversations, Widgets, Whitelabel, Workflows BETA, Integrations, Access Control, Limits & Usage, Profile — con onboarding self-service en 3 pasos y enlace temporal de 24 h ([[2026-1022-myclone-competidor-arquitectura]]).

La conclusión de este nivel es incómoda para la comparación: **cada pestaña del dashboard tiene superficie de API**, lo que confirma que no es una fachada. Y el stack no es el diferencial —ambas partes usan Next.js, Vercel, NextAuth, PostHog y Sentry—, así que replicar cualquier mejora de instrumentación es barato. El diferencial real del competidor está en **el embed, el pipeline de ingesta y los contadores de uso**, que son producto, no infraestructura.

## Fricciones que quedan para juicio humano

1. **Mapa de competencia desactualizado** — [[2026-1022-solo-personify-compite-de-verdad]] vs [[2026-1022-myclone-verticalizacion-y-transparencia]]: el mapa de `comparisons/myownclone-competitors.md` no menciona a MyClone.is.
2. **Onboarding contradictorio** — el código tiene un funnel de 4 pasos y signup público ([[2026-1022-onboarding-cuatro-pasos-encuestas]]) pero `/registro` redirige a `/contacto` ([[2026-1022-onboarding-manual-sin-self-service]]). Ambos son ciertos en momentos distintos; el estado real del alta no está verificado.
3. **"Ventaja" que puede no ser ventaja** — [[2026-1022-myclone-carece-modos-memories-ni-visitors]] afirma que MyClone.is no tiene modos/memorias, pero su propia lista de endpoints incluye `visitors` y `capture-lead`. El handoff se contradice sobre el alcance de la ventaja.
4. **Prioridad de roadmap en conflicto** — el founder dice MVP primero ([[2026-1022-mvp-salir-al-mercado-pronto]]); el handoff interno marca el versionado de prompts como 🔴 ALTA y primero ([[2026-1022-plan-orden-implementacion-myownclone]]).
5. **Delfi** — el transcript solo sostiene que Delfi "no solamente te responda con lo que tú ya le has puesto de conocimiento"; la nota legacy [[myownclone-vs-delfi]] va más lejos al atribuirle alucinación.

## Certezas

- `solid` (81 átomos): hechos observados directamente (conteos de endpoints, headers HTTP, versiones de framework, código de our own repo).
- `tentative` (27 átomos): inferencias, rutas deducidas de bundles JS, afirmaciones del founder y planes de trabajo.

La línea entre ambos es real y no se ha difuminado: los endpoints "inferidos de JS" del deep-dive de junio están marcados `tentative`; la superficie de 227 endpoints confirmada por OpenAPI está marcada `solid`.
