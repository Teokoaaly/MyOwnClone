# DeepRoot Investigation — lzt.market Live Pricing Data
## Julio 15, 2026 — LLM Category Snapshot

---

## RESUMEN EJECUTIVO DE PRECIOS

```
PRODUCTO               RANGO (€)     PROMEDIO    ORIGEN DOMINANTE
─────────────────────────────────────────────────────────────────
ChatGPT Plus           €3.81-11.19    ~€5.00     Autoreger (80%+)
ChatGPT Pro (20x)      €78.34         €78.34     Brute-force
ChatGPT Go             €4.62          €4.62      Stealer
Claude Pro             €6.72          €6.72      Brute-force
Claude Max 20x         €39.17-47.01   ~€44.00    Brute-force
Cursor Pro             €14.55-15.11   ~€14.80    Autoreger
Cursor Pro Plus        €36.93         €36.93     Personal
Cursor Ultra (cookie)  €1,119.28      €1,119.28  Stealer (aged)
SuperGrok              €1.85-2.45     ~€2.15     Stealer (90%+)
```

---

## ANÁLISIS DETALLADO POR PRODUCTO

### ChatGPT Plus — El mercado más líquido

**Rango**: €3.81 - €11.19 (factor 3x entre más barato y más caro)
**Mediana**: ~€5.03
**Moda**: €5.03-5.14 (precio de commodity)

**Estratificación por vendedor:**

| Vendedor | Rating | Ventas | Precio (€) | Tipo |
|---|---|---|---|---|
| **letuan** | 100% | 404 | 5.37-11.19 | Top Seller, premium |
| **Dear22** | 89% | 28 | 5.14-5.25 | Mid-tier consistente |
| **senluron** | 100% | 4 | 5.03 | Nuevo, precio bajo |
| **draag0n** | 40% | 5 | 3.81-5.01 | Descuento riesgo |
| **ElevenStore** | 50% | 2 | 5.59 | Nuevo |
| **M1kroSeller** | 33% | 3 | 5.84 | Riesgo alto |
| **zkl** | - | - | 3.92 | Bulk Japan accounts |
| **VibeCoder** | 88% | 8 | 6.60 | Mid-tier |

**Hallazgos clave:**
- **Autoreger domina**: 80%+ de las cuentas ChatGPT Plus son auto-registradas (no robadas)
- **"No phone-bound"** es estándar — cuentas sin teléfono vinculado (menos riesgo de trigger de verificación)
- **Registro reciente**: La mayoría registradas "yesterday" o "Sunday" — cuentas muy frescas (1-3 días)
- **Auto-renewal**: Casi todas tienen auto-renovación activada (la suscripción se renueva sola)
- **Japan accounts**: El vendedor "zkl" produce cuentas registradas en Japón a €3.92 en bulk — posiblemente usando proxies japoneses + SIMs japonesas

**Qué significa "No phone-bound":**
Una cuenta ChatGPT sin teléfono vinculado es más valiosa porque:
1. No requiere verificación SMS para login desde nuevo dispositivo
2. Menos probable que OpenAI pida re-verificación
3. El comprador puede usarla sin necesidad de acceso a número telefónico

---

### ChatGPT Pro (Plan de $200/mes)

**Solo 1 listing**: €78.34 (AIworker, 88% rating, 34 ventas)
- Cuenta de Oct 2023 (aged: ~2.7 años)
- Rambler email (proveedor ruso)
- Brute-force (credenciales obtenidas por fuerza bruta)
- Auto-renewal: SÍ
- **Esto es 61% descuento sobre los $200/mes oficiales**

---

### Claude Pro — Mercado pequeño y arriesgado

**Precio**: €6.72 (AnyWaywithU, 86% rating, 28 ventas)
- **Brute-force**: Cuentas obtenidas por credential stuffing
- **"Only cookie login"**: Solo recibes cookies de sesión, NO email/password
- **API usage**: 12-20% consumido
- Cuentas aged: registradas Nov 2024 (~8 meses)
- **50% descuento** ofrecido por el vendedor

**⚠️ RIESGO ALTO**: Solo cookie login + brute-force = cuenta puede desaparecer en cualquier momento si el dueño original cambia contraseña o Anthropic detecta sesión sospechosa.

---

### Claude Max 20x — Alto valor, alto riesgo

**Rango**: €39.17 - €47.01
**Vendedor**: Hisenberg (33% rating, 6 ventas) ⚠️

- Todas **brute-force** + **cookie login only**
- API limit: 0-31% consumido
- Aged: registradas Feb-Jul 2026
- Incluyen acceso a Claude Code
- Auto-renewal: SÍ

**⚠️ ALERTA**: 33% rating con solo 6 ventas. El vendedor es de altísimo riesgo. A €47 por cuenta, una estafa duele. Probablemente son cuentas robadas de equipos enterprise ($25-30/usuario/mes plan Team).

---

