---
id: thread-myownclone-gtm-monetization-roadmap
type: thread
updated: 2026-10-23
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md, raw/articles/myownclone-founder-transcript.md]
links: ["[[myownclone]]", "[[emprenda-aprendiendo]]", "[[myownclone-strategy-and-vision]]", "[[myownclone-vs-myclone-is]]", "[[myownclone-estado-live-2026-10]]"]
---

# Thread — Alta, monetización y roadmap de MyOwnClone

Cómo entra un cliente, qué paga y en qué orden se construye lo que falta. Este thread cierra el triángulo: [[myownclone-strategy-and-vision]] (intención), [[myownclone-platform-architecture]] (código) y aquí, el funnel y el plan.

> **⚠️ Actualizado 2026-10-22 — la fricción nº1 de este thread está resuelta.**
> La re-verificación en vivo (`0-raw/2026-10-22-myownclone-live-reverification.md`) concluye que **el alta self-service está desplegada y abierta**: `/registro` sirve un formulario real con magic link, código de 6 dígitos, Google OAuth, recuperación de contraseña y requisitos de contraseña de 12 caracteres; el onboarding tiene los pasos nombre → personalidad → idioma → confirmación; y la landing tiene sección de precios, con el vocabulario de planes `free`, `basic`, `pro`, `scale` y `enterprise`. La lectura de mayo ("beta con onboarding manual caso por caso") era el estado de la generación anterior del despliegue. Ver [[2026-1022-live-verify-alta-y-precios-ya-publicos]] y [[myownclone-estado-live-2026-10]].

## El alta: dos verdades que no caben juntas

> **Nota 2026-10-23.** Esta sección conserva la lectura de mayo tal como se formuló, porque documenta el conflicto. El estado actual es que **el alta self-service está desplegada** — el banner de arriba y [[myownclone-estado-live-2026-10]] mandan. Para el estado vivo ver §"El alta vivo".

El lado del código: [[2026-1022-onboarding-cuatro-pasos-encuestas]] describe un funnel de cuatro pasos encadenados, con detalle que solo existe si alguien lo diseñó y alguien lo construyó:

1. `/registro` → email, nombre, **subdominio con validación en tiempo real** (`tunombre.myownclone.com`), aceptación de términos y privacidad, opción de Google OAuth, planes Pro/Scale/Enterprise con precio dinámico (`€{price}`) bajo badge "Acceso Beta" con precio bloqueado de por vida.
2. Stripe Checkout — tarjeta obligatoria, mensual, sin permanencia.
3. `/registro/exito` — código mágico de 6 dígitos.
4. `/registro/onboarding` — nombre del clon, subdominio, y dos encuestas: de dónde te conocieron (X, YouTube, Instagram, LinkedIn, Podcast, Newsletter, Recomendación, Google, Anuncio, Otro) y para qué lo usarás (atender alumnos, capturar leads, recomendar productos, soporte automático, Q&A, Otro).

[[2026-1022-auth-magic-link-codigo-seis-digitos]] confirma el método de autenticación principal (magic link de 6 dígitos por email, Google OAuth como alternativa) con seis estados de error diferenciados: email inválido, código incorrecto, código caducado, Google cancelado, email no verificado, cuenta sin tenant, pago requerido. Ese último —"cuenta sin tenant"— es la señal más fuerte de que el sistema de altas está pensado para producción.

El lado público: [[2026-1022-onboarding-manual-sin-self-service]] — `/registro` y `/en/signup` hacen meta-refresh a `/contacto`, y el texto de portada declara "de momento entramos caso por caso. Escríbenos contándonos el tuyo y vemos si encaja". El formulario de contacto es una Server Action con honeypot anti-spam y validación estricta (nombre 2-80, email ≤254, mensaje 20-3000).

Y [[2026-1022-beta-activo-trafico-real]] cierra el triángulo por el lado del back-office: el panel de tenants muestra signups, MRR, pagos fallidos y cancelaciones, con coste desglosado por tenant (responses, words, period cost, lifetime cost). Hay facturación real. El propio informe lo matiza: "beta con onboarding manual caso por caso".

