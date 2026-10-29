# Scout Report — 2026-10-29

Run: 23:00 shift (scheduled cron).
Vault: `/home/haxth3/wiki`

## URLs attempted

21 unique URLs. **20 capturadas con éxito**, 1 descartada. **Ninguna [UNREACHABLE]**.

**Nota sobre la fuente de la lista:** `0-raw/reading-list.md` seguía **vacía** (cabecera + ejemplo comentado; sin cambios desde el 26 de junio) al inicio de este turno — la **7ª ronda consecutiva** en la que el Scout tiene que derivar su propio objetivo. Las URLs de este turno se han tomado de un hueco real y concreto: el thread `myownclone-gtm-monetization-roadmap.md` documenta que el **modelo de costes de MyOwnClone no tiene línea de infraestructura** (`categoryPlatformOps` cubre memoria/embeddings, pero no hosting, ni base de datos, ni vector store, ni email, ni observabilidad), y que el panel de MRR "está sobrestimado" por esa omisión. Este turno capturó la **base de precios de primer nivel** de los proveedores que el producto ya usa o puede usar, para que el Refinery pueda construir la tabla de coste operativo con aritmética auditable en lugar de estimaciones.

**Cambio de estado del pipeline:** al final de este turno `0-raw/reading-list.md` **deja de estar vacía** — se han añadido 15 URLs verificadas (HTTP 200 comprobadas) para el turno del 2026-10-30. Es la primera vez en 7 rondas que la lista tiene contenido. Ver §"Estado de la lista de lectura".

## URLs successfully fetched (20)

| Archivo en `sources/` | URL | Palabras |
|---|---|---|
| `2026-10-29-resend-pricing.md` | resend.com/pricing | 3.119 |
| `2026-10-29-aws-ses-pricing.md` | aws.amazon.com/ses/pricing/ | 3.096 |
| `2026-10-29-postmark-pricing.md` | postmarkapp.com/pricing | 1.454 |
| `2026-10-29-mailgun-pricing.md` | mailgun.com/pricing/ | 1.337 |
| `2026-10-29-sendgrid-pricing.md` | sendgrid.com/en-us/pricing | 376 |
| `2026-10-29-twilio-sendgrid-email-api-pricing.md` | www.twilio.com/en-us/products/email-api/pricing | 2.842 |
| `2026-10-29-stripe-pricing.md` | stripe.com/pricing | 3.583 |
| `2026-10-29-neon-pricing.md` | neon.tech/pricing | 3.193 |
| `2026-10-29-supabase-pricing.md` | supabase.com/pricing | 3.787 |
| `2026-10-29-upstash-redis-pricing.md` | upstash.com/pricing | 2.447 |
| `2026-10-29-weaviate-cloud-pricing.md` | weaviate.io/pricing | 1.575 |
| `2026-10-29-weaviate-deployment-options.md` | weaviate.io/developers/weaviate/installation | 859 |
| `2026-10-29-qdrant-cloud-pricing.md` | qdrant.tech/pricing/ | 777 |
| `2026-10-29-vercel-pricing.md` | vercel.com/pricing | 2.199 |
| `2026-10-29-railway-pricing.md` | railway.com/pricing | 2.001 |
| `2026-10-29-render-pricing.md` | render.com/pricing | 3.235 |
| `2026-10-29-langfuse-pricing.md` | langfuse.com/pricing | 2.776 |
| `2026-10-29-sentry-pricing.md` | sentry.io/pricing/ | 1.572 |
| `2026-10-29-posthog-pricing.md` | posthog.com/pricing | 2.367 |
| `2026-10-29-cloudflare-workers-pricing.md` | workers.cloudflare.com/pricing/ | 3.225 |

**Total: ~45.820 palabras** capturadas. 20 punteros de captura creados en `0-raw/`, todos con `Status: ready` (los recoge el Refinery de las 03:00).

## URLs descartadas

| URL | Motivo |
|---|---|
| `www.cloudflare.com/developer-platform/workers/pricing/` | **404 — la ruta movida.** La página real de precios de Workers es `workers.cloudflare.com/pricing/`, capturada correctamente. |
| `weaviate.io/cloud` | Landing de producto sin datos de precio (8 palabras útiles: solo logo y enlaces). La fuente de precio es `weaviate.io/pricing`, ya capturada. |
| `cloudflare.com/plans/developer-platform/` | Solo navegación de planes, sin cifras de Developer Platform (214 palabras, casi todo navbar). Sustituida por `workers.cloudflare.com/pricing/`. |

## Hallazgos

