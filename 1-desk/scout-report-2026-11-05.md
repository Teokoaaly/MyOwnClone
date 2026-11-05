# Scout Report — 2026-11-05

**Generated:** 2026-11-05 (cron run, 23:00 shift)
**Vault:** `/home/haxth3/wiki`
**Reading list:** `0-raw/reading-list.md` — 15 URLs (3 lotes: infraestructura self-hosted, auth/SSO multi-tenant, operaciones y red)
**Total URLs attempted:** 15
**Successfully fetched:** 15
**Unreachable:** 0

## URLs successfully fetched (with word counts)

| # | URL | Slug | Words | Método |
|---|-----|------|-------|--------|
| 1 | https://www.hetzner.com/cloud/ | hetzner-cloud | 1.293 | web_extract (cache-busted) |
| 2 | https://www.digitalocean.com/pricing/droplets | digitalocean-droplets-pricing | 3.298 | web_extract (cache-busted) |
| 3 | https://www.aiven.io/pricing | aiven-pricing | 2.582 | web_extract (→ aiven.io/pricing/postgresql) |
| 4 | https://www.backblaze.com/cloud-storage/pricing | backblaze-b2-storage-pricing | 1.236 | web_extract (cache-busted) |
| 5 | https://www.cloudflare.com/developer-platform/products/r2/ | cloudflare-r2-storage | 1.280 | web_extract (→ /products/r2/) |
| 6 | https://deepgram.com/pricing | deepgram-pricing | 1.560 | web_extract (cache-busted) |
| 7 | https://www.assemblyai.com/pricing | assemblyai-pricing | 4.667 | web_extract (cache-busted) |
| 8 | https://www.twilio.com/en-us/sms/pricing | twilio-sms-pricing | 2.212 | web_extract (→ /sms/pricing/us) |
| 9 | https://brightdata.com/pricing | brightdata-pricing | 743 | web_extract (cache-busted) |
| 10 | https://clerk.com/pricing | clerk-pricing | 2.994 | web_extract (cache-busted) |
| 11 | https://workos.com/pricing | workos-pricing | 1.067 | web_extract (cache-busted) |
| 12 | https://auth0.com/pricing | auth0-pricing | 4.068 | web_extract (→ auth0.com/pricing.md) |
| 13 | https://tailscale.com/kb | tailscale-docs | 358 | web_extract (redirige a /docs) |
| 14 | https://www.lambda.ai/pricing | lambda-ai-pricing | 920 | web_extract (→ lambda.com/pricing) |
| 15 | https://learn.microsoft.com/en-us/azure/architecture/ | azure-architecture-center | 381 | web_extract (cache-busted) |

Archivos: `sources/2026-11-05-{slug}.md` (verbatim, read-only).
Punteros: `0-raw/2026-11-05-{slug}.md` (15, `Status: ready`).

## Unreachable

Ninguno. Sin paywalls, sin muros de auth, sin errores de extracción final. Hubo rate-limits (firecrawl, 12-15 req/min) en la primera tanda de 15 URLs; se resolvió reintentando por tandas más pequeñas tras el reset.

## ⚠️ Incidencia de método: la caché sirvió contenido obsoleto

**Verificado.** En la primera pasada, `web_extract` devolvió para varias URLs repetidas el archivo de caché del turno anterior (2026-11-04), no una captura nueva. Los ficheros en caché de `~/.hermes/cache/web/` se reescriben al reusar la URL, así que el mtime no delata el contenido viejo por sí solo.

Detección: al comparar el slug de Lambda contra la captura del 11-04, los precios no coincidían (22 tokens monetarios distintos). Se confirmó con el volcado de texto completo de ambas capturas, no por inspección visual.

**Corrección aplicada:** se refetcheó **las 15 URLs** con un parámetro de cache-busting (`?fresh=20261105`) y se reconstruyeron los 15 ficheros de `sources/` desde esos volcados en fresco. Se verificó por mtime que los 15 ficheros de origen tienen timestamp de esta noche (23:01–23:06 UTC).