**Lectura honesta**: lo más probable es que el flujo de 4 pasos sea **código funcional pero cerrado al público** — una ventana de beta abierta por la que se han incorporado los clientes que aparecen en el panel. Las tres notas son ciertas y describen tres capas distintas (código, puerta pública, back-office). La fricción no está en los hechos: está en que **nadie ha verificado el estado real del alta**. Es una pregunta de una sesión: `curl -I https://myownclone.com/registro`.

## Planes, trial y precios

[[2026-1022-stripe-planes-trial-30-dias]] — tres planes (Pro, Scale, Enterprise), trial de 30 días con tarjeta obligatoria, y cortesías sin tarjeta otorgadas por el platform admin (cupones 100% off, asignables "forever", por N meses o hasta fecha concreta). El juego completo de estados recognized por la app: `active`, `trialing`, `past_due`, `unpaid`, `canceled`, `incomplete`, `none`, `complimentary`. **Matiz 2026-10-23:** el vocabulario vivo de planes tiene **cinco** (`free`, `basic`, `pro`, `scale`, `enterprise`), no tres — ver [[2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant]].

[[2026-1022-stripe-webhook-confirmado]] confirma la integración en producción por artefacto: `/api/webhooks/stripe` → 405 Method Not Allowed (solo POST). **Ojo: la re-verificación del 2026-10-22 encuentra ese webhook en 404**, así que este artefacto ya no prueba la integración en producción — ver §"Correcciones".

[[2026-1022-precio-99-mensual]] da el ancla de precio desde el transcript: 99 €/mes, un millón de palabras de entrenamiento, 4.000 respuestas del clon, comparado contra el uso real de [[emprenda-aprendiendo]] (3.000+ conversaciones/mes, 100+ alumnos).

Y el hueco era brutal: [[2026-1022-sin-pagina-precios-ni-docs]] — `/pricing`, `/plans`, `/features`, `/blog`, `/changelog`, `/roadmap`, `/docs`, `/documentation`, `/about`, `/register`, `/terms` y `/privacy` devuelven **todos 404**, y ninguna página enlaza a documentación externa. Hay un producto cobrando 99 €/mes sin página de precios. **Matiz 2026-10-23:** la landing `/` ya tiene sección de precios, pero sin importes `€` en el HTML de servidor y sin URL propia — `/pricing` cae en el catch-all de slug. Los precios son públicos pero no tienen página, y ningún importe está verificado en vivo. La única superficie legal pública son seis documentos ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]): Aviso Legal, Privacidad, Cookies, Términos, DPA y Clone Terms — y `/terms` y `/privacy` dan 404 en la raíz pese a existir `/en/legal/terms`. Esa asimetría ES-vs-EN está documentada en [[2026-1022-i18n-es-first-jurisdiccion-es]].

## Costes: el modelo de quién paga qué

[[2026-1022-costes-por-categoria-tenant]] — tres categorías con pagador explícito: `categoryCloneResponses` y `categoryIngestion` facturables al tenant; `categoryPlatformOps` (memoria, embeddings, clasificadores internos) las paga MyOwnClone. El panel de plataforma lo expone con desglose por proveedor (Anthropic + OpenAI + email) y por eje (chat vs. ops). Esto está bien diseñado y es una ventaja de negocio real frente a un competidor que no publica contadores.

[[2026-1022-platform-admin-tenants-costes-mrr]] añade el back-office completo: control sobre la base de tenants (búsqueda, orden, filtrado, "View as" / impersonación, invitaciones, concesión de planes), buzón de feedback, gestor de FAQs, tracking de MRR por tiers y tracking de coste.