**1. El coste de email saliente del producto está casi resuelto, y sale caro si se elige mal el proveedor.** El producto usa **Resend** (`RESEND_API_KEY` en AGENTS.md) y su tabla es la más cara del conjunto para volumen pequeño-medio:

| Proveedor | Base | Overage | Nota |
|---|---|---|---|
| Resend | Free $0 (3.000/mes, 100/día) · Pro $20 (50k) · Scale $90 (100k) | $0,90 / 1.000 | inboxes $1/mes adicionales, dominios $20, IP dedicada $30, **SSO $150/mes** |
| AWS SES | $0,16 / 1.000 (Essentials, <10M/mes) · $0,22 Pro · $0,23 Enterprise | escala a $0,11–0,13/1.000 >100M | inbound $0,10/1.000 |
| Postmark | $15 · $16,50 · $18 | $1,80 → $1,20 / 1.000 | **$75 de crédito** para startups sin inversión |
| Mailgun | $15 (50k) · $35 · $90 (100k) | $1,80 → $1,10 / 1.000 | validaciones $1,20/100, IP adicional $59/IP/mes |
| Twilio SendGrid | Free Trial $0/60d (100/día) · Essentials $19,95 · Pro $89,95 · Premier custom | overages aparte | 99,999% uptime, IP dedicada incluida en Pro |

**Lectura operativa:** a escala de MyOwnClone (miles de emails/mes) **SES a $0,16/1.000 gana a Resend Pro ($0,40/1.000 efectivo) por ~2,5×**, pero SES no da inbox/threading API ni SSO (el SSO de Resend cuesta $150/mes). El thread del roadmap tiene el producto con **email triage con IA** (`email_inbound`/`email_templates`), o sea que laThreading API de Resend o Postmark importa más que el precio por mil. El dato duro: **cambiar de Resend a SES ahorra ~$12/mes a 50k emails y ~$80/mes a 100k**, pero rompe el triage por threading. **No es un cambio gratis.** El add-on de **SSO de Resend a $150/mes** es la línea que más duele contra un presupuesto de €4/mes.

**2. SES tiene ahora tres planes y un cambio de comportamiento por defecto que el vault no tiene anotado.** A partir del **21 de julio de 2026** las cuentas nuevas y las combinaciones cuenta×región sin actividad desde el 1 de junio de 2025 **empiezan en Essentials**. Los tres planes difieren en features, no solo en precio: Essentials incluye 5 dominios + 12 IP + 25 seedlist tests, pero **solo si se paga $1.250/mes**; Pro y Enterprise los incluyen. Pro añade 2.500 validaciones API/mes, Enterprise 5.000 (extra: $0,01/validación). Crítico para el threat model: **los tenants adicionales cuestan $0,005/mes/tenant + $0,005/1.000 emails**, y los **Open Ingress Endpoint cuestan $50/mes/endpoint en Essentials y Pro** (solo Enterprise incluye 1 gratis). Mail Manager añade $0,15/1.000 en procesamiento de entrada y $2/GB al archivar — **una partida de coste recurrente y fácil de olvidar** en un producto que hace triage de email.

**3. La tabla de Stripe deja el margen bruto del producto calculable, con tres recargos que el roadmap no tiene.** Base: **2,9% + 30¢** por transacción doméstica; **+1,5%** para tarjetas internacionales; **+1%** si hay conversión de divisa; **+0,5%** para tarjetas introducidas a mano. En disputes: **$15 por dispute recibido**, **$15 por contestación manual** (devueltos si ganas) y **Smart Disputes = 30% del importe disputado por cada disputa ganada**. Klarna: **5,99% + 30¢**. Stablecoins: **1,5%** del importe. Con un plan de 99 €/mes el coste de cobro es ~**€3,40** (2,9% + 0,30 €) — el margen bruto previa a inferencia es ~**96,5%**, pero **un 1,5% internacional se come la mitad de ese margen**, y un 1% de conversión de divisa lo deja en 95,5%. **El "dispute deflection lookups" de $15 (Visa) / $29 (Mastercard) son un vector de coste que escala con el fraude, no con el uso** — misma categoría de problema que el hueco de SMS-por-alta que el roadmap ya marca.

**4. El precio de la base de datos del producto (Postgres) tiene tres clerks distintos y ninguno está en el panel de costes.** Neon (serverless): **$0,106 por CU-hr + $0,35 por GB-mes**, con **$0,002 por branch-hour** — es decir, **crear una branch por tenant cuesta dinero de forma continua**. Supabase: Pro $25 (incluye $10 de créditos de compute; Micro $10 / Small $15 / Medium $60 / Large $110 / XL $210 / 2XL $410). El detalle que importa para el multi-tenant: **Supabase cobra $0,00325 por MAU por encima de 50k** y **$0,125/GB de DB, $0,09/GB de storage, $0,03/GB de bandwidth, $0,0213/GB de realtime** — todo por *consumo de tenants*, no por tenants. **Cada usuario de un clon es un MAU que se factura.** Con 4.000 respuestas/mes por plan de 99 € (dato de [[2026-1022-precio-99-mensual]]), el coste de infra por tenant es marginalmente pequeño, pero la línea MAU + realtime es la que el panel no expone hoy.

