---
id: myownclone-estado-live-2026-10
type: thread
updated: 2026-10-23
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[myownclone-security-surface]]", "[[myownclone-platform-architecture]]", "[[myownclone-gtm-monetization-roadmap]]", "[[myownclone-vs-myclone-is]]"]
---

# Thread — Estado vivo de MyOwnClone (verificado 2026-10-22)

Este thread existe por un motivo concreto: **el corpus OSINT atomizado el 2026-10-22 describe un producto que ya no está desplegado**. La re-verificación con `curl` del 2026-10-22 (fuente: `0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md`) encuentra diferencias en hosting, superficie DNS, hardening, superficie de API, onboarding, precios, identidad legal y diseño. No es un matiz: es otra generación del producto.

Mientras no se resuelva, la regla de lectura del vault es: **los átomos con `sources:` en `raw/articles/` describen la generación de mayo–junio 2026 y sirven como historial, no como estado actual.** Los átomos `2026-1022-live-verify-*` y `2026-1023-live-verify-*` sí describen el presente.

## La tabla que explica casi todo

| Átomo de mayo (histórico) | Estado vivo 2026-10-22 | Átomo actual |
|---|---|---|
| Vercel Edge `cdg1::iad1` | nginx 1.28.3 en `212.227.169.99`, cert Let's Encrypt del 2026-10-14 | [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] |
| 9 subdominios en 216.150.x.x | 2 hosts (apex + www); los otros 7 sin DNS | [[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]] |
| Cero CSP, sin headers de seguridad, CORS `*` | 2 CSPs (una estricta), HSTS, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy; cero CORS; sin `Set-Cookie` en `GET /login` | [[2026-1022-live-verify-csp-y-headers-ahora-presentes]] |
| `/admin` filtra 266 KB de `AdminPlatform*` | `/admin` sirve la página de clon; cero `AdminPlatform*`; subrutas con 307 a `/login`; `/admin/platform/tenants`, `/admin/clon`, `/admin/cerebro` → 404; `/dashboard` → 307 `/resumen`, `/dashboard/resumen` → 404 | [[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]] |
| No hay API REST | `/api/clones`, `/api/inbox`, `/api/clones/x/prompts` → 401 JSON | [[2026-1022-live-verify-superficie-rest-api-inexistente-antes]] |
| `/registro` → meta-refresh a `/contacto` | formulario real de alta con magic link + Google; el onboarding ofrece `slugSuffix: ".myownclone.yourdomain.com"` y `urlSuffix: ".myownclone.com"` | [[2026-1022-live-verify-alta-y-precios-ya-publicos]] + [[2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio]] |
| Sin precios, sin docs | landing con sección "Pick your plan." (basic/pro/scale/enterprise) | [[2026-1022-live-verify-alta-y-precios-ya-publicos]] |
| Seis documentos legales | una sola página `/legal` de diez secciones | [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]] |
| `robots.txt` con prefijos bloqueados | `robots.txt` no se sirve: catch-all 200 con el slug como `<h1>` | [[2026-1022-live-verify-robots-sitemap-y-404-como-catchall]] |
| Sentry + PostHog | sin identificadores en el HTML ni en los chunks: ni `sentry.io`, ni `posthog`, ni `sentry-public_key`, ni `sentry-org_id`, ni `phc_*`, ni `eu.i.posthog.com` | [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] + [[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]] |
| Poppins + `myownclone-theme` + `--brand-lime` | DM Sans + `localStorage["theme"]` + `--bg-page`/`--text-primary`/`--color-accent-violet` | [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]] |
| Español-primero, `og:locale: es_ES` | `/`, `/es` y `/en` devuelven `lang="en"` y cuerpos idénticos | [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]] |
| Marea Kiss LLC (Wyoming), rep. Eugenio Oller | Myownclone llc, 30 N Gould St Ste R Sheridan WY, rep. Jacinto Guzman II | [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]] |
| Aviso Legal coherente con la infraestructura | sección III sigue declarando hosting en **Vercel Inc.** (440 N Barranca Ave #4133, Covina, CA 91723) y BD en **Neon Inc.**, con el documento fechado el 11 de mayo de 2026 | [[2026-1023-live-verify-aviso-legal-aun-declara-vercel]] |
| Panel de back-office sin regla de acceso documentada | el Aviso Legal declara que el **panel de administración del creador requiere suscripción activa**, que el visitante del clon va **anónimo o con OTP por email**, y que ley aplicable y jurisdicción son **España** (LSSI-CE) | [[2026-1023-live-verify-panel-del-creador-condicionado-a-suscripcion]] |
| Back-office sin métricas de negocio visibles | el i18n vivo expone `mrrCostsMarginLegend: "MRR / Costs / Margin"`, `costs30d: "Costs (30d)"`, estados de tenant `tenant`/`trial`/`suspended`, `stripeCustomer`/`stripeSubscription`/`subscriptionStatus`, planes `free`/`basic`/`pro`/`scale`/`enterprise` y 9 secciones del dashboard del creador (`biblioteca`, `cerebro`, `inbox`, `productos`, `reuniones`, `analiticas`, `facturacion`, `configuracion`, `resumen`) | [[2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant]] |
| Tres silos: enseña / soporte / **recomienda productos** | el bundle nombra los modos `pedagogy`, `sales`, `support` (botones "Learn" / "Support" / "Sales") y el Aviso Legal repite "pedagogía, ventas y soporte"; guardarrail vigente `"notEnoughInfo": "I don't have enough information to answer this question accurately. Would you like me to notify the team?"` | [[2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle]] |
| Sin rate limiting | **sin rate limiting todavía** (12× login 200, 15× API 401) | [[2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error]] |

## Lo que sí sobrevive

Tres cosas del corpus de mayo siguen vivas en la versión actual, y por eso no todo el trabajo de mayo está obsoleto:

**El rate limiting sigue ausente.** Es el único hallazgo de hardening que sobrevive al redespliegue. [[2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error]] lo confirma con 12 y 15 repeticiones. Pero hay un matiz nuevo: el bundle contiene la cadena `"rateLimit": "Too many requests. Please wait a moment."`, o sea la feature está implementada en cliente y no conectada al enforcement de servidor. Y el objetivo alcanzable sin sesión son login y registro — justo donde el abuso de magic link y el brute force importarían.

**El chat público sigue roto.** `POST /api/myownclone/public/clones/x/chat` → 404. Coincide con el bug conocido `myownclone_public_bp` no registrado. La función central del producto sigue sin endpoint accesible desde fuera.

**El vocabulario interno del back-office sigue viajando al cliente.** La fuga ya no es el *código* del panel sino el *vocabulario*: 238 cadenas i18n del namespace `admin` — impersonación con su token y su motivo de auditoría, `audit_log`, `courtesy credits`, estados de suscripción — llegan en el payload de cualquier página de clon y en `/registro`. La landing no lo lleva. Ver [[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]].

## El cambio de arquitectura que cambia la lectura

Hay una discrepancia que conviene decir en voz alta porque atraviesa todas las threads: **el Aviso Legal publicado dice que el sitio está alojado en Vercel Inc.** (440 N Barranca Ave #4133, Covina, CA 91723) y que la base de datos está operada por Neon Inc. — pero el sitio se sirve desde nginx autoalojado. El aviso legal tiene fecha de *11 de mayo de 2026*, anterior al redespliegue. Dos lecturas posibles: (a) el aviso legal está desactualizado respecto a la infraestructura real, lo cual es un problema de cumplimiento por sí mismo; (b) la infraestructura de octubre es un cambio transitorio — un ensayo de self-hosting — que todavía no se ha reflejado en los papeles. Ninguna de las dos se puede decidir desde fuera. Es una pregunta para el founder, y es probablemente la pregunta más urgente del vault. Ver [[2026-1023-live-verify-aviso-legal-aun-declara-vercel]].

## Un cambio de producto con lectura ambigua

El catch-all de un solo segmento es el hallazgo más confuso. Bueno: `/admin`, `/pricing`, `/robots.txt` y `/zzz-random-99` devuelven todos 200 con la misma plantilla de chat de clon, así que no hay fugas por rutas ocultas ni enumeración de rutas internas. Mal: **todo 404 de una sola palabra devuelve 200**, lo que rompe el contrato HTTP, hace que `robots.txt` y `sitemap.xml` no existan para los buscadores, y significa que buena parte de la lectura de junio —"el panel vive en `/admin`"— era en realidad una interpretación errónea de un catch-all. Para un producto cuyo valor es que la gente comparte clones públicos, que no exista un sitemap es un problema de distribución, no de estética.

## Lo que la re-verificación del 2026-10-23 añadió al cuadro

La segunda pasada de captura (archivada en `0-raw/archive/`) no repitió lo ya medido: abrió lo que la primera había dejado sin muestrear — el Aviso Legal leído como documento de reglas de negocio, el bundle buscado por identificadores de instrumentación, el formulario de alta leído como oferta de producto, y el i18n del back-office leído como vocabulario de plataforma. Lo que salió:

**El Aviso Legal no es solo identidad: es la fuente de tres reglas de negocio que el vault no tenía registradas.** [[2026-1023-live-verify-panel-del-creador-condicionado-a-suscripcion]]: (1) el acceso al panel de administración del creador **requiere suscripción activa**; (2) el visitante de un clon publicado interactúa **anónimo o identificándose con un OTP enviado a su email**; (3) la ley aplicable y la jurisdicción son **España** (LSSI-CE), sobre una LLC de Wyoming y una base de datos en Neon. La versión española es la única operativa; la inglesa sigue siendo un placeholder. Esto convierte el back-office en un producto **de pago**, no en una beta cerrada.

**El Aviso Legal se contradice a sí mismo con la infraestructura real.** [[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]: la sección "III. Hosting y prestadores de servicio" sigue nombrando a **Vercel Inc.** y **Neon Inc.**, con fecha de última actualización 11 de mayo de 2026, mientras el sitio lo sirve nginx autoalojado. Matiza la lectura "la capa legal ha sido reconstruida": la identidad (entidad, domicilio, representante, emails) sí; el clausulado de infraestructura no se tocó tras la migración de octubre.

**La instrumentación de terceros desapareció del bundle, no solo del HTML.** [[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]] amplía la fila Sentry+PostHog: en el HTML y en los chunks JS no aparecen ni `sentry.io`, ni `posthog`, ni `sentry-public_key`, ni `sentry-org_id`, ni claves `phc_*`, ni `eu.i.posthog.com`. Desaparece con ellos la DSN pública `6b2d7ed6999454df87ccf844aa85ba70` y el entorno `vercel-production` del corpus de mayo. Es un indicio fuerte de reconstrucción de frontend: reubicar hosting no elimina un SDK.

**El onboarding vende un dominio propio que el backend no resuelve.** [[2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio]]: los placeholders `slugSuffix: ".myownclone.yourdomain.com"` y `urlSuffix: ".myownclone.com"` aparecen en la UI de alta self-service, junto a los cuatro pasos ya verificados (`name` → `personality` → `language` → `confirm`). El control está expuesto al cliente aunque la resolución (DNS, SSL) siga sin existir. Frente a MyClone.is, que ya expone `POST /custom-domains` con verificación y cuota por tier, MyOwnClone muestra el hueco en el formulario sin cerrarlo.

**El back-office sigue siendo un producto de plataforma, con métricas de negocio.** [[2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant]] confirma en la build desplegada el vocabulario completo: `MRR / Costs / Margin`, `Costs (30d)`, estados de tenant `tenant`/`trial`/**`suspended`** (este último, nuevo para el vault), `stripeCustomer`/`stripeSubscription`/`subscriptionStatus`, los cinco planes (`free`, `basic`, `pro`, `scale`, `enterprise`) y las nueve secciones del dashboard del creador. El código de los módulos ya no se sirve, pero el mapa de negocio sigue siendo legible sin sesión.

**El tercer modo se llama `sales`, no "recomienda".** [[2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle]]: el bundle nombra `pedagogy`, `sales` y `support`, con `Sales` entre los tres botones del grupo "Conversation mode" (Learn / Support / Sales) de la página del clon, y el Aviso Legal repite "tres modos de comportamiento (pedagogía, ventas y soporte)". El guardarrail vigente es `"notEnoughInfo": "I don't have enough information to answer this question accurately. Would you like me to notify the team?"` — convierte un gap de conocimiento en acción (notificar al equipo).

**Detalles que enriquecen átomos ya existentes, sin cambiar su veredicto:** la sección de precios vive en la landing `/` y **no tiene URL propia** (`/pricing` cae en el catch-all de slug y devuelve la página de chat), sin importes `€` en el HTML de servidor; el árbol de plataforma desapareció del back-office (`/admin/platform/tenants`, `/admin/clon`, `/admin/cerebro` → 404) mientras `/dashboard` → 307 a `/resumen`; no se observó ninguna cabecera `Set-Cookie` en `GET /login`; el módulo `feedbackWidget` sigue compilado en el bundle aunque sus rutas de gestión ya no respondan; y el triage del inbox expone su descripción comercial viva, `automationDesc: "AI triage for incoming emails, classify intent, suggest replies and recommend products."` — es decir, el triage también **recomienda productos**, lo que conecta soporte con el silo comercial.

## Impacto por thread

- **[[myownclone-security-surface]]** — reescrito: el hardening HTTP ausente ya está implementado, la fuga de código del panel está cerrada, y las prioridades 1 y 2 de la lista de mayo están cumplidas. Queda el rate limiting y queda decidir qué hacer con los 238 strings de admin en el bundle público.
- **[[myownclone-platform-architecture]]** — las secciones sobre hosting, superficie de API, stack de diseño e instrumentación describen la generación anterior. Lo que se mantiene vigente es la arquitectura de dos repos (Flask + Next.js) descrita en el código, que es un hallazgo del checkout local, no del sitio desplegado.
- **[[myownclone-gtm-monetization-roadmap]]** — la sección de onboarding y funnel queda desactualizada: el alta self-service está desplegada y la landing tiene precios. La parte de intención comercial (lo que el founder *quiere* que sea) sigue válida porque no depende del despliegue.
- **[[myownclone-vs-myclone-is]]** — la comparación de superficie técnica queda invalidada en lo que se refiere al hosting, la API y el panel; la comparación de *capacidades de producto* se sostiene porque procede del código y del material del founder, no del HTML servido.

## Fricciones abiertas

1. **El Aviso Legal contradice la infraestructura real** (Vercel en el papel, nginx en el servidor). Requiere decisión del founder: actualizar el aviso o revertir el despliegue. La re-verificación del 2026-10-23 acota el alcance: no es un problema de identidad (entidad, domicilio, representante y emails sí están al día) sino del **clausulado de infraestructura**, que quedó intacto tras la migración de octubre — [[2026-1023-live-verify-aviso-legal-aun-declara-vercel]].
2. **¿Qué versión del producto es la buena?** La nueva tiene hardening, alta self-service, precios y API. La antigua tiene la arquitectura de dos repos documentada, el panel con impersonación, bookings y triage. ¿Se migró el panel a la nueva versión o la nueva es un front reconstruido sobre el mismo backend? Ninguna de las dos páginas expone la verdad completa.
3. **El chat público 404** es el bug conocido `myownclone_public_bp` y es la función central del producto. Debería ser la prioridad de código por encima de todo lo que este thread discutió.
4. **La localización ha desaparecido.** `/es` no cambia el idioma, todo es `lang="en"`, y el namespace legal inglés es un placeholder que dice literalmente que debe revisarse con un abogado antes de un lanzamiento público. Para una operación española, esto es una regresión.
5. **Los 238 strings de `admin` en el bundle público**: cabe decidir si es Acceptable (el vocabulario no es el código) o si conviene un bundle de i18n separado por rol. Con el 2026-10-23 el objeto es mayor: el vocabulario no solo nombra impersonación y planes, sino **métricas de plataforma** (`MRR / Costs / Margin`, `Costs (30d)`) y el estado `suspended` — [[2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant]].
6. **El marketing y el producto no dicen lo mismo del tercer modo.** El copy público habla de "enseña / da soporte / **recomienda tus productos**"; el código implementa `pedagogy` / `support` / **`sales`**, con botón "Sales" en la interfaz del clon y mención en el Aviso Legal. No es un error del corpus: es una divergencia entre discurso y modelo de datos, y cambia la lectura comercial del producto — [[2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle]].
7. **El dominio propio se ofrece en el alta pero no existe como capacidad.** El formulario de alta muestra `.myownclone.yourdomain.com` al usuario final, mientras el backend no verifica DNS ni emite SSL. O es un placeholder de texto, o el marketing del onboarding va por delante de la infraestructura — [[2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio]].
8. **El back-office es de pago y su versión legal es solo española.** El Aviso Legal declara que el panel del creador exige suscripción activa, mientras el texto placeholder en inglés sigue sin revisarse con abogado: el cumplimiento LSSI-CE se declara en un documento que solo existe en español — [[2026-1023-live-verify-panel-del-creador-condicionado-a-suscripcion]]. Además, el panel vive en `/resumen`, `/cerebro`, `/biblioteca`, `/inbox`, `/productos`, `/reuniones`, `/analiticas`, `/facturacion`, `/configuracion` (no en `/admin/*`, que devuelve 404 en sus subrutas de plataforma): hay que decidir si esa es la URL de producto o si falta un redirect.
9. **¿Dónde está la instrumentación?** Si no hay Sentry ni PostHog en el bundle vivo, no hay observabilidad de errores ni de producto en la build desplegada. O la instrumentación se retiró al reconstruir el frontend, o la build de octubre es distinta y la DSN de mayo ya no aplica — [[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]. El vault no puede decidirlo, pero sí puede afirmar que **hoy no se observa ninguno de los dos SDK**.

Ver también: [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] y [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]].
