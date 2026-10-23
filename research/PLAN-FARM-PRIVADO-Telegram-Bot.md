# PLAN OPERACIONAL — Account Farm + Relay Privado
## Infraestructura oculta · Telegram bot · Solo invitación

> **Objetivo:** Crear y gestionar cuentas AI + relay API para uso privado.
> **Distribución:** Bot de Telegram privado (solo invitación, 100% anónimo).
> **Principio:** Si no hay producto público, no hay a quién demandar.

---

## 0. ARQUITECTURA GENERAL

```
┌─────────────────────────────────────────────────────────────────┐
│ TÚ + USUARIOS DE CONFIANZA (Telegram)                           │
│                                                                  │
│  Telegram → Bot privado (solo invitación)                        │
│  Comandos: /cuenta chatgpt, /relay gpt4, /stock, /crear        │
└──────────────────────────────┬──────────────────────────────────┘
                               │ Telegram Bot API
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ VPS PRINCIPAL (Flokinet/AlexHost, Rumanía/Moldavia)             │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                    │
│  │ BOT MANAGER      │  │ NEW-API RELAY    │                    │
│  │ (Python)         │  │ (Go, puerto 3000)│                    │
│  │                  │  │                  │                    │
│  │ - Recibe comandos│  │ - Pool de API    │                    │
│  │ - Despacha       │  │   keys upstream  │                    │
│  │   cuentas        │  │ - Rate limiting  │                    │
│  │ - Gestiona stock │  │ - Billing int.   │                    │
│  └────────┬─────────┘  └────────┬─────────┘                    │
│           │                     │                                │
│  ┌────────▼─────────────────────▼─────────┐                    │
│  │           STORAGE (SQLite local)        │                    │
│  │                                         │                    │
│  │  accounts      — cuentas creadas        │                    │
│  │  users         — usuarios Telegram      │                    │
│  │  relay_keys    — API keys generadas     │                    │
│  │  usage_log     — consumo por usuario    │                    │
│  └─────────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
                               │
          ┌────────────────────┴────────────────────┐
          │                                         │
┌─────────▼─────────┐                    ┌──────────▼──────────┐
│ VPS FARMER #1     │                    │ VPS FARMER #2       │
│ (Flokinet, NL)    │                    │ (Shinjiru, MY)       │
│                   │                    │                      │
│ Playwright        │                    │ Playwright           │
│ + proxies         │                    │ + proxies            │
│ + SMS API client  │                    │ + SMS API client     │
│                   │                    │                      │
│ Crea cuentas      │                    │ Crea cuentas         │
│ → las sube al      │                    │ → las sube al        │
│   VPS principal   │                    │   VPS principal      │
└───────────────────┘                    └──────────────────────┘
```

---

## 1. COMPONENTES

### 1.1 Bot de Telegram (Python)

```python
# bot_manager.py — Pseudocódigo de arquitectura

COMANDOS:
  /start         → Verificar si el usuario está en whitelist
  /cuenta <tipo> → Solicitar cuenta (chatgpt_plus, claude_pro, etc.)
  /relay <modelo>→ Generar API key temporal para relay
  /stock         → Ver disponibilidad de cuentas
  /estado <id>   → Ver estado de una cuenta creada
  /crear <tipo>  → (Admin) Disparar creación de cuentas
  /invitar <id>  → (Admin) Añadir usuario a whitelist
  /ban <id>      → (Admin) Banear usuario
  /stats         → (Admin) Estadísticas de uso

FLUJO /cuenta chatgpt_plus:
  1. Usuario pide cuenta
  2. Bot verifica stock en DB
  3. Si hay stock → entrega credenciales + instrucciones
  4. Si no hay → "Sin stock. Próximo lote en ~X horas."
  5. La cuenta se marca como "entregada" + timestamp + user_id

FLUJO /relay gpt4:
  1. Usuario pide acceso API
  2. Bot crea API key en New-API con límite de tokens
  3. Devuelve: endpoint + key + límite
  4. Registra en DB para tracking de uso
```

### 1.2 Account Farmer (Playwright + Python)

