---
source_url: file:///home/haxth3/myownclone_investigacion_technical.md
ingested: 2026-05-25
sha256: b672dc8299ce0ec94d5073314e89c315d030ca241406b67f8d91793bf011432e
---

     1|# Investigacion Tecnica - myownclone
     2|
     3|## Resumen Ejecutivo
     4|
     5|myownclone es una plataforma SaaS multi-tenant que permite a creadores con marca personal entrenar clones de IA con su propio contenido. La empresa esta registrada como Marea Kiss LLC en Wyoming, EE.UU. El CEO es Eugenio Jose Oller de Torres.
     6|
     7|---
     8|
     9|## 1. DNS y Subdominios
    10|
    11|### IPs publicas de myownclone (direcciones de la red 216.150.x.x):
    12|
    13|| Subdominio         | IPs encontradas                          |
    14||--------------------|------------------------------------------|
    15|| myownclone.com        | 216.150.1.193, 216.150.16.129           |
    16|| api.myownclone.com    | 216.150.16.1, 216.150.16.129           |
    17|| app.myownclone.com    | 216.150.16.129, 216.150.1.65            |
    18|| admin.myownclone.com  | 216.150.1.1, 216.150.1.193              |
    19|| www.myownclone.com    | 216.150.1.1, 216.150.16.1               |
    20|| dashboard.myownclone.com | 216.150.16.193, 216.150.1.193        |
    21|| support.myownclone.com | 216.150.16.1, 216.150.1.1             |
    22|| status.myownclone.com | 216.150.16.1, 216.150.16.193           |
    23|| docs.myownclone.com   | 216.150.16.65, 216.150.1.65            |
    24|
    25|- docs.myownclone.com, status.myownclone.com y dashboard.myownclone.com devolvian 404 en el momento de la consulta
    26|- admin.myownclone.com requiere autenticacion
    27|
    28|---
    29|
    30|## 2. Stack de Infraestructura
    31|
    32|### Frontend
    33|- **Framework:** Next.js (v14+ con turbopack)
    34|- **Hosting:** Vercel (x-vercel-id muestra cdg1::iad1)
    35|- **Deployment:** app.myownclone.com y api.myownclone.com son fronts Vercel con Next.js 14
    36|- **Renderizado:** SSR + RSC (React Server Components)
    37|- **CDN/WAF:** Vercel Edge Network
    38|- **Error tracking:** Sentry (trace disponible en cada pagina, org_id: 4511315838173184, sentry-environment: vercel-production)
    39|- **Analytics:** PostHog (apiHost: https://eu.i.posthog.com, apiKey: phc_tn48YvixjuzzdhbNFLzt9hD7TfwbH2AssUxG2gAiPWei)
    40|- **Fonts:** Poppins + JetBrains Mono (woff2)
    41|- **Estilos:** CSS modular con variables CSS custom (--bg, --fg, --accent, etc.)
    42|- **i18n:** Soporte multi-idioma incorporado (locale routing: /es, /en)
    43|
    44|### Backend / API
    45|- **Lenguaje base:** No confirmado directamente, pero el patron de rutas y la estructura sugiere Next.js API Routes (serverless)
    46|- **Base de datos:** Neon Inc. (PostgreSQL serverless) - segun aviso legal
    47|- **Auth:** NextAuth.js o equivalente con JWT/sesiones - la UI menciona OTP (one-time passwords) para visitantes
    48|- **Hosting API:** Vercel serverless functions bajo api.myownclone.com
    49|
    50|### AI/LLM
    51|- **Modelos:** Anthropic (Claude) + OpenAI - el dashboard de platform admin muestra "Anthropic + OpenAI + email" como coste
    52|- **TTS/STT:** Browser MediaRecorder API + Web Speech API para notas de voz
    53|- **Embedding:** Probablemente OpenAI embeddings o similar para la memoria del clon
    54|- **Clasificadores:** Internos de platform (categoryPlatformOps)
    55|
    56|### Email
    57|- **Envio:** Integracion SMTP/API de email (resolviendo a traves de *@myownclone.com)
    58|- **Inbound:** contacto@myownclone.com es el punto central de inbound hoy por hoy
    59|- **Dominio personalizado:** Soportado pero no activo todavia ("proximamente")
    60|
    61|### Pagos
    62|- **Gateway:** Stripe (mencionado en el admin de tenants: trial, checkout links, cupones 100% off)
    63|- **Planes:** Pro, Scale, Enterprise (con precios diferenciados)
    64|- **MRR tracking:** Hay dashboard de metricas de facturacion y costes
    65|
    66|---
    67|
    68|## 3. Arquitectura de la Aplicacion
    69|
    70|### Rutas publicas descubiertas:
    71|- / (homepage, marketing)
    72|- /en (version inglesa)
    73|- /login
    74|- /registro (signup)
    75|- /legal/aviso-legal
    76|- /legal/privacidad
    77|- /legal/cookies
    78|- /legal/terminos
    79|- /legal/dpa
    80|- /legal/clon-terms
    81|- /contacto
    82|- /sitemap.xml
    83|
    84|### Rutas bloqueadas por robots.txt:
    85|- /admin, /api/, /embed/, /__t/, /c/, /registro/onboarding, /registro/exito
    86|- Versiones inglesas de las mismas
    87|
    88|### Subdominios funcionales:
    89|- **app.myownclone.com** - interfaz del clon para visitantes
    90|- **api.myownclone.com** - API REST + frontend autenticado (creator dashboard)
    91|- **admin.myownclone.com** - panel de administracion de plataforma (multi-tenant)
    92|
    93|### Arquitectura multi-tenant:
    94|- Cada "tenant" es un creador con su propio slug/subdominio
    95|- Subdominios publicos: `[slug].myownclone.com` (unpublished por defecto hasta que el creator publica)
    96|- Dominio personalizado: soportado pero no obligatorio
    97|- Aislamiento entre tenants - el aviso legal lo menciona explicitamente
    98|
    99|---
   100|
   101|## 4. Endpoints y APIs Internas
   102|
   103|### Patrones de API observados en el JS:
   104|A partir del codigo fuente embebido en el HTML, se observan referencias a:
   105|- Proveedores de API para clon responses (backend LLM)
   106|- Endpoints de ingestion de contenido
   107|- Operacion log para audit trail de cada tenant
   108|- Cost tracking por categoria (clone responses, ingestion, platform ops)
   109|- Gestion de sesiones y suplantacion (impersonation) con expiration de 30 min
   110|
   111|### Estructura de costes:
   112|- **categoryCloneResponses** - respuestas del clon (facturable al tenant)
   113|- **categoryIngestion** - ingestion de contenido (facturable al tenant)
   114|- **categoryPlatformOps** - operaciones internas como memoria, embeddings, clasificadores (pagado por myownclone)
   115|
   116|### Auth Flow:
   117|- Login con email/password
   118|- OTP para visitantes anonimos
   119|- Sesiones de suplantacion (impersonation) de 30 min con audit log
   120|
   121|---
   122|
   123|## 5. Modelo de Negocio y Producto
   124|
   125|### Tres modos del clon:
   126|1. **Pedagogia** - ensena con el contenido del creador
   127|2. **Ventas** - recomienda productos
   128|3. **Soporte** - da soporte
   129|
   130|### Funcionalidades descubiertas:
   131|- Inbox/Triage: gestion de inbound emails con IA que propone respuestas en la voz del creador
   132|- Memorias: contexto persistente ensenado al clon
   133|- Plantillas: respuestas reusables que el clon propone
   134|- Etiquetas: clasificacion de tickets
   135|- Booking: sistema de reservas con videollamada integrada
   136|- Grabaciones compartidas: con transcripcion y chat con el clon
   137|- Feedback widget: captura de errores y sugerencias con screenshots
   138|
   139|### Planes y Precios:
   140|- **Pro, Scale, Enterprise** - los tres planes visibles en el admin
   141|- Trial de 30 dias con Stripe (tarjeta obligatoria)
   142|- Cortesias sin tarjeta
   143|- MRR tracking, pagos fallidos, cancelaciones
   144|- Coste desglosado por tenant (responses, words, period cost, lifetime cost)
   145|
   146|---
   147|
   148|## 6. Equipo
   149|
   150|### Representante legal:
   151|- **Eugenio Jose Oller de Torres** - Sole Member de Marea Kiss LLC
   152|- En la app aparece como "Eugenio Oller" (signature placeholder en el admin: "Best,\nEugenio Oller\nCEO at myownclone")
   153|
   154|### Compania:
   155|- **Marea Kiss LLC** - Wyoming, EE.UU.
   156|- Domicilio: 30 N Gould St, Ste R, Sheridan, WY 82801
   157|- Email general: contacto@myownclone.com
   158|- Email DPO: privacy@myownclone.com
   159|
   160|### Tech stack del equipo (inferido):
   161|- Next.js/React (el producto entero esta construido con el)
   162|- PostgreSQL (Neon)
   163|- Vercel (deployment)
   164|- Sentry (monitoring)
   165|- PostHog (analytics)
   166|- Stripe (payments)
   167|- SFTP para hosting? No confirmado
   168|
   169|---
   170|
   171|## 7. Hallazgos Clave
   172|
   173|1. **Todo el stack es serverless/managed**: Vercel (frontend+API), Neon (DB). No hay servidores propios visibles.
   174|
   175|2. **Arquitectura multi-tenant madura**: Aislamiento completo entre creators, con panel de admin de plataforma, suplantacion de usuarios, audit log, y tracking de costes por tenant.
   176|
   177|3. **Modelo de costes por uso**: Cada tenant tiene costos desglosados por categoria (respuestas del clon vs ingestion vs ops). Parece un modelo de coste + margin.
   178|
   179|4. **Stack moderno y completo**: Next.js 14, React 18, TypeScript (inferido por el uso de modulos), Tailwind-style CSS (variables), Sentry, PostHog, Stripe.
   180|
   181|5. **Producto en beta activo**: Hay signups, MRR, pagos fallidos, cancelaciones - la plataforma tiene trafico real.
   182|
   183|6. **Sin documentacion publica de API**: No hay docs.myownclone.com ni api.myownclone.com/public-api. La API es completamente privada.
   184|
   185|7. **Euge Oller no tiene repos públicos en GitHub** relacionados con myownclone - o estan en cuenta privada o la empresa no ha publicado codigo open source.
   186|
   187|---
   188|
   189|## Archivos generados
   190|
   191|- `/home/haxth3/myownclone_investigacion_technical.md` - este informe