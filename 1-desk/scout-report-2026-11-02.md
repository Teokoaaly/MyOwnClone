# Scout Report — 2026-11-02

**Generated:** 2026-11-02 (cron run, 23:00 shift)
**Vault:** `/home/haxth3/wiki`
**Reading list:** `0-raw/reading-list.md` — 15 URLs (3 lotes: infraestructura self-hosted, auth/SSO multi-tenant, operaciones y red)
**Total URLs attempted:** 15
**Successfully fetched:** 15
**Unreachable:** 0

## URLs successfully fetched (with word counts)

| # | URL | Slug | Word count | Method |
|---|-----|------|------------|--------|
| 1 | https://www.hetzner.com/cloud/ | hetzner-cloud | 1.293 | web_extract |
| 2 | https://www.digitalocean.com/pricing/droplets | digitalocean-droplets-pricing | 3.297 | web_extract |
| 3 | https://www.aiven.io/pricing | aiven-postgresql-pricing | 2.581 | web_extract |
| 4 | https://www.backblaze.com/cloud-storage/pricing | backblaze-b2-storage-pricing | 1.227 | web_extract |
| 5 | https://www.cloudflare.com/developer-platform/products/r2/ | cloudflare-r2-storage | 1.280 | web_extract |
| 6 | https://deepgram.com/pricing | deepgram-pricing | 1.560 | web_extract |
| 7 | https://www.assemblyai.com/pricing | assemblyai-pricing | 4.663 | web_extract |
| 8 | https://www.twilio.com/en-us/sms/pricing | twilio-sms-pricing | 2.212 | web_extract |
| 9 | https://brightdata.com/pricing | brightdata-pricing | 750 | web_extract |
| 10 | https://clerk.com/pricing | clerk-pricing | 2.994 | web_extract |
| 11 | https://workos.com/pricing | workos-pricing | 601 | web_extract (tablas markdown) |
| 12 | https://auth0.com/pricing | auth0-pricing | 4.068 | web_extract (doc `.md` de precios) |
| 13 | https://tailscale.com/kb | tailscale-docs | 316 | web_extract (redirige a `/docs`) |
| 14 | https://www.lambda.ai/pricing | lambda-gpu-pricing | 236 | web_extract |
| 15 | https://learn.microsoft.com/en-us/azure/architecture/ | azure-architecture-center | 272 | web_extract |

Archivos: `sources/2026-11-02-{slug}.md` (verbatim, read-only).
Punteros: `0-raw/2026-11-02-{slug}.md` (15, `Status: ready`).

## Unreachable

Ninguno. Sin paywalls, sin muros de auth, sin errores de extracción.

## Comparativa con la captura de ayer (2026-11-01)

La lista de lectura **no ha cambiado desde el 2026-10-29**: es la tercera noche consecutiva con las mismas 15 URLs. Comprobé el material nuevo contra `sources/2026-11-01-*.md` con dos medidas: similitud de texto y extracción de tokens monetarios.

| Slug | Palabras (ayer → hoy) | Tokens €/$ (ayer → hoy) | Tokens solo hoy | Veredicto |
|---|---|---|---|---|
| deepgram-pricing | 1.560 → 1.560 | 64 → 64 | 0 | idéntico |
| clerk-pricing | 2.994 → 2.994 | 66 → 66 | 0 | idéntico |
| auth0-pricing | 4.068 → 4.068 | 209 → 209 | 0 | idéntico |
| twilio-sms-pricing | 2.212 → 2.212 | 108 → 108 | 0 | sin cambios de precio |
| digitalocean-droplets-pricing | 3.321 → 3.297 | 79 → 79 | 0 | sin cambios de precio |
| aiven-postgresql-pricing | 3.508 → 2.581 | 18 → 18 | 0 | sin cambios de precio (texto más corto) |
| backblaze-b2-storage-pricing | 1.868 → 1.227 | 13 → 13 | 0 | sin cambios de precio (texto más corto) |
| cloudflare-r2-storage | 1.311 → 1.280 | 7 → 7 | 0 | sin cambios de precio |
| assemblyai-pricing | 4.307 → 4.663 | 197 → 198 | `$15 per` ×1 | sin cambios de precio; +1 token ("$15 per TB/mes" FAQ Overdrive) |
| brightdata-pricing | 743 → 750 | 0 → 0 | — | índice sin cifras (ver abajo) |
| hetzner-cloud | 1.668 → 1.293 | 7 → 16 | `€ 5.99` ×2, `€ 0.00` ×3, `€ 1.00`, `€ 0.0096`, `€ 1,571.91`, `€ 1,296.59`, `€ 1,336.39` | el nuevo extract incluye la calculadora de coste y la comparativa de egreso que ayer faltaban; `€ 72.70 per` de ayer desapareció (era del texto de cookies/navegación, no de precio de producto) |