```python
# farmer.py — Arquitectura del creador de cuentas

CONFIG POR PROVEEDOR:

CHATGPT_FREE:
  email_domain: catch-all en dominio propio
  sms_provider: sms-activate.org (API key comprada con crypto)
  sms_country: Indonesia / Filipinas / Kenia (mejor pass rate)
  proxy_type: residential (1 IP por cuenta)
  browser: playwright + stealth plugin
  delays: random 30s-5min entre pasos
  output: email + password + session_token + created_at

CHATGPT_PLUS:
  mismo_que_free +
  payment_method: gift_card_app_store_filipinas
  gift_card_source: comprar con crypto en plataformas P2P
  billing_country: Filipinas (₱999 = ¥110 = ~€13.50)
  nota: SOLO si hay presupuesto para gift cards legítimas

CLAUDE_PRO:
  email_domain: dominio propio
  sms_provider: sms-activate.org
  sms_country: UK / Alemania (Claude bloquea países baratos)
  proxy_type: residential
  payment: gift card o tarjeta virtual
  dificultad: ALTA (Claude tiene mejor detección anti-fraud)

PROVEEDORES SMS (orden de preferencia):
  1. sms-activate.org — API, pago crypto, 180+ países
  2. 5sim.net — API, más barato, pago crypto
  3. sms-activate.ru — mismo servicio, interfaz rusa
  4. SIM física + modem USB — máxima pass rate, más caro

PROXIES RESIDENCIALES:
  ⚠️ NO DATACENTER — OpenAI los detecta al instante
  Opciones:
  - BrightData (antes Luminati): 7-day free trial → $500 crédito
  - Webshare: 10 proxies gratis para empezar
  - IPRoyal: barato ($2/GB), crypto
  - Proxy-Cheap: rotativos residenciales, crypto
```

### 1.3 New-API Relay

```bash
# Desplegar en VPS principal
git clone https://github.com/QuantumNous/new-api.git
cd new-api
docker-compose up -d

# Configurar:
# - Puerto 3000: admin panel
# - Puerto 80: API pública (solo accesible desde VPS, no expuesto)
# - API keys upstream: OpenAI, Anthropic, Google
# - Rate limiting por usuario
# - Billing interno (tracking de tokens, no cobro)

# El bot de Telegram crea API keys via New-API admin API
# Cada usuario recibe endpoint + key + límite
```

---

## 2. ESQUEMA DE DATOS (SQLite, todo local)

```sql
-- Cuentas creadas
CREATE TABLE accounts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  provider TEXT NOT NULL,         -- 'chatgpt' | 'claude' | 'gemini' | 'grok'
  tier TEXT NOT NULL,             -- 'free' | 'plus' | 'pro' | 'max'
  email TEXT NOT NULL,
  password TEXT,
  session_token TEXT,             -- JSON: cookies + user agent
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_by TEXT,                -- 'farmer_1' | 'farmer_2' | 'manual'
  created_country TEXT,           -- País del proxy usado
  phone_country TEXT,             -- País del SMS
  cost_usd REAL,                  -- Coste de creación
  status TEXT DEFAULT 'available', -- 'available' | 'assigned' | 'banned' | 'expired'
  assigned_to TEXT,               -- Telegram user ID
  assigned_at TIMESTAMP,
  banned_at TIMESTAMP,
  notes TEXT
);

-- Usuarios de Telegram
CREATE TABLE users (
  id INTEGER PRIMARY KEY,         -- Telegram user ID
  username TEXT,
  first_name TEXT,
  role TEXT DEFAULT 'user',       -- 'user' | 'admin'
  invited_by INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  active BOOLEAN DEFAULT 1
);

-- API keys del relay
CREATE TABLE relay_keys (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER REFERENCES users(id),
  key TEXT UNIQUE NOT NULL,
  token_limit INTEGER,            -- Tokens máximos
  tokens_used INTEGER DEFAULT 0,
  models TEXT,                    -- 'gpt-4o,claude-opus-4-8'
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP,
  active BOOLEAN DEFAULT 1
);

-- Log de uso del relay
CREATE TABLE usage_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  relay_key_id INTEGER,
  model TEXT,
  prompt_tokens INTEGER,
  completion_tokens INTEGER,
  cost_usd REAL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stock tracking
CREATE TABLE stock (
  provider TEXT,
  tier TEXT,
  available INTEGER DEFAULT 0,
  total_created INTEGER DEFAULT 0,
  total_banned INTEGER DEFAULT 0,
  avg_lifetime_hours REAL,        -- Vida media antes de ban
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (provider, tier)
);
```