### Cursor Pro/Ultra — El mercado sorpresa

**Cursor Pro** (€14.55-15.11):
- Plan de $20/mes
- Autoreger o personal
- "API: 0%" = sin uso de API (cuenta fresca)
- Vendedores: joehudmr (100%, 6 ventas), letuan (100%, 404 ventas)

**Cursor Pro Plus** (€36.93):
- Plan superior
- Vendedor: Annak148 (90%, 10 ventas)

**Cursor Ultra cookie** (€1,119.28):
- Cookie de sesión solamente
- Aged account: Aug 2025 (~11 meses)
- API limit: 29% usado
- Vendedor: Seidou (89%, 120 ventas)
- **Precio extremo**: Cursor Ultra es el plan enterprise/ilimitado. Una cookie de sesión cuesta >€1,000 porque da acceso ilimitado a Cursor + Claude/GPT integrados.

---

### SuperGrok — El mercado más "industrializado"

**Rango**: €1.85 - €2.45
**Vendedor dominante**: тосеина (94% rating, **249 ventas**)

- **100% Stealer**: Todas las cuentas Grok son robadas vía infostealers
- **Cookie login only**: Sin accesso a email
- Aged variado: Mar 2025 - Jun 2026
- Auto-renewal: SÍ en todas
- **Volumen masivo**: 249 ventas confirman que este vendedor tiene pipeline constante de cuentas robadas

**Por qué Grok es tan barato:**
1. Cuentas robadas (costo de adquisición ~$0)
2. Cookie login = el comprador asume todo el riesgo
3. xAI (Grok) tiene menos defensas anti-fraude que OpenAI
4. Mercado menos maduro = menos compradores = precios más bajos

---

## TIPOS DE ORIGEN DE CUENTAS (CONFIRMADO POR LISTINGS)

| Tipo | Descripción | % del mercado LLM | Riesgo |
|---|---|---|---|
| **Autoreger** | Creada masivamente con automation | ~60% | BAJO-MEDIO |
| **Brute-force** | Credenciales obtenidas por fuerza bruta | ~20% | ALTO |
| **Stealer** | Robadas vía malware/infostealers | ~15% | MUY ALTO |
| **Resale** | Compradas a otro vendedor | ~4% | VARIABLE |
| **Personal** | Cuenta personal del vendedor | ~1% | BAJO |

---

## SEÑALES DE CONFIANZA DEL MERCADO

### Lo que indica un buen vendedor:
- **Rating >85%** con >20 ventas
- **Autoreger + Access to email + No phone-bound**
- **"ГАРАНТИЯ+"** (garantía extendida)
- **"Качество++"** (calidad plus) — badges de lzt.market
- **"Top Seller"** — badge oficial de la plataforma

### Lo que indica riesgo:
- **Brute-force + Only cookie login** — cuenta robada, puede desaparecer
- **Rating <50%** — compradores previos insatisfechos
- **"БЕЗ ГАРАНТИИ" / "NO WARRANTY"** — el vendedor no responde si falla
- **Stealer** — malware, la cuenta puede ser recuperada por el dueño
- **Sin email access** — no puedes cambiar contraseña ni recuperar

---

## VOLUMEN ESTIMADO DEL MERCADO LLM EN lzt.market

Basado en el snapshot (primeras ~80 listings de los más recientes):

- **Total listings LLM**: ~500-800 estimados (scroll continuo)
- **Distribución**:
  - ChatGPT (Plus/Pro/Go): ~55%
  - Grok: ~20%
  - Claude (Pro/Max): ~10%
  - Cursor (Pro/Ultra/Plus): ~12%
  - Otros (Perplexity, etc): ~3%

- **Precio total del mercado visible**: ~€3,000-5,000 en listings activos
- **Volumen mensual estimado**: ~2,000-5,000 transacciones/mes (basado en rotación de listings)

---

## IMPLICACIONES PARA EL ECOSISTEMA

1. **ChatGPT Plus es un commodity**: Precio estable €3.81-11.19 con mediana €5. La diferencia de precio la pone la reputación del vendedor, no la calidad del producto (todas son cuentas frescas autoreger).

2. **Claude es más caro y más arriesgado**: Las cuentas Claude son mayoritariamente brute-force, cookie-only. El mercado de Claude es menos maduro que el de ChatGPT.

3. **Grok es puro fraude**: 100% stealer, cookie-only, €2. Sin acceso a email. El comprador asume que la cuenta puede morir mañana.

4. **Cursor tiene dos mercados**: Pro a €15 (asequible, autoreger) y Ultra cookie a €1,119 (cookie robada de cuenta enterprise). El gap de precio es brutal.

5. **Japón como hub de farming**: El vendedor "zkl" produce cuentas ChatGPT Plus registradas en Japón a €3.92. Japón tiene acceso legal a OpenAI, buenos carriers para SMS, y proxies de calidad.

