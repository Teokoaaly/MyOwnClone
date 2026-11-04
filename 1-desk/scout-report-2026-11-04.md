# Scout Report — 2026-11-04

**Generated:** 2026-11-04 (cron run, 23:00 shift)
**Vault:** `/home/haxth3/wiki`
**Reading list:** `0-raw/reading-list.md` — 15 URLs (3 lotes: infraestructura self-hosted, auth/SSO multi-tenant, operaciones y red)
**Total URLs attempted:** 15
**Successfully fetched:** 15
**Unreachable:** 0

## URLs successfully fetched (with word counts)

| # | URL | Slug | Words | Método |
|---|-----|------|-------|--------|
| 1 | https://www.hetzner.com/cloud/ | hetzner-cloud | 1.293 | web_extract |
| 2 | https://www.digitalocean.com/pricing/droplets | digitalocean-droplets-pricing | 3.298 | web_extract |
| 3 | https://www.aiven.io/pricing | aiven-pricing | 2.581 | web_extract (→ aiven.io/pricing/postgresql) |
| 4 | https://www.backblaze.com/cloud-storage/pricing | backblaze-b2-storage-pricing | 1.228 | web_extract |
| 5 | https://www.cloudflare.com/developer-platform/products/r2/ | cloudflare-r2-storage | 1.280 | web_extract (→ /products/r2/) |
| 6 | https://deepgram.com/pricing | deepgram-pricing | 1.560 | web_extract |
| 7 | https://www.assemblyai.com/pricing | assemblyai-pricing | 4.663 | web_extract |
| 8 | https://www.twilio.com/en-us/sms/pricing | twilio-sms-pricing | 2.212 | web_extract (→ /sms/pricing/us) |
| 9 | https://brightdata.com/pricing | brightdata-pricing | 743 | web_extract |
| 10 | https://clerk.com/pricing | clerk-pricing | 2.994 | web_extract |
| 11 | https://workos.com/pricing | workos-pricing | 1.067 | web_extract |
| 12 | https://auth0.com/pricing | auth0-pricing | 4.068 | web_extract (→ auth0.com/pricing.md) |
| 13 | https://tailscale.com/kb | tailscale-docs | 316 | web_extract (redirige a /docs) |
| 14 | https://www.lambda.ai/pricing | lambda-gpu-pricing | 920 | web_extract |
| 15 | https://learn.microsoft.com/en-us/azure/architecture/ | azure-architecture-center | 272 | web_extract |

Archivos: `sources/2026-11-04-{slug}.md` (verbatim, read-only).
Punteros: `0-raw/2026-11-04-{slug}.md` (15, `Status: ready`).

## Unreachable

Ninguno. Sin paywalls, sin muros de auth, sin errores de extracción.

## Comparativa con la captura anterior (verificada)

La lista de lectura **no ha cambiado desde el 2026-10-29**: quinta noche consecutiva con las mismas 15 URLs. Se comparó el material nuevo contra la captura más reciente de cada slug (11-03 para 12 slugs, 11-02 para 3: brightdata, cloudflare, lambda) con extracción de tokens monetarios y de marcadores de novedad.

| Slug | Comparado con | Palabras (prev → hoy) | Tokens monetarios (prev → hoy) | Novedad real |
|---|---|---|---|---|
| clerk-pricing | 11-02 | 2.994 → 2.994 | 66 → 66 | ninguna |
| cloudflare-r2-storage | 11-02 | 1.280 → 1.280 | 7 → 7 | ninguna |
| azure-architecture-center | 11-02 | 272 → 272 | 0 → 0 | ninguna |
| brightdata-pricing | 11-02 | 750 → 743 | 0 → 0 | ninguna (sigue siendo índice sin cifras) |
| lambda-gpu-pricing | 11-02 | 236 → 920 | 8 → 28 | **nuevos precios + fecha de cambio** |
| deepgram-pricing | 11-03 | 1.382 → 1.560 | 64 → 64 | columnas de precio/hora añadidas |
| twilio-sms-pricing | 11-03 | 1.607 → 2.212 | 106 → 108 | **sección RCS + Traffic Optimization Engine** |
| workos-pricing | 11-03 | 769 → 1.067 | 24 → 33 | **tablas de Audit Logs / Radar recuperadas** |
| aiven-pricing | 11-03 | 1.461 → 2.581 | 16 → 18 | cifra de coste self-managed ($150k–$300k+/año) |
| digitalocean-droplets-pricing | 11-03 | 1.479 → 3.298 | 70 → 79 | tablas completas de droplets |
| assemblyai-pricing | 11-03 | 485 → 4.663 | 16 → 198 | **AssemblyAI-TTS-1, Self Hosted, LLM Gateway** |
| auth0-pricing | 11-03 | 819 → 4.068 | 3 → 209 | doc `.md` completo de precios |
| backblaze-b2-storage-pricing | 11-03 | 1.069 → 1.228 | 12 → 13 | sin cambios de precio |
| hetzner-cloud | 11-03 | 1.241 → 1.293 | 18 → 16 | sin cambios de precio (menos ruido de calculadora) |
| tailscale-docs | 11-03 | 300 → 316 | 0 → 0 | sin cambios |