---

## 3. BOT DE TELEGRAM — CÓDIGO MÍNIMO

```python
# bot.py — Versión mínima funcional
import os
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Config
BOT_TOKEN = os.environ["BOT_TOKEN"]  # Bot creado con número virtual
ADMIN_IDS = [123456789]              # Tu Telegram ID
DB_PATH = "/data/farm.db"

def is_whitelisted(user_id: int) -> bool:
    db = sqlite3.connect(DB_PATH)
    row = db.execute("SELECT active FROM users WHERE id = ?", (user_id,)).fetchone()
    db.close()
    return row is not None and row[0] == 1

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_whitelisted(user.id):
        await update.message.reply_text("⛔ Acceso denegado.")
        return
    await update.message.reply_text(
        f"✅ Bienvenido, {user.first_name}.\n"
        f"Comandos:\n"
        f"/cuenta <tipo> — Solicitar cuenta\n"
        f"/relay <modelo> — API key para relay\n"
        f"/stock — Disponibilidad\n"
    )

async def cmd_cuenta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_whitelisted(user.id): return
    args = context.args
    if not args:
        await update.message.reply_text("Uso: /cuenta chatgpt_plus")
        return
    tipo = args[0].lower()
    db = sqlite3.connect(DB_PATH)
    # Buscar cuenta disponible
    row = db.execute(
        "SELECT id, email, password FROM accounts WHERE provider LIKE ? AND status='available' LIMIT 1",
        (f"%{tipo}%",)
    ).fetchone()
    if not row:
        await update.message.reply_text(f"❌ Sin stock de '{tipo}'.")
        db.close()
        return
    # Asignar cuenta
    acc_id, email, password = row
    db.execute(
        "UPDATE accounts SET status='assigned', assigned_to=?, assigned_at=CURRENT_TIMESTAMP WHERE id=?",
        (str(user.id), acc_id)
    )
    db.commit()
    db.close()
    await update.message.reply_text(
        f"📧 Cuenta: `{email}`\n"
        f"🔑 Password: `{password}`\n"
        f"⚠️ No compartir. Si se banea, avisa.",
        parse_mode="Markdown"
    )

async def cmd_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_whitelisted(user.id): return
    db = sqlite3.connect(DB_PATH)
    rows = db.execute(
        "SELECT provider, tier, available, total_created, total_banned FROM stock"
    ).fetchall()
    db.close()
    msg = "📊 STOCK:\n"
    for r in rows:
        msg += f"• {r[0]} {r[1]}: {r[2]} disp. ({r[3]} creadas, {r[4]} baneadas)\n"
    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cuenta", cmd_cuenta))
    app.add_handler(CommandHandler("stock", cmd_stock))
    app.run_polling()

if __name__ == "__main__":
    main()
```

---

## 4. FARMER — CREACIÓN DE CUENTAS (Playwright)