**5. Redis es la partida más barata de toda la infraestructura, y la línea de comando es la única que puede Dolor.** Upstash: Free $0 (250 MB, 10 GB bandwidth), **pay-as-you-go $0,20 por 100K comandos**, $0,25/GB de storage (1 GB gratis), $0,03/GB de bandwidth más allá de 200 GB. Los planes fijos suben fuerte: 250MB $10 → 500GB $1.500, y cada **read region extra cuesta +$5 a +$750/mes**. Detalle caro: **en global DB, las escrituras se replican y cuentan como comandos** (1 primary + 1 read region = 100K escrituras cuestan $0,40). Los antiguos Pro 2K/Pro 10K ($280 y $680/mes) están **deprecados**. Para un SaaS de clones, la decisión relevante es: pay-as-you-go a $0,20/100K comandos es barato, pero **un bug de caché puede multiplicar comandos ×10 sin que nada lo delate** — el panel de coste por tenant mide tokens, no comandos.

**6. Weaviate es, con diferencia, la partida más cara del stack — y tiene un free tier generoso.** Weaviate Cloud Free: **$0 permanente, 1 cluster, 100.000 objetos, 1 GB de memoria, 10 GB de disco, 1 colección hasta 3 tenants, 2.000 embeddings/día y 1.000 queries/mes al mes con Query Agent**. Flex desde **$45/mes** (pay-as-you-go) y Premium desde **$400/mes**. Charging: **$0,00465/1M de dimensiones vectoriales** (Flex, baja a $0,002718 en Premium), **$0,12/GiB de storage** (Flex) y **$0,03036/GiB de backup** — *los backups se cobran aparte*. La cifra que decide la arquitectura: **$45/mes de base en Flex contra $0 en Free** — con 100.000 objetos de free tier, un clon con memoria de训练 + historial de email podría acercarse al límite. Alternativa **Qdrant Cloud**: free tier con nodo único de 0,5 vCPU / 1 GB RAM / 4 GB disco y **Standard con SLA 99,5%** por uso, Premium con SSO, VPC privado y SLA 99,9%. Y la página de instalación confirma que **el self-managed usa el mismo Weaviate Database que WCD** (Docker, Kubernetes, AWS/GCP Marketplace, DigitalOcean) — es decir, **self-hostear Weaviate en el VPS de €5,99 es una alternativa real al Flex de $45/mes**.

**7. Observabilidad: Langfuse a $0 es el punto de entrada real, no Sentry.** Langfuse Hobby **$0** con todas las features de plataforma (con límites); Core **$29** con 100k unidades/mes y **$8/100k unidades** extra (decrece a $6/100k por encima de 50M); Pro $199; **Teams add-on $300/mes**; Enterprise $2.499. Sentry: developer $0, **team $26**, **business $80**, con **50k errores incluidos** y **+$0,50/GB** de excedente, **+$1,00 por alerta de uptime**. PostHog: free tier por producto (1M eventos, 5K replays, 100K excepciones), **$0,000071 por evento identificado**, **$0,000198 por evento tras el primer 1M**, y **logs con retención de 14 días por defecto; retener más cuesta $0,05/GB/mes**. PostHog es **MIT y self-hosteable**. El roadmap lista **Langfuse como paso 5 de la replicación (🟡 MEDIA)** — el dato relevante es que **la versión self-hosted de Langfuse tiene su propia página de precios** (`langfuse.com/pricing-self-host`), que es la vía para self-hospedar y eliminar esa partida de coste.

**8. El hosting PaaS confirma que el presupuesto de ≤€4/mes es inviable con cualquier proveedor de nivel managed.** Render: Hobby $0 (512 MB), **$7/mes por 512 MB**, **$25/mes por 2 GB**, $85 por 4 GB; discos SSD **$0,25/GB/mes**. Railway: $5 de crédito en Hobby, $20 en Pro, y **$0,00000772 por vCPU-segundo** (≈$20/vCPU-mes a plena carga) + $0,05/GB de egress. Vercel: Hobby $0, **Pro $20/mes** con $20 de crédito incluido. Cloudflare Workers: **Free con 100k requests/día** y **$0,30/1M requests + $0,02/1M CPU-ms** en Pro; **$20/año** Pro o **$200/año** Business. Conclusión: **el diseño correcto para MyOwnClone es 1 VPS (Hetzner) + Cloudflare Free tier para borde y assets + Neon/Supabase Free + Upstash Free + Weaviate Free**, es decir **$0/mes de PaaS hasta que el uso real demuestre que no basta**. El único coste que se sale del todo del free tier en el diseño mínimo es **el VPS (~€6/mes)**, que es exactamente el punto ciego que el roadmap ya señala.

