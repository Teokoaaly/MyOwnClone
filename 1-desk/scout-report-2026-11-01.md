# Scout Report — 2026-11-01

**Generated:** 2026-11-01 (cron run, 23:00 shift)
**Vault:** `/home/haxth3/wiki`
**Reading list:** `0-raw/reading-list.md` — 15 URLs (3 lotes: infraestructura self-hosted, auth/SSO multi-tenant, operaciones y red)
**Total URLs attempted:** 15
**Successfully fetched:** 15
**Unreachable:** 0

## URLs successfully fetched (with word counts)

| # | URL | Slug | Word count | Method |
|---|-----|------|------------|--------|
| 1 | https://www.hetzner.com/cloud/ | hetzner-cloud | 1.678 | jina reader |
| 2 | https://www.digitalocean.com/pricing/droplets | digitalocean-droplets-pricing | 3.331 | jina reader |
| 3 | https://www.aiven.io/pricing | aiven-postgresql-pricing | 3.518 | jina reader |
| 4 | https://www.backblaze.com/cloud-storage/pricing | backblaze-b2-storage-pricing | 1.878 | jina reader |
| 5 | https://www.cloudflare.com/developer-platform/products/r2/ | cloudflare-r2-storage | 1.321 | jina reader |
| 6 | https://deepgram.com/pricing | deepgram-pricing | 1.566 | web_extract |
| 7 | https://www.assemblyai.com/pricing | assemblyai-pricing | 4.317 | web_extract |
| 8 | https://www.twilio.com/en-us/sms/pricing | twilio-sms-pricing | 2.222 | web_extract |
| 9 | https://brightdata.com/pricing | brightdata-pricing | 753 | web_extract |
| 10 | https://clerk.com/pricing | clerk-pricing | 3.004 | web_extract |
| 11 | https://workos.com/pricing | workos-pricing | 611 | web_extract (render manual a tablas) |
| 12 | https://auth0.com/pricing | auth0-pricing | 4.078 | jina reader (`.md` pricing doc) |
| 13 | https://tailscale.com/kb | tailscale-docs | 1.806 | jina reader (redirige a `/docs`) |
| 14 | https://www.lambda.ai/pricing | lambda-gpu-pricing | 1.270 | jina reader |
| 15 | https://learn.microsoft.com/en-us/azure/architecture/ | azure-architecture-center | 1.172 | jina reader |

Archivos: `sources/2026-11-01-{slug}.md` (verbatim, read-only).
Punteros: `0-raw/2026-11-01-{slug}.md` (15, `Status: ready`).

## Unreachable

Ninguno. Sin paywalls, sin muros de auth, sin errores de extracción.

## Notas de método

- La lista de lectura **no ha cambiado** desde el turno del 2026-10-31: contiene las mismas 15 URLs del lote 2026-10-29. Es una re-captura (la página de precios puede haber cambiado), archivada bajo la fecha de hoy. Precedente en el vault: `2026-10-22-hetzner-cloud.md` y `2026-10-31-hetzner-cloud.md` coexisten.
- `web_extract` se ejecutó en dos tandas (5 URLs cada una). La tanda de 5 (deepgram, assemblyai, twilio, brightdata, clerk) devolvió 107 KB y se desbordó a disco; se parseó el JSON del spillover para escribir las fuentes sin re-emitir el contenido por el contexto. La otra tanda (workos, auth0, tailscale, lambda, azure) volvió inline.
- Para las URLs cuyo `web_extract` inline Was voluminoso, se usó el reader de Jina (`r.jina.ai`) como vía de escritura directa a disco, y se verificó **paridad de cifras** contra el `web_extract` de la tanda anterior: los conjuntos de tokens monetarios coinciden ($ deepgram 40/40, assemblyai 55/55, clerk 27/30 con 3 falsos positivos, brightdata 10/0 — la página de brightdata expone los precios en subpáginas, el extract principal es un índice).
- **WorkOS** fue el único caso donde el reader de Jina recortaba la página a 636 palabras perdiendo las tablas de SSO/Directory Sync/Audit Logs/Radar. Se sobrescribió con la extracción de `web_extract` renderizada a tablas markdown (fichero `sources/2026-11-01-workos-pricing.md`, 611 palabras). La tabla de precios por número de conexiones ($125/$100/$80/$65) es la fuente primaria.
- **Auth0**: `auth0.com/pricing` devuelve HTML vacío (tracker de anuncios); `auth0.com/pricing.md` sí devuelve el documento de precios completo en markdown (334 líneas de tabla, 105 tokens monetarios). Capturado desde ahí.
- **Tailscale**: `tailscale.com/kb` redirige a `tailscale.com/docs` (índice de documentación, no página de precios). Capturado el índice real.

