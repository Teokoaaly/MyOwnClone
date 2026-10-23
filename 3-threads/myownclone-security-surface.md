---
id: thread-myownclone-security-surface
type: thread
updated: 2026-10-23
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md, sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]]", "[[2026-1023-ai-security-tools-taxonomia-15-categorias]]"]
---

# Thread — Superficie de ataque de MyOwnClone

Síntesis de los átomos de seguridad derivados del informe de vulnerabilidades verificadas (2026-05-25) y del recon de frontend. Todos los hallazgos están trazados a `raw/articles/myownclone-vulnerabilities-confirmed.md` y corroborados de forma independiente por el scrape público.

> **⚠️ Actualizado 2026-10-22 — la re-verificación en vivo invalida la mitad de este thread.**
> Un `curl` contra el sitio desplegado el 2026-10-22 (fuente: `0-raw/2026-10-22-myownclone-live-reverification.md`) encuentra que el producto se ha redesplegado: ahora se sirve desde nginx autoalojado, con CSP, headers de seguridad y sin CORS, y con la fuga de código del panel **cerrada**. Los hallazgos de mayo son historia del despliegue anterior, no del actual. La sección "Prioridad sugerida" de abajo está obsoleta y se reemplaza por "Prioridades tras la re-verificación". Ver [[myownclone-estado-live-2026-10]] para la tabla completa de deltas.

## El hallazgo principal

Un GET sin sesión a `/admin` devuelve **HTTP 200 con 266 KB de HTML** donde el payload RSC ya contiene el código del panel de administración (`AdminPlatformTenants`, `AdminPlatformInbox`, `AdminPlatformResumen`, `AdminPlatformSpam`, `AdminPlatformFeedback`, `AdminImpersonationBanner`) antes de que se ejecute el redirect. El redirect es un `<meta http-equiv="refresh">` en cliente, no un 307 de servidor.

Consecuencia: la barrera de auth del back-office no se aplica en servidor. 81+ referencias a features internas quedan descargables sin sesión — incluyendo el vocabulario completo de estados de suscripción y el módulo de impersonación.

Ver [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]] y [[2026-1022-admin-rutas-bilingues-sin-subdominio]].

Fricción abierta: el scrape de junio registra un 307 `NEXT_REDIRECT` en `/admin`, y el informe de mayo registra 200 con payload. Son observaciones de fechas distintas, o un cambio de comportamiento. **No resuelto — requiere re-verificación con curl antes de actuar.** La nota [[2026-1022-dns-superficie-publica-myownclone]] también afirma que `/admin` responde 200 con autenticación, lo que no encaja con ninguna de las dos lecturas.

## Hardening HTTP ausente

Verificado por curl, no inferido:

| Ausencia | Átomo |
|---|---|
| CSP (y por tanto mitigación de XSS) | [[2026-1022-ausencia-csp-xss-sin-mitigacion]] |
| Headers de seguridad (HSTS, X-Frame-Options, Referrer-Policy…) | [[2026-1022-sin-headers-de-seguridad]] |
| Rate limiting | [[2026-1022-sin-rate-limiting]] |
| CORS restrictivo en login/registro (wildcard) | [[2026-1022-cors-wildcard-en-login-y-registro]] |
| `HttpOnly`/`Secure` en la cookie `NEXT_LOCALE` | [[2026-1022-cookie-next-locale-sin-httponly-ni-secure]] |

Fricción con la nota legacy `entities/myownclone.md`, que describe "aislamiento completo". No es compatible con la ausencia total de hardening HTTP verificado por curl.

## Superficie lesser-known

- **DSN de Sentry público** — [[2026-1022-sentry-dsn-publico-contamina-dashboards]]: la clave de ingestión es pública por diseño, pero eso permite spamming de eventos falsos en nuestro dashboard y agotar la quota. Fricción adicional: el release hash difiere entre los dos informes para la misma fecha, lo que sugiere que uno de los dos tomó una build distinta.
- **Códigos de chunk débiles** y Turbopack experimental en producción — [[2026-1022-frontend-nextjs-vercel-sentry-posthog]].
- **Superficie oculta en robots.txt** — [[2026-1022-superficie-oculta-robots-txt]]: prefijos bloqueados que devuelven 404 sin marca, más el meta-refresh de 260 KB en `/registro`.
- **Email inbound sin dominio propio** — [[2026-1022-email-inbound-contacto-sin-dominio-propio]]: una única casilla `contacto@` en lugar del comodín `*@` que sí implementa el código ([[2026-1022-admin-bandeja-global-y-spam]]).

## Nota de fecha

