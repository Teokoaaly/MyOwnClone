# Investigación VPS Baratos + Plan Meta-Search AI Engine
## Sesión completa — Julio 15, 2026

---

## PROYECTO: "Skyscanner de suscripciones AI y APIs"

Meta-buscador que agrega y compara ofertas de cuentas AI (ChatGPT, Claude, Gemini, etc.) y API relays (中转站) a través de mercados chinos (卡网), rusos (lzt.market), y relays independientes.

### Stack propuesto
- **Frontend:** Next.js 14 App Router
- **DB:** Supabase (PostgreSQL)
- **Scrapers:** Node.js (Playwright) corriendo en workers existentes
- **Detector:** Python (fork de Veridrop para verificar relays)
- **Hosting:** Vercel free + VPS barato para scrapers

### Monetización
1. Relays patrocinados (USDT) — pagan por visibilidad, no por score
2. API freemium (datos de precios para terceros)
3. Afiliados (comisión por ventas referidas)
4. Alertas de precio premium

### Diferenciación vs PriceAI.cc
- Multi-idioma (EN, ES, RU, ZH) — no solo chino
- Multi-moneda (USD, EUR, crypto, CNY, RUB)
- API pública + alertas de precio + histórico
- Cubre lzt.market (mercado ruso)
- Mismo rigor Veridrop para verificar relays

### Filtro ético
Solo autoreger/resale legítimo. Nada de cuentas robadas/brute-force/stealer.

---

## ALTERNATIVAS DE HOSTING (de más barata a menos)

### Opción A: $0 — Static + GitHub Pages + Workers existentes
- Frontend estático en GitHub Pages (gratis)
- Datos en JSON generado por cron en workers (hta6ms6, ubuntu-1, picoclaw)
- Búsqueda client-side con fuse.js
- **Límite:** sin cuentas de usuario, sin alerts, sin feedback

### Opción B: $0 — SQLite en worker + archivos estáticos
- SQLite + FastAPI en uno de tus workers
- GitHub Pages frontend consume la API
- Necesita Cloudflare Tunnel (gratis) o Tailscale para exponer sin IP pública

### Opción C: $0 — Cloudflare Workers + D1 + Pages
- Cloudflare Pages (500 builds/mes gratis)
- Cloudflare Workers (100k req/día gratis)
- Cloudflare D1 (SQLite, 5GB gratis)
- Cron Triggers para scrapers
- Todo bajo mismo dominio, SSL gratis
- Escala hasta ~100k usuarios sin pagar

### Opción D: $0 — Telegram Bot first (validación inmediata)
- Bot de Telegram en vez de web
- `/search chatgpt pro` → resultados scrapeados
- Workers scrapean y cachean en JSON/SQLite local
- Validación de mercado en 48h, sin frontend
- Si tracciona → migrar a Opción C

---

## VPS BARATOS — Precios actualizados Julio 2026

### ≤$1/mes (pago anual)
| Proveedor | RAM | CPU | Disco | Tráfico | Precio/año | Por mes |
|-----------|-----|-----|-------|---------|-----------|---------|
| CloudServer | 1GB | 1 | 20GB SSD | 1TB | **$10.00** | $0.83 |
| DediRock | 768MB | 1 | 10GB SSD | 1TB | **$10.18** | $0.85 |
| RackNerd | 768MB | 1 | 10GB SSD | 1TB | **$10.28** | $0.86 |
| ServerHost | 1GB | 1 | 15GB NVMe | ∞ | **$11.00** | $0.92 |
| ColoCrossing | 1GB | 1 | 25GB SSD | 20TB | **$10.99** | $0.92 |

### ≤$2/mes (pago anual)
| Proveedor | RAM | CPU | Disco | Tráfico | Precio/año | Por mes |
|-----------|-----|-----|-------|---------|-----------|---------|
| RackNerd | 1.5GB | 1 | 30GB SSD | 3TB | **$16.88** | $1.41 |
| DediRock | 2GB | 1 | 20GB SSD | 2TB | **$20.88** | $1.74 |
| RackNerd | 2GB | 2 | 25GB SSD | 4TB | **$20.98** | $1.75 |
| ServerHost | 2GB | 1 | 30GB NVMe | ∞ | **$21.88** | $1.82 |
| CloudServer | 2GB | 1 | 50GB SSD | 5TB | **$23.88** | $1.99 |

### Calidad/precio (Europa, ≥$3/mes)
| Proveedor | RAM | CPU | Disco | Precio/mes | Notas |
|-----------|-----|-----|-------|-----------|-------|
| Netcup | 2GB | 2 | 40GB | €2.80 | RS serie, muy fiable |
| OVHcloud | 2GB | 1 | 20GB | ~$3.50 | Starter VPS |
| Hetzner CX22 | 4GB | 2 | 40GB | €3.99 | Calidad alemana |
| Contabo S | 8GB | 4 | 50GB | €4.50 | Mucha RAM por € |
| BuyVM | 1GB | 1 | 20GB | $3.50 | +$1.25/IP extra |

### GRATIS (con trampa)
| Proveedor | RAM | CPU | Disco | Precio | Ojo |
|-----------|-----|-----|-------|--------|-----|
| Oracle Free | 24GB | 4 ARM | 200GB | **$0** | Difícil pillar slot ARM, esperas de semanas |

---

## RECOMENDACIÓN PARA MVP

**Arquitectura separada (recomendada):**
- Vercel free (frontend) → rápido, CDN global
- VPS barato (solo scraper) → si peta, la web sigue viva
- PostgreSQL + pg_graphql en el VPS → API REST auto-generada
- NextAuth.js en frontend → auth sin dependencia de Supabase
- Cloudflare R2 gratis → backups diarios de DB

**¿Por qué NO Supabase SaaS?** → tier gratuito deja colgado a largo plazo, vendor lock-in
**¿Por qué NO Supabase auto-hospedado?** → 7 contenedores Docker, 700-800MB RAM mínimo, pesado para VPS de $2

**Alternativa ligera a Supabase self-hosted:**
- PostgreSQL solo + extensión pg_graphql → API GraphQL automática como PostgREST
- NextAuth.js para auth (sin GoTrue/Supabase Auth)
- Solo ~200MB RAM → cabe en VPS de 768MB ($10/año)
- Admin con DBeaver o pgAdmin desde tu máquina local

**Presupuesto final con esta arquitectura:**

| Capa | Donde | Costo |
|------|-------|-------|
| Frontend Next.js | Vercel free | $0 |
| DB + API | PostgreSQL+pg_graphql en VPS | incluido en VPS |
| Scraper Playwright | Mismo VPS | incluido en VPS |
| Auth | NextAuth.js en Vercel | $0 |
| Backups | Cloudflare R2 free tier | $0 |
| Dominio | .io/.cc | ~$1/mes |
| **TOTAL** | | **~$1-2/mes** |

**VPS recomendado:** RackNerd 768MB ($10.28/año) solo scraper, o 2GB ($20.98/año) si metes PostgreSQL.

---

## FUENTES
- LowEndBox: [2 USD VPS](https://lowendbox.com/blog/2-usd-vps-cheap-vps-under-2-month/)
- LowEndBox: [$1 VPS](https://lowendbox.com/blog/1-vps-1-usd-vps-per-month/)
- ColoCrossing: [Ofertas LowEndTalk](https://www.colocrossing.com/lowendtalk-lowendbox-special-offers/)
- Plan maestro: `wiki/research/PLAN-MAESTRO-MetaSearch-AI-Accounts-Relays.md`