[[2026-1022-auth-otp-impersonacion-30min]] detalla la impersonación: el operador entra por `/admin/platform/tenants`, activa modo explícito de soporte ("View as" / "Support mode") con banner rojo, expiración automática de 30 minutos, y audit log por tenant. Es una función de soporte real, con límites. Es también la que se ve expuesta por la fuga de `/admin` — ver [[myownclone-security-surface]].

[[2026-1022-gap-monetizacion-creador-stripe-connect]] — el creator **no cobra**: solo hay planes de plataforma. MyClone.is sí tiene monetización por persona vía Stripe Connect (`POST /stripe/personas/{id}/connect/onboard`, pricing models `one_time`, `subscription`, `one_time_duration`). Dado el modelo de negocio del founder (el clon es la oferta high-ticket del infoproductor), esto es un gap de modelo de negocio, no de feature: sin Stripe Connect, el clon no puede ser vendible como producto propio del creator.

## El coste real de un alta y de un mes de servicio

El modelo de costes del vault —[[2026-1022-costes-por-categoria-tenant]]— parte de un corte que hoy se sabe incompleto: separa el gasto en **inferencia facturable al tenant** (`categoryCloneResponses`, `categoryIngestion`) frente a **operación interna absorbida por la plataforma** (`categoryPlatformOps`), y el panel lo expone por proveedor (Anthropic + OpenAI + email) y por eje (chat vs. ops). La refinery del 2026-10-23 presiona ese corte por los dos lados: **no hay línea de hosting** y **no hay línea de verificación por alta**.

El hosting es real —el sitio se sirve desde nginx autoalojado— y no cabe en ninguna de las tres categorías documentadas. La referencia de precio más barata verificable es el plan compartido más barato de Hetzner Cloud: **CPX02, 1 vCPU AMD, €5,99/mes o €0,0096/h sin IVA** ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]], [[2026-1023-hetzner-facturacion-por-hora-0-0096]]), es decir **un 50 % por encima del presupuesto de referencia de ≤ €4/mes** ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Que el VPS vivo sea ese plan concreto no está confirmado: es una inferencia.

La verificación por alta es la otra línea ausente. El producto **no la tiene hoy** (ver §"el alta vivo" más abajo), pero si se añadiera, sería un coste marginal por tenant y no por uso: en 5sim una activación va de **$0,1026 a $8,8897**, con mediana $0,8942 en 175 filas y 98 filas a $1 o menos ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). Hay una capa más barata y más frágil —el 接码 de 卡网 a ¥0,20–¥0,57 y el correo a ¥0,02 ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]])— y una comisión de recarga del 10 % sobre el saldo ([[2026-1023-lzt-topup-mastercard-comision-10]]) que multiplica todo lo comprado con ese saldo.

Y hay una confusión de unidades que puede costar caro: **una suscripción mensual no es un paquete de tokens de API**. La propia fuente lo dice —"月订阅多是产品内额度，不等同 API token 包" ([[2026-1023-priceai-suscripcion-no-es-api-token]]). "Coding Plan" y "Token Plan" son **categorías de producto** con pago fijo y cuota por ventana (5 h / semana / mes o 7 días), no precio por token ([[2026-1023-priceai-token-plan-como-categoria-producto]]). Tabla de esas líneas, todas de la misma captura:

| Suscripción | Precio | Cuota | Modelos |
|---|---|---|---|
| OpenCode Go | **$10/mes** | $12/5h · $30/sem · $60/mes | 12 |
| Alibaba Model Studio Coding Plan | **$50/mes** | 6.000 req/5h · 45.000/sem · 90.000/mes | 5 |
| Tencent TokenHub Coding Plan Lite | **40 元/mes** | 1.200 req/5h · 9.000/sem · 18.000/mes | 3 |
| Tencent TokenHub Coding Plan Pro | **200 元/mes** | 6.000 req/5h · 45.000/sem · 90.000/mes | 3 |
| Alibaba Bailian Token Plan Lite | **¥39/mes起** | 700 Credits/5h · 2.500 Credits/7d | 1 (preview) |
| StepFun Step Plan | 49 / 99 / 199 / 699 元/mes | ~100 a ~5.000 prompts/5h · ~1.500 a ~75.000 llamadas/5h | 1 |