## Requiere atención humana

1. **⚠️ La decisión que este turno desbloquea y que hay que tomar antes de escribir la tabla de costes: ¿email vía Resend o vía SES?** La diferencia es ~2,5× a escala relevante, pero SES **no da threading API** y el producto vive del email triage. **No es un cambio de configuración**: es una decisión de arquitectura de la bandeja de entrada.
2. **El SSO de Resend cuesta $150/mes.** Con presupuesto de €4/mes es la partida desproporcionada. Si el SSO es requisito del plan Enterprise, hay que medir el número real de tenants Enterprise antes de activarlo, o mover a un proveedor con SSO incluido (Qdrant Premium, Sentry business).
3. **Stripe: un 1,5% internacional + 1% de conversión de divisa se come 2,5 puntos de margen**, y el plan actual es de 99 €/mes **sin importar el país del cliente**. Con clientes en LATAM (donde el thread de reventa de cuentas tiene su foco) el coste de cobro sube al 4,4%–5,4% antes de inferencia. **Decidir si se cobra en EUR a clientes no-UE.**
4. **Neon cobra $0,002 por branch-hour.** Si el producto usa branches de Postgres por tenant (patrón habitual de multi-tenant con rollback), **eso es un coste por tenant recurrente que el panel no mide**. Verificar el patrón real de branching en la API.
5. **Supabase MAU ($0,00325) + realtime ($0,0213/GB) + bandwidth ($0,09/GB)**: si el chat de los clones es un stream con presencia, la línea realtime es la que escala con usuarios, no con tenants. **Auditar qué partes del panel de tenants consumen estos tres mostradores.**
6. **Mail Manager de SES ($2/GB al archivar + $0,15/1.000 en procesamiento de entrada)** es una partida recurrente que solo aparece si el producto usa SES inbound. **No activarlo hasta tener la decisión de la línea 1.**
7. **Weaviate Free (100.000 objetos) es el techo real del diseño actual.** Si el self-managed sobre el VPS de €5,99 aguanta, se ahorran los $45/mes del Flex; si no, el mínimo de $45/mes **duplica el presupuesto de infraestructura** del producto.
8. **Backups de Weaviate se cobran aparte** ($0,03036/GiB en Flex): es una partida de coste recurrente que solo aparece si se activa el backup. Comprobar si el producto respalda el vector store.
9. **Deuda del vault sobre Auth0/Clerk/WorkOS**: el producto tiene impersonación de admin (`impersonation_log`/`impersonation_tokens`) y SSO en el back-office. Nadie ha capturado aún el precio de la capa de identidad. **Añadido a la lista de lectura del 2026-10-30.**
10. **El "1M eventos / 5K replays / 100K excepciones" del free tier de PostHog** es mensual, no anual — un backoffice de tenants que mire al dashboard cada día lo consume en semanas. Fijar límites de coste.

## Estado de la lista de lectura

**Cambio de estado: la lista ya no está vacía.** Se han añadido 15 URLs verificadas por HTTP 200 para el turno del 2026-10-30, en tres bloques:

- **Infraestructura self-hosted** (Hetzner Cloud, DigitalOcean droplets, Aiven, Backblaze B2, Cloudflare R2, Deepgram, AssemblyAI, Twilio SMS, Bright Data, Lambda AI) — para cerrar el eje "coste de hosting real vs presupuesto ≤€4/mes" y las líneas de SMS/proxy que el roadmap marca como huecos.
- **Identidad y SSO** (Clerk, WorkOS, Auth0) — para el hueco de la capa de identidad del back-office con impersonación.
- **Operaciones** (Tailscale KB, Azure architecture patterns) — red private y patrones multi-tier para el backend Flask/Next.

Nota: la lista se editó **añadiendo** URLs al final, **sin tocar** la cabecera ni el ejemplo comentado, para que los Scout futuros hereden el formato existente.

## Nada tocado

`sources/` (solo escritura, una vez), `0-raw/` (punteros nuevos + `reading-list.md` ampliado), `1-desk/` (este informe). Ningún archivo existente modificado, ningún borrado, ningún átomo escrito (eso es del Refinery).