**Conclusión verificada: ningún precio de producto existente cambió.** Las diferencias de longitud y de tokens son de método de captura (la captura del 11-03 fue voluminosa solo en 12 slugs; 5 de esos weren't re-captured). Los "tokens nuevos" en aiven, assemblyai, auth0 y workos proceden de que la captura anterior estaba truncada, no de cambios de precio.

### Novedades verificables de esta tanda

1. **Lambda — cambio de precio announced con fecha.** La página incluye la nota: *"New prices take effect November 16, 2026, at 00:00 UTC. Until then, log in to your Lambda Cloud account to see current pricing."* Las cifras de la tabla son las **nuevas** (B200 SXM6 $6.79/GPU/hr, H100 SXM $4.09, A100 PCIe $1.99, A6000 $1.09 en 8x; B200 HGX $6.69, H100 HGX $3.99, A100 80GB $2.79, A100 40GB $1.99, V100 $0.79 en 1x/4x/8x). Clusters 1-Click: B200 $9.86 (16 GPU) → $8.87 (256+); H100 $6.16 → $5.54.
2. **AssemblyAI — TTS y self-hosting.** Banner: *"AssemblyAI-TTS-1: Text-to-speech for voice agents"*. Nueva navegación con *LLM Gateway*, *Guardrails & Safety*, *Speech Understanding API* y *Self Hosted*. Precios STT: Universal-3.5 Pro $0.21/hr, Universal-2 $0.15/hr; realtime Universal-3.6 Pro $0.12/hr, Universal-Streaming $0.04/hr.
3. **Twilio — RCS y producto nuevo.** Sección RCS con precios por carrier (AT&T $0.0045, T-Mobile $0.0062 out / $0.0025 in, Verizon $0.005, US Cellular $0.0062). Nuevo add-on *Traffic Optimization Engine* "Starting at $300 /month". SMS/MMS US sin cambios: $0.0083 outbound, MMS $0.022, carrier fees AT&T $0.0035–T-Mobile $0.0045–Verizon $0.005.
4. **Deepgram — más detalle de tarifas.** Nova-3 monolingüe $0.0077/min ($0.0065 con volumen), multilingüe $0.0092/min ($0.0078). TTS: Flux $0.0450/1k chars, Aura-2 $0.030, Aura-1 $0.0150. Voice Agent Standard $0.075/min, Advanced $0.163/min. Créditos: $200 iniciales, Growth desde $4.000/año (hasta 20% menos).
5. **Aiven — argumento de coste self-managed.** "$150,000–$300,000+ per year per service" para operar tu propia BD/streaming en producción (salario + on-call + incidentes). Planes PostgreSQL: Free $0 · Developer $5 · Hobbyist $12 · Startup $75 · Business $180 · Premium $270/mes.
6. **WorkOS — tablas recuperadas.** AuthKit $2.500/mes por cada 1M MAU adicionales (1M gratis); SSO y Directory Sync $125/$100/$80/$65 por conexión (1-15, 16-30, 31-50, 51-100); Audit Logs $125/mes streaming + $99/mes por 1M eventos retenidos; Radar $100/mes por 50K checks; dominio custom $99/mes.
7. **DigitalOcean — tabla completa.** Basic 512 MiB $4.00/mes ($0.00595/h) … 16 GiB $96; CPU-optimized 4 GiB $42, 8 GiB $84; General Purpose 8 GiB $63. Facturación por segundo desde 2026-01-01 (mínimo 60 s o $0.01). Snapshots $0.06/GB/mes, backups 20% semanal / 30% diario.
8. **Auth0 — doc completo.** Free hasta 25.000 MAUs; Essentials $35 (B2C) / $150 (B2B) a 500 MAUs; Professional $240 (B2C) / $800 (B2B); yearly = 11× el mensual. El documento incluye tablas de tiers de MAU y add-ons (AI Agents, M2M tokens, Enterprise SSO connections).
9. **Clerk — sin cambios.** Hobby $0 (50.000 MRU/app), Pro $25/mes o $20/mes anual, Business $300/mes o $250/mes anual; SSO extra $75/mo; B2B org extra $1/mo; Protect $0.002/check tras 10.000/mes. Nota: *Directory Sync* $75/mo **desde 1 de enero de 2027**.
10. **Backblaze — sin cambios.** B2 $6.95/TB/mes, B2 Overdrive $15/TB/mes, egress gratis hasta 3× el almacenamiento promedio, excedente $0.01/GB.
11. **Cloudflare R2 — sin cambios.** Standard $0.015/GB-month, Infrequent Access $0.01/GB-month (+$0.01/GB de recuperación), 10 GB gratis, sin coste de egreso.
12. **Tailscale / Azure — sin cifras.** Tailscale redirige a `/docs` (índice, "Last validated Feb 4, 2026"); Azure Architecture Center es catálogo de patrones sin precios.

## Notas de método

- `web_extract` en tres tandas de 5 + 2 URLs (AssemblyAI y Lambda con `char_limit` reducido para forzar volcado a disco). Los 15 textos completos quedaron en `~/.hermes/cache/web/` y se copiaron a `sources/` **sin pasar por el contexto**, evitando truncamiento.
- **Auth0**: `auth0.com/pricing` devuelve HTML vacío (tracker de anuncios); `auth0.com/pricing.md` devuelve el documento de precios completo (4.068 palabras). Mismo método que 11-01/11-02.
- **Aiven**: `/pricing` redirige a `/pricing/postgresql`. Capturado el texto de la página resuelta, con la nota de que el precio es por plan de servicio y hay que fijar cloud + región.
- **Tailscale**: `/kb` → `/docs`. Índice de documentación, sin precios (ya detectado el 11-01, sigue sin resolverse).
- **Bright Data**: la raíz sigue siendo un índice de enlaces a subpáginas, sin cifras. Los precios están en `/pricing/proxy-network`, `/pricing/web-scraper`, `/pricing/scraping-browser`, `/pricing/web-scraper/studio`.
- Se probó antes una vía alternativa con el reader de Jina (`r.jina.ai`) en paralelo: devolvió banners de cookies y tablas peor renderizadas que `web_extract` (ej. Twilio 1.587 palabras vía Jina vs 2.212 con las tablas de carrier fees completas). **Se descartó y se usó solo `web_extract`.**

## Requiere atención humana

1. **La lista de lectura lleva cinco noches sin rotar.** Las mismas 15 URLs se recapturan a diario y el material de precios es idéntico salvo el anuncio de Lambda del 16/11/2026. El Scout solo lee la lista, así que no la he tocado. Para que el Refinery no genere átomos duplicados de lotes ya refinados, conviene **vaciar `0-raw/reading-list.md` o sustituirlo por URLs nuevas**. Ejes aún sin cubrir: **colas/mensajería** (SQS, Redis Streams, RabbitMQ), **facturación de IA por token** (OpenRouter, LiteLLM, OpenAI-compatible), **email transaccional** (cubierto el 10-29), **observabilidad** (cubierto el 10-29), **vector store self-hosted** (cubierto el 10-29) y **hosting de modelos** (vLLM/TGI).
2. **Bright Data y Tailscale llevan 4 noches sin aportar cifras** (detectado el 11-01, sin resolver). Si el Refinery necesita coste de proxies o de red, hacen falta las subpáginas `/pricing/proxy-network` y `/pricing/web-scraper` de Bright Data y `/pricing` de Tailscale.
3. **Lambda es el único cambio de precio real del lote**, y aún no es efectivo (16/11/2026). Si el thread `3-threads/` de hosting/GPU tiene un átomo con las cifras de Lambda, ese átomo queda desactualizado a partir del 16/11. No lo he tocado: eso es trabajo del Refinery.
4. **Fricción sin resolver en el material**: "egress gratis" de R2 tiene matiz (no hay coste de egreso pero sí operaciones Class A/B); y Backblaze B2 ($6.95/TB) vs R2 Standard ($0.015/GB-month = $15/TB) no son comparables sin normalizar unidades y el matiz de los 3× de almacenamiento gratis de B2.