Los tres subdominios públicos sirven el **mismo deployment** (ver [[2026-1022-dns-superficie-publica-myownclone]]), y `api.` es un alias, no una API real: los 404/405 en `/api/` confirman que no hay API Routes. La API real es Flask en el puerto 5001, expuesta por el frontend vía Server Actions ([[2026-1022-mutaciones-rsc-sin-api-rest]]).

## Superficie legal y de datos — lo que el hardening no cubre

La superficie pública se cierra con dos átomos que no son de seguridad HTTP pero que sí exponen datos:

- [[2026-1022-superficie-legal-publica-dpa-clon-terms]] — el footer expone seis documentos legales: Aviso Legal, Privacidad, Cookies, Términos, DPA y "Clone Terms". Cuatro tienen versión inglesa en `/en/legal/*`; el Aviso Legal **solo existe en español**. La entidad legal es Marea Kiss LLC (Wyoming, según [[2026-1022-euge-oller-clon-personal-en-delphi]]) y la operación es español-primero ([[2026-1022-i18n-es-first-jurisdiccion-es]]): la combinación "sede en Wyoming + aviso legal solo en español + GDPR" es un punto que merece revisión jurídica, no una conclusión.
- [[2026-1022-superficie-oculta-robots-txt]] — `robots.txt` bloquea prefijos que no están en el sitemap: `/embed/`, `/__t/`, `/c/`, más los flujos de onboarding. El scrape confirma que `/embed/`, `/__t/` y `/c/` devuelven 404 y `/api/` 404 o 405, así que hoy no exponen nada — pero la superficie existe en el mapa y conviene saber qué es cada prefijo antes de que alguien lo sirva.

Un detalle de la fuga de `/admin` que merece atención operativa: el payload expone el vocabulario completo de estados de suscripción (active, trialing, past_due, unpaid, canceled, incomplete, complimentary, suspended, deleted) y los nombres de los módulos de impersonación. Eso no es solo "código fuente filtrado": es un **mapa de la API interna del back-office**, gratis, para cualquiera que haga un GET.

## El mapa del campo: qué hay disponible hoy para un SaaS con IA multi-tenant

> **Actualizado 2026-10-23.** Esta sección no re-verifica nada del producto: resume lo que el campo de herramientas de seguridad para IA ofrece hoy, para poder decidir qué NO construir y qué SÍ merece una dependencia. Viene de 15 átomos atomizados el 2026-10-23 a partir de la lista curada `awesome-ai-security-tools` (CC0, README generado, ver [[2026-1023-ai-security-tools-repo-cc0-readme-generado-y-metricas-estaticas]]).

La lista indexa **377 herramientas en 15 categorías de problema** más **45 listas "awesome"** relacionadas (422 entradas con marcador de lista). Las cifras por categoría son **un conteo propio del lector sobre los encabezados del README**: no están publicadas como métricas por el repo, así que se citan como lectura del documento, no como dato del autor (nota de método en [[2026-1023-ai-security-tools-taxonomia-15-categorias]]).

