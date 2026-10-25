---
id: 2026-10-25-refinery-brightdata
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
---

# Briefing de Refinery — Bright Data (precios de proxy)

**Captura procesada:** `0-raw/2026-10-24-brightdata-proxy-pricing.md` → archivada en `0-raw/archive/2026-10-25-2026-10-24-brightdata-proxy-pricing.md`
**Fuente original:** `sources/2026-10-24-brightdata-proxy-pricing.md` (https://brightdata.com/pricing/proxy-network, 479 líneas, capturada el 2026-10-24)
**Átomos creados:** 15, todos con prefijo `2026-1024-brightdata-`
**Thread tocado:** ninguno. La actualización (ya aplicada el 2026-10-25) se propuso en `1-desk/thread-addition-brightdata.md` y quedó integrada en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§10 nueva + fricciones 18–22).

## Qué aporta esta captura al vault

Un **segundo proveedor de proxy de escala industrial**, frente al único que había medido (DataImpulse). La conclusión de fondo no es que Bright Data sea mejor o peor: es que **el sector del proxy no tiene un $/GB de mercado**, tiene un $/GB por proveedor con un factor ×8 entre el más barato ($0,50/GB datacenter) y el más caro ($4,00/GB PAYG) en el mismo tipo de insumo.

## Los cinco hallazgos que cambian algo

1. **El precio del proxy se multiplica.** $4,00/GB en PAYG frente a $1/GB residencial y $0,50/GB datacenter de DataImpulse: ×4 y ×8. El orden "correo ≪ captcha ≪ proxy ≪ SMS" de la §7 del thread se mantiene; **la magnitud del proxy deja de ser una constante**.

2. **El compromiso de capital eclipsa al descuento por volumen.** Los tres planes con compromiso van de $499/mes (141 GB) a $1.999/mes (798 GB) para un descuento unitario total del 37,5 %. El mínimo de $499/mes está dos órdenes de magnitud por encima del techo de ≤ €4/mes del vault. El único modo comprable con ese presupuesto es el PAYG — que es precisamente el modo sin SLA y sin programa enterprise.

3. **El KYC decide qué pool se puede usar.** Obligatorio y previo para las redes Residential y Mobile (videollamada + verificación de empresa o datos personales); no mencionado para Datacenter e ISP; **expresamente exento para Web Unlocker**, que además resuelve captcha y reintentos. Es decir: el pool con mejor tasa de bloqueo está detrás de identidad, el pool sin KYC es el que bloquean las plataformas, y Web Unlocker es el atajo que evita ambas cosas.

4. **El modelo de contrato es el opuesto al de DataImpulse.** Compromiso mínimo mensual que se paga igual sin uso, cobro por adelantado íntegro el día del alta con liquidación prorrateada después, aviso al 85 % del saldo, suspensión al 100 %, y **las IPs asignadas no se recuperan al suspender**. Frente al "tráfico que nunca caduca" del otro proveedor, aquí el saldo se repone o se pierde el activo.

5. **Dos hallazgos operativos fino, que son los más útiles:**
   - **El ancho de banda factura cabeceras HTTP** ("request headers + request data (POST) + response headers + response data"). En scraping de muchas peticiones pequeñas, el $/GB se aplica a un volumen inflado respecto del payload real.
   - **El límite de gasto por zona se recalcula cada 15 minutos**, así que el límite duro real es el configurado + 15 min × tasa de pico. Es el control granular más fino que ha publicado cualquier proveedor de proxy del vault.

## Advertencia metodológica

Todo lo que hay en esta página es **claim del propio proveedor**: no hay una sola medición de tráfico, latencia o tasa de bloqueo. Un dato concreto que hay que tener presente: **la captura contiene dos tablas de precio por IP con etiquetas de plan idénticas y sin decir a qué red pertenece cada una** (10 IPs a $1,8/IP en una y a $1,40 en la otra; 1000 IPs a $1,30 frente a $0,90 — una diferencia del 28,6 % al 44,4 %). El átomo correspondiente queda en `tentative` a propósito: **una cifra de $/IP sin producto es una cifra sin unidad**. Y la red móvil se describe pero **no tiene pestaña de precio**, de modo que la tabla de coste por insumo del thread sigue con un hueco en su tramo superior.

## Fricciones añadidas (para el §9 del thread)

18. El $/GB del proxy es un parámetro de proveedor, no de mercado (×8 entre dos proveedores medidos).
19. El compromiso de $499/mes hace Bright Data inaccesible con el presupuesto del vault; la comparación entre proveedores exige dos ejes, $/GB y $/mes comprometido.
20. Suspensión por saldo = corte de lote + pérdida de las IPs; una IP whitelistada es efímera.
21. Bloquear el login desde un país distinto al de la tarjeta es una regla de geolocalización del acceso: cambiar de IP tiene coste de cuenta, no solo de tráfico.
22. La captura no permite asignar las dos tablas de $/IP a un producto ni cotizar la red móvil.

## Pendiente para el Editor

- Aplicado el 2026-10-25: `1-desk/thread-addition-brightdata.md` quedó integrado en `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (§10 + fricciones 18–22, renumeradas) y la nota de método recoge esta tercera tanda de capturas.
- Decidir si los 15 átomos de Bright Data se agrupan en un sub-bloque propio de la §8 o si se mezclan con los de DataImpulse. La propuesta escrita asume un bloque propio (§10), porque el patrón de contrato es inverso y mezclarlos confunde la comparación.
- Nota: `2-atoms/2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar.md` es el único átomo en `tentative` de esta tanda; conviene que el Editor lo confirme o lo marque como tal en el índice.
