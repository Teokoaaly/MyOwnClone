# PLAN MAESTRO — AI Account & Relay Meta-Search Engine
## "Skyscanner for AI Subscriptions and APIs"

> **Basado en:** DeepRoot Investigation (93% cobertura del ecosistema)
> **Fecha:** Julio 15, 2026
> **Stack objetivo:** Next.js 14+ · Supabase · Node.js scrapers · Python detector · Cloudflare R2
> **Costo MVP:** ~$120-180/mes | **Tiempo MVP:** 6-8 semanas (1 dev full-stack)

---

## 0. VISIÓN DEL PRODUCTO

Un agregador unificado que permite buscar, comparar y verificar:
- **Cuentas AI** (ChatGPT, Claude, Gemini, Grok, Midjourney, Cursor, Perplexity...)
- **API Relays** (中转站 — acceso API a modelos via proxy)
- A través de mercados chinos (卡网), rusos (lzt.market), y relays independientes

### ¿Por qué no existe aún fuera de China?

PriceAI.cc resuelve esto pero SOLO para mercado chino (idioma, moneda CNY, WeChat/Alipay). Un aggregador internacional tiene:
- **Mercado 5-10x más grande** (desarrolladores globales, no solo China)
- **Menos competencia** (0 competidores fuera de China)
- **Monetización más fácil** (affiliate global, créditos crypto, sponsored listings en USD)

---

## 1. ARQUITECTURA GENERAL

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FRONTEND (Next.js 14 App Router)              │
│                                                                      │
│  /                          → Landing + búsqueda unificada           │
│  /accounts                  → Cuentas AI (ChatGPT, Claude, etc)     │
│  /relays                    → API Relays con Veridrop scores        │
│  /compare                   → Comparador side-by-side               │
│  /alerts                    → Alertas de precio/stock               │
│  /submit                    → Submit relay para verificar           │
│  /api                       → API pública (pricing data)            │
│                                                                      │
│  Componentes: SearchBar · PriceTable · ScoreBadge · TrustMeter      │
│              PriceChart · RegionSelector · CurrencyConverter        │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   SUPABASE (DB)      │
                    │                      │
                    │  stations (relays)   │
                    │  offers (productos)  │
                    │  verifications       │
                    │  feedback            │
                    │  price_history       │
                    │  users (auth)        │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────▼───────┐   ┌──────────▼──────────┐   ┌───────▼───────┐