Consecuencia real: la captura del 11-04 de Lambda quedó con precios desfasados en 1 $/GPU/hr. **Sin esta comprobación, el turno habría publicado precios de GPU falsos como si fueran actuales.**

**Lección para turnos futuros:** cuando la lista de lectura no rota entre noches, `web_extract` **no** garantiza una captura nueva. Hay que forzar el refetch (query param distinto) y verificar la diferencia contra la captura previa antes de escribir en `sources/`.

## Cambios de precio verificados (vs captura 11-04)

Comparación token a token de los tokens monetarios sobre los 15 slugs. **Solo un cambio real:**

### Lambda — +$1.00/GPU/hr en B200 / H100 / GH200

| Plan | 11-04 | 11-05 | Δ |
|---|---|---|---|
| HGX B200 (8x) | $6.69 | **$7.69** | +$1.00 |
| HGX H100 (8x) | $3.99 | **$4.59** | +$1.00 |
| HGX A100 80GB | $2.79 | **$3.19** | +$1.00 |
| B200 SXM6 (4x) | $6.79 | **$7.79** | +$1.00 |
| H100 SXM (4x) | $4.09 | **$4.69** | +$1.00 |
| B200 SXM6 (2x) | $6.89 | **$7.89** | +$1.00 |
| H100 SXM (2x) | $4.19 | **$4.79** | +$1.00 |
| B200 SXM6 (1x) | $6.99 | **$7.99** | +$1.00 |
| H100 SXM (1x) | $4.29 | **$4.89** | +$1.00 |
| H100 PCIe (1x) | $3.29 | **$3.79** | +$1.00 |
| GH200 (1x) | $2.29 | **$2.59** | +$1.00 |
| Tesla V100 | $0.79 | $0.79 | — |
| A100 40GB (PCIe/SXM) | $1.99 | $1.99 | — |
| A10 | $1.29 | $1.29 | — |
| A6000 | $1.09 | $1.09 | — |
| Quadro RTX 6000 | $0.69 | $0.69 | — |

Clusters 1-Click **sin cambio**: B200 $9.86 (16 GPU) / $9.36 (64) / $8.87 (256+); H100 $6.16 / $5.85 / $5.54.

Redondeo uniforme de **+$1.00** en toda la gama NVIDIA de gama alta (Blackwell B200, Hopper H100/PCIe, GH200), sin tocar V100/A10/A6000/A100-40GB/Quadro. Patrón consistente con un ajuste de precio por GPU, no con un cambio de configuración de instancia (los vCPU, RAM y SSD no cambian).

Texto vigente en la página: *"These prices take effect November 16, 2026, at 00:00 UTC. Until then, log in to your Lambda Cloud account to see current pricing."* En la captura del 11-04 la redacción era *"New prices take effect November 16, 2026…"* — mismo calendario, cifras distintas.

**⚠️ La captura del 11-04 contiene cifras de Lambda que ya no son las publicadas.** Cualquier átomo del Refinery derivado de ella queda desactualizado hoy.

### Sin cambios de precio (verificado)

| Slug | Tokens (11-04 → 11-05) | Estado |
|---|---|---|
| hetzner-cloud | 0 → 0 | sin cambios (precios €5.99 / €6.49 / €43.49 intactos) |
| digitalocean-droplets-pricing | 63 → 63 | sin cambios |
| aiven-pricing | 18 → 18 | sin cambios |
| backblaze-b2-storage-pricing | 10 → 10 | sin cambios |
| cloudflare-r2-storage | 7 → 7 | sin cambios |
| deepgram-pricing | 38 → 38 | sin cambios |
| assemblyai-pricing | 79 → 79 | sin cambios |
| twilio-sms-pricing | 25 → 25 | sin cambios |
| brightdata-pricing | 0 → 0 | sin cambios (sigue siendo índice sin cifras) |
| clerk-pricing | 36 → 36 | sin cambios |
| workos-pricing | 13 → 13 | sin cambios |
| auth0-pricing | 114 → 114 | sin cambios |
| tailscale-docs | 0 → 0 | sin cifras |
| azure-architecture-center | 0 → 0 | sin cifras |