**Conclusión verificada: ningún precio de producto cambió entre 2026-11-01 y 2026-11-02.** Las diferencias de longitud de texto son de renderizado (la extracción de ayer incluía banners de cookies y tablas que hoy no aparecen), no de contenido. La única mejora real es Hetzner, que hoy trae la calculadora de coste con el desglose por vCPU/hora (€ 0.0096/h, 20 TB incluidos, € 1.00/TB extra en la UE).

## Notas de método

- `web_extract` en tres tandas de 5 URLs. Las páginas grandes se desbordaron a disco (`~/.hermes/cache/web/`); el texto completo se leyó de ahí para escribir las fuentes sin re-emitirlo por el contexto.
- **Hetzner**: la captura del 11-01 vino del reader de Jina (con banners de cookies); la de hoy vía `web_extract` es más limpia y añade la calculadora de coste. Contenido más útil, no menos.
- **Aiven / Backblaze**: el extract de hoy es ~25-35% más corto que el de ayer sin perder ningún token monetario → es que la página tiene menos texto navegable ahora, no que falten datos.
- **Auth0**: `auth0.com/pricing` devuelve HTML vacío (tracker de anuncios); `auth0.com/pricing.md` sí devuelve el documento de precios completo en markdown. Capturado desde ahí (mismo método que el 11-01).
- **Tailscale**: `tailscale.com/kb` redirige a `tailscale.com/docs` (índice de documentación, no página de precios). Capturado el índice real.
- **Bright Data**: `brightdata.com/pricing` es un índice con enlaces a subpáginas; 0 tokens monetarios en la raíz.
- **WorkOS**: renderizado a tablas markdown desde `web_extract` (mismo tratamiento que el 11-01, cuando Jina recortaba a 636 palabras).

## Datos clave presentes en las fuentes (verificados)

