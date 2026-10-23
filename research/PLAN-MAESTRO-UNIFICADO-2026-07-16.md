# PLAN MAESTRO UNIFICADO — Julio 16, 2026
## Meta-Search AI Engine + Farm Privado + Infraestructura

> Basado en: PLAN-MAESTRO-MetaSearch, PLAN-FARM-PRIVADO, VPS-MetaSearch-Plan, DeepRoot Investigation
> Objetivo: Un plan ejecutable que une las 3 patas del negocio

---

## MAPA GLOBAL: 3 PROYECTOS, 1 ECOSISTEMA

```
                    ┌──────────────────────────────────────┐
                    │     PROYECTO A: META-SEARCH ENGINE    │
                    │     (PÚBLICO · Monetizable · SEO)     │
                    │                                      │
                    │  Agregador de cuentas AI + relays     │
                    │  Multi-idioma (EN/ES/RU/ZH)           │
                    │  Monetización: relays patrocinados     │
                    │  Stack: Next.js + Vercel + VPS $1/mes │
                    │  Costo: $1-2/mes + dominio            │
                    └──────────────┬───────────────────────┘
                                   │
                                   │ mismos datos,
                                   │ mismos scrapers
                                   │
                    ┌──────────────▼───────────────────────┐
                    │     PROYECTO B: FARM + RELAY PRIVADO │
                    │     (PRIVADO · Telegram Bot)          │
                    │                                      │
                    │  Creación de cuentas AI automatizada  │
                    │  Relay New-API para uso propio         │
                    │  Bot Telegram solo invitación          │
                    │  Infra: VPS Flokinet/AlexHost (XMR)   │
                    │  Costo: $25-40/mes                    │
                    └──────────────┬───────────────────────┘
                                   │
                                   │ conocimiento del
                                   │ mercado alimenta
                                   │
                    ┌──────────────▼───────────────────────┐
                    │     PROYECTO C: INFRA + DATOS         │
                    │     (COMPARTIDO)                      │
                    │                                      │
                    │  Workers existentes (hta6ms6, etc)    │
                    │  Scrapers de 卡网 + lzt.market         │
                    │  Detector Veridrop fork               │
                    │  Wiki/research como knowledge base    │
                    └──────────────────────────────────────┘
```

---

## REGLA DE ORO: CONSTRUIR EN PARALELO, NO EN SERIE

Los 3 proyectos comparten:
- **Scrapers** (mismos datos alimentan al meta-search Y al farm)
- **Conocimiento de mercado** (lo que scrapeas del meta-search te dice qué cuentas crear)
- **Infraestructura** (workers existentes para scrapers ligeros)

No hay que esperar a terminar A para empezar B. Van a la vez.

---

## FASE 1: CIMIENTOS (Semana 1-2) — Julio 16-30, 2026

### 1A. Meta-Search Engine MVP ($0)

**Objetivo:** Landing page funcional con datos semilla, deployado en Vercel.

```
Día 1-2:   Crear proyecto Next.js 14 + Tailwind + shadcn/ui
Día 3-5:   Landing page (/) con búsqueda unificada
           Páginas /accounts, /relays, /compare
           Insertar 50+ registros semilla (datos reales de DeepRoot)
Día 6-7:   Deploy Vercel + dominio .io/.cc ($1/mes)
           SEO básico + sitemap
```

**Stack (versión minimalista $0/mes):**
- Vercel free (frontend) + Cloudflare Pages (fallback)
- SQLite en VPS barato o worker existente (NO Supabase)
- Datos semilla estáticos (sin scraper aún)

**¿Por qué NO Supabase?** → Tier gratuito te deja colgado. PostgreSQL directo en VPS es más barato y sin vendor lock-in. Si necesitas DB serverless → Cloudflare D1 (gratis hasta 5GB).

### 1B. Farm Privado ($25)

**Objetivo:** Tener 1 bot de Telegram funcional con stock manual de cuentas.

```
Día 1-2:   Comprar VPS Flokinet (XMR, ~$15/mes, 4GB RAM)
           Comprar dominio catch-all .xyz ($2/año, Njalla crypto)
           Crear bot Telegram con @BotFather (número virtual)
Día 3-4:   SQLite schema + bot.py mínimo (/cuenta, /stock, /invitar)
           Deploy New-API con Docker en VPS
Día 5-7:   Comprar 2-3 API keys OpenAI/Anthropic en lzt.market para relay
           Probar flujo: /cuenta → entrega credencial → /relay → API key
```

**No automatizar aún la creación de cuentas.** Primero valida que el bot funciona con cuentas compradas manualmente. El farmer automático (Playwright + SMS) va en Fase 2.

### 1C. Infraestructura de Datos