## Datos clave presentes en las fuentes (verificados)

| Fuente | Dato confirmado en el texto |
|---|---|
| Hetzner Cloud | CPX02 1 vCPU AMD € 5.99/mes (excl. VAT); 20 TB tráfico incluido; € 1.00/TB adicional en la UE; SLA 99.9% |
| DigitalOcean | Basic 512 MiB $4.00/mes; CPU-optimized 2 vCPU $42/mes; snapshots $0.06/GB/mes; backups 20% (semanal) / 30% (diario) |
| Aiven PostgreSQL | Free $0 · Developer $5 · Hobbyist $12 · Startup $75 · Business $180 · Premium $270/mes |
| Backblaze B2 | $6.95/TB/mes (B2) · $15/TB/mes (B2 Overdrive); egress gratis hasta 3× el almacenamiento; $0.01/GB excedente |
| Cloudflare R2 | Standard $0.015/GB-month · Infrequent Access $0.01/GB-month; Class A $4.50/M, Class B $0.36/M; 10 GB gratis |
| Deepgram | $200 de crédito inicial; Growth prepago hasta 20% de ahorro ($4.000+/año) |
| AssemblyAI | precio por hora de audio y por minuto |
| Twilio SMS | precios por segmentación de país |
| Bright Data | 400M+ IPs residenciales mensuales; los precios concretos están en subpáginas |
| Clerk | precio por MAU (10K / 100K / 1M) |
| WorkOS | AuthKit 1M MAUs gratis, luego $2,500/1M; SSO $125→$65 por conexión; Audit Logs $125/mo (streaming) + $99/mo (retención); Radar $100/50K checks; dominio custom $99/mo; Scale $1,000/mo |
| Auth0 | Free hasta 25.000 MAUs; Essentials $35 (B2C) / $150 (B2B); Professional $240 (B2C) / $800 (B2B) a 500 MAUs; yearly = 11× mensual; AI Agents +50% |
| Tailscale | plataforma Zero Trust de conectividad por identidad; el índice de docs no contiene precios |
| Lambda | B200 $6.69/GPU/hr · H100 $3.99 · A100 80GB $2.79 · A100 40GB $1.99 · V100 $0.79; clusters B200 desde $9.86/GPU/hr (16 GPUs) |
| Azure Architecture Center | catálogo de patrones, arquitecturas de referencia y guías del Well-Architected Framework; sin precios |

## Requiere atención humana

1. **La lista de lectura no rota.** Las mismas 15 URLs llevan dos noches seguidas. Si el objetivo era capturarlas una sola vez, conviene vaciar `0-raw/reading-list.md` (no lo he tocado: el Scout solo lee) o añadir URLs nuevas para el lote del 2026-11-02. Ejes aún sin cubrir en esta tanda: **gestión de correo transaccional** (ya cubierto el 10-29), **observabilidad** (Langfuse/Sentry — 10-29), **vector store self-hosted** (Qdrant/Weaviate — 10-29), **facturación de IA por token** (ninguna URL de OpenRouter/OpenAI/LiteLLM/OpenAI-compatible en este lote) y **colas/CronJobs**.
2. **Bright Data y Tailscale no aportan precios en la URL raíz.** La página de brightdata.com/pricing es un índice (los precios están en `/pricing/proxy-network`, `/pricing/web-scraper`); tailscale.com/kb redirige al índice de docs. Si el Refinery necesita cifras de coste de proxies o de red, hacen falta las subpáginas específicas.
3. **El atómico de Hetzner del 10-31 ya existía** (`2-atoms/2026-1031-hetzner-cloud.md`, 15 átomos del lote 10-31 ya refinados). La re-captura de hoy puede generar duplicación de átomos si no se marca como actualización. No lo he tocado: eso es trabajo del Refinery.
4. **Fricción ya visible en el propio material**: el precio de salida de DigitalOcean ($4.00/mes el más barato) y los $6.95/TB de Backblaze vs los $0.015/GB-month de R2 ($15/TB) no son comparables en la misma unidad sin normalizar; y el claim de "egress gratis" de R2 tiene Matiz — Cloudflare no cobra egreso pero sí las operaciones de clase A/B.