│ COLLECTOR     │   │ DETECTOR SERVICE    │   │ FEEDBACK      │
│ RUNTIME       │   │ (Python/FastAPI)    │   │ ENGINE        │
│ (Node.js)     │   │                     │   │               │
│               │   │ Verifica relays:    │   │ User reviews  │
│ Scrapea:      │   │ - thinking_sig      │   │ Ban reports   │
│ - 卡网         │   │ - context window    │   │ Evidence img  │
│ - lzt.market  │   │ - model identity    │   │ Trust scoring │
│ - Relay APIs  │   │ - token usage       │   │               │
│               │   │ Score 0-100         │   │ R2 storage    │
│ Cada 15-30min │   │                     │   │               │
└───────────────┘   └─────────────────────┘   └───────────────┘
```

---

## 2. MODELO DE DATOS (Supabase/PostgreSQL)

```sql
-- ============================================================
-- STATIONS: Relays y vendedores de cuentas
-- ============================================================
CREATE TABLE stations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  website_url TEXT,
  api_base_url TEXT,
  
  -- Tipo
  station_type TEXT NOT NULL DEFAULT 'reseller',  -- 'relay' | 'reseller' | 'both'
  market TEXT NOT NULL DEFAULT 'cn',              -- 'cn' | 'ru' | 'intl'
  source_type TEXT DEFAULT 'collected',            -- 'collected' | 'user_submitted' | 'merchant'
  
  -- Sistema técnico (relays)
  station_system TEXT,  -- 'new_api' | 'one_api' | 'custom' | 'mj_proxy' | null
  channel_types TEXT[], -- 'official_api' | 'reverse_engineered' | 'reseller' | etc
  
  -- Confianza
  veridrop_score INT,              -- 0-100
  veridrop_signature_rate FLOAT,   -- 0.0-1.0
  veridrop_last_check TIMESTAMPTZ,
  trust_score FLOAT DEFAULT 0,     -- Calculado: Veridrop(40%) + feedback(30%) + uptime(20%) + latency(10%)
  
  -- Disponibilidad
  availability_7day FLOAT,         -- 0.0-1.0
  avg_latency_ms INT,
  last_checked_at TIMESTAMPTZ,
  
  -- Riesgo y recomendación
  risk_labels TEXT[] DEFAULT '{}',
  usage_advice TEXT DEFAULT 'pending',  -- 'recommended' | 'try_small' | 'cautious' | 'avoid'
  
  -- Negocio
  payment_methods TEXT[],           -- 'wechat' | 'alipay' | 'usdt' | 'crypto' | 'card'
  minimum_top_up TEXT,
  refund_policy TEXT,
  commercial_relation TEXT DEFAULT 'none',  -- 'none' | 'affiliate' | 'sponsored'
  
  status TEXT DEFAULT 'active',     -- 'active' | 'limited' | 'unavailable'
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- OFFERS: Productos/precios
-- ============================================================
CREATE TABLE offers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  station_id UUID REFERENCES stations(id) ON DELETE CASCADE,
  
  -- Producto
  product_name TEXT NOT NULL,        -- "ChatGPT Plus 1 Month"
  product_category TEXT NOT NULL,    -- 'chatgpt' | 'claude' | 'gemini' | 'grok' | etc
  product_type TEXT NOT NULL,        -- 'subscription' | 'api_relay' | 'account'
  canonical_model TEXT,              -- 'GPT-4o' | 'Claude Opus 4.8' | etc (normalizado)
  
  -- Precio
  price DECIMAL(10,2) NOT NULL,
  currency TEXT DEFAULT 'USD',
  price_usd DECIMAL(10,2),          -- Normalizado para comparación
  original_price DECIMAL(10,2),     -- Precio oficial (para calcular descuento)
  
  -- Detalles
  duration_days INT,                -- 30 = mensual, 365 = anual
  account_origin TEXT,              -- 'autoreger' | 'brute_force' | 'stealer' | 'resale' | 'personal'
  access_type TEXT,                 -- 'full_email' | 'cookie_only' | 'api_key'
  phone_bound BOOLEAN DEFAULT true,
  stock_status TEXT DEFAULT 'in_stock',
  
  -- Metadata
  source_url TEXT,
  source_collector TEXT,            -- 'kami' | 'dujiao' | 'lzt_market' | 'manual'
  first_seen_at TIMESTAMPTZ DEFAULT now(),
  last_seen_at TIMESTAMPTZ DEFAULT now(),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- PRICE HISTORY: Tracking de evolución de precios
-- ============================================================
CREATE TABLE price_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  offer_id UUID REFERENCES offers(id) ON DELETE CASCADE,
  price DECIMAL(10,2) NOT NULL,
  price_usd DECIMAL(10,2),
  stock_status TEXT,
  recorded_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_price_history_offer_time ON price_history(offer_id, recorded_at DESC);