```
Día 1-3:   Script de scraping mínimo para 1-2 卡网 chinos
           Correr en worker existente (hta6ms6) con cron cada 30 min
           Output: JSON → guardar en wiki/research/data/
Día 4-5:   Fork mínimo de Veridrop (solo detector thinking_signature)
           Correr en Python, validar 5 relays conocidos
```

---

## FASE 2: DATOS REALES + FARM AUTOMÁTICO (Semana 3-5) — Agosto 2026

### 2A. Meta-Search con datos vivos

```
☐ 2A.1  Scraper 卡网 chino completo (kami + dujiao + shopApi)
☐ 2A.2  Scraper lzt.market con Playwright (requiere cuenta)
☐ 2A.3  Normalizador de productos (canonical model resolver)
☐ 2A.4  PostgreSQL en VPS barato (RackNerd 768MB $10/año o 2GB $21/año)
☐ 2A.5  API interna: GET /api/offers?category=chatgpt&max_price=10
☐ 2A.6  Frontend conectado a API real
☐ 2A.7  Price history (gráficos con Chart.js)
```

### 2B. Farmer Automático

```
☐ 2B.1  VPS farmer #1 (Shinjiru/AlexHost, $8/mes, 2GB, crypto)
☐ 2B.2  Instalar Playwright + stealth plugins
☐ 2B.3  Proxies residenciales (Webshare 10 gratis para empezar)
☐ 2B.4  API SMS-Activate (comprar saldo con crypto)
☐ 2B.5  Script farm_chatgpt.py (creación automatizada)
☐ 2B.6  Cron cada 30-60 min: crear 3-5 cuentas/lote
☐ 2B.7  Pipeline Claude + Gemini (más difíciles, más valiosas)
☐ 2B.8  Dashboard de stock en bot: /stats
```

### 2C. Detector Service

```
☐ 2C.1  Fork completo de Veridrop (12 detectores)
☐ 2C.2  API: POST /api/detect/{claude,openai,gemini}
☐ 2C.3  Callback a DB cuando termina job
☐ 2C.4  Página /verify en meta-search
```

---

## FASE 3: MONETIZACIÓN + ESCALA (Semana 6-8) — Septiembre 2026

### 3A. Monetización Meta-Search

```
MES 1-2 (gratis, construir tráfico):
  - Listados gratuitos para todos los relays
  - Contenido SEO: guías, comparativas, "best relays 2026"
  - Sin muro de pago

MES 3+ (empezar a cobrar):
  ☐ Contactar top 20 relays (score >80 en Veridrop)
  ☐ Ofrecer S1=$2000, S2=$1000, S3=$500/mes (sponsored)
  ☐ Pago en USDT (Telegram/Discord del relay)
  ☐ API premium: $10-50/mes acceso a datos
  ☐ AFF lzt.market (automático cuando tengas tráfico)
```

**El modelo "付费不买分":** El pago afecta VISIBILIDAD, nunca el score. Igual que Veridrop.

### 3B. Farm Privado — Usuarios

```
☐ Invitar 3-5 usuarios de confianza
☐ Solo por invitación tuya (/invitar <telegram_id>)
☐ Si tracciona → escalar a 2-3 VPS farmers más
☐ Añadir Claude Pro, Grok, Gemini Advanced al pipeline
```

### 3C. Infraestructura Final

```
☐ Cloudflare R2 para backups diarios de DB
☐ Sentry free para monitoreo de errores
☐ Uptime monitoring (healthchecks.io free tier)
☐ Dominio .io/.cc (~$1/mes)
```

---

## COSTES TOTALES POR PROYECTO

### Meta-Search Engine (Proyecto A)

| Item | Mensual | Anual |
|------|---------|-------|
| VPS scraper (RackNerd 768MB) | $0.86 | $10.28 |
| Dominio .io/.cc | $1.00 | $12.00 |
| Vercel (frontend) | $0 | $0 |
| Cloudflare R2 (backups) | $0 | $0 |
| **TOTAL** | **$1.86/mes** | **$22.28/año** |

Con PostgreSQL en VPS de 2GB: $2.75/mes ($33/año)

### Farm + Relay Privado (Proyecto B)

| Item | Mensual | Anual |
|------|---------|-------|
| VPS principal (Flokinet, 4GB) | $15.00 | $180.00 |
| VPS farmer #1 (Shinjiru, 2GB) | $8.00 | $96.00 |
| Dominio catch-all .xyz | $0.17 | $2.00 |
| SMS-Activate (saldo) | $5-15 | variable |
| Proxies residenciales (Webshare) | $0-10 | variable |
| API keys upstream | $10-30 | variable |
| VPN (Mullvad) | $5.00 | $60.00 |
| **TOTAL** | **$43-83/mes** | **~$500-1000/año** |