```python
# farm_chatgpt.py — Script de creación de cuenta ChatGPT
import asyncio
import random
import json
import sqlite3
from playwright.async_api import async_playwright

async def create_chatgpt_account(proxy_url: str, sms_provider: str, country: str = "indonesia"):
    """
    Crea 1 cuenta ChatGPT.
    proxy_url: http://user:pass@ip:port (residential)
    sms_provider: 'sms-activate' o '5sim'
    country: código país para SMS
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            proxy={"server": proxy_url},
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ]
        )
        context = await browser.new_context(
            user_agent=random_user_agent(),
            viewport={"width": 1366, "height": 768},
            locale="en-US",
            timezone_id="Asia/Jakarta" if country == "indonesia" else "Asia/Manila",
        )
        page = await context.new_page()
        
        # Stealth injection
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
        """)
        
        # --- FLUJO DE REGISTRO ---
        await page.goto("https://chat.openai.com/auth/signup")
        await asyncio.sleep(random.uniform(2, 5))
        
        # Email (generado de dominio propio)
        email = generate_email()
        await page.fill('input[name="email"]', email)
        await asyncio.sleep(random.uniform(0.5, 2))
        await page.click('button[type="submit"]')
        
        # Password
        password = generate_password()
        await page.fill('input[name="password"]', password)
        await asyncio.sleep(random.uniform(1, 3))
        await page.click('button[type="submit"]')
        
        # SMS Verification
        phone_number = await get_sms_number(sms_provider, country, "openai")
        await page.fill('input[type="tel"]', phone_number)
        await asyncio.sleep(5)
        otp = await wait_for_sms(sms_provider, phone_number, timeout=120)
        await page.fill('input[aria-label*="code"]', otp)
        await asyncio.sleep(2)
        
        # Guardar sesión
        cookies = await context.cookies()
        await browser.close()
        
        return {
            "email": email,
            "password": password,
            "cookies": json.dumps(cookies),
            "proxy_country": country,
            "phone": phone_number,
            "created_at": datetime.now().isoformat()
        }

# Funciones auxiliares
def generate_email():
    """Genera email catch-all en dominio propio"""
    return f"usr{random.randint(10000,99999)}@{os.environ['CATCHALL_DOMAIN']}"

def generate_password():
    return ''.join(random.choices('abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789', k=16))

async def get_sms_number(provider, country, service):
    """Obtiene número virtual de SMS-Activate o 5SIM"""
    # Implementación de API de SMS-Activate/5SIM
    pass

async def wait_for_sms(provider, phone_number, timeout=120):
    """Espera el código SMS y lo devuelve"""
    pass
```

---

## 5. SETUP PASO A PASO (Día 1-7)

```
───────────────────────────────────────────────────────────────
FASE 0: INFRA OCULTA (Día 1-2)
───────────────────────────────────────────────────────────────

☐ 0.1 Comprar VPS principal en Flokinet (XMR)
      - 4GB RAM, 2 vCPU, 50GB SSD (~$15/mes)
      - Ubuntu 22.04
      - Pago: XMR (sin KYC)

☐ 0.2 Comprar VPS farmer en Shinjiru/AlexHost (XMR)
      - 2GB RAM, 1 vCPU (~$8/mes)
      - Ubuntu 22.04

☐ 0.3 Crear bot de Telegram con @BotFather
      - Usar número virtual (no tu número real)
      - Nombre genérico, foto random

☐ 0.4 Comprar dominio catch-all para emails de cuentas
      - Dominio .xyz o .cyou barato (~$2/año)
      - Njalla o Internet.bs (crypto)
      - Configurar catch-all → email al farmer crea emails infinitos

☐ 0.5 Conectarse SIEMPRE via VPN a todo
      - Mullvad (crypto, ~$5/mes)
      - O ProtonVPN (crypto)

───────────────────────────────────────────────────────────────
FASE 1: BOT + RELAY (Día 2-3)
───────────────────────────────────────────────────────────────

☐ 1.1 Instalar Python + dependencias en VPS principal
☐ 1.2 Crear SQLite DB con schema
☐ 1.3 Deploy bot.py con systemd
☐ 1.4 Deploy New-API con Docker
☐ 1.5 Conseguir 1-2 API keys de OpenAI/Anthropic para el relay
      - Comprar en lzt.market o crear con tu propio farmer
☐ 1.6 Probar: /cuenta, /relay, /stock con tu usuario admin

───────────────────────────────────────────────────────────────
FASE 2: FARMER (Día 3-5)
───────────────────────────────────────────────────────────────

☐ 2.1 Instalar Playwright + dependencias en VPS farmer
☐ 2.2 Conseguir proxies residenciales
      - Empezar con Webshare (10 proxies gratis)
      - O BrightData free trial ($500 crédito)
☐ 2.3 Registrar API key en SMS-Activate (crypto)
☐ 2.4 Crear primer lote manual: 3-5 cuentas ChatGPT Free
      - Verificar pass rate, ajustar delays, cambiar país SMS si falla
☐ 2.5 Automatizar creación con cron cada 30 min

───────────────────────────────────────────────────────────────
FASE 3: OPERACIÓN (Día 5-7)
───────────────────────────────────────────────────────────────

☐ 3.1 Invitar usuarios de confianza al bot
      - Solo por invitación tuya
      - /invitar <telegram_id>
☐ 3.2 Monitorear ban rate
      - Cuentas que duran <24h → ajustar país SMS/proxy
      - Cuentas que duran >7 días → buena señal
☐ 3.3 Escalar: añadir 2-3 VPS farmer más si demanda crece
☐ 3.4 Opcional: añadir Claude, Grok, Gemini al pipeline
```