| Categoría | Entradas | Qué cubre | ¿Aplica a MyOwnClone? |
|---|---|---|---|
| AI Agent & Coding-Agent Security | 101 | Agentes de código: escáneres de skills/MCP, reglas y benchmarks, y **runtime protection** (61 de las 101) | **Sí, parcialmente** — la subsección de runtime es transferible; el resto está orientado a agentes de código, no a un endpoint de chat (ver [[2026-1023-ai-security-tools-agente-como-categoria-dominante]]) |
| LLM Red-Teaming & Guardrails | 68 | Prompt injection, jailbreak, fuga de datos, tool misuse **en la frontera del modelo** | **Sí, con una distinción** — cubre la capa de modelo, no el guardarrail de retrieval del clon, que es otra cosa ([[2026-1023-ai-security-tools-guardarrail-de-retrieval-no-es-guardarrail-de-seguridad]], [[2026-1022-guardarrail-no-alucinar]]) |
| CTF/Exploit/Bug-Bounty Agents & Benchmarks | 27 | Benchmarks de CTF, agentes de explotación y campos de bug bounty | No |
| Pentest & Red-Team Agents | 29 | Servidores MCP ofensivos (150 y 200+ herramientas) y agentes autónomos | No como producto — **sí como amenaza**: el endpoint público es un objetivo automatizable ([[2026-1023-ai-security-tools-servidores-mcp-ofensivos-con-200-herramientas]]) |
| AI/ML Supply Chain & Model Security | 24 | Escaneo de artefactos de modelo, SBOM de IA, emisión de claves | **No todavía** — el clon consume modelos de proveedor, no distribuye pesos ([[2026-1023-ai-security-tools-clasificadores-y-llms-de-seguridad-con-licencia-no-permisiva]]) |
| AI-Powered SAST | 22 | "Skills" de revisión de código para agentes de código | **No** — y además el README admite que el más popular es "workflow skill, not a standalone scanner" ([[2026-1023-ai-security-tools-sast-ia-como-skill-no-como-scanner]]) |
| AI-Powered Recon & Narrow ML Tools | 20 | Reconocimiento y utilidades ML estrechas | No |
| Reverse Engineering | 20 | IDA, Ghidra, binarios bridged a MCP | No |
| LLM-Driven Fuzzing | 14 | Fuzzing dirigido por LLM | No |
| Threat Intelligence | 13 | Fuentes de inteligencia | No |
| Cloud/IaC/DFIR/OSINT/Phishing | 13 | Nubes, DFIR, phishing | No |
| Log Analysis/SIEM/SOC Triage | 10 | Triaje de logs y SIEM | No por ahora, pero es la categoría que el producto necesitaría al instrumentar ([[2026-1022-gap-observabilidad-prompts-langfuse]]) |
| Autotriage of Security Findings | 7 | Filtrado de hallazgos de otros escáneres | **Sí, con una condición**: presupone la observabilidad que el clon no tiene ([[2026-1023-ai-security-tools-autotriage-de-hallazgos-con-ia]]) |
| LLM Honeypots & Deception | 6 | Señuelos con LLM para delatar al atacante | Marginal y barato; MCP aparece aquí como protocolo honeypot ([[2026-1023-ai-security-tools-honeypots-llm-y-decepcion-6-entradas]]) |
| AI-Powered Threat Modeling | 3 | Modelado de amenazas con IA | No como dependencia; la categoría más pequeña frente a las 101 de agentes dice dónde está el presupuesto del campo |

El patrón de fondo: la categoría dominante está orientada a **agentes de código con permisos**, no a agentes conversacionales. El clon vive en otro sitio —IA enteramente en servidor ([[2026-1022-ia-y-auth-totalmente-servidor]]), un único canal de escritura (Server Actions, [[2026-1022-mutaciones-rsc-sin-api-rest]]) y documentos de biblioteca controlados por el usuario, que es la misma categoría de "datos no fiables" que las skills de un agente ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]).

### Tres fricciones para juicio humano

Las tres son contradicciones entre lo que dice el campo y lo que este thread ya tenía registrado del producto. Ninguna se auto-resuelve: están para decisión de una persona.

