# MASTER DEFINITIVO — TH3F4Rm3R · Julio 2026
## Documento único. No repetir investigaciones ya hechas.

---

## ÍNDICE RÁPIDO

1. [Qué es TH3F4Rm3R](#1-qué-es-th3f4rm3r)
2. [Qué funciona YA (local)](#2-qué-funciona-ya-local)
3. [Componentes VERIFICADOS](#3-componentes-verificados)
4. [Arquitectura objetivo](#4-arquitectura-objetivo)
5. [Costes REALES](#5-costes-reales)
6. [VPS baratos (auditado Julio 2026)](#6-vps-baratos)
7. [Legalidad (España)](#7-legalidad-españa)
8. [PENDIENTE verificar](#8-pendiente-verificar)
9. [Lo que ya NO hay que investigar otra vez](#9-no-repetir)

---

## 1. QUÉ ES TH3F4Rm3R

Sistema privado (no público) para crear y gestionar cuentas AI (ChatGPT, Claude) + relay API.
**Distribución:** Bot de Telegram privado, solo invitación.
**Principio:** Si no hay producto público, no hay a quién demandar.

### Proyectos hermanos (mismo ecosistema)

| Proyecto | Tipo | Estado |
|---|---|---|
| **TH3F4Rm3R** (Farm privado) | Telegram bot + relay | ✅ Funcionando local |
| **Meta-Search Engine** | Web pública agregador | 📋 Planeado, no ejecutado |
| **Vault** (ephemeral-shield) | React frontend OTP/admin | 🟡 Existe, build roto |

---

## 2. QUÉ FUNCIONA YA (LOCAL)

```
Máquina: 3.8GB RAM, 2.4GB libre
Ruta: /opt/farm/

Servicios systemd corriendo:
├── farm-bot.service       → @f4rm34_bot (14.5MB RAM)
├── farm-relay.service     → Proxy MiniMax :3001 (0.6MB)
└── farm-dashboard.service → API :8080 (4.9MB)

Archivos:
├── bot.py                  → Telegram bot funcional
├── dashboard_api.py        → REST API + OTP polling
├── relay.py                → Proxy OpenAI-compatible → MiniMax
├── farmer.py               → Legacy (no activo)
├── data/farm.db            → SQLite con cuentas
├── vault/                  → React frontend
├── new-api-data/           → Config New-API relay
└── venv/                   → Python deps

GitHub: https://github.com/Teokoaaly/Accouncreator
Ephemeral-shield: /tmp/ephemeral-shield/ (puerto 3004, build roto)
ChatGPT-creator: /tmp/chatgpt-creator/ (Go, crea cuentas via API)

Cuentas existentes: farmer1784268529161137, farmer1784268533663121,
                    farmer1784268540159157@web-library.net
                    pass=ChatGPT2026!Farm
                    mail.tm: web-library.net, pass=Farmer<TIMESTAMP>!
```

### Lo que SÍ funciona del creador de cuentas
- Crear cuentas via API de OpenAI (bypass registro web)
- mail.tm para email temporal
- Cuentas se registran correctamente

### Lo que NO funciona
- Login en navegador → IP datacenter bloqueada por OpenAI
- Age verification → No implementada
- El /tmp/chatgpt-creator no maneja DOB/name requerido post-API

---

## 3. COMPONENTES VERIFICADOS

### Email — NotLetters ✅
```
URL:     https://notletters.com/
Precio:  0.05₽ (~$0.0005) por email
API:     REST + IMAP + Web
Notas:   Dominios rotativos sin blacklist de IA
         Estándar en lzt.market
```

### SMS — HeroSMS ✅
```
URL:     https://hero-sms.com/
Precio:  Desde $0.006/SMS
Notas:   Heredero de SMS-Activate (CERRADO)
         5SIM es alternativa: https://5sim.net/ (desde $0.01)
```

### Proxy residencial — DataImpulse ✅
```
URL:     https://dataimpulse.com/
Precio:  $1/GB, mínimo $5 (5GB)
Notas:   90M+ IPs reales, 195 países, tráfico no caduca
         Crypto aceptado
         Alternativa: IPRoyal ($1.75/GB, crypto)
```

### CAPTCHA — 2captcha ✅
```
URL:     https://2captcha.com/
Precio:  ~$2-3/1000 CAPTCHAs
Notas:   Solo si Turnstile sigue bloqueando con IP residencial
```

### Email temporal actual — mail.tm ✅
```
Dominio: web-library.net
Usuario: farmer<TIMESTAMP>@web-library.net
Pass:    Farmer<TIMESTAMP>!
Notas:   Funciona, pero NotLetters es mejor para producción
```

### Ecosistema de relays — New-API ✅
```
Repo:    https://github.com/Calcium-Ion/new-api (42K+ stars, Go)
Función: Gateway multi-protocolo OpenAI↔Claude↔Gemini
         Weighted routing, auto-ban dead keys, billing engine
```

### Verificación de relays — Veridrop ✅
```
URL:     https://veridrop.org
Función: 4,122 relays auditados
         thinking_signature de Anthropic como detector infalsificable
```

### Mercado de cuentas — lzt.market ✅
```
URL:     https://lzt.market/
Precios reales (Julio 2026):
  ChatGPT Plus   €3.81-11.19  (promedio ~€5, 80%+ autoreger)
  ChatGPT Pro    €78.34        (brute-force)
  Claude Pro     €6.72         (brute-force)
  SuperGrok      €1.85-2.45    (90%+ stealer)
```

### Gift Cards Apple — Noones.com ✅
```
URL:     https://noones.com/
Función: P2P crypto, compra gift cards App Store Filipinas
Notas:   Para ChatGPT Plus via IAP (Apple ID filipino)
         ~€13.50/mes vs €22 en España
```

### VPS baratos con crypto — Verificado Julio 2026 ✅

| Proveedor | RAM | Precio | Crypto | Ubicación | URL |
|---|---|---|---|---|---|
| Skhron.eu | 512MB | €2.34/mes | BTC | 🇸🇪 Suecia | https://skhron.eu/services/bitcoin |
| BuyVM | 1GB | $3.50/mes | BTC | 🇺🇸 USA | https://buyvm.net/kvm-dedicated-server-slices/ |
| Hostkey | 1GB | €3/mes | BTC | 🇪🇺 EU | https://hostkey.com/vps/bitcoin-vps/ |
| Evoxt | 512MB | $2.99/mes | BTC/LTC | Asia/EU | https://evoxt.com/ |
| ExtraVM | ? | $4.50/mes | BTC/XMR/50+ | 8 locations | https://extravm.com/crypto-vps |
| HostBrr | 512MB | ~€3/mes | Crypto | 🇩🇪 Alemania | https://my.hostbrr.com/ |

NO caben en presupuesto $4/mes:
- FlokiNET (€7.99+)
- 1984 Hosting (€79+)
- AnubizHost ($24.99+)
- AlexHost (no verificado)
- NiceVPS VPS (€9.99+)

Dominios anónimos:
- Njalla (https://njalla.com) — XMR, ellos son el dueño legal
- Internet.bs — BTC, WHOIS privacy

VPN anónima:
- Mullvad — crypto, ~$5/mes (NO VERIFICADO si acepta crypto actualmente)
- ProtonVPN — crypto

---

## 4. ARQUITECTURA OBJETIVO

```
                    TÚ + AMIGOS (Telegram)
                           │
            ┌──────────────┴──────────────┐
            │   Bot Telegram (privado)     │
            │   /cuenta /relay /stock      │
            └──────────────┬──────────────┘
                           │
          ┌────────────────▼────────────────┐
          │     VPS PRINCIPAL (≤$4/mes)      │
          │     Skhron.eu / BuyVM / Hostkey  │
          │                                  │
          │  ┌────────────┬──────────────┐   │
          │  │ Bot Manager │ New-API Relay│   │
          │  │ (Python)    │ (Go/Docker)  │   │
          │  └─────┬───────┴──────┬───────┘   │
          │        └──────┬───────┘           │
          │      SQLite DB (todo local)       │
          └───────────────────────────────────┘
                           │
          ┌────────────────▼────────────────┐
          │   TÚ (PC local, via VPN)         │
          │   Playwright Farmer on-demand     │
          │   + DataImpulse proxies          │
          │   + NotLetters email              │
          │   + HeroSMS/5SIM                  │
          │                                  │
          │   Crea cuentas → sube al VPS     │
          └──────────────────────────────────┘
```

---

## 5. COSTES REALES

### Infraestructura fija (mes)

| Concepto | Coste | Notas |
|---|---|---|
| VPS (Skhron/BuyVM/Hostkey) | €2.34-3.50 | Bitcoin |
| VPN (Mullvad) | ~$5 | Crypto (pendiente verificar) |
| Dominio catch-all | ~$0.17 | .xyz en Njalla |
| **TOTAL FIJO** | **~$5-8/mes** | |

### Coste por cuenta ChatGPT Free

| Componente | Proveedor | Coste |
|---|---|---|
| Email | NotLetters | $0.001 |
| SMS | 5SIM/HeroSMS | $0.01-0.05 |
| Proxy (5MB) | DataImpulse | $0.005 |
| CAPTCHA | 2captcha (si necesario) | $0-0.002 |
| **TOTAL** | | **$0.02-0.06** |

### Inversión inicial única

| Concepto | Mínimo |
|---|---|
| DataImpulse 5GB | $5 |
| NotLetters balance | $1 |
| HeroSMS o 5SIM | $2 |
| 2captcha | $2 |
| Dominio .xyz (Njalla) | ~$2/año |
| **TOTAL INICIAL** | **~$12** |

---

## 6. VPS BARATOS (auditado Julio 2026)

Ya verificado en esta sesión. Ver tabla en sección 3.

---

## 7. LEGALIDAD (ESPAÑA)

| Actividad | ¿Delito? | Peor consecuencia |
|---|---|---|
| Crear cuenta con bot | ❌ No (civil) | Baneo de cuenta |
| Usar proxies residenciales | ❌ No | Nada |
| Relay API | ❌ No | Nada |
| SMS virtuales | ❌ No | Nada |
| Pagar con gift cards propias | ❌ No | Cuenta baneada |
| Pagar con tarjeta robada | ✅ SÍ (Art. 248 CP) | Cárcel |
| Robar credenciales | ✅ SÍ (Art. 197 CP) | Cárcel |
| Compartir sin vender | ❌ No (civil) | Cuentas baneadas |

---

## 8. PENDIENTE VERIFICAR

### CRÍTICO (bloquea el pipeline)
- [ ] ¿El Playwright stealth bypass funciona en Julio 2026 contra OpenAI?
- [ ] ¿DataImpulse IPs pasan realmente el registro de OpenAI?
- [ ] ¿5SIM tiene números que OpenAI acepta actualmente?
- [ ] ¿El repo https://github.com/Calcium-Ion/new-api sigue activo?
- [ ] ¿Se puede resolver el age verification (nombre+DOB) via API?

### ALTO (necesario para producción)
- [ ] ¿Mullvad acepta crypto en Julio 2026?
- [ ] ¿Noones.com vende gift cards Apple PH sin KYC?
- [ ] ¿BrightData free trial sigue existiendo?
- [ ] ¿sms-activate.ru funciona independientemente?
- [ ] ¿Heroku/GitHub aceptan cuenta nueva sin teléfono?

### MEDIO (mejoras)
- [ ] Arreglar build ephemeral-shield (TanStack Start)
- [ ] Fix definitivo atob() en share.$token.tsx
- [ ] Verificar repos alternativos a chatgpt-creator en GitHub
- [ ] ¿SIM física + modem USB es viable?

### BAJO (futuro)
- [ ] Midjourney relay (Discord webhook)
- [ ] Suno2openai integración
- [ ] Expansión a Claude/Grok/Gemini

---

## 9. NO REPETIR

### Documentos existentes (no crear nuevos duplicados)

| Documento | KB | Contenido |
|---|---|---|
| `MASTER-DEFINITIVO-2026-07.md` | este | Plan unificado (reemplaza a todos) |
| `FARMER-COMPONENTES-VERIFICADOS.md` | 2KB | Componentes verificados |
| `AI-Account-Relay-Ecosystem-DeepRoot-2026-07.md` | 35KB | Mapa del ecosistema |
| `AI-Account-Relay-Supplement-Gaps-2026-07.md` | 16KB | Midjourney, Suno, gaps |
| `AI-Account-Relay-lztmarket-Pricing-2026-07.md` | 12KB | Precios reales lzt.market |
| `PLAN-MAESTRO-MetaSearch-AI-Accounts-Relays.md` | 21KB | Meta-search engine |
| `PLAN-FARM-PRIVADO-Telegram-Bot.md` | 23KB | Farm privado (DESACTUALIZADO, usar ESTE doc) |
| `PLAN-MAESTRO-UNIFICADO-2026-07-16.md` | 13KB | Plan unificado |
| `VPS-MetaSearch-Plan-2026-07-15.md` | 6KB | VPS investigación |
| `SESION-COMPLETA-DeepRoot-2026-07-15.md` | ? | Sesión original |
| `AI-Resale-Ecosystem-Complete.md` | ? | Ecosistema completo |
| `sesiones-hermes-2026-07-13-y-07-14.md` | ? | Sesiones anteriores |

### Investigaciones YA HECHAS (no volver a hacer)

- ✅ Ecosistema completo de relays y cuentas (DeepRoot, 35KB)
- ✅ Precios reales de lzt.market (12KB)
- ✅ VPS baratos ≤$4/mes con crypto (esta sesión)
- ✅ Componentes farmer: email, SMS, proxy, captcha (verificados)
- ✅ Legalidad en España
- ✅ Proveedores de gift cards (Noones)
- ✅ Comparativa Cloudflare vs sin CDN (OPSEC)
- ✅ Arquitectura: bot + relay + farmer

### Correcciones al plan original (ya aplicadas en este documento)

| Dato viejo | Dato corregido |
|---|---|
| SMS-Activate.org | ❌ CERRADO → HeroSMS / 5SIM |
| Webshare proxies | ❌ Datacenter → DataImpulse residencial |
| Email .xyz catch-all | ❌ Sub-óptimo → NotLetters |
| $0.20-0.60/cuenta | ❌ Inflado → $0.02-0.06 real |
| Flokinet $15/mes | ❌ → Desde €7.99/mes |
| $68-113/mes total | ❌ Inflado → ~$5-8/mes fijo |

---

*Última actualización: 20 Julio 2026*
*Este documento reemplaza a PLAN-FARM-PRIVADO-Telegram-Bot.md*
*Cualquier nueva investigación se añade AQUÍ, no en un documento nuevo.*
