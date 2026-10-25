---
id: 2026-10-25-refinery-iproyal
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-iproyal-pricing.md]
---

# Briefing — Refinery: captura IPRoyal (precios de proxy)

**Qué se procesó:** `0-raw/2026-10-24-iproyal-pricing.md` → 10 átomos nuevos + 1 extensión de átomo existente + 1 propuesta de thread + este briefing. La captura se ha movido a `0-raw/archive/2026-10-25-2026-10-24-iproyal-pricing.md`.

**Fuente:** `iproyal.com/pricing/`, 384 palabras, render plano de la home de precios. Cinco tarjetas de producto + un bloque de distintivos + una sección de cinco casos de uso. **Nada de esto es medición**: son claims de home sin tabla de planes, sin inventario, sin SLA.

## Los números que se han transcrito

| Línea | Precio "from" | Unidad | Escala declarada |
|---|---|---|---|
| Residential | **$1.75/GB** | por GB | 64M+ proxy pool |
| ISP | **$1.80/proxy** | por proxy | 500K+ unique IPs |
| Datacenter | **$1.39/proxy** | por proxy | 60+ locations, "unlimited bandwidth" |
| Mobile | **$117/month** | suscripción mensual | 4.5M+ IPs, 5G/4G/3G, hasta 100 Mbps |
| Web Unblocker (IA) | **$1.00/1000 requests** | por mil de solicitudes | — |

## Los tres hallazgos

1. **El $/GB no es la unidad del sector: es la de DataImpulse.** IPRoyal publica cinco líneas con **cinco unidades distintas** (GB, proxy, mes, mil de requests). Esto obliga a corregir la simplificación de la §7/§8 del thread "economia-de-la-verificacion-y-reventa-de-cuentas", donde el proxy se trata íntegramente como $/GB. En particular, el datacenter de IPRoyal se factura por proxy **con "unlimited bandwidth"**: hay una línea de proxy cuyo **coste marginal de bytes es cero**, lo que contradice el diagnóstico "el proxy es la única partida cuyo coste depende de un volumen que nadie controla" tal como está escrito.

2. **El móvil pasa de coste marginal a coste fijo recurrente.** $117/mes frente a $2/GB prepago. Un solo mes de móvil de IPRoyal supera por más de un orden de magnitud el techo de ≤ €4/mes que el vault se fijó para infraestructura: no es asignable a un pipeline de pocas altas.

3. **El prepago sin caducidad es norma del sector, confirmado por segunda vía.** "No expiry, no subscription / Traffic never expires" (DataImpulse) y "no restrictions, no contracts, and traffic that never expires" (IPRoyal). Mismo contrato en dos proveedores independientes — y por tanto la misma fricción: saldo que no caduca y no avisa es gasto sin techo natural.

## Fricciones levantadas (3, para juicio humano)

- **Residencial ×1,75**: el de IPRoyal ($1.75/GB) es ×1,75 el de DataImpulse ($1/GB). El átomo levanta la fricción contra la jerarquía interna de DataImpulse (datacenter = mitad, móvil = doble, premium = ×5): esa escala es **de catálogo, no de sector**, y el criterio "el más barato por GB" puede estar comprando riesgo, pool y rotación, no bytes.
- **Datacenter sin coste marginal**: el "unlimited bandwidth" por proxy presiona la lectura de que el $/GB es la unidad que decide el coste total del scraping.
- **"Pagar por el resultado" no es una propiedad técnica**: el Web Unblocker de IPRoyal es la misma capacidad conceptual que el Web Unlocker de 2Captcha, con precio de catálogo equivalente ($1.00/1000 vs $0.5–$2.99/1000), pero cobro por **request intentada** frente a **captcha resuelto**. La asimetría de riesgo la asume el cliente en un caso y el proveedor en el otro.

## Lo que la captura NO da (y es la conclusión de calidad de fuente)

Ni un plan, ni un mínimo de compra, ni forma de pago, ni comisión, ni SLA, ni uptime, ni ISO/GDPR, ni política de reembolso, ni duración de sesión, ni un solo país enumerado (solo "60+ locations"). En su lugar, ocho distintivos de terceros ("Best Software 2026", Capterra, G2 ×3, Source Force, Gold Winner, Geekflare, Slashdot), todos como imágenes sin fecha, categoría, puntuación ni reseñas. **IPRoyal es la fuente de precio más débil del vault y, a la vez, la segunda confirmación del contrato prepago.** Sirve como precio de entrada y como prueba de que el mercado converge hacia cobrar por el resultado; no sirve como base de una proyección de gasto.

**Aparte, un apunte para `el-agregador-de-precios-como-producto`:** los casos de uso que IPRoyal destaca son tres de precio (Price Monitoring, Travel Fare Aggregation con "location-specific pricing", SEO/SERP Scraping) más Stock Market Data Collection. Es decir, existe infraestructura comercial publicada específicamente para **capturar el precio que un usuario concreto ve en una geografía concreta**.

## Ficheros

**Átomos nuevos en `2-atoms/`** (prefijo `2026-1024`):
- `2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio.md`
- `2026-1024-iproyal-residencial-175-por-gb-y-pool-de-64m.md`
- `2026-1024-iproyal-isp-180-por-proxy-y-500k-ips.md`
- `2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones.md`
- `2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips.md`
- `2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes.md`
- `2026-1024-iproyal-pool-de-64m-sin-desglose-geografico.md`
- `2026-1024-iproyal-solo-precios-from-sin-escalera-de-volumen.md`
- `2026-1024-iproyal-casos-de-uso-precios-y-viajes.md`
- `2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla.md` *(certainty: tentative — los distintivos son imágenes sin metadatos)*

**Átomo existente extendido** (nota fechada al final, sin sobrescribir nada):
- `2-atoms/2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy.md` → nota fechada "2026-10-24 (captura IPRoyal)" que delimita la escala de precios al catálogo de DataImpulse.

**Propuesta de thread (NO aplicada a `3-threads/` por paralelismo):**
- `1-desk/thread-addition-iproyal.md` → nueva §8.7 "Un segundo proveedor de proxy: cuando el $/GB es solo la unidad de uno" + fricción nº18 propuesta + nota de método, para pegar en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md`.

**Briefing:** este archivo, `briefings/2026-10-24-refinery-iproyal.md`.