| Fuente | Dato confirmado en el texto |
|---|---|
| Hetzner Cloud | CPX02 1 vCPU AMD € 5.99/mes (excl. VAT); 20 TB tráfico incluido; € 1.00/TB adicional en la UE; € 0.0096/hora; egreso AWS € 1,571.91/mes vs Hetzner € 0.00/mes a 20 TB; SLA 99.9% |
| DigitalOcean | Basic 512 MiB $4.00/mes ($0.00595/h); 1 GiB $6.00; 2 GiB $12.00; 4 GiB $24.00; CPU-Optimized 2 vCPU $42.00; General Purpose 8 GiB $63.00; per-second billing desde 2026-01-01 |
| Aiven PostgreSQL | Free $0 · Developer $5 · Hobbyist $12 · Startup $75 · Business $180 · Premium $270/mes; PITR 2/14/30 días según plan; BYOC disponible |
| Backblaze B2 | $6.95/TB/mes (B2) · $15/TB/mes (B2 Overdrive, egress ilimitado); egress gratis hasta 3× el almacenamiento; $0.01/GB excedente; Class D $0.004/10k calls; primeros 10 GB gratis |
| Cloudflare R2 | Standard $0.015/GB-month · Infrequent Access $0.01/GB-month + $0.01/GB de recuperación; Class A $4.50/M, Class B $0.36/M; 10 GB-month gratis; sin coste de egreso |
| Deepgram | Nova-3 monolingüe $0.0077/min ($0.46/h), multilingüe $0.0092/min; Growth prepago desde $4,000/año hasta 20% menos; crédito inicial $200 (~43.000 min); endpoint EU (api.eu.deepgram.com); diarization $0.0020/min |
| AssemblyAI | Universal-3.5 Pro $0.21/h · Universal-2 $0.15/h; keyterms +$0.05/h; diarization +$0.02/h; Medical Mode +$0.15/h |
| Twilio SMS (US) | SMS $0.0083/segmento (outbound e inbound, long code/toll-free/short code); MMS outbound $0.022; carrier fees AT&T $0.0035–T-Mobile $0.0045–Verizon $0.005; fallo $0.001/msg; long code $1.15/mes, toll-free $2.15/mes; short code aleatorio $1,000/trimestre |
| Bright Data | 400M+ IPs residenciales mensuales; 50.000+ clientes; los precios concretos están en subpáginas |
| Clerk | Hobby $0 (50.000 MRU/app); Pro $25/mes o $20/mes anual; Business $300/mes o $250/mes anual; MRU = usuario que vuelve 24h+ tras el registro; SMS auth US/CA $0.01; SSO extra $75/mo; B2B org extra $1/mo; Protection $0.002/check tras 10.000/mes |
| WorkOS | AuthKit 1M MAUs gratis, luego $2.500/1M; SSO $125→$65 por conexión; Audit Logs $125/mo (streaming) + $99/mo (retención); Radar $100/50K checks; dominio custom $99/mo; Scale $1.000/mo; Enterprise SLA 99.99% |
| Auth0 | Free hasta 25.000 MAUs; Essentials $35 (B2C) / $150 (B2B); Professional $240 (B2C) / $800 (B2B) a 500 MAUs; yearly = 11× mensual; AI Agents +50%; SSO connection extra $100/mes; M2M 2.500 tokens $10/mes |
| Tailscale | plataforma Zero Trust de conectividad por identidad (sustituye VPN/SASE/PAM); el índice de docs no contiene precios |
| Lambda | B200 $6.69/GPU/hr · H100 $3.99 · A100 80GB $2.79 · A100 40GB $1.99 · V100 $0.79; clusters B200 desde $9.86/GPU/hr (16 GPUs) |
| Azure Architecture Center | catálogo de patrones, arquitecturas de referencia y guías del Well-Architected Framework; sin precios |

## Requiere atención humana

1. **La lista de lectura lleva tres noches sin rotar.** Las mismas 15 URLs se recapturan a diario y el material es idéntico (verificado: 0 cambios de precio en 12 de 12 fuentes con cifras; Hetzner solo gana detalle de calculadora). El Scout solo lee la lista, así que no la he tocado. Para que el Refinery no genere átomos duplicados de un lote ya refinado, conviene **vaciar `0-raw/reading-list.md` o sustituirlo por URLs nuevas**. Los 15 punteros de hoy están en `0-raw/` con `Status: ready`: si el Refinery ya procesó el lote del 11-01, estos son redundantes salvo por el detalle nuevo de Hetzner.
2. **Bright Data y Tailscale no aportan cifras en la URL raíz** (ya detectado el 11-01, sin resolver). Si el Refinery necesita coste de proxies o de red, hacen falta `/pricing/proxy-network` y `/pricing/web-scraper` (Bright Data) y `/pricing` (Tailscale).
3. **Ejes aún sin cubrir en este lote**: colas/mensajería (SQS/Redis Streams/RabbitMQ), email transaccional (cubierto el 10-29), observabilidad (cubierto el 10-29), vector store self-hosted (cubierto el 10-29) y **facturación de IA por token** (ninguna URL de OpenRouter/OpenAI/LiteLLM en este lote).
4. **Fricción sin resolver en el material**: el "egress gratis" de R2 tiene matiz (Cloudflare no cobra egreso pero sí las operaciones Class A/B, $4.50/M y $0.36/M); y Backblaze B2 ($6.95/TB) vs R2 Standard ($0.015/GB-month = $15/TB) no son comparables sin normalizar unidades ni unambigüedad sobre si el egreso de B2 (3× gratis) cubre el patrón de uso real.
