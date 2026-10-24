---
id: 2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---

## Claim
DataImpulse ofrece cuatro tipos de proxy con posicionamiento explícito. **Residencial**: "real IP addresses assigned by internet service providers", first-party, ethical, country targeting gratis; usos: web scraping, market research, SERP tracking, ad verification, AI training. **Móvil**: "route through real carrier networks (**5G/4G/3G/LTE**)", "the most defended IPs", "Low block rates", sticky sessions; usos: social media management, in-app QA, ad verification, scraping donde las IPs residenciales están bloqueadas; la propia página matiza que "3G works for basic scraping on static pages, but JavaScript-heavy websites need 4G, while high-volume scraping performs best with 4G or 5G". **Datacenter**: "server-based IPs", "Sub-100 ms latency", "Randomized datacenter (smooth subnet access)", "**99.9% uptime**"; usos: price and SERP monitoring, brand protection, ad verification. **Premium residencial**: "high-quality IP addresses", "All targeting options included", "Dedicated Proxy Manager, extra API endpoints, and free filtering by country, state, city, ZIP, and ASN"; usos: SERP&SEO monitoring, market research, scraping, localization, QA testing.

## Why It Matters
La segmentación no es de marketing sino de **rendimiento por euro**: si el objetivo es scraping simple de páginas estáticas, el datacenter a $0.50/GB con 99.9 % de uptime gana; si la plataforma bloquea IPs de servidor, el móvil a $2/GB es el que "no está bloqueado"; el premium residencial a $5/GB es el único que incluye todo el targeting y un Proxy Manager dedicado.
Para el vault esto mapea directamente contra su pipeline de ingesta asíncrono ([[2026-1022-myclone-scraping-ingestion-pipeline]]): los endpoints `/scraping/website` y `/scraping/bulk-onboard` son precisamente el tipo de carga que distingue "cheap and blocked" de "expensive and working", y el matiz 3G/4G/5G es una decisión de coste por tarea, no un detalle de configuración.

## Nota de verificación
Las declaraciones de latencia (<100 ms), uptime (99.9 %) y de "low block rates" son **claims del propio proveedor**, no medidas verificadas por la captura; la captura no publica latencia por país ni tasa de bloqueo medida.
