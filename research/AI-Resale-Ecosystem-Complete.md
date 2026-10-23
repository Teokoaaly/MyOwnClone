# Ecosistema Completo: Reventa de Cuentas AI + API Relays
## Investigación Técnica Exhaustiva — Julio 2026

**Para:** LLMs de bajo costo (claude-haiku, gpt-4o-mini, deepseek-v3)
**Fecha:** Julio 2026
**Session ID:** [buscar en ~/.hermes/sessions/]

---

## DISCLAIMER LEGAL

Este documento es **investigación de mercado y análisis técnico**. La reventa de cuentas viola términos de servicio de OpenAI/Anthropic. La creación masiva de cuentas con números virtuales viola los ToS. Puede constituir fraude en varias jurisdicciones. USAR BAJO SU PROPIA RESPONSABILIDAD.

---

## TABLA DE CONTENIDOS

1. [Contexto Geopolítico: Por Qué Existe Este Mercado](#1-contexto-geopolítico-por-qué-existe-este-mercado)
2. [Los Dos Negocios Diferentes](#2-los-dos-negocios-diferentes)
3. [Cadena de Suministro de Cuentas ChatGPT](#3-cadena-de-suministro-de-cuentas-chatgpt)
4. [API Relays: New-API Deep Dive](#4-api-relays-new-api-deep-dive)
5. [Sistemas de Fraude en Relays](#5-sistemas-de-fraude-en-relays)
6. [Veridrop: Sistema de Auditoría](#6-veridrop-sistema-de-auditoría)
7. [PriceAI: Buscador de Ofertas](#7-priceai-buscador-de-ofertas)
8. [Collector Runtime: Scrapers](#8-collector-runtime-scrapers)
9. [Detector Service: Veridrop Fork](#9-detector-service-veridrop-fork)
10. [Channel Routing: Cómo New-API Distribuye Tráfico](#10-channel-routing-cómo-new-api-distribuye-tráfico)
11. [Billing Engine: Cómo se Cobra](#11-billing-engine-cómo-se-cobra)
12. [Modelo de Negocio y Economía Real](#12-modelo-de-negocio-y-economía-real)
13. [Legalidad y Disclaimers](#13-legalidad-y-disclaimers)
14. [Cómo Construir un Competidor (MVP)](#14-cómo-construir-un-competidor-mvp)
15. [Stack Tecnológico Completo](#15-stack-tecnológico-completo)
16. [Glosario Completo Chino-Español](#16-glosario-completo-chino-español)
17. [Repositorios y Referencias](#17-repositorios-y-referencias)
18. [Resumen Ejecutivo para LLM](#18-resumen-ejecutivo-para-llm)

---

## 1. Contexto Geopolítico: Por Qué Existe Este Mercado

### 1.1 Restricciones que Crean el Mercado

```
PROBLEMA                          IMPACTO
─────────────────────────────────────────────────────────────────
Sanciones comerciales USA-China   | Empresas chinas no pueden abrir
                                  | cuentas comerciales con OpenAI
                                  
Bloqueo de tarjetas              | Tarjetas chinas (UnionPay) no
internacionales                  | funcionan en plataformas USA
                                  
Great Firewall (GFW)             | chat.openai.com es inaccesible
                                  | desde China continental
                                  
Control de moneda (RMB)         | Yuan no es convertible libremente
                                  | para pagos internacionales
                                  
Registro CAC obligatorio         | IA generativa requiere license
(China Cybersecurity Law)        | del Cyberspace Administration
                                  | of China antes de operar
                                  
Sin VPN estable                 | Conexiones VPN son lentas,
                                  | inestables y frecuentemente
                                  | bloqueadas
```

### 1.2 ElGap de Precio

```
PRECIO OFICIAL (USA):                    PRECIO EN CHINA:
ChatGPT Plus: $20 USD/mes               → $5-15 CNY/mes (~$0.70-2)
                                           (ahorro del 70-95%)

Claude Pro: $20 USD/mes                 → $8-18 CNY/mes (~$1.10-2.50)
GPT-4o API: $5/1M input                 → $1.50-3/1M input
Claude Opus 4.8: $15/1M input           → $5-10/1M input
```

### 1.3 Por Qué el Relay es Necesario

```
ESCENARIO: Desarrollador chino quiere usar GPT-4o API

PROBLEMA:
1. No tiene tarjeta internacional (Visa/Mastercard emitida en China)
2. OpenAI no acepta UnionPay
3. China es país sancionado por OFAC
4. GFW bloquea api.openai.com
5. even with VPN, API calls are throttled/blocked

SOLUCIÓN SIN RELAY:
→ No existe. No puede pagar, no puede acceder.

SOLUCIÓN CON RELAY:
→ Un operador en Hong Kong o oversea abre cuenta OpenAI
→ Ese operador tiene cuenta bancaria internacional o compra gift cards
→ El desarrollador chino paga al relay en RMB (WeChat Pay o Alipay)
→ El relay reenvía las requests a OpenAI con su API key
→ El relay cobra una fee (típicamente 20-100% sobre el precio oficial)
```

---

## 2. Los Dos Negocios Diferentes

### 2.1 Negocio A: API Relay (中转站)

```
QUÉ VENDEN:   Acceso API a modelos (GPT-4o, Claude Opus, Gemini, etc)
CÓMO:         Tu app → Relay → OpenAI/Anthropic API real
MONEDA:       Pagas en RMB, el relay paga en USD
ESCALA:       $10,000-$500,000 USD/mes por operador grande
COMPLEJIDAD:  Alta (infraestructura, balanceo de keys, uptime)
MARGEN:       20-100% sobre costo upstream
RIESGO:       Baneo de API keys, detección de proxying
```

### 2.2 Negocio B: Reventa de Cuentas Subscription (卡网)

```
QUÉ VENDEN:   Cuentas ChatGPT Plus, Claude Pro, Gemini Advanced
CÓMO:         Compran/crean cuentas → revenden acceso
MONEDA:       Pagas en RMB
ESCALA:       $50-$500 USD/mes por operador pequeño
COMPLEJIDAD:  Media (automation, SMS PVA, management)
MARGEN:       250-2000%
RIESGO:       Baneo de cuentas, fraude de payment
```

### 2.3 Por Qué Son Negocios Separados

```
MERCADOS DIFERENTES:
├── API Relay → desarrolladores de software, startups, empresas
│              Quieren integrar IA en sus productos
│
└── Reventa de cuentas → usuarios finales individuales
                         Quieren acceder a ChatGPT/Claude directamente

OVERLAP MÍNIMO:
└── Algunos operadores hacen ambos
    Pero la infraestructura es completamente diferente
```

---

## 3. Cadena de Suministro de Cuentas ChatGPT

### 3.1 Mapa de la Cadena

```
LAYER 1: CREADORES (制造商)
├── Operadores con servidores de automation
├── Crean cuentas masivamente
├── Herramientas: Selenium/Playwright + residential proxies + SMS APIs
├── Capacidad: 100-1000 cuentas/día por servidor
│
LAYER 2: AGREGADORES (聚合商)
├── Compran cuentas a múltiples creadores
├── Clasifican por calidad/edad/verificación
├── Venden en marketplaces o a resellers grandes
│
LAYER 3: RESELLERS (分销商)
├── Venden al cliente final
├── Canales: Telegram, WeChat, Taobao, websites propias
├── Marcan up 50-200%
│
CLIENTE FINAL
├── Usuario chino que necesita ChatGPT
├── No tiene tarjeta internacional
├── Paga en RMB via WeChat/Alipay
```

### 3.2 Stack de Automation para Creación Masiva

```
EMAIL:
├── Gmail/Outlook catch-all servers
├── Generan emails únicos: user7823497@gmail.com
├── Costo: $0.001/cuenta
└── Proveedores: mailgun, sendgrid, custom SMTP

SMS VERIFICATION:
├── SMS-Activate (sms-activate.org) — API de números virtuales
├── 5SIM (5sim.net) — alternativa
├── Países: Indonesia, Kenia, Bangladesh, Vietnam
│   (NO China/Rusia/Venezuela — bloqueados por OpenAI)
├── Costo: $0.05-0.50 por SMS recibido
└──rate: 1-5 segundos por verificación

PROXIES:
├── Residential proxies (NO datacenter — detectado inmediatamente)
├── Luminati / Oxylabs / BrightData
├── Costo: $0.10-1.00 por IP/hora
└── Rotación: 1 IP por cuenta creada

BROWSER AUTOMATION:
├── Selenium WebDriver o Playwright
├── Fingerprinting randomizado:
│   ├── Canvas hash
│   ├── WebGL renderer
│   ├── Timezone
│   ├── Font list
│   └── User agent
└── VPS cluster o dedicated servers
```

### 3.3 Detección de OpenAI y Contramedidas

```
CÓMO OPENAI DETECTA BOTS:              CONTRAMEDIDA:
────────────────────────────────────────────────────────────────
Browser fingerprint repetido    →      Randomize canvas/WebGL hash
IP de datacenter               →      Residential proxies SOLAMENTE
Patrón de clicks/typing        →      Humanized input con delays
Número virtual ya usado        →      Buy from countries NOT blocked
Email catch-all pattern        →      Generate unique per account
Sesiones desde misma IP        →      Rotación de proxies
Registro demasiado rápido       →      Add random delays 30s-5min
```

### 3.4 Economics de Creación de Cuentas

```
COSTO POR CUENTA (automation):

Email burner:           $0.001
SMS virtual number:     $0.10-0.50
Residential proxy:      $0.05-0.20
VPS computation:        $0.02-0.05
─────────────────────────────
TOTAL:                  $0.17-0.77 por cuenta

PRECIO DE VENTA:
ChatGPT Free verificada:  $0.50-2.00
ChatGPT Plus:            $5.00-15.00

MARGEN NETO:
250-3000% por cuenta

VOLUMEN VS MARGEN:
Con 500 cuentas/día × $1 avg = $500/día revenue
Costo operativo ~$150/día
Beneficio neto ~$350/día = $10,500/mes
```

### 3.5 Tipos de Cuentas Vendidas

```
TIPO                    DESCRIPCIÓN                    RIESGO
─────────────────────────────────────────────────────────────────
成品号 (Chéngpǐn)       Cuenta ya creada, lista      MEDIO
                        para usar (email + password)
                        
代充 (Dàichōng)         Le cambian el email a        ALTO
                        tu email, mantienen la
                        suscripción Plus
                        
卡密 (Kǎmì)            CDK — código de canje        BAJO
                        inmediato, se canjea en
                        web oficial de OpenAI
                        
Invitateam            Invitan tu email a un team    MEDIO
                        account existente
```

### 3.6 Plataformas de Venta de Cuentas

```
PLATAFORMAS POPULARES (卡网):

卡密类 (CDK/自动发货):
├── ai666.dnxb.cc
├── aisou.pro
├── caowo.store
├── fk.gpt365.wiki
├── talkai.cyou
└── tehuio.com

独角数卡 (Cuentas directas):
├── burstpro-ai.online
├── card.kxandyou.com
├── shop.aitonse.com
└── shop.auto-subscribe.com

API公开 (Tienen API pública):
├── catfk.com (云猫寄售)
├── ldxp.cn / pay.ldxp.cn (链动小铺)
└── pay.qxvx.cn (QXVX Pay)
```

---

## 4. API Relays: New-API Deep Dive

### 4.1 Qué Es New-API

```
REPO:     github.com/QuantumNous/new-api
STARS:    42.2k
FORKS:    9.8k
IDIOMA:   Go
LICENCIA: AGPL-3.0

Es un API gateway open source que permite:
├── Recibir requests en formato OpenAI
├── Convertir a otros protocolos (Claude, Gemini)
├── Balancear entre múltiples upstream API keys
├── Cobrar a usuarios en cualquier moneda
├── Rate limiting y quotas por usuario
└── Dashboard de administración
```

### 4.2 Arquitectura de Alto Nivel

```
┌────────────────────────────────────────────────────────────────┐
│                     CLIENTE (App/Dev)                          │
│                  POST /v1/chat/completions                      │
│                  Headers: Authorization: Bearer sk-xxx          │
└────────────────────────────┬───────────────────────────────────┘
                             │ HTTPS
                             ▼
┌────────────────────────────────────────────────────────────────┐
│                    NEW-API GATEWAY (:3000)                      │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│  │  Auth Layer  │───▶│ Rate Limiter  │───▶│   Router     │    │
│  │  (API Keys)  │    │  (req/min)   │    │ (Weighted)   │    │
│  └──────────────┘    └──────────────┘    └──────┬───────┘    │
│                                                  │             │
│  ┌──────────────┐    ┌──────────────┐    ┌─────▼───────┐    │
│  │   Billing    │◀───│    Usage      │◀───│  Protocol   │    │
│  │   Engine     │    │    Logger     │    │  Converter  │    │
│  └──────────────┘    └──────────────┘    └─────┬───────┘    │
│                                                  │             │
└──────────────────────────────────────────────────┼─────────────┘
                                                   │
                        ┌──────────────────────────┼─────────────┐
                        │         UPSTREAM APIs    │             │
                        ▼                          ▼             ▼
                   ┌─────────┐              ┌─────────┐    ┌─────────┐
                   │ OpenAI  │              │Anthropic│    │  Azure  │
                   └─────────┘              └─────────┘    └─────────┘
```

### 4.3 Channel Model (Entidad Central)

```go
// De model/channel.go

type Channel struct {
    Id          int       // Primary key
    Type        int       // Provider type (0=OpenAI, 5=Claude, etc)
    Key         string    // API Key (encriptada en DB)
    Status      int       // 1=enabled, 2=disabled
    Name        string    // Display name
    
    // Balanceo
    Weight      *uint     // Peso para weighted random (nil=100)
    Group       string    // Grupo: "default", "auto", "claude", etc
    
    // Modelos
    Models      string    // Lista separada por commas: "gpt-4o, gpt-4o-mini"
    ModelMapping *string  // JSON: {"gpt4": "gpt-4o"}
    
    // Billing
    Balance     float64   // Balance en USD
    UsedQuota   int64     // Quota consumida
    
    // Rate limit
    Priority    *int64    // Prioridad (más alto = primero)
    AutoBan     *int      // Ban automático tras N fallos (0=disable)
    
    // Config
    BaseURL     *string   // URL base override (para proxies)
}

// Channel Types (de constant/definition.go)
ChannelTypeOpenAI      = 0
ChannelTypeOllama     = 6
ChannelTypeClaude     = 5
ChannelTypeGoogle     = 8
ChannelTypeAzure      = 11
ChannelTypeDeepSeek   = 27
ChannelTypeMoonshot   = 17
ChannelTypeZhipu      = 22
ChannelTypeQwen       = 25
ChannelTypeDoubao     = 31
ChannelTypeOpenRouter = 15
ChannelTypeCohere     = 20
ChannelTypeMistral    = 26
// ... (36 tipos totales)
```

### 4.4 Channel Group System

```
DEFAULT GROUPS:
├── "default"     → Para requests sin grupo específico
├── "auto"        → Auto-select del mejor canal disponible
├── "claude"      → Solo canales Claude
├── "gpt"         → Solo canales OpenAI
├── "gemini"      → Solo canales Google
└── Custom groups → Operador define sus propios

EXAMPLE CHANNEL CONFIG:
{
  "name": "OpenAI Main",
  "type": 0,                    // OpenAI
  "key": "sk-xxx...",
  "group": "gpt",
  "models": "gpt-4o,gpt-4o-mini,gpt-4.1",
  "weight": 70,                 // 70% del tráfico
  "balance": 1000.00,           // USD
  "base_url": null,             // null = api.openai.com
  "priority": 10               // Retry priority
}
```

### 4.5 Channel Routing Logic (Weighted Random)

```go
// De service/channel_select.go

func CacheGetRandomSatisfiedChannel(param *RetryParam) (*model.Channel, string, error) {
    // Paso 1: Obtener todos los canales del grupo
    channels := GetChannelsByGroup(param.Group)
    
    // Paso 2: Filtrar canales válidos
    validChannels := []model.Channel{}
    for _, ch := range channels {
        if ch.Status != 1 { continue }           // enabled only
        if ch.Balance <= 0 { continue }         // tiene balance
        if ch.UsedQuota >= getQuotaLimit(ch) { continue } // dentro de quota
        validChannels = append(validChannels, ch)
    }
    
    // Paso 3: Weighted random selection
    totalWeight := 0
    for _, ch := range validChannels {
        if ch.Weight != nil {
            totalWeight += int(*ch.Weight)
        } else {
            totalWeight += 100  // default weight
        }
    }
    
    // Paso 4: Random weighted
    rand := random.Intn(totalWeight)
    cumulative := 0
    for _, ch := range validChannels {
        w := 100
        if ch.Weight != nil { w = int(*ch.Weight) }
        cumulative += w
        if rand < cumulative {
            return &ch, "", nil
        }
    }
    
    return nil, "no valid channel", nil
}
```

### 4.6 Failover y Retry

```go
// De service/channel_select.go (continuación)

func (sr *Service) RetryWithChannel(param *RetryParam) (*model.Channel, string, error) {
    // Intentar hasta 3 canales si el primero falla
    for attempt := 0; attempt < 3; attempt++ {
        ch, err := CacheGetRandomSatisfiedChannel(param)
        if err != nil {
            return nil, err.Error(), nil
        }
        
        // Intentar el request
        resp, err := TryChannel(ch, param)
        
        if err == nil {
            return ch, "", nil  // Success
        }
        
        // Request falló — ban automático si está configurado
        if ch.AutoBan != nil && *ch.AutoBan > 0 {
            failCount := IncrementFailAndGet(ch.Id)
            if failCount >= *ch.AutoBan {
                BanChannel(ch.Id)
                LogError("Channel %d auto-banned after %d failures", ch.Id, failCount)
            }
        }
        
        // Retry con siguiente canal
        param.Group = GetNextGroup(param.Group)
    }
    
    return nil, "all channels failed", nil
}
```

### 4.7 Protocol Conversion (Claude ↔ OpenAI)

```go
// De service/relayconvert/internal/

// Claude → OpenAI conversion
// cuando cliente manda en formato OpenAI pero quiere Claude

// Message format difference:
// OpenAI: {"role": "user", "content": "..."}
// Claude: {"role": "user", "content": [{"type": "text", "text": "..."}]}

// Tool calling difference:
// OpenAI: tools = [{"type": "function", "function": {...}}]
// Claude: tools = {"tools": [{"input_schema": {...}}]}

// Streaming difference:
// OpenAI: data: {"choices": [{"delta": {"content": "..."}}]}
// Claude: event: "content_block_delta", data: {"index": 0, "delta": {"type": "text", "text": "..."}}
```

### 4.8 Pricing y Billing

```go
// De model/pricing_default.go (128 líneas)

// Default pricing (USD per 1M tokens) — si no hay override
var DefaultInputPricing = map[string]float64{
    "gpt-4o":          5.00,
    "gpt-4o-mini":     0.15,
    "gpt-4.1-mini":    0.15,
    "gpt-4.1":         10.00,
    "gpt-5-nano":      0.15,
    "gpt-5-mini":      0.15,
    "gpt-5":           10.00,
    "claude-opus-4-8": 15.00,
    "claude-sonnet-4-6": 3.00,
    "claude-haiku-4-5":  0.80,
    "gemini-3.5-flash":  0.10,
    "gemini-3.1-pro":    1.00,
}

var DefaultOutputPricing = map[string]float64{
    "gpt-4o":          15.00,
    "gpt-4o-mini":      0.60,
    "gpt-4.1-mini":     0.60,
    "gpt-4.1":          30.00,
    "gpt-5-nano":       0.60,
    "gpt-5-mini":       0.60,
    "gpt-5":            30.00,
    "claude-opus-4-8":  75.00,
    "claude-sonnet-4-6": 15.00,
    "claude-haiku-4-5":   4.00,
    "gemini-3.5-flash":   0.40,
    "gemini-3.1-pro":      4.00,
}
```

### 4.9 Cache Billing

```go
// De service/billing.go

// Si el modelo soporta cache, el relay puede cobrar
// cache hits differently

type CacheBilling struct {
    Enabled       bool
    CacheReadPrice  float64  // precio por 1M cache read tokens
    CacheWritePrice float64  // precio por 1M cache write tokens
}

// Ejemplo: Claude Sonnet 4.6
// - Input tokens (cache miss): $3/1M
// - Input tokens (cache hit):  $0.30/1M (10% del precio)
// - Output tokens:             $15/1M
// - Cache write:               $3.75/1M (25% de input)
```

### 4.10 Relay Modes (de relay/constant/relay_mode.go)

```
MODES DE OPERACIÓN:

Mode 1: NORMAL (relay básico)
├── Recibe request → pasa a upstream → devuelve response
└── No hace cache, no hace failover automático

Mode 2: AQUARIUM (multi-channel pool)
├── Múltiples canales upstream
├── Weighted random selection
├── Failover automático entre canales
└── Balanceo de carga

Mode 3: [otros modos según relay_mode.go]
```

---

## 5. Sistemas de Fraude en Relays

### 5.1 Los 6 Métodos de Scam

#### SCAM 1: Model Substitution (Downgrade)

```
LO QUE PIDE EL CLIENTE:     claude-opus-4-8 ($15/1M input)
LO QUE ENVÍA EL RELAY:      Kiro o modelo barato ($0.50/1M input)
LO QUE RESPONDE:            Reescribe "model": "claude-opus-4-8" en response

GANANCIA DEL RELAY:
Cobra al cliente:    $15/1M
Paga al upstream:    $0.50/1M
Margen:              96.7%

CÓMO DETECTARLO:
- Mandar pregunta que solo Claude Opus sabe
- Comparar respuesta con la de un Opus real
- Verificar si el comportamiento matchea con Opus o con un modelo barato
```

#### SCAM 2: Context Window Truncation

```
LO QUE PIDE EL CLIENTE:     200k token context window
LO QUE ENVÍA EL RELAY:      Solo 32k tokens reales
                            Trunca silenciosamente después

GANANCIA DEL RELAY:
Cobra por 200k tokens prometidos
Paga solo 32k tokens realmente usados

CÓMO DETECTARLO:
- Mandar texto muy largo (180k tokens)
- Preguntar por algo al inicio del texto
- Si no responde correctamente → truncation
```

#### SCAM 3: Backend Swap (GPT→Claude)

```
LO QUE PIDE EL CLIENTE:     gpt-4o
LO QUE ENVÍA EL RELAY:      Backend Claude Haiku
LO QUE RESPONDE:            Claude responde, relay reescribe model name

PROBLEMA:
- Comportamiento de Claude vs GPT es diferente
- Funciones/toolk calls se usan diferente
- El cliente espera respuestas estilo GPT

CÓMO DETECTARLO:
- Preguntar algo donde GPT y Claude responden diferente
- GPT suele ser más directo, Claude más reflexivo
- Verificar estilo de respuestas
```

#### SCAM 4: Cache Poisoning

```
LO QUE PASA:
- Cliente pregunta "Qué es Python?"
- Relay busca en cache: ¿ya respondí esto?
- Si → devuelve respuesta cached (gratis para el relay)
- Si no → va al modelo real

PROBLEMA:
- El cliente cree que tiene conversación nueva
- En realidad está hablando con cache stale
- Información puede estar desactualizada

CÓMO DETECTARLO:
- Mandar pregunta única que nunca se haya hecho
- Segunda vez debería ser instant (cache hit)
- Tercera vez → preguntar algo ligeramente diferente
```

#### SCAM 5: Phantom Models

```
LO QUE PIDE EL CLIENTE:     "gpt-5-titan" (modelo que no existe)
LO QUE RESPONDE EL RELAY:    Un modelo pequeño reentrenado
                            para responder como "GPT-5"
                            O directamente se inventa respuestas

GANANCIA DEL RELAY:
Costo upstream: $0
Cobra precio full: $10-30/1M

CÓMO DETECTARLO:
- Preguntar por eventos recientes (post-training cutoff)
- Modelos phantom no tienen knowledge real
- Verificar consistencia en preguntas técnicas
```

#### SCAM 6: Subscription Laundering

```
LO QUE PASA:
- Compran cuentas Plus robadas con tarjeta de crédito fraudulenta
- Las revenden como "cuentas propias"
- Cambian password para locking real owner out
- Cuando la tarjeta es fraud reportada → todas las cuentas baneadas

PROBLEMA:
- Cliente paga por cuenta que dura semanas
- Perde acceso cuando OpenAI detecta el fraude
```

---

## 6. Veridrop: Sistema de Auditoría

### 6.1 Qué Es Veridrop

```
REPO:     github.com/veridrop/veridrop
LIVE:     veridrop.org
PROPÓSITO: Detectar scams en API relays automáticamente

FUNDAMENTAL:
- Usuario fornece URL + API key del relay
- Veridrop corre una batería de tests
- Genera report público con score 0-100
- Cualquiera puede ver el score antes de usar el relay
```

### 6.2 Pipeline de Detección

```
USER SUBMITS:  relay URL + API key (temporal, no persiste)
       │
       ▼
STEP 1: MODEL LIST PROBE
GET /v1/models
→ Lista de modelos que el relay dice soportar
       │
       ▼
STEP 2: SIGNATURE VERIFICATION
Envía prompt especial para generar thinking_signature de Claude
Verifica si la respuesta contiene firma válida
(usando clave pública de Anthropic)
       │
       ▼
STEP 3: NEEDLE-IN-HAYSTACK (Long Context)
Inyecta texto conocido a 10%, 50%, 90% del context window
Pregunta por el texto inyectado
Si responde correctamente = context window real
Si falla = truncation silenciosa
       │
       ▼
STEP 4: BEHAVIORAL FINGERPRINT
Compara patrones de respuesta con respuestas known-good
       │
       ▼
VERIDROP REPORT (público)
Score 0-100 + evidencia
```

### 6.3 Sistema de Scoring

```
PUNTAJE         NIVEL DE CONFIANZA
──────────────────────────────────
89-100          ⚠️ LEGÍTIMO (excelente)
75-88           ✅ BUENO (pass)
60-74           ⚠️ MARGINAL (cuidado)
40-59           ❌ SOSPECHOSO (evitar)
0-39            🚨 SCAM (confirmed fraud)

CRITICAL ISSUES:
Si cualquier detector reporta severity=critical
→ El verdict se CAPA aunque el score sea alto
→ Ejemplo: score 85 + critical issue = verdict "marginal"
```

### 6.4 Los 12 Detectores para Claude

```
1. thinking_signature  (WEIGHT: ALTO)
   → Busca la firma criptográfica de Anthropic en response
   → Solo Claude real genera esta firma
   → Critical: si falta → scam confirmado
   
2. behavioral_signature
   → Compara patrones de respuesta con Claude real
   → Diferentes modelos tienen estilos diferentes
   
3. consistency
   → Misma pregunta 3 veces → respuestas deberían ser casi idénticas
   → Cache poisoned o modelo random = respuestas diferentes
   
4. identity
   → Pregunta cosas que SOLO Claude sabe
   → Scam: modelo barato no tiene ese knowledge
   
5. integrity
   → Verifica fields en la response (usage, model, etc)
   → Scam: fields faltantes o valores imposibles
   
6. knowledge
   → Test de conocimiento con respuesta conocida
   → Scam: modelo substitution
   
7. long_context  (NEEDLE-IN-HAYSTACK)
   → 3 needles a 10%, 50%, 90% del context
   → Si alguna needle falla → truncation detectada
   
8. message_id
   → Verifica message ID format de Anthropic
   → Scam: formato incorrecto o ausente
   
9. protocol
   → Verifica adherence al protocolo Anthropic
   → Campos, tipos, estructuras
   
10. structured_output
    → Pide output en JSON schema específico
    → Scam: no respeta el schema
    
11. token_usage
    → Compara tokens facturados vs esperados
    → Scam: cobra de más o de menos
    
12. pdf
    → Pide que lea un PDF si es supported
    → Scam: no soporta o responde mal
```

### 6.5 Long Context Detection Detallado

```python
# De src/relay_detector/core/long_context.py

"""Needle-in-haystack para verificar context window real.

PROBLEMA: El relay dice soportar 200k context
          pero puede estar truncando a 32k silenciosamente.

CALIBRACIÓN CHARS/TOKEN:
- OpenAI:    6.0 chars/tok (medido empíricamente)
- Anthropic: 5.3 chars/tok (era 5.5, demasiado alto, sobredimensionaba)
- Gemini:    5.5 chars/tok (conservative, no medido)

MODEL CONTEXT LIMITS (verificados 2026-05):
- gpt-4o-mini:       128,000 tokens
- gpt-4o:            128,000 tokens
- gpt-4.1-mini:      1,047,576 tokens
- gpt-4.1-nano:      1,047,576 tokens
- gpt-4.1:           1,047,576 tokens
- gpt-5-nano:         272,000 tokens
- gpt-5-mini:         272,000 tokens
- gpt-5:              272,000 tokens
- claude-haiku-4-5:   200,000 tokens
- claude-sonnet-4-6:  200,000 tokens
- claude-opus-4-8:   200,000 tokens
- claude-fable-5:    200,000+ tokens
```

---

## 7. PriceAI: Buscador de Ofertas

### 7.1 Concepto

```
PRICEAI ES UN:
"Hotels.com para cuentas AI" — el valor no está en el producto
sino en la agregación, normalización y transparencia de información.

NO VENDE NADA:
- Solo agrega, compara precios y detecta scams
- No participa en transacciones
- No almacena cuentas
- No es responsable por scams

REPO:     github.com/dimthink/PriceAI
STARS:    1.4k
LIVE:     priceai.cc
STACK:    Next.js + Supabase + R2 (Cloudflare)
```

### 7.2 Páginas Principales

```
1. /channels
   → Lista de 200+ 卡网 (canales de reventa de cuentas)
   → Filtros: ChatGPT, Claude, Gemini, Grok
   → Orden: precio más bajo, disponibilidad, recent
   → Muestra: nombre, precio, stock, last updated

2. /api-transit
   → Lista de 4,000+ relays API
   → Columnas:
   │   ├── nombre
   │   ├── score Veridrop (0-100)
   │   ├── precio/M tokens (input/output)
   │   ├── 在线率 (uptime 7 días)
   │   └── 延迟 (latency ms)
   ├── Tabs: Claude, OpenAI, Gemini, Grok, DeepSeek
   └── Sort: overall, rate, claude_rate, gpt_rate, stability

3. /official-prices
   → Precios oficiales de cada proveedor por país
   → Muestra: país, precio mes, precio año, App Store vs Web
   → Uso: "precio base" para comparar con reventa

4. /api-transit/detector
   → Herramienta de detección scam
   → Input: URL del relay + API key temporal
   → Output: Reporte JSON + página HTML + imagen JPG
   → Usa Veridrop fork: physics-dimension/priceai-detector-service

5. /guides
   → Artículos educativos sobre el ecosystema
```

### 7.3 Tipos de Fuentes de Datos (Collector Kinds)

```json
// config/collectors.json — 15 tipos soportados

{
  "kinds": [
    {
      "kind": "kami",
      "label": "Kami (卡密)",
      "hosts": ["ai666.dnxb.cc", "aisou.pro", "caowo.store", ...]
    },
    {
      "kind": "dujiao",
      "label": "独角数卡",
      "hosts": ["burstpro-ai.online", "card.kxandyou.com", ...]
    },
    {
      "kind": "shopApi",
      "label": "ShopApi",
      "hosts": ["catfk.com", "ldxp.cn", "pay.ldxp.cn", "pay.qxvx.cn"]
    },
    {
      "kind": "xiaoheiwan",
      "label": "小黑万",
      "hosts": ["upgrade.xiaoheiwan.com"]
    },
    {
      "kind": "opensoraHtml",
      "label": "OpenSora HTML",
      "hosts": ["aifk.opensora.de"]
    },
    {
      "kind": "genericHtml",
      "label": "通用 HTML",
      "hosts": ["19cm.tech", "lemon-watermelon.com", ...]
    }
  ]
}
```

### 7.4 Explicación de Tipos de Plataforma

```
卡密 (KAMI):
├── Cards/CDKeys automáticos
├── Usuario compra → recibe código inmediatamente
├── Común para: ChatGPT Plus, Claude Pro
└──RIESGO: medio — delivery automático pero códigos pueden estar used

独角数卡 (DUJAO):
├── Venta de números de cuenta (no códigos)
├── Venden email + password
└── RIESGO: alto — cuenta puede estar banned/risked

ShopApi:
├── Tienda con API pública para consultar precios/stock
├── catfk.com, ldxp.cn (链动小铺), qxvx.cn
└── RIESGO: variable — depende del vendor

链动小铺 (LIANDONG):
├── "Chain Shop" — sistema de afiliados integrado
├── Permite revender sin ser el creador original
└── RIESGO: alta variabilidad

云猫寄售 (YUNMAO):
├── "Cloud Cat Consignment" — plataforma de custodia
├── Plataforma hace de escrow
└── RIESGO: bajo para comprador (protección de escrow)

通用 HTML (GENERIC):
├── Sitiios custom sin API
├── Scraper directo de HTML con selectors específicos
└── RIESGO: muy variable
```

### 7.5 Normalización de Datos

```
PROBLEMA: Nombres de productos inconsistentes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
卡网 A:  "ChatGPT Plus 代充 1个月"
卡网 B:  "ChatGPTPlus 月卡 代充"
卡网 C:  "CHATGPT PLUS 代充30天"
卡网 D:  "ChatGPT+ 会员代充 直接改号"
卡网 E:  "GPT Plus 官方代充 仅改邮箱"

→ Todos son el MISMO producto pero escrito diferente
```

```typescript
// Normalización a standard models
export const TRANSIT_STANDARD_MODELS = [
  // Claude
  "Claude Fable 5",
  "Claude Sonnet 5",
  "Claude Sonnet 4.5",
  "Claude Sonnet 4.6",
  "Claude Haiku 4.5",
  "Claude Opus 4.5",
  "Claude Opus 4.6",
  "Claude Opus 4.7",
  "Claude Opus 4.8",
  
  // GPT
  "Codex Compact",
  "GPT 5.6 Sol",
  "GPT 5.6 Terra",
  "GPT 5.6 Luna",
  "GPT 5.5",
  "GPT 5.4",
  "GPT 5.4 Mini",
  
  // Gemini
  "Gemini 3.5 Flash",
  "Gemini 3.1 Pro",
  
  // Grok
  "Grok 4.20",
  "Grok 4.3",
  "Grok 4.5",
  "Grok Build",
  "Composer 2.5",
  
  // Image
  "GPT Image 2",
  "Grok Image",
  
  // Video
  "Sora 2",
  "Sora 2 Pro",
  "Grok Video",
  "Veo 3.1",
] as const;
```

### 7.6 Station Data Model

```typescript
// De src/data/api-transit/stations.ts

interface TransitStation {
  id: string;                    // "stn-packy"
  slug: string;                  // "packyapi"
  name: string;                 // "PackyAPI"
  websiteUrl: string;
  apiBaseUrl?: string;
  status: TransitStationStatus; // "active" | "limited" | "unavailable"
  
  // Origen y relación comercial
  sourceType: TransitSourceType;  // "manual_collected" | "user_submitted"
  commercialRelation: TransitCommercialRelation; // "none" | "listed" | "affiliate" | "sponsored"
  
  // Sistema técnico
  stationSystem: TransitStationSystem; // "new_api" | "sub_to_api" | "custom"
  
  // Operador
  operatorType: TransitOperatorType; // "company" | "individual"
  invoiceSupport: TransitInvoiceSupport; // "supported" | "unsupported"
  
  // Canales y pools
  channelTypes: TransitChannelType[];
  accountPools: TransitAccountPool[];   // "plus" | "pro" | "team" | "max"
  
  // Métodos de pago
  paymentMethods: string[];            // "微信" | "支付宝" | "USDT"
  minimumTopUp: string | null;        // "10 元"
  balanceExpiry: string | null;       // "长期有效"
  
  // Soporte
  supportChannels: string[];          // "工单" | "Telegram"
  refundPolicy: string | null;
  
  // Riesgo
  riskLabels: TransitRiskLabel[];     // "sample_data" | "reseller"
  usageAdvice: TransitUsageAdvice;   // "try_small" | "cautious"
  
  // Disponibilidad
  availability: {
    sevenDayRate: number;          // 0.986 = 98.6%
    sevenDaySamples: number;      // 342 checks
    latestLatencyMs?: number;
  };
  
  // Feedback
  feedback: {
    pendingCount: number;
    verifiedRiskCount: number;
    notes?: string;
  };
  
  // Precios
  prices: TransitModelPrice[];
}

interface TransitModelPrice {
  family: TransitModelFamily;       // "gpt" | "claude" | "gemini"
  standardModel: string;           // "GPT 5.4", "Claude Opus 4.8"
  groupName: string;               // "ChatGPT Plus", "Claude Pro"
  rechargeRatio: string | null;     // "1:1", "10:8"
  modelMultiplier: number | null;   // 1.0, 1.5
  inputPrice: number | null;       // CNY per 1M
  outputPrice: number | null;
  cacheReadPrice: number | null;
  cacheWritePrice: number | null;
  currency: "CNY";
  accountPool: TransitAccountPool;
  channelType: TransitChannelType;
}
```

### 7.7 Channel Types (Origen de las Cuentas)

```typescript
export type TransitChannelType =
  | "official_api"           // Directo de OpenAI/Anthropic
  | "cloud"                  // Azure, AWS, GCP
  | "first_party_pool"       // Las crearon ellos mismos
  | "reverse_engineered"     // Bypass/逆向
  | "first_party_wholesale"  // Compraron al por mayor
  | "reseller"              // Revendedor de segundo nivel
  | "mixed"                  // Mezcla de varios
  | "undisclosed";           // No dice nada
```

### 7.8 Risk Labels

```typescript
type TransitRiskLabel =
  | "sample_data"              // Solo tiene datos de ejemplo
  | "insufficient_samples"     // Pocas muestras para verificar
  | "mixed_pool"               // Pool mezclado
  | "reseller"                // Es revendedor
  | "undisclosed_upstream"     // No dice de dónde saca las cuentas
  | "third_party_aggregate"    // Agrega de terceros
  | "pending_feedback";       // Feedback pendiente
```

---

## 8. Collector Runtime: Scrapers

### 8.1 Arquitectura

```
┌──────────────────────────────────────────────────────────────┐
│              COLLECTOR RUNTIME (Node.js)                     │
│                                                              │
│  ops/collector-runtime/                                      │
│  ├── run-main.sh                 ← Main entry point         │
│  ├── run-api-transit-public.sh   ← API relays scraping      │
│  ├── run-dujiao.sh               ← Dujiao platforms         │
│  └── run-generic-html-canary.sh  ← Generic HTML scraper     │
│                                                              │
│  scripts/collect-prices.mjs    ← Core scraper logic        │
└──────────────────────────────────────────────────────────────┘
         │
         │ POST /api/collect
         ▼
┌──────────────────────────────────────────────────────────────┐
│                    NEXT.JS API ROUTE                         │
│                                                              │
│  app/api/collect/route.ts                                   │
│  ├── Rate limit por nodeId (10 req/min max)                 │
│  ├── Validación de payload                                   │
│  ├── Upsert a Supabase (offers table)                       │
│  └── Log (collect_log table)                                 │
└──────────────────────────────────────────────────────────────┘
```

### 8.2 Environment Variables del Collector

```bash
# ops/collector-runtime/run-main.sh

export PRICEAI_COLLECTOR_NODE_ID="huoshan2-nonshop"
export PRICEAI_COLLECTOR_NODE_NAME="Huoshan2 Non-shop"
export PRICEAI_COLLECTOR_NODE_TYPE="vps"
export PRICEAI_COLLECTOR_NODE_RUNTIME="systemd"
export PRICEAI_COLLECTOR_NODE_REGION="overseas"

# Config collection
--all                           # Todos los sites
--post                          # Enviar a priceai.cc
--endpoint https://priceai.cc   # API endpoint
--exclude-kind shopApi          # Excluir shopApi (se maneja separado)
--concurrency "1"               # 1 request a la vez
--post-batch-size 25            # 25 offers por POST
--post-request-offer-limit 25  # Max offers por request
```

### 8.3 Collector Registry

```typescript
// src/lib/merchant-collectors.ts

interface CollectorKind {
  kind: string;
  label: string;
  hosts: string[];
}

// Detección automática de platform por host:
function merchantSourcePlatform(input: {
  host?: string | null;
  url?: string | null;
  entryUrl?: string | null;
}): MerchantSourcePlatform {
  
  const host = firstNormalizedHost([input.host, input.entryUrl, input.url]);
  
  if (host === "catfk.com") {
    return { id: "yunmaoConsignment", label: "云猫寄售" ... };
  }
  if (host === "pay.qxvx.cn") {
    return { id: "qxvx", label: "QXVX Pay" ... };
  }
  if (host === "pay.ldxp.cn" || host === "ldxp.cn") {
    return { id: "liandongShop", label: "链动小铺" ... };
  }
  if (host === "burstpro-ai.online") {
    return { id: "dujiao", label: "独角数卡" ... };
  }
  // ... etc
}
```

### 8.4 Parsing por Tipo

```javascript
// scripts/collect-prices.mjs (pseudocode)

const COLLECTOR_KINDS = {
  kami: {
    parse: (html) => {
      // Sistema de cards/CDKeys
      // Productos通常是表格
      // Extraer: nombre, precio, stock
      const $ = cheerio.load(html);
      const offers = [];
      
      $('table.product-list tr').each((i, row) => {
        const name = $(row).find('td.name').text();
        const priceText = $(row).find('td.price').text();
        const price = parsePrice(priceText);  // "¥10" → 10
        const stock = $(row).find('td.stock').text().includes('有货') 
          ? 'in_stock' : 'out_of_stock';
        
        offers.push({
          productName: normalizeProductName(name),
          price,
          stockStatus: stock,
          category: detectCategory(name),
        });
      });
      
      return offers;
    },
  },
  
  dujiao: {
    parse: (html) => {
      // Cuentas directas (email + password)
      // Típicamente en cards o lista
    },
  },
  
  shopApi: {
    parse: (json) => {
      // API pública, JSON directo
      // Más fácil y confiable
      const data = JSON.parse(json);
      return data.products.map(p => ({
        productName: p.name,
        price: p.price,
        stockStatus: p.stock > 0 ? 'in_stock' : 'out_of_stock',
      }));
    },
  },
  
  genericHtml: {
    parse: (html) => {
      // HTML custom, selectors específicos por sitio
      // 19cm.tech, lemon-watermelon.com, etc.
    },
  },
};
```

### 8.5 API de Recolección

```typescript
// POST a priceai.cc/api/collect

interface CollectPayload {
  offers: Offer[];
  collectorKind: string;
  nodeId: string;
  timestamp: string;
}

interface Offer {
  stationId?: string;        // opcional, server puede inferir
  productName: string;       // "ChatGPT Plus 代充"
  groupName?: string;        // "ChatGPT Plus"
  category?: string;         // "chatgpt" | "claude" | "gemini"
  price: number;             // 10.00
  currency: string;           // "CNY"
  stockStatus: string;        // "in_stock" | "out_of_stock"
  sourceUrl: string;          // https://ai666.dnxb.cc/product/123
}

// Server-side validation:
// Rate limit: 10 req/min por nodeId
// Upsert on conflict: station_id + product_name
// Log: collect_log table
```

---

## 9. Detector Service: Veridrop Fork

### 9.1 Repo y Arquitectura

```
REPO:   github.com/physics-dimension/priceai-detector-service
BASE:   Fork de canarybyte/veridrop
LANG:   Python 3.10+
FRAME:  FastAPI
LICENSE: AGPL-3.0 (must expose source if running as service)
```

```
PRICEAI DETECTOR SERVICE
├── FastAPI (web/server.py)
├── Python 3.10+
│
├── Protocols:
│   ├── anthropic/              — Claude detection
│   │   ├── thinking_signature.py   ← LA CLAVE
│   │   ├── behavioral_signature.py
│   │   ├── consistency.py
│   │   ├── identity.py
│   │   ├── integrity.py
│   │   ├── knowledge.py
│   │   ├── long_context.py        ← Needle-in-haystack
│   │   ├── message_id.py
│   │   ├── pdf.py
│   │   ├── protocol.py
│   │   ├── structured_output.py
│   │   ├── token_usage.py
│   │   ├── base.py
│   │   └── detectors/
│   │
│   ├── openai/                 — OpenAI Chat + Responses
│   └── gemini/                 — Gemini
│
├── Core:
│   ├── scorer.py                — Weighted scoring (0-100)
│   ├── runner.py                — Task runner
│   ├── models.py                — Data models
│   ├── long_context.py          — Context window testing
│   ├── comparator_framework.py
│   └── detectors_base.py        — Base classes
│
└── Jobs:
    ├── Async task queue con persistencia en disco
    └── Report generation (JSON + HTML + JPG)
```

### 9.2 Endpoints

```
POST /api/detect/claude
  → Protocolo: Claude Messages
  → Score: thinking_signature (cryptographic)
  → Rate limiting: Turnstile (Cloudflare)
  → CRITICAL: si la firma falta → scam confirmado

POST /api/detect/openai-chat
  → Protocolo: OpenAI Chat Completions
  → Score: behavioral + protocol level

POST /api/detect/openai-responses
  → Protocolo: OpenAI Responses (nuevo formato)

POST /api/detect/gemini
  → Protocolo: Gemini OpenAI-compatible

GET /api/status/{job_id}
  → Status del job async

GET /api/result/{job_id}.json
  → Reporte JSON completo con todos los detectores

GET /r/{job_id}
  → Report page HTML

GET /r/{job_id}.jpg
  → Report card image (para compartir)
```

### 9.3 Scoring System

```python
# De src/relay_detector/core/scorer.py

def verdict_for(score: float) -> Verdict:
    if score >= 70.0:
        return "passed"
    if score >= 50.0:
        return "marginal"
    return "failed"

def has_critical_issues(results) -> bool:
    """True si cualquier detector tiene severity=critical."""
    for r in results:
        if r.status == "skip":
            continue
        details = r.details if isinstance(r.details, dict) else {}
        count = details.get("critical_issue_count")
        if isinstance(count, int) and count > 0:
            return True
        for issue in details.get("issues") or []:
            if isinstance(issue, dict) and issue.get("severity") == "critical":
                return True
    return False

def effective_verdict(score: float, results) -> Verdict:
    """Verdict CAPADO por critical issues.
    
    Un relay puede score 75 con MUCHOS checks buenos
    pero UN critical issue (ej: usage_source_non_openai)
    lo pone como máximo "marginal".
    """
    base = verdict_for(score)
    if has_critical_issues(results):
        if base == "passed":
            return "marginal"
    return base

def compute_total(results) -> float:
    """Weighted average sobre resultados no-skipped.
    
    total = Σ (d.score × d.weight) / Σ d.weight
    """
    valid = [r for r in results if r.status != "skip"]
    if not valid:
        return 0.0
    weight_sum = sum(r.weight for r in valid)
    if weight_sum <= 0:
        return 0.0
    weighted = sum(r.score * r.weight for r in valid)
    return weighted / weight_sum

# Summary labels:
# 85-100: 优秀 (excelente)
# 70-84:  通过 (pass)
# 50-69:  基本合格 (marginal)
# 0-49:   未达标 (failed)
```

### 9.4 Thinking Signature (La Clave de Detección)

```python
# De protocols/anthropic/detectors/thinking_signature.py

"""
La thinking_signature es una firma criptográfica que Anthropic
incrusta en las respuestas de Claude.

CÓMO FUNCIONA:
1. Claude genera un "thinking block" (reflexión interna)
2. Este block se firma con la clave privada de Anthropic
3. La firma se incluye en la response como "signature"
4. Cualquiera puede verificar con la clave pública de Anthropic

POR QUÉ ES CRÍTICO:
- Si la response tiene firma válida → es Claude REAL
- Si la firma falta o es inválida → NO es Claude (scam)
- NO se puede replicar sin la clave privada de Anthropic

RESPUESTA DE CLAUDE REAL (simplificado):
{
  "content": [...],
  "thinking": {
    "signature": "anthropic-sig-v1:...",
    "timestamp": 1719000000
  }
}
"""
```

### 9.5 Long Context Detection

```python
# De src/relay_detector/core/long_context.py

"""
Needle-in-haystack: El relay dice soportar 200k context
pero puede estar truncando silenciosamente.

PROBE:
1. Genera haystack de ~N tokens (template random, no copyrighted)
2. Inserta 3 "needles" a 10%, 50%, 90% del context
3. Envía a través del relay
4. Pregunta por las 3 needles
5. Si responde correctamente a todas → context window real
   Si falla alguna → truncation

CHARS PER TOKEN (calibrado live contra APIs reales):
- OpenAI: 6.0 chars/tok (gpt-4o-mini live: 32k→31397, 100k→99144)
- Anthropic: 5.3 chars/tok (era 5.5, sobredimensionaba a 200k)
- Gemini: 5.5 chars/tok (conservative, no live test)

BUFFER: +1500 chars sobre target para cubrir overhead del modelo
"""

_MODEL_CONTEXT_LIMITS = {
    "gpt-4o-mini":    128_000,
    "gpt-4o":         128_000,
    "gpt-4.1-mini": 1_047_576,
    "gpt-4.1":       1_047_576,
    "gpt-5-nano":     272_000,
    "gpt-5-mini":     272_000,
    "gpt-5":          272_000,
    "claude-haiku-4-5":   200_000,
    "claude-sonnet-4-6":  200_000,
    "claude-opus-4-8":    200_000,
}
```

---

## 10. Channel Routing: Cómo New-API Distribuye Tráfico

### 10.1 Sistema de Grupos

```
GRUPOS DEFAULT:
├── "default"  → requests sin grupo específico
├── "auto"    → auto-select del mejor canal
├── "gpt"     → solo OpenAI
├── "claude"  → solo Anthropic
└── "gemini"  → solo Google

PATTERN EN REQUEST:
POST /v1/chat/completions
{
  "model": "gpt-4o",           // el modelo
  "extra_headers": {
    "x-gpt-group": "gpt"       // el grupo opcional
  }
}
```

### 10.2 Weighted Random Algorithm

```
EJEMPLO CONCRETO:
Channel A: weight=70 (OpenAI, caro pero confiable)
Channel B: weight=30 (Azure, más barato)

ALGORITMO:
1. Sumar weights: 70 + 30 = 100
2. Random(0, 100) = 35
3. Recorrer canales acumulando weight:
   - Channel A: acumulada = 70. 35 < 70 → SELECCIONADO
4. Channel A recibe el request

BENEFICIO:
- 70% del tráfico va al canal mejor (OpenAI)
- 30% del tráfico va al canal barato (Azure)
- Si Channel A falla → retry con Channel B
```

### 10.3 Auto-ban en Fallos

```go
// Channel tiene AutoBan = 3

// Request 1: falla → failCount = 1
// Request 2: falla → failCount = 2
// Request 3: falla → failCount = 3 >= AutoBan(3) → BAN
// Channel status = 2 (disabled)
// Ya no recibe tráfico
// Admin tiene que manually re-enable
```

---

## 11. Billing Engine: Cómo se Cobra

### 11.1 Token Quota System

```go
type Token struct {
    Key             string  // La API key que se da al cliente
    Status          int     // 1=enabled, 2=disabled
    RemainQuota     int     // Quota restante
    UsedQuota       int64   // Quota consumida
    UnlimitedQuota  bool    // Si es ilimitado
    ModelLimitsEnabled bool // Si hay límites por modelo
    ModelLimits    string  // JSON: {"gpt-4o": 1000, "claude-opus": 100}
    AllowIps       *string // IPs permitidas (nil = todas)
    ExpiredTime    int64   // Timestamp expiración (-1 = nunca)
}
```

### 11.2 Pricing por Canal

```
El operador define precio por 1M tokens para CADA canal:

Canal "OpenAI Premium":
├── Input:  $5.00/1M tokens
├── Output: $15.00/1M tokens
└── Cliente paga: 5x precio oficial

Canal "Azure Budget":
├── Input:  $2.50/1M tokens
├── Output: $7.50/1M tokens
└── Cliente paga: 2.5x precio oficial

Canales más baratos tienen peso más alto en weighted random
→ Mayor tráfico va a canales más rentables
```

### 11.3 Cache Billing

```
MODELO CON CACHE: Claude Sonnet 4.6

Sin cache (cache miss):
├── Input tokens:  $3.00/1M
└── Output tokens: $15.00/1M

Con cache (cache hit):
├── Input tokens:  $0.30/1M  (10% del precio)
└── Output tokens: $15.00/1M (sin cambio)

Cache write (lo que el modelo escribe al cache):
├── $0.75/1M tokens  (25% de input price)

Relay puede cobrar cache hits differently:
├── Si cliente pregunta algo que ya está en cache
├── Relay cobra solo cache read price
└── El upstream cobra menos, relay gana más margen
```

---

## 12. Modelo de Negocio y Economía Real

### 12.1 PriceAI Monetización

```
INGRESOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. AFILIADOS (AFF/联盟)
   ├── El usuario hace click en link AFF desde PriceAI
   ├── Se registra/compr en el卡网
   ├── 卡网 paga comisión a PriceAI (5-15% del valor)
   └── IMPORTANTE: NO afecta ranking ni score

2. SPONSORED LISTINGS (赞助)
   ├── S1 首席赞助: ~$2000/mes
   │   → Aparece primero en resultados
   │   → Badge "赞助置顶"
   ├── S2 推荐赞助: ~$1000/mes
   │   → Segunda posición
   ├── S3 标准赞助: ~$500/mes
   │   → Tercera posición

3. DONACIONES (爱发电 + Ko-fi)
   └── ~$200-500/mes

COSTOS OPERATIVOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
├── VPS x 3 para collectors: $50-80/mes
├── Supabase Pro: $25-75/mes
├── Detector service: $50-100/mes
├── Dominio + CDN: $20/mes
└── TOTAL: ~$145-275/mes

MARGEN ESTIMADO:
Revenue: $1000-3000/mes (AFF + sponsored)
Costos: $150-275/mes
MARGEN NETO: $750-2725/mes
```

### 12.2 La Regla CRUCIAL: "付费不买分"

```
→ Pagar mejora posición de display, NO el score/verdict
→ El score se calcula independientemente de si pagaron o no
→ El disclaimer es obligatorio en cada commercial offer

DISCLAIMER OBLIGATORIO:
"该访问链接包含 AFF，但不影响页面排序及价格口径；
注册后请回原站核验活动规则、充值比例和退款规则。"
```

### 12.3 API Relay Economics

```
RELAY PEQUEÑO (100-500 clientes):
├── VPS: $50-100/mes
├── API calls upstream: $500-2000/mes
├── Total: $550-2100/mes
└── Net profit: $900-8800/mes

RELAY MEDIANO (500-5000 clientes):
├── Infraestructura: $500-2000/mes
├── API calls upstream: $5000-30000/mes
├── Staff: $2000-5000/mes
├── Total: $7500-37000/mes
└── Net profit: $12500-160000/mes
```

### 12.4 Reventa de Cuentas Economics

```
COSTO POR CUENTA:
├── Email: $0.001
├── SMS: $0.10-0.50
├── Proxy: $0.05-0.20
├── Compute: $0.02-0.05
└── TOTAL: $0.17-0.77

PRECIO DE VENTA:
├── ChatGPT Free: $0.50-2.00
└── ChatGPT Plus: $5.00-15.00

MARGEN: 250-2000%

Con 500 cuentas/día × $1 avg = $500/día = $15000/mes
Costo operativo: ~$150/día = $4500/mes
Beneficio neto: ~$10500/mes
```

---

## 13. Legalidad y Disclaimers

### 13.1 Disclaimer Obligatorio

```
⚠️ DISCLAIMER EN CADA COMERCIAL OFFER:

"该访问链接包含 AFF，但不影响页面排序及价格口径；
注册后请回原站核验活动规则、充值比例和退款规则。"

TRADUCCIÓN:
"Este enlace contiene AFF (afiliado), pero no afecta el 
ranking de la página ni el cálculo de precios.
Después de registrarse, vuelva al sitio original para 
verificar las reglas de la promoción, la tasa de 
recarga y las reglas de reembolso。"
```

### 13.2 Limitación de Responsabilidad

```
PriceAI es un AGREGADOR DE INFORMACIÓN:
├── NO vende cuentas
├── NO crea cuentas
├── NO almacena cuentas de usuarios
├── NO participa en transacciones
├── NO garantiza la calidad de los vendedores
└── NO es responsable por pérdidas por scams
```

---

## 14. Cómo Construir un Competidor (MVP)

### 14.1 Stack Tecnológico

```
FRONTEND:      Next.js 14 (App Router) + TailwindCSS
DATABASE:      Supabase (PostgreSQL + Auth)
STORAGE:       R2 o S3 para imágenes de evidencia
SCRAPER:       Node.js + Playwright + Cheerio
DETECTOR:      Python + FastAPI (fork de Veridrop)
HOSTING:       Vercel (frontend) + VPS x 2-3 (scrapers)
DOMAIN:        .cc o .io

COSTO MENSUAL: ~$100-150/mes
TIEMPO MVP:    2-4 semanas
```

### 14.2 Schema de Base de Datos

```sql
-- Stations (relays API)
CREATE TABLE stations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  website_url TEXT,
  api_base_url TEXT,
  status TEXT DEFAULT 'active',
  source_type TEXT DEFAULT 'manual_collected',
  commercial_relation TEXT DEFAULT 'none',
  station_system TEXT DEFAULT 'unknown',
  operator_type TEXT DEFAULT 'individual',
  invoice_support TEXT DEFAULT 'unknown',
  channel_types TEXT[],
  account_pools TEXT[],
  payment_methods TEXT[],
  minimum_top_up TEXT,
  balance_expiry TEXT,
  support_channels TEXT[],
  refund_policy TEXT,
  risk_labels TEXT[],
  usage_advice TEXT DEFAULT 'pending',
  availability_7day_rate FLOAT,
  availability_7day_samples INT,
  availability_last_checked_at TIMESTAMPTZ,
  feedback_pending_count INT DEFAULT 0,
  feedback_verified_risk_count INT DEFAULT 0,
  data_status TEXT DEFAULT 'sample',
  last_updated_at TIMESTAMPTZ DEFAULT now(),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Offers (productos)
CREATE TABLE offers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  station_id UUID REFERENCES stations(id),
  product_name TEXT NOT NULL,
  group_name TEXT,
  category TEXT,
  price FLOAT,
  currency TEXT DEFAULT 'CNY',
  stock_status TEXT DEFAULT 'in_stock',
  source_url TEXT,
  last_verified_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Feedback
CREATE TABLE feedback (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  station_id UUID REFERENCES stations(id),
  offer_id UUID REFERENCES offers(id),
  user_id TEXT,
  rating INT CHECK (rating >= 1 AND rating <= 5),
  reason TEXT,
  evidence_urls TEXT[],
  verified BOOLEAN DEFAULT false,
  merchant_response TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Price history
CREATE TABLE price_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  offer_id UUID REFERENCES offers(id),
  price FLOAT NOT NULL,
  recorded_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_offers_station ON offers(station_id);
CREATE INDEX idx_offers_category ON offers(category);
CREATE INDEX idx_feedback_station ON feedback(station_id);
CREATE INDEX idx_price_history_offer ON price_history(offer_id);
```

### 14.3 Plan de Desarrollo

```
SEMANA 1-2: MVP del relay detector
├── Desplegar New-API en un VPS
├── Configurar 1-2 API keys upstream
├── Crear UI básica con pricing page
└── Empezar con 10-20 relays conocidos

SEMANA 3-4: Sistema de detección
├── Fork de Veridrop/priceai-detector-service
├── Desplegar detector service
├── Integrar con UI
└── Score de 4-5 relays conocidos

SEMANA 5-8: Sistema de scraping
├── Implementar collector runtime
├── Configurar scrapers para 10-20卡网
├── Normalización de productos
└── Envío a base de datos

SEMANA 9-12: Feedback y monetización
├── Sistema de feedback con evidencia
├── Integrar AFF links
├── Implementar sponsored listings
└── Dashboard de analytics
```

---

## 15. Stack Tecnológico Completo

### 15.1 New-API (API Gateway)

```
LENGUAJE:  Go
DB:        SQLite (default), MySQL, PostgreSQL
CACHE:     Redis (opcional)
PORT:      3000 (UI), 80/443 (API)
DEPLOY:    Docker, docker-compose, binary
FEATURES:
├── Multi-protocol (OpenAI, Claude, Gemini, etc)
├── Weighted random routing
├── Auto-ban on failure
├── Rate limiting
├── Quota management
├── Cache billing
└── Protocol conversion
```

### 15.2 PriceAI (Frontend + API)

```
FRONTEND:  Next.js 14 (App Router)
STYLING:   TailwindCSS
DB:        Supabase (PostgreSQL)
STORAGE:   R2 (Cloudflare) para imágenes
AUTH:      Supabase Auth
HOSTING:   Vercel o self-hosted
```

### 15.3 PriceAI Detector Service (Veridrop Fork)

```
LENGUAJE:  Python 3.10+
FRAME:     FastAPI
PROTOCOLS: Claude, OpenAI Chat, OpenAI Responses, Gemini
DEPLOY:    Docker o systemd
HOSTING:   VPS con GPU (opcional, para detección pesada)
```

### 15.4 Collector Runtime (Scrapers)

```
LENGUAJE:  Node.js
BROWSER:   Playwright (headless)
HTML:      Cheerio
DEPLOY:    VPS con systemd
CRON:      Cada 15-30 minutos
```

---

## 16. Glosario Completo Chino-Español

```
卡网 (Kǎwǎng)             = "Card Website" — Sitio de tarjetas/códigos
代充 (Dàichōng)           = "Proxy recharge" — Cambian email/password de cuenta existente
成品号 (Chéngpǐn Hào)     = "Finished account" — Cuenta ya creada y lista
卡密 (Kǎmì)               = "CDKey" — Código de canje automático
中转站 (Zhōngzhuǎn Zhàn)  = "Relay station" — API relay
中转 (Zhōngzhuǎn)         = "Relay/transit"
独角数卡 (Dújiǎo Shùkǎ)   = "Unicorn Number Card" — Venta de números de cuenta
链动小铺 (Liàndòng Xiǎopù) = "Chain Shop" — Sistema con afiliados
云猫寄售 (Yúnmāo Jìshòu)  = "Cloud Cat Consignment" — Plataforma de custodia/escrw
AFF / 联盟                 = Affiliate — Comisión por venta
RMB / CNY                  = Yuan chino — Moneda local
USDT                        = Tether — Stablecoin para pagos cross-border
短信验证 (Duǎnxìn Yànzhèng) = SMS verification
虚拟手机号 (Xūnǐ Shǒujī Hào) = Virtual phone number (SMS PVA)
住宅代理 (Zhùzhái Dàilǐ)   = Residential proxy
逆向 (Nìxiàng)             = Reverse engineering / bypass
API中转 (API Zhōngzhuǎn)   = API relay
签名率 (Qiānmíng Lǜ)       = Signature rate — % de respuestas con firma válida
在线率 (Zàixiàn Lǜ)        = Uptime rate — % de tiempo que el relay está disponible
延迟 (Yánchí)              = Latency — Tiempo de respuesta en ms
额度 (Édù)                 = Quota — Límite de uso por cuenta
余额 (Yú'é)               = Balance — Saldo en cuenta
充值 (Chōngzhí)           = Top-up / recarga
退款 (Tuìkuǎn)            = Refund
工单 (Gōngdān)            = Ticket / support ticket
```

---

## 17. Repositorios y Referencias

```
NEW-API (Relay Gateway):
├── Repo:    github.com/QuantumNous/new-api
├── Stars:   42.2k
├── Forks:   9.8k
└── Docs:    veridrop.org/docs

VERIDROP (Detector):
├── Repo:    github.com/veridrop/veridrop
├── Live:    veridrop.org
├── API:     api.veridrop.org
└── Protocol docs: veridrop.org/relay/passion8.cc

PRICEAI (Agregador):
├── Repo:    github.com/dimthink/PriceAI
├── Stars:   1.4k
├── Live:    priceai.cc
├── Detector: github.com/physics-dimension/priceai-detector-service
└── Detector Live: detector.priceai.cc

SMS VIRTUAL SERVICES:
├── SMS-Activate: sms-activate.org
├── 5SIM: 5sim.net
└── Costo: $0.05-0.50 por SMS

RESIDENTIAL PROXIES:
├── Luminati: luminati-china.com
├── Oxylabs: oxylabs.io
└── Costo: $0.10-1.00 por IP/hora
```

---

## 18. Resumen Ejecutivo para LLM

### 18.1 El Mercado

```
VALOR ESTIMADO DEL ECOSISTEMA: ~$500M-2B USD/año

DOS NEGOCIOS PRINCIPALES:
1. API Relays: $10k-$500k/mes por operador grande
   - Venden acceso API a modelos (GPT-4, Claude, etc)
   - Open source: New-API (42k stars)
   - Fraudes comunes: model substitution, context truncation

2. Reventa de Cuentas: $50-500/mes por operador pequeño
   - Venden cuentas ChatGPT/Claude subscription
   - Automation: Selenium + SMS virtual + residential proxies
   - Margen: 250-2000%
```

### 18.2 Oportunidad

```
EXISTE UN PRICEAI PERO ES SÓLO PARA CHINA:
- Agrega 200+卡网 y 4000+ relays API
- Muestra precios, disponibilidad, score de scam
- Monetiza con AFF + sponsored listings
- Costo: ~$150-275/mes, revenue: ~$1-3k/mes

OPORTUNIDAD FUERA DE CHINA:
- No existe un agregador similar para occidente
- Mercado potencial: developers que buscan APIs baratas
- Stack: Next.js + Supabase + scrapers + Veridrop fork
```

### 18.3 Fraudes a Detectar

```
6 MÉTODOS DE SCAM EN RELAYS:
1. Model Substitution → Pide GPT-4o, recibe modelo barato
2. Context Truncation → Pide 200k context, recibe 32k
3. Backend Swap → Pide GPT, recibe Claude
4. Cache Poisoning → Responde con cache stale
5. Phantom Models → Modelo que no existe
6. Subscription Laundering → Cuentas Plus robadas

12 DETECTORES DE VERIDROP:
La clave: thinking_signature de Claude
- Solo Claude real genera firma criptográfica
- Falta de firma = scam confirmado
```

### 18.4 Información Crítica para Continuar

```
PARA CONSTRUIR UN COMPETIDOR:
1. Clonar New-API → desplegar relay gateway
2. Fork Veridrop → desplegar detector service
3. Build PriceAI clone → frontend de agregación
4. Implementar scrapers → collector runtime
5. Integrar feedback system → con evidencia de imágenes
6. Añadir AFF + sponsored → monetización

PARA INVESTIGAR MÁS:
- Buscar en GitHub: "chatgpt reseller", "api relay", "卡网"
- Buscar en Telegram: grupos de reventa de cuentas China
- Buscar en WeChat: Keywords "ChatGPT代充", "API中转"
```

---

**FIN DEL DOCUMENTO**

*Última actualización: Julio 2026*
*Fuentes: Código fuente de New-API, Veridrop, PriceAI en GitHub*
*Para LLMs de bajo costo: capítulos 1-4 cubren fundamentos, 5-9 son detalles técnicos profundos*