-- ============================================================
-- VERIFICATIONS: Resultados de detector (Veridrop fork)
-- ============================================================
CREATE TABLE verifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  station_id UUID REFERENCES stations(id) ON DELETE CASCADE,
  
  protocol TEXT NOT NULL,            -- 'claude' | 'openai' | 'gemini'
  model_tested TEXT,
  mode TEXT DEFAULT 'standard',      -- 'quick' | 'standard' | 'full'
  
  score INT,                         -- 0-100
  verdict TEXT,                      -- 'passed' | 'marginal' | 'failed'
  signature_rate FLOAT,              -- Solo Claude
  
  detectors_json JSONB,              -- Resultados por detector
  critical_issues INT DEFAULT 0,
  
  job_id TEXT UNIQUE,                -- ID del job en detector service
  public_report_url TEXT,            -- URL del reporte público
  
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- FEEDBACK: Reviews de usuarios
-- ============================================================
CREATE TABLE feedback (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  station_id UUID REFERENCES stations(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id),
  
  rating INT CHECK (rating >= 1 AND rating <= 5),
  title TEXT,
  body TEXT,
  
  -- Evidencia
  evidence_urls TEXT[] DEFAULT '{}',   -- URLs de R2
  ban_reported BOOLEAN DEFAULT false,
  ban_after_days INT,                  -- Días hasta ban (si aplica)
  
  -- Moderación
  verified_by_admin BOOLEAN DEFAULT false,
  merchant_response TEXT,
  
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- ALERTS: Notificaciones de precio/stock
-- ============================================================
CREATE TABLE alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id),
  
  product_category TEXT NOT NULL,
  canonical_model TEXT,
  price_threshold_usd DECIMAL(10,2),   -- Alertar si baja de este precio
  min_trust_score INT DEFAULT 70,      -- Solo relays con score > X
  
  enabled BOOLEAN DEFAULT true,
  last_triggered_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Índices
CREATE INDEX idx_stations_type_market ON stations(station_type, market);
CREATE INDEX idx_stations_trust ON stations(trust_score DESC);
CREATE INDEX idx_offers_category_model ON offers(product_category, canonical_model);
CREATE INDEX idx_offers_price_usd ON offers(price_usd ASC);
CREATE INDEX idx_offers_station ON offers(station_id);
CREATE INDEX idx_feedback_station ON feedback(station_id);
CREATE INDEX idx_verifications_station ON verifications(station_id);
```

---

## 3. STACK TECNOLÓGICO

| Capa | Tecnología | Por qué |
|---|---|---|
| **Frontend** | Next.js 14 (App Router) + TailwindCSS + shadcn/ui | SSR, SEO, rutas, componentes |
| **Auth** | Supabase Auth (GitHub + Google OAuth) | Gratis, integrado con DB |
| **Database** | Supabase (PostgreSQL) | Row-level security, realtime, $25/mes Pro |
| **Cache** | Redis (Upstash free tier) | Rate limiting, session cache |
| **Storage** | Cloudflare R2 | Imágenes de evidencia, $0.015/GB |
| **Scrapers** | Node.js + Playwright + Cheerio | JS-heavy sites, headless browser |
| **Detector** | Python 3.11 + FastAPI (fork Veridrop) | 12 detectores Claude + OpenAI + Gemini |
| **Hosting** | Vercel (frontend) + 2-3 VPS (scrapers/detector) | Serverless + dedicated |
| **Payments** | Polar.sh / LemonSqueezy | Affiliate tracking, sponsored listings |
| **Monitoring** | Sentry (free tier) + Supabase logs | Error tracking |

---

## 4. FUENTES DE DATOS

### Grupo A: Mercados Chinos (卡网) — vía scrapers

```
TIPO          PLATAFORMAS                              FRECUENCIA
─────────────────────────────────────────────────────────────────
kami          ai666.dnxb.cc, aisou.pro, caowo.store   Cada 15 min
dujiao        burstpro-ai.online, card.kxandyou.com   Cada 15 min
shopApi       catfk.com, ldxp.cn, pay.qxvx.cn         Cada 15 min
genericHtml   19cm.tech, lemon-watermelon.com         Cada 30 min
```

### Grupo B: Mercado Ruso — vía scrapers + browser

```
lzt.market    LLM category + Подписки                  Cada 30 min
              (requiere cuenta + cookies de sesión)
              Extraer: nombre, precio, vendedor, rating,
              origen, tipo acceso, antigüedad
```

### Grupo C: Relays API — vía detector service

```
Veridrop API   Consultar scores de relays conocidos    Cada 6 horas
               (si Veridrop ofrece API pública)