---

## 6. COSTES OPERACIONALES

```
CONCEPTO                        MENSUAL (USD)     PAGO
──────────────────────────────────────────────────────────
VPS principal (Flokinet)            $15           XMR
VPS farmer × 2                      $16           XMR
VPN (Mullvad)                        $5           XMR
Dominio catch-all (.xyz)             $2           XMR
Proxies residenciales               $20-50        crypto/BTC
SMS virtual (100-200 SMS)           $10-25        crypto
──────────────────────────────────────────────────────────
TOTAL                              ~$68-113/mes
```

**Coste por cuenta ChatGPT Free**: $0.20-0.60 (email $0 + SMS $0.10-0.40 + proxy $0.05-0.15)

**Si produces 20 cuentas/día**: 600/mes. Con 20% ban rate → 480 cuentas viables/mes. Suficiente para 10-20 usuarios.

---

## 7. SEGURIDAD OPERACIONAL (OPSEC)

```
✅ HACER:
├── Siempre VPN antes de tocar cualquier VPS
├── VPS en jurisdicciones que ignoran C&D (Rumanía, Moldavia, Malasia)
├── Dominio comprado con XMR, WHOIS privacy
├── Telegram bot con número virtual (no tu SIM real)
├── GitHub: cuenta nueva, email ProtonMail, solo crypto
├── Comunicación con usuarios: solo Telegram (cifrado)
├── NUNCA mencionar tu nombre real, ubicación, o datos personales
└── Rotar wallets crypto (no reutilizar direcciones)

❌ NO HACER:
├── NO usar servicios KYC (Vercel, AWS, Google Cloud, Stripe, Coinbase)
├── NO usar tu email/GitHub personal para nada de esto
├── NO conectarte a los VPS sin VPN
├── NO usar tu número de teléfono real para el bot de Telegram
├── NO usar Cloudflare (te pueden banear la cuenta y pedir KYC)
├── NO crear más de lo que consumes (no es negocio, es uso privado)
└── NO vender a desconocidos (solo invitación personal)
```

---

## 8. PLAN DE CAÍDA (¿Qué pasa si...?)

```
ESCENARIO                        RESPUESTA
──────────────────────────────────────────────────────────
VPS cae o Flokinet cierra       → Backup de DB en otro VPS.
                                  Recrear en AlexHost en 2h.

OpenAI banea todas tus cuentas  → Rotar país SMS + proxy.
                                  Nuevo lote en 6-12h.

Alguien filtra el bot            → /ban inmediato. Rotar token.
                                  El bot es privado, sin
                                  exposición pública.

Telegram banea el bot            → Bot nuevo con otro número
                                  virtual. Reinvitar usuarios.

Te roban una API key del relay   → Revocar key. Nueva key.
                                  Limitar tokens por key.

Flokinet entrega tus datos       → No tienen nada. Pagaste
                                  con XMR, email falso, sin KYC.
                                  El VPS solo tiene SQLite.
```

---

*Este no es un producto. Es una herramienta para ti y los tuyos. Sin web pública, sin marketing, sin usuarios desconocidos. Lo que no se ve, no se demanda.*