1. **"Aislamiento completo entre tenants" vs. aislamiento que el campo califica de incompleto.** La nota de entidad afirma aislamiento completo entre tenants; el aislamiento se observa a nivel de datos, no de superficie HTTP ([[2026-1022-ausencia-csp-xss-sin-mitigacion]]). Pero la industria califica de forma rutinaria sus propias afirmaciones de aislamiento — "shared-kernel containers are not a microVM boundary", "exfiltration prevention is explicitly out of scope" — porque aislamiento de runtime y aislamiento de datos son dos cosas distintas y verificables por separado ([[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]). O "aislamiento completo" describe solo filas en base de datos y el término se está usando con más fuerza que la evidencia, o hay un límite de runtime no documentado.
2. **Telemetría por defecto con ID persistente vs. DSN público como canal de escritura no autenticado.** El listado trata la telemetría activada por defecto con opt-out documentado como práctica normal en herramientas que manejan código y prompts ([[2026-1023-ai-security-tools-telemetria-activa-por-defecto]]); la DSN de Sentry del clon es, según [[2026-1022-sentry-dsn-publico-contamina-dashboards]], un canal de escritura no autenticado que permite enviar eventos falsos. O la DSN es un descuido de configuración (y conviene arreglarlo igual), o "telemetría por defecto" solo es aceptable cuando el identificador no permite escribir en el sistema de la víctima.
3. **La capa de autotriage presupone la observabilidad que falta.** El campo construyó una categoría entera para filtrar y verificar la salida de un detector antes de que llegue a un humano ([[2026-1023-ai-security-tools-autotriage-de-hallazgos-con-ia]]); el clon no tiene observabilidad de prompts ni evaluación de calidad ([[2026-1022-gap-observabilidad-prompts-langfuse]]). O la ausencia es menor porque no hay volumen de hallazgos que filtrar, o es exactamente el hueco que impide auditar el propio pipeline de calidad.

### Límites honestos de esta fuente

- Es una **lista curada**, no una auditoría del producto ni un escáner. El propio README aplica un patrón editorial consistente de advertencia por entrada — "heuristic", "not a guarantee", "project-reported", "not independently reproduced" — y la entrada más popular de la categoría de SAST se autodescribe como skill, no como escáner ([[2026-1023-ai-security-tools-aviso-de-no-es-un-escanner-como-patron-editorial]]). La fuente no verifica nada por sí misma.
- Sus **métricas son estáticas**: las estrellas y las fechas de último commit son snapshots declarados como tales, con la entrada más reciente refrescada el 2026-10-21 ([[2026-1023-ai-security-tools-repo-cc0-readme-generado-y-metricas-estaticas]]). "Popularidad = salud" no se puede leer de aquí.
- El README **no se escribe a mano**: se genera desde `data/sections.json` validado por un esquema, lo cual sí es una buena noticia — las cifras citadas son reconstruibles.
- Y el patrón de postura del campo es **monitor-only y fail-open** por defecto: bloqueo opt-in, monitor por defecto, fallos que pasan ([[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]). Copiar una de estas herramientas sin instrumentación es copiar la parte fail-open sin la parte fail-closed.

### Señales de estructura de mercado (no de riesgo inmediato)

Dos datos que no son un hallazgo del clon pero que condicionan decisiones de dependencia:

- **Licencias.** Cinco modelos clasificadores de prompt injection, tres gated o con licencia no permisiva; siete "specialty security LLMs" con licencias Llama 3.1 Community, restrictivas o bases *abliterated*. La disponibilidad real de un clasificador está detrás de una puerta de acceso o de una licencia, así que es una decisión de producto, no un `pip install` ([[2026-1023-ai-security-tools-clasificadores-y-llms-de-seguridad-con-licencia-no-permisiva]]).
- **Consolidación.** OpenAI anunció la adquisición de `promptfoo` en marzo de 2026; el proyecto sigue en MIT pero el README pide "track governance". El estándar de facto de la categoría de red-teaming de LLM pasa a tener un único mantenedor corporativo detrás: el gobierno de esa dependencia puede cambiar aunque la licencia no ([[2026-1023-ai-security-tools-promptfoo-adquisicion-openai-marzo-2026]]).

## Prioridades tras la re-verificación (2026-10-22)

La lista de mayo —mover la auth de `/admin` al servidor, añadir CSP, añadir rate limiting— ya no describe la realidad. Reordenada contra el estado verificado:

1. **Rate limiting en login/registro y email inbound — sigue pendiente.** Es el único hallazgo de hardening de mayo que sobrevive. Verificado: 12 peticiones consecutivas a `/login` → doce `200`; 15 a `/api/clones` → quince `401`; ningún `429`. Matiz: el bundle ya contiene `"rateLimit": "Too many requests. Please wait a moment."`, así que la feature existe en cliente y no está conectada al enforcement de servidor. Es un trabajo de conexión, no de diseño. Ver [[2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error]].
2. **Decidir qué hacer con los 238 strings i18n del namespace `admin` que siguen en el bundle público.** La fuga de *código* está cerrada; la de *vocabulario* no: impersonación (incluido "Copy this token and use it in the Authorization header to impersonate the tenant"), `audit_log`, `courtesy credits`, estados de suscripción. La landing no lo lleva, las páginas de clon y `/registro` sí. Separar el bundle de i18n por rol es la solución limpia. Ver [[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]].
3. **Arreglar el contrato HTTP del catch-all.** Toda ruta de un solo segmento devuelve `200` con la plantilla de chat, incluidos `robots.txt` y `sitemap.xml`. No hay fuga de rutas internas —bien— pero no hay sitemap para los buscadores y el código de estado miente. Ver [[2026-1022-live-verify-robots-sitemap-y-404-como-catchall]].
4. **Revisar la afirmación de hosting del Aviso Legal.** El aviso dice Vercel Inc. y Neon Inc.; el servidor es nginx autoalojado desde `212.227.169.99`. Desajuste de cumplimiento. Ver [[myownclone-estado-live-2026-10]].

Lo que ya está hecho y no hay que volver a pedir: auth de servidor en las subrutas de admin (`307` a `/login`), CSP (dos, una de ellas estricta en `/admin` y `/registro`, con `frame-ancestors 'none'`), HSTS con `includeSubDomains; preload`, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy`, `Permissions-Policy`, y la eliminación del CORS `*`.

## Prioridad sugerida (mayo 2026 — superada, se conserva como registro)

1. Mover la barrera de auth de `/admin` al servidor. Es la fuga más grande, verificada y con impacto directo en impersonación y gestión de tenants.
2. CSP como mínimo report-only, luego estricta.
3. Rate limiting en login/registro y en los endpoints de email inbound.

Los tres son cambios de una tarde en el código, no de rediseño. Nada de esto se ha ejecutado: este thread documenta, no modifica.