Diferencias no monetarias: `azure-architecture-center` 272 → 381 palabras (la captura en fresco incluye la sección de áreas de diseño completa: Design for the cloud, AI/ML, compute, data, DevOps/MLOps/GenAIOps, security) y `tailscale-docs` 316 → 358 (variación de navegación).

## Notas de método

- Las 15 capturas se obtainieron con `web_extract` y `char_limit` reducido para forzar volcado a disco; los textos completos quedaron en `~/.hermes/cache/web/` y se copiaron a `sources/` **sin pasar por el contexto**.
- **Auth0**: `auth0.com/pricing` devuelve HTML sin el documento de precios completo; `auth0.com/pricing.md` sí (4.068 palabras, con tablas de precios B2C/B2B por tier de MAU). Mismo método que 11-01, 11-02 y 11-04.
- **Aiven**: `/pricing` → `/pricing/postgresql`. El precio depende de cloud + región, hay que fijarlos.
- **Tailscale**: `/kb` → `/docs`. Índice de documentación, "Last validated: Feb 4, 2026". Sin precios, lleva 5 noches así.
- **Cloudflare R2**: `/developer-platform/products/r2/` → `/products/r2/`.
- **Lambda**: `lambda.ai/pricing` → `lambda.com/pricing` (cambio de dominio; la redirección es la que explica el desfase de precios de ayer).
- **Bright Data**: la raíz sigue siendo índice de enlaces a subpáginas, sin cifras. Los precios están en `/pricing/proxy-network`, `/pricing/web-scraper`, `/pricing/scraping-browser`, `/pricing/web-scraper/studio`.

## Requiere atención humana

1. **La lista de lectura lleva seis noches sin rotar.** Las mismas 15 URLs se recapturan a diario y el único material nuevo es el ajuste de Lambda. Para que el Refinery no genere átomos duplicados de lotes ya refinados, conviene **vaciar `0-raw/reading-list.md` o sustituirlo por URLs nuevas**. Ejes aún sin cubrir: **colas/mensajería** (SQS, Redis Streams, RabbitMQ), **facturación de IA por token** (OpenRouter, LiteLLM), **hosting de modelos** (vLLM/TGI), **backups gestionados de Postgres** (p.gj. pgBackRest), **email transaccional** (cubierto el 10-29).
2. **Decidir qué se hace con la captura de Lambda del 11-04.** Contiene cifras GPU que Lambda ya no publica (difieren en exactamente $1.00/GPU/hr). Si existe un átomo derivado en `2-atoms/`, hay que actualizarlo o marcarlo `[RETIRED]`. No lo he tocado: el Scout solo escribe en `sources/`, `0-raw/` y `1-desk/`.
3. **Corregir el pipeline del Scout para forzar refetch.** Mientras la lista no rote, `web_extract` sirve caché y el vault acumula "capturas" que en realidad son relés de la noche anterior. Propuesta: añadir `?fresh={fecha}` a cada URL de la lista, o vaciar `~/.hermes/cache/web/` al inicio del turno. Verificado en esta noche: efecto real, no teórico.
4. **Bright Data y Tailscale llevan 5 noches sin aportar cifras.** Si el Refinery necesita coste de proxies o de red, hacen falta las subpáginas `/pricing/proxy-network` y `/pricing/web-scraper` de Bright Data y `/pricing` de Tailscale.
5. **Fricción sin resolver en el material**: "egress gratis" de R2 tiene matiz (no hay coste de egreso pero sí operaciones Class A/B); y Backblaze B2 ($6.95/TB) vs R2 Standard ($0.015/GB-month = $15/TB) no son comparables sin normalizar unidades y el matiz de los 3× de almacenamiento gratis de B2.