([[2026-1023-priceai-opencode-go-10-usd-y-60-usd-al-mes]], [[2026-1023-priceai-alibaba-coding-plan-50-usd]], [[2026-1023-priceai-tencent-tokenhub-coding-plan-lite-y-pro]], [[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]], [[2026-1023-priceai-stepfun-step-plan-prompts-y-llamadas]].) StepFun es el único caso que publica la conversión explícita: **~15 llamadas de modelo por prompt**, que es lo que hace comparables por fin los planes con unidades distintas.

El coste de una suscripción fija **no se puede imputar a un tenant por token**, y el panel de costes —que solo mide consumo por token— no lo refleja. Además, una capacidad nueva que se quiera añadir abre su propia partida: el proxy de Midjourney es la pieza de imagen ya existente, Apache-2.0, con siete aplicaciones de terceros encima, y su README **ofrece comercialmente una API no oficial** por WeChat sin publicar ningún precio ([[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]); para un clon con imagen sería una partida de coste sin SLA y con riesgo de baneo de cuenta ([[2026-1023-midjourney-proxy-relevancia-para-clones-con-imagen]]).

| Partida de coste | Unidad | Escala con | ¿En el panel? |
|---|---|---|---|
| Inferencia facturable (`cloneResponses`, `ingestion`) | token / respuesta | **uso** | sí, por proveedor y eje |
| Operación interna (`categoryPlatformOps`) | consumo interno | uso (parcial) | sí, dentro de `ops` |
| Hosting / VPS | €5,99/mes o €0,0096/h | **ni tenants ni uso** (fijo; baja a céntimos si el servidor puede apagarse) | **no** |
| Verificación por alta (SMS, si se añade) | $0,1026–$8,8897 por unidad | **tenants** (una por alta) | **no** |
| Comisión de recarga del saldo | 10 % sobre saldo | multiplica todo lo comprado con ese saldo | **no** |
| Insumo de alta barato (código 接码 / correo) | ¥0,20–¥0,57 / ¥0,02 | **tenants** | **no** |
| Suscripción fija de proveedor | €/mes con cuota por ventana | **ni tenants ni uso** (cuota con techo) | **no** |
| Imagen (proxy no oficial), si se ofrece | sin precio publicado | uso, más riesgo de baneo | **no** |

Dos avisos de fiabilidad, explícitos: el suelo de hosting de €5,99 es **dentro del catálogo de Hetzner**, no un precio universal — existen claims de sponsor de VPS chinos a 68 元/año (Aliyun) y 199 元/año (Tencent) para auto-hospedar un relay, sin SLA y sin verificación de PriceAI ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]); y que el VPS vivo sea un CPX02 de Hetzner **no está confirmado**.

## El alta vivo: no hay SMS, y el dominio propio ya se ofrece

La re-verificación del 2026-10-23 fija el flujo de alta tal como está hoy: **`/registro` sirve magic link + código de 6 dígitos + Google OAuth, sin verificación por teléfono**. No hay ningún paso de SMS. La ausencia es, por ahora, una buena noticia para el coste marginal — el alta no paga una línea por signup — pero el vault **no sabe si es deliberada** (evitar coste y fraude) o accidental (nunca se diseñó el paso).

El onboarding vivo sí ofrece algo nuevo: los placeholders `slugSuffix: ".myownclone.yourdomain.com"` y `urlSuffix: ".myownclone.com"`, junto a los cuatro pasos ya verificados (`name` → `personality` → `language` → `confirm`) ([[2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio]]). Es decir, **el control de dominio propio está expuesto al cliente final** aunque el backend que lo resuelve sigue sin existir — sin verificación DNS ni SSL, tal como dice [[2026-1022-gap-custom-domains-campo-inactivo]]. Frente al competidor, que ya expone `POST /custom-domains` con verificación y cuota por tier, MyOwnClone muestra el hueco en el formulario sin cerrarlo.