Relay directo  POST /v1/models → listar modelos        Cada 1 hora
               GET precios desde página del relay      (para top 100)
```

### Grupo D: Precios Oficiales — vía scraping ligero

```
priceai.cc     /official-prices/*                      Cada 24 horas
               Precios App Store por región

openai.com     /pricing                                Cada 7 días
anthropic.com  /pricing                                Cada 7 días
```

---

## 5. FASES DE DESARROLLO

### FASE 0: Infraestructura Base (Semana 1)

```
☐ 0.1  Crear proyecto Next.js 14 con App Router + TailwindCSS + shadcn/ui
☐ 0.2  Crear proyecto Supabase + ejecutar schema SQL
☐ 0.3  Configurar Supabase Auth (GitHub + Google OAuth)
☐ 0.4  Configurar Vercel deploy automático desde GitHub
☐ 0.5  Configurar Cloudflare R2 bucket para imágenes
☐ 0.6  Crear estructura de carpetas:
        src/app/ (rutas)
        src/components/ (ui reutilizable)
        src/lib/ (db, api clients, utils)
        collectors/ (scrapers Node.js)
        detector/ (Python FastAPI fork)
```

### FASE 1: Páginas Estáticas + Datos Semilla (Semana 2)

```
☐ 1.1  Landing page (/) con búsqueda unificada
☐ 1.2  Página /accounts con tabla de productos (datos semilla)
☐ 1.3  Página /relays con tabla de relays + scores (datos semilla)
☐ 1.4  Componente SearchBar con autocompletado
☐ 1.5  Componente PriceTable con ordenación/filtros
☐ 1.6  Componente ScoreBadge (Veridrop 0-100 con colores)
☐ 1.7  Insertar 50+ registros semilla (stations + offers) basados en datos reales
```

### FASE 2: Scrapers — Mercado Chino (Semana 3)

```
☐ 2.1  Crear collector runtime en Node.js (collect-prices.mjs)
☐ 2.2  Implementar parser para tipo 'kami' (CDKeys)
☐ 2.3  Implementar parser para tipo 'dujiao' (cuentas directas)
☐ 2.4  Implementar parser para tipo 'shopApi' (API JSON)
☐ 2.5  Implementar normalizador de productos (canonical model resolver)
☐ 2.6  Implementar POST a Supabase (upsert offers + stations)
☐ 2.7  Deploy collector en VPS #1 con cron cada 15 min
☐ 2.8  Insertar metadatos de precio oficial (desde priceai.cc + manual)
```

### FASE 3: Scrapers — Mercado Ruso (lzt.market) (Semana 4)

```
☐ 3.1  Implementar autenticación en lzt.market vía Playwright
☐ 3.2  Navegar a LLM category y extraer listings (paginación)
☐ 3.3  Parsear: nombre, precio, vendedor, rating, origen, tipo acceso
☐ 3.4  Navegar a Подписки y extraer listings
☐ 3.5  Normalizar a modelo de datos unificado
☐ 3.6  Mapear categorías lzt.market → product_category canónico
☐ 3.7  Deploy en VPS #1 (mismo collector runtime, diferente schedule)
```

### FASE 4: Detector Service (Semana 5)

```
☐ 4.1  Clonar priceai-detector-service (Python FastAPI)
☐ 4.2  Configurar endpoints: POST /api/detect/{claude,openai,gemini}
☐ 4.3  Configurar almacenamiento de jobs en disco
☐ 4.4  Implementar callback: al terminar job → POST result a Supabase
☐ 4.5  Frontend: página /verify con formulario (URL relay + API key)
☐ 4.6  Frontend: página de resultados con score + breakdown por detector
☐ 4.7  Deploy detector en VPS #2 con systemd
```

### FASE 5: Trust & Reputation System (Semana 6)

```
☐ 5.1  Implementar feedback form en página de station
☐ 5.2  Subida de imágenes a R2 (evidencia de scam/ban)
☐ 5.3  Cálculo de trust_score compuesto:
       Veridrop(40%) + feedback_rating(30%) + uptime(20%) + latency(10%)
☐ 5.4  Badge de confianza: "Verified" / "Caution" / "Avoid"
☐ 5.5  Página de perfil de station con gráfico de precio histórico
☐ 5.6  Price chart component (últimos 90 días, Chart.js o Recharts)
```

### FASE 6: Alertas + API Pública (Semana 7)

```
☐ 6.1  Sistema de alertas: crear/editar/eliminar
☐ 6.2  Cron job que evalúa alertas cada 30 min → email/webhook
☐ 6.3  API pública: GET /api/v1/offers?category=chatgpt&max_price=10
☐ 6.4  API pública: GET /api/v1/stations/:slug
☐ 6.5  API pública: GET /api/v1/prices/history?model=gpt-4o
☐ 6.6  Rate limiting en API (Upstash Redis)
☐ 6.7  Documentación de API (OpenAPI/Swagger)
```

### FASE 7: Monetización + Launch (Semana 8)

```
☐ 7.1  Sistema de affiliate links (AFF) con tracking de clicks
☐ 7.2  Sponsored listings: S1/S2/S3 con badges visuales
☐ 7.3  Disclaimer "付费不买分" (no afecta score)
☐ 7.4  Página de transparencia (explica modelo de negocio)
☐ 7.5  SEO: sitemap, meta tags, structured data
☐ 7.6  Tests finales + deploy producción
☐ 7.7  Analytics (Plausible o PostHog)
```

---

## 6. MONETIZACIÓN (CORREGIDA — sin dependencia de CNY ni acuerdos previos)

### ⚠️ Lo que NO funciona para ti

| Lo que NO | Por qué |
|---|---|
| AFF de 卡网 chinos | Pagan en CNY a WeChat/Alipay — necesitas cuenta bancaria china |
| Acuerdo directo con lzt.market | No firman con desconocidos sin tráfico probado |
| Cobrar en RMB | Sin acceso al sistema bancario chino |

### ✅ Lo que SÍ funciona (desde día 1, cobrando en crypto/USD)

```
FUENTE                      CÓMO SE COBRA                    MES 1-3     MES 4+
──────────────────────────────────────────────────────────────────────────────
Relays patrocinados         USDT/ETH por Telegram.            $0          $2-4K
(S1/S2/S3 sponsored)        Los relays YA pagan esto
                             en Veridrop (S1=$2000/mes).
                             Contacto: DM en Telegram,
                             Discord del relay.

API premium                 Stripe/Polar.sh/LemonSqueezy.    $0          $200-500
                             Freemium: 100 req/día gratis.
                             Pro: $10-50/mes acceso datos.

Donaciones                  Ko-fi + GitHub Sponsors.         $50-200     $100-300
                             (Sin comisiones absurdas)

AFF lzt.market (futuro)     Sistema propio de lzt.market.    $0          $200-500
                             Pagan en EUR/USD/crypto.
                             Llega solo cuando tengas tráfico
                             — sin acuerdo previo necesario.
──────────────────────────────────────────────────────────────────────────────
TOTAL REALISTA                                              $50-200     $2.5K-5K
```

### Estrategia para cada fuente:

**1. Relays patrocinados (la fuente principal — 80% del revenue)**

Los relays chinos YA pagan $500-2000/mes por visibilidad en Veridrop. Les ofreces algo que no tienen: **mercado internacional**. Contacto directo:

```
PASO 1: Identificar top 20 relays con score >80 en Veridrop
PASO 2: Buscar su Telegram/Discord/email de soporte
PASO 3: Mensaje: "Tu relay ya tiene score 89 en Veridrop.
         Lo listamos en nuestro aggregator internacional.
         Por $500/mes (S3) apareces destacado. Pagas en USDT."
PASO 4: Sin respuesta → listarlos igual (gratis).
         Cuando vean tráfico, vuelven solos.
```

**Ejemplo real:** Passion8 (score 89, 256 verificaciones, relay #1 del mundo) ya invierte en imagen. Un listing patrocinado en un aggregator inglés les da acceso a developers que nunca han oído hablar de 中转站. El ROI es obvio.

**2. lzt.market — sin acuerdo, sin problema**

No necesitas acuerdo. El modelo es:
- Scrapeas precios públicos (es información de mercado, como Google Shopping)
- Pones link normal a la página del vendedor (no affiliate)
- Cuando tengas 10K+ visitas/mes, el equipo de lzt.market TE contacta a TI
- Mismo camino que hizo PriceAI con los 卡网 chinos

**3. API access — ingresos pasivos**

Tus datos normalizados (precios en USD, scores Veridrop, histórico) tienen valor para:
- Developers que quieren integrar comparador en sus apps
- Dashboards de empresas que monitorean costes de API
- Bots de Telegram/Discord que alertan de ofertas

**Modelo "付费不买分"**: El pago solo afecta VISIBILIDAD, nunca el score. Mismo estándar ético que Veridrop.

---

## 7. VENTAJAS COMPETITIVAS vs PRICEAI

| Feature | PriceAI | Nosotros |
|---|---|---|
| **Idioma** | Solo chino | Multi-idioma (EN, ES, RU, ZH) |
| **Mercado ruso** | No cubre lzt.market | ✅ lzt.market |
| **Moneda** | Solo CNY | Multi-currency (USD, EUR, CNY, RUB) |
| **Pagos** | WeChat/Alipay | PayPal, crypto, card |
| **API pública** | No | ✅ REST API |
| **Alertas precio** | No | ✅ Email/webhook |
| **Histórico precios** | No | ✅ Gráficos 90 días |
| **Verificación relays** | Sí (Veridrop) | ✅ Igual (fork Veridrop) |
| **Trust scoring** | Básico | ✅ Compuesto (Veridrop + feedback + uptime) |
| **Open source** | AGPL-3.0 | AGPL-3.0 (mismo modelo) |

---

## 8. RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| **lzt.market bloquea scraper** | ALTA | MEDIO | Rotación de proxies + cuentas备用, fallback a datos cached |
| **卡网 cambian estructura HTML** | ALTA | MEDIO | Monitor de errores + alertas, tests de integración diarios |
| **Veridrop cierra/limita API** | BAJA | ALTO | Fork propio del detector, independencia total |
| **Problemas legales (ToS)** | MEDIO | ALTO | Disclaimer claro, no almacenar cuentas, solo agregar info pública |
| **OpenAI/Anthropic cambian precios** | ALTA | BAJO | Scraper de páginas oficiales cada 24h |
| **Cloudflare bloquea scrapers** | ALTA | MEDIO | Residential proxies (BrightData free tier para empezar) |
| **Competencia (otro aggregator)** | BAJA | MEDIO | First-mover advantage fuera de China, SEO agresivo |

---

## 9. MÉTRICAS DE ÉXITO

```
MES 1: 100 stations, 500 offers, 50 usuarios registrados
MES 2: 500 stations, 2,000 offers, 500 usuarios, primeras alertas
MES 3: 1,000+ stations, 5,000+ offers, 2,000 usuarios, primeros AFF revenue
MES 6: 3,000+ stations, 15,000+ offers, 10,000 usuarios, revenue >$2k/mes
```

---

## 10. PRIMEROS PASOS (MAÑANA)

```
1. Crear repo en GitHub
2. `npx create-next-app@latest --typescript --tailwind --app`
3. Crear proyecto Supabase + ejecutar schema SQL
4. Deploy a Vercel (dominio temporal)
5. Insertar 50 stations semilla con datos reales de la investigación
6. Publicar landing page con búsqueda funcional
```

---

*Plan maestro cerrado. Listo para ejecución cuando des la orden.*
