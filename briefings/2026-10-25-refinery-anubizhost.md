# Briefing — Refinery 2026-10-24 (Anubiz Host)

## Qué entró

- Captura procesada: `0-raw/2026-10-24-anubizhost-offshore-vps.md` (puntero) → fuente `sources/2026-10-24-anubizhost-offshore-vps.md` (505 palabras, home de anubizhost.com)
- Atomos creados: **6** (todos `2026-1024-anubiz-*`)
- Atomos extendidos: **2** (`2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad`, `2026-1024-noones-jurisdicciones-globalmente-restringidas`)
- Thread actualizado: **1** (`3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros` — nueva §8.10, filas en §1/§4/§6/§8.4, fricciones 21–23)
- Atoms retired: **0** · borrados: **0**

## Los átomos

| Átomo | Idea |
|---|---|
| `2026-1024-anubiz-sin-kyc-registro-anonimo-con-cripto` | "No KYC on signup" — el no-KYC alcanza al **alta**, no solo al pago; seis cripto (BTC, ETH, LTC, XMR, USDT, USDC) |
| `2026-1024-anubiz-el-mismo-plan-cuesta-segun-la-jurisdiccion` | 5 planes con specs **idénticas** a $29,99 o $34,99 según país: spread del **16,67 %** |
| `2026-1024-anubiz-dmca-ignored-etiquetado-por-plan-y-no-por-producto` | "DMCA IGNORED" está etiquetado **por plan**, y los dos más baratos (NL, DE) no lo llevan; incluye bloque `## [FRICTION]` |
| `2026-1024-anubiz-doce-ubicaciones-declaradas-frente-a-diez-prometidas` | 12 ubicaciones en la lista, "10 countries" en el CTA, 6 con precio: la página se contradice |
| `2026-1024-anubiz-99-5-de-uptime-y-metricas-de-confianza-sin-sla` | 99,5 % de uptime = **≈3,6 h de caída al mes**, la cifra más baja del tramo, sin SLA ni certificaciones |
| `2026-1024-anubiz-catalogo-cuatro-lineas-y-suelo-en-19-99` | 4 líneas con precio ($19,99 / $29,99 / $34,99 / $147,99) + "GPU infrastructure" sin ficha |

## Lo que aporta al vault

**1. El precio como función de la jurisdicción.** Es la primera vez que el vault mide un caso donde el **precio de catálogo es directamente un proxy del régimen jurídico** de la ubicación: mismo producto, mismo hardware, +16,67 % según dónde esté. Eso añade una tercera partida "que se paga dos veces" al mapa del thread: egreso, backup y ahora jurisdicción.

**2. La escala de minimización de datos crece un peldaño.** Anubiz formula el no-KYC como propiedad **del alta de la cuenta** ("on signup", "Anonymous sign-up with cryptocurrency payments"), lo que lo sitúa con Skhron en el extremo pero con alcance declarado distinto. La escala queda: HostBrr < Evoxt < ExtraVM < **Anubiz** ≈ Skhron < HostKey < NoOnes. Ninguno del extremo "no pide nada" publica marco AML/CTF ni términos de servicio.

**3. La fricción principal (marcada, no resuelta).** Anubiz opera en la UE (NL, DE, FI, RO), vende "DMCA IGNORED" y "no obligation to comply with foreign takedown requests", y **no publica GDPR ni ninguna certificación, ni SLA, ni créditos**, con 99,5 % de uptime. O el distintivo no se sostiene en la UE, o el proveedor no puede venderse a clientes empresariales. Registrado como `## [FRICTION]` en el átomo de DMCA y como fricción 22 del thread.

**4. El caso más neto de "ubicaciones" no verificable.** 12 en la lista, 10 en el CTA, 6 vendibles, 0 fichas técnicas. En un mercado donde el thread ya comparaba "17 regiones" contra "3 ubicaciones" (magnitudes incomparables), aquí el recuento ni siquiera es fiable **dentro del propio proveedor**.

## Para el humano

- **El precio de $19,99–$34,99 es 5× el techo de ≤ €4/mes** que el vault fijó para infraestructura. Anubiz no entra en el rango de presupuesto; entra en el mapa como **referencia de postura de identidad y de jurisdicción**.
- **Riesgo de contraparte no registrado hasta ahora**: un proveedor cuyo argumento de venta es la no obligación de cumplir retiradas es exactamente el perfil que puede volverse un problema cuando el producto aloja contenido de terceros. La fricción 22 del thread deja esto abierto.
- **Verificaciones pendientes si se quiere cotizar**: ficha de `/product/moldova-vps-i` y `/product/japan-vps-i` (las dos ubicaciones sin plan visible), ancho de banda incluido, política de backup, SLA, y si el "no obligation to comply with foreign takedown requests" es una cláusula contractual o un distintivo de marketing.
- **Sin modificar**: `sources/` y `0-raw/` quedan intactos; la captura se movió a `0-raw/archive/2026-10-25-2026-10-24-anubizhost-offshore-vps.md`.

*Refinery run — 2026-10-24. Captura única: `2026-10-24-anubizhost-offshore-vps`.*