El resto de la re-verificación confirma el bucle de ingreso que este thread describe, y le añade una regla de negocio que el vault no tenía registrada:

- **El panel del creador es de pago.** El Aviso Legal declara que "el acceso al panel de administración del creador requiere una suscripción activa" ([[2026-1023-live-verify-panel-del-creador-condicionado-a-suscripcion]]). Es la pieza que convierte el back-office en producto de suscripción y no en beta cerrada. El mismo documento añade que el visitante de un clon publicado interactúa **anónimo o con OTP por email** — que es el canal de acceso real al producto público.
- **El vocabulario del back-office confirma el modelo de margen.** El i18n vivo expone `mrrCostsMarginLegend: "MRR / Costs / Margin"`, `costs30d: "Costs (30d)"`, los estados de tenant `tenant`/`trial`/**`suspended`** (este último nuevo para el vault), `stripeCustomer`/`stripeSubscription`/`subscriptionStatus` y los cinco planes `free, basic, pro, scale, enterprise` ([[2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant]]). MRR, costes a 30 días y margen son exactamente las tres líneas que el modelo de costes necesita y que la tabla de arriba no cubre.
- **El tercer modo se llama `sales`, no "recomienda".** El bundle nombra `pedagogy`, `sales` y `support`, con `Sales` entre los tres botones de "Conversation mode" (Learn / Support / Sales) y el Aviso Legal repitiendo "pedagogía, ventas y soporte" ([[2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle]]). El copy de marketing sigue diciendo que el clon "recomienda productos". No es un error del corpus: es una divergencia entre discurso y modelo de datos, y el triage del inbox conecta soporte con el silo comercial (`automationDesc` incluye "recommend products").

## Correcciones a afirmaciones de este thread

Cuatro afirmaciones de este documento quedaron desactualizadas por la re-verificación. La autoridad del estado vivo es [[myownclone-estado-live-2026-10]].

1. **El alta manual ya no es el estado.** La sección "El alta: dos verdades que no caben juntas" recoge todavía la lectura de mayo: `/registro` y `/en/signup` haciendo meta-refresh a `/contacto`. Hoy `/registro` sirve formulario real y `/contacto` sigue existiendo como vía paralela. La tabla de fricciones nº1 debe leerse como **cerrada** —el banner del 2026-10-22 ya lo dice, pero el cuerpo y la lista de fricciones seguían expresando el conflicto.
2. **El webhook de Stripe ya no devuelve 405.** [[2026-1022-stripe-webhook-confirmado]] se apoyaba en `405 Method Not Allowed` para dar por confirmada la integración en producción; la re-verificación del 2026-10-22 lo encuentra en **404**. La integración ya no es verificable por ese artefacto: el argumento de "Stripe está integrado" ya no se sostiene con la URL, solo con el bundle (planes, trial, checkout) y la existencia de la sección de precios.
3. **"Sin página de precios" es una afirmación caduca y su sustituta es más precisa.** [[2026-1022-sin-pagina-precios-ni-docs]] listaba `/pricing` entre los 404; hoy la landing `/` tiene sección de precios ("Pick your plan."), **pero sin importes `€` en el HTML de servidor** y **sin URL propia**: `/pricing` cae en el catch-all de slug y devuelve la página de chat. Los precios son públicos pero no tienen página.
4. **La lista de planes cambió y el ancla de precio quedó sin confirmar.** El thread repite "tres planes (Pro, Scale, Enterprise)" y "cuatro planes" según la línea; el vocabulario vivo tiene **cinco** (`free`, `basic`, `pro`, `scale`, `enterprise`). Y el ancla de 99 €/mes viene del transcript del founder ([[2026-1022-precio-99-mensual]]), no de la landing viva: **el vault no ha verificado en vivo ningún importe**. Cualquier plan de monetización que se apoye en "99 €/mes" está descansando en una cifra de mayo.

## El roadmap, y su conflicto

El handoff fija un orden explícito — [[2026-1022-plan-orden-implementacion-myownclone]]:

| # | Paso | Prioridad | Esfuerzo |
|---|---|---|---|
| Step 4 | Bug fixes de consistencia de schema | 🔴 CRÍTICO | — |
| Step 1 | Prompt versioning | 🔴 ALTA | medio |
| Step 2 | Lead / visitor | 🔴 ALTA | **bajo** |
| Step 3 | Workflows ("solo si hay demanda de usuarios") | 🟡 MEDIA | alto |
| Step 5 | Langfuse (observabilidad) | 🟡 MEDIA | — |

[[2026-1022-plan-replicacion-myclone-fases-prioridad]] lo empaqueta en 4 fases: Fase 1 (semanas 1-2) versioning + lead capture; Fase 2 (3-4) workflows; Fase 3 (5-6) Stripe Connect; Fase 4 (7+) Langfuse, voice cloning y custom domains.

El detalle de cada paso está en átomos dedicados: [[2026-1022-plan-prompt-versioning-nuestro]] (dos tablas `prompt_versions`/`prompt_variables`, cuatro endpoints `history`/`restore`/`diff`, `generate_change_summary()` con `difflib`, tab "Historial" en `cerebro/page.tsx`, migración que crea la versión 1 desde los prompts activos), [[2026-1022-plan-lead-capture-visitors]] (tabla `visitors`, endpoint público `capture-lead`, proxy `GET /api/visitors`, popup "Ingresa tu email" tras 3 mensajes), [[2026-1022-plan-workflows-nuestro]] (cuatro tablas replicando el modelo de MyClone, output_template `lead_summary` con secciones `profile, situation, need, score, follow_up_questions`), [[2026-1022-plan-langfuse-instrumentacion-nuestra]] (trace `clone-chat` con `metadata{clone_id, mode}`, span `llm-inference`).

**El conflicto sin resolver**: [[2026-1022-mvp-salir-al-mercado-pronto]] (el founder: MVP primero, salir ya) contra el Step 1 del handoff (versionado de prompts, una feature interna de gobernanza, no de lanzamiento). Y una segunda tensión entre documentos: [[2026-1022-gap-workflows-myownclone]] pone workflows en Fase 2 (semanas 3-4) mientras el handoff los deja para el final ("solo si hay demanda"). Dos documentos, dos priorizaciones del mismo trabajo.

## Fricciones abiertas

1. **Estado real del alta — CERRADA.** Código de 4 pasos vs. `/registro` → `/contacto` vs. signups y MRR en el panel. Resuelto por la re-verificación del 2026-10-22: el alta self-service está desplegada y la landing tiene precios. [[2026-1022-live-verify-alta-y-precios-ya-publicos]], [[myownclone-estado-live-2026-10]]. La lectura de mayo ([[2026-1022-onboarding-cuatro-pasos-encuestas]], [[2026-1022-onboarding-manual-sin-self-service]], [[2026-1022-beta-activo-trafico-real]]) queda como historial.
2. **MVP vs. gobernanza** — [[2026-1022-mvp-salir-al-mercado-pronto]] vs [[2026-1022-plan-orden-implementacion-myownclone]].
3. **Workflows: Fase 2 o último** — [[2026-1022-plan-replicacion-myclone-fases-prioridad]] vs [[2026-1022-plan-workflows-nuestro]].
4. **8 gaps vs. 7** — [[2026-1022-myclone-vs-myownclone-gaps-api]] vs [[2026-1022-plan-replicacion-myclone-fases-prioridad]]: la ingesta de YouTube queda fuera del plan.
5. **El creator no cobra** — [[2026-1022-gap-monetizacion-creador-stripe-connect]] vs el modelo de negocio de [[2026-1022-low-ticket-a-high-ticket-con-clon]] ([[myownclone-strategy-and-vision]]).
6. **Sin página de precios — MATIZADA.** [[2026-1022-sin-pagina-precios-ni-docs]] vs [[2026-1022-precio-99-mensual]]. Hoy la landing `/` tiene sección de precios, pero **sin importes `€` en el HTML de servidor y sin URL propia** (`/pricing` cae en el catch-all). Y el ancla de 99 €/mes sigue siendo una cifra de mayo sin verificar en vivo — ver §"Correcciones".
7. **Captura de leads: discurso vs código** — [[2026-1022-gap-lead-capture-visitors]] vs [[2026-1022-instancia-como-captador-de-leads]].

## Fricciones nuevas para juicio humano

Las que la refinery del 2026-10-23 abrió y que este thread no puede cerrar solo. Todas apuntan al mismo sitio: **el modelo de costes y el modelo de ingresos del producto están construidos sobre un corpus de mayo que ya no describe el producto desplegado.**

1. **El modelo de costes no tiene línea de infraestructura.** [[2026-1022-costes-por-categoria-tenant]] solo separa inferencia facturable de operación interna; el hosting es un coste fijo real que no aparece en ninguna de las dos. O se imputa dentro de `categoryPlatformOps` sin desglose visible, o el MRR del panel está sobrestimado. [[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]].
2. **El modelo de costes no tiene línea por alta.** Si alguna vez se añade verificación por SMS (o cualquier paso antifraude por signup), es un coste que **escala con tenants**, no con uso, y no encaja en ninguna categoría existente: o se factura al tenant, o se absorbe y erosiona el margen en silencio. Hoy el alta **no tiene SMS**, así que la línea está vacía por omisión — y nadie ha dicho si es decisión o descuido. [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]].
3. **≤ €4/mes de infraestructura no alcanza: el suelo es €5,99.** Ningún plan del catálogo de Hetzner baja de €5,99/mes sin IVA, un 50 % por encima del presupuesto de referencia; la única palanca es la facturación por hora (€0,0096/h) si el servidor puede estar apagado. [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]], [[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]], [[2026-1023-hetzner-facturacion-por-hora-0-0096]].
4. **Suscripción y token no son la misma unidad, y el panel solo mide tokens.** Si la capa de inferencia migra a Coding Plans / Token Plans (OpenCode Go a $10/mes, Alibaba a $50/mes), la línea "Anthropic"/"OpenAI" del panel mezcla coste variable facturable con coste fijo absorbido, o bien omite la suscripción entera. [[2026-1023-priceai-suscripcion-no-es-api-token]], [[2026-1023-priceai-token-plan-como-categoria-producto]].
5. **Marketing vs. código en el tercer modo.** El copy dice "recomienda productos"; el bundle, la interfaz y el Aviso Legal dicen `sales` / "ventas". No es un error del corpus: es una divergencia entre discurso y modelo de datos que cambia la lectura comercial del producto. [[2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle]].
6. **El dominio propio se ofrece en el alta y no tiene camino de resolución.** El onboarding vivo muestra `.myownclone.yourdomain.com` al cliente final; el backend no verifica DNS ni emite SSL, y el competidor ya expone `POST /custom-domains` con verificación y cuota por tier. O se cierra el flujo, o se retira el placeholder. [[2026-1023-live-verify-onboarding-ofrece-sufijo-de-dominio-propio]], [[2026-1022-gap-custom-domains-campo-inactivo]].
7. **No hay ni un importe verificado en vivo.** La landing tiene sección de precios pero sin `€` en el HTML de servidor y sin URL propia, y el webhook de Stripe ha pasado de 405 a 404. El ancla de 99 €/mes es una cifra de mayo venida del transcript. Antes de decidir cualquier precio hay que leer los importes reales. [[2026-1022-live-verify-alta-y-precios-ya-publicos]], [[myownclone-estado-live-2026-10]].

Ver también: [[myownclone-vs-myclone-is]] para el detalle de cada gap frente al competidor.