---

## DECISIONES CLAVE YA TOMADAS

### 1. ¿Supabase o PostgreSQL directo?
**PostgreSQL directo en VPS.** Tier gratuito Supabase = vendor lock-in. Self-hosted Supabase = 7 contenedores, 800MB RAM mínimo. PostgreSQL solo + pg_graphql = 200MB RAM, cabe en VPS de $1.

### 2. ¿VPS barato cuál?
**RackNerd 768MB ($10.28/año)** para empezar. Si necesitas PostgreSQL → 2GB ($20.98/año). Ambos en stock ahora. Alternativa: DediRock 2GB ($20.88/año).

### 3. ¿Oracle Free Tier?
Difícil pillar slot en España. Si aparece → bienvenido, pero no cuentes con ello.

### 4. ¿Qué construir primero?
**Meta-Search (frontend estático) + Bot Telegram (manual).** En paralelo. Ambos validan el mercado en <2 semanas.

### 5. ¿Monetización desde día 1?
No. Mes 1-2: construir tráfico y datos. Mes 3+: sponsored relays + API premium.

---

## VENTAJAS COMPETITIVAS (LAS 5 BARRERAS DE ENTRADA)

1. **Datos:** Scrapers de 卡网 + lzt.market + relays. Nadie más los tiene unificados.
2. **Verificación:** Fork de Veridrop con 12 detectores. Barrera técnica alta.
3. **Multi-idioma:** EN/ES/RU/ZH. PriceAI.cc solo cubre chino.
4. **Multi-moneda:** USD/EUR/Crypto/CNY/RUB. Sin fricción de pago.
5. **Transparencia:** "付费不买分" — visibilidad ≠ score. Confianza del usuario.

---

## RIESGOS REALES (sin endulzar)

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| lzt.market bloquea scraping | Media | Alto | Rate limiting, respetar robots.txt, usar cuentas reales |
| OpenAI/Anthropic banean cuentas farmeadas | Alta | Medio | Rotación de proxies, diversificar países SMS, stock buffer |
| Relays no quieren pagar sponsored | Media | Alto | Listarlos gratis primero, el tráfico convence solo |
| VPS barato se cae | Baja | Bajo | Frontend en Vercel (no se cae), backups R2 |
| Cambio legal en UE contra reventa | Baja | Alto | Farm en VPS fuera de UE (Flokinet Rumanía, Shinjiru Malasia) |
| Supabase te corta el free tier | Alta | Alto | No usar Supabase → PostgreSQL directo |

---

## CRONOGRAMA VISUAL

```
JULIO 2026          AGOSTO 2026             SEPTIEMBRE 2026
│ FASE 1 │          │ FASE 2   │            │ FASE 3         │
│ SEM 1-2│          │ SEM 3-5  │            │ SEM 6-8        │
│        │          │          │            │                │
│ ██     │          │ ████     │            │ ████           │
│ CIMIEN │          │ DATOS    │            │ MONETIZA       │
│ TOS    │          │ REALES   │            │ + ESCALA       │
│        │          │          │            │                │
│ A: MVP │          │ A: Scrap │            │ A: Sponsored   │
│ estátic│          │ pers vivos           │ listings       │
│ B: Bot │          │ B: Farm  │            │ B: Usuarios    │
│ manual │          │ automáti│            │ B: +Claude/Grok│
│ C: 1-2 │          │ C: Veridr│            │ C: Backups R2  │
│ scrape │          │ op fork  │            │ C: Monitor     │
```

---

## PRIMER PASO — HOY

1. Crear repo GitHub para meta-search engine
2. `npx create-next-app@latest` con TypeScript + Tailwind
3. Elegir dominio (.io o .cc) y comprar
4. Deploy a Vercel (gratis)
5. Pedir VPS RackNerd 768MB ($10.28/año)

---

## ARCHIVOS RELACIONADOS

- `PLAN-MAESTRO-MetaSearch-AI-Accounts-Relays.md` — Plan detallado del meta-search
- `PLAN-FARM-PRIVADO-Telegram-Bot.md` — Plan del farm + bot privado
- `VPS-MetaSearch-Plan-2026-07-15.md` — Investigación de VPS baratos
- `AI-Resale-Ecosystem-Complete.md` — DeepRoot completo (65KB, 2113 líneas)
- `AI-Account-Relay-Ecosystem-DeepRoot-2026-07.md` — Resumen ejecutivo DeepRoot
- `AI-Account-Relay-lztmarket-Pricing-2026-07.md` — Pricing real de lzt.market
- `SESION-COMPLETA-DeepRoot-2026-07-15.md` — Sesión completa del 15 julio