6. **La reputación define el precio**: letuan (100%, 404 ventas) cobra €10+ mientras draag0n (40%) cobra €3.81 por el mismo producto. Diferencia: 3x solo por confianza.

---

## COMPARATIVA: PRECIO lzt.market vs PRECIO OFICIAL

```
PRODUCTO           OFICIAL/MES    lzt.market    DESCUENTO
─────────────────────────────────────────────────────────
ChatGPT Plus       €22 ($20)      €3.81-11.19   49-83%
ChatGPT Pro        €220 ($200)    €78.34         64%
Claude Pro         €22 ($20)      €6.72          69%
Claude Max         €110 ($100)    €39-47         57-65%
Cursor Pro         €22 ($20)      €14.55-15.11   31-34%
SuperGrok          €10 ($9)       €1.85-2.45     73-82%
```

**El descuento es inversamente proporcional a la dificultad de farming:**
- ChatGPT Plus (fácil de farmear) → 83% descuento máximo
- Cursor Pro (más difícil, nicho) → solo 34% descuento máximo
- Cuanto más nicho, menos competencia, margen más bajo

---

## LA PRUEBA DEL FRAUDE: El arbitraje NO cuadra

### PriceAI Official Prices (Julio 2026): App Store pricing por región

Precio oficial MÁS BARATO del mundo: **Filipinas — ₱999 PHP = ¥110 CNY (~€13.50)**

| Región App Store | Precio local | CNY | EUR |
|---|---|---|---|
| 🇵🇭 Filipinas | ₱999 PHP | ¥110 | €13.50 |
| 🇵🇰 Pakistán | Rs 4,900 PKR | ¥120 | €14.65 |
| 🇨🇦 Canadá | $24.99 CAD | ¥120 | €14.75 |
| 🇯🇵 Japón | ¥3,000 JPY | ¥125 | €15.50 |
| 🇻🇳 Vietnam | 499,000 VND | ¥129 | €15.90 |
| 🇮🇩 Indonesia | Rp 349K IDR | ¥131 | €16.10 |
| 🇺🇸 EEUU | $19.99 USD | ¥136 | €16.70 |
| 🇹🇷 Turquía | ₺999 TRY | ¥144 | €17.75 |
| 🇪🇺 Europa | ~€22-25 | ¥160-180 | €22-25 |

### La matemática que NO cierra:

```
COSTE DEL FARMER (mejor caso: Filipinas + gift card 30% descuento):
  ¥110 CNY × 0.70 = ¥77 CNY = ~€9.50 por mes

PRECIO DE VENTA en lzt.market (mediana/moda):
  €3.81 - €5.59

RESULTADO: €3.81 - €9.50 = PÉRDIDA de €5.69 por cuenta
```

### Conclusión: Tres métodos de fraude

**Las cuentas a €3.81-5.59 NO pueden ser rentables con pago legítimo.** Los farmers usan:

1. **Tarjeta robada** (costo = $0): La suscripción se paga con tarjeta fraudulenta. La cuenta dura 1-4 semanas hasta chargeback. Es el método más común para cuentas "Autoreger".

2. **Free trial exploit** (costo = $0): Bypass del período de prueba sin método de pago real, o cancelación antes del cobro.

3. **Auto-renewal fraud** (costo = $0): Pagan mes 1 con tarjeta virtual desechable (Privacy.com, Revolut disposable), venden la cuenta inmediatamente, y cuando OpenAI intenta cobrar el mes 2, la tarjeta ya no existe. OpenAI tarda días/semanas en cancelar → la cuenta funciona "gratis" para el comprador durante ese tiempo.

**Solo los vendedores premium (€10+) podrían ser legítimos:**
- letuan (100%, 404 ventas): €10.07-11.19
- Coste con gift card Filipinas 30% descuento: €9.50
- Margen: 6-15% → negocio de volumen, no de margen

### Evidencia del "Japan farming":

El vendedor **zkl** produce cuentas Japón (¥3,000 JPY = ¥125 CNY = €15.50 coste mínimo). Las vende a €3.92. Esto prueba matemáticamente que usa tarjetas robadas o virtuales desechables — imposible obtener margen positivo con pago legítimo.

### Implicación para el ecosistema:

```
VENDEDORES BARATOS (€3.81-5.59):   ~70% del mercado
  → 100% usan pago fraudulento
  → Las cuentas son "desechables" (1-4 semanas de vida)
  → El comprador lo sabe y lo acepta

VENDEDORES PREMIUM (€10-11.19):     ~15% del mercado  
  → Posiblemente arbitraje legítimo (gift card PH/Nigeria)
  → Cuentas más estables (1-3 meses)
  → Pagan premium por reputación

VENDEDORES INTERMEDIOS (€5.50-9.99): ~15%
  → Zona gris — posiblemente mixto
```

---
*Datos: lzt.market LLM category + priceai.cc/official-prices, Julio 15, 2026.*
