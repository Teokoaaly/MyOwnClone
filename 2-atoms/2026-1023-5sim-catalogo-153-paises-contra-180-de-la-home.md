---
id: 2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-products-catalog.md]
links: ["[[2026-1023-5sim-catalogo-1221-servicios-nombres-unicos]]", "[[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]", "[[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]", "[[2026-1023-5sim-paises-no-occidentales-mas-baratos]]"]
---

## Claim
El número de países que 5sim declara **cambia según la página**: el catálogo (`/en/products`, capturado el 2026-10-22) muestra en el paso 2 "Select country" ocho países antes del botón `Show all 153` — **England, USA, Canada, Indonesia, Philippines, Cambodia, South Africa, India** — y declara por tanto **153 países**; la home afirma "more than 180 countries" y "numbers originating from around 180 countries"; y el CSV de precios del servicio `telegram` solo contiene **111 países**. Tres cifras para el mismo proveedor en la misma fecha. Además, tres de los ocho países que la página preselecciona (Indonesia, Philippines, Cambodia) son mercados no occidentales.

## Why It Matters
La cobertura geográfica es un dato de coste, no de marketing: si el número de países baja de 180 a 153 al entrar al catálogo y a 111 en el inventario real de un servicio, entonces **"país disponible" debe verificarse servicio a servicio** antes de prometer un país concreto en un flujo de verificación ([[2026-1023-5sim-catalogo-1221-servicios-nombres-unicos]]). La presencia de Indonesia, Philippines y Cambodia entre los ocho destacados de la página es la misma geografía que aparece en el suelo de precio por país ([[2026-1023-5sim-paises-no-occidentales-mas-baratos]]): el proveedor expone primero donde tiene inventario barato, no donde el comprador suele estar.

## [FRICTION]
> [[2026-1023-5sim-claim-500k-numeros-y-piso-0008]] (escrita hoy, desde la home) reproduce la declaración "Over 500,000 numbers originating from around 180 countries online" y "more than 180 countries", y ya registra su propio conflicto con "Show all 153".
> Este átomo añade la **tercera cifra** que faltaba en ese conflicto —los 111 países del CSV de precios de `telegram`— y muestra que la página del catálogo no contradice a la home sino que la matiza: el propio selector de 5sim destaca Indonesia, Philippines, Cambodia e India, es decir, parte de los 153 son precisamente los países baratos y de alta demanda.
> Las tres cifras no pueden ser todas "países disponibles": o "180" cuenta cobertura potencial y no stock vendible, o el CSV y el catálogo están desactualizados respecto al marketing de la home. Marcado para juicio humano, no auto-resuelto.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo documenta tres cifras de cobertura para 5sim (180 en la home, 153 en el catálogo, 111 en el CSV de `telegram`) y propone como explicación que "**180 cuenta cobertura potencial y no stock vendible**".

La captura de OnlineSim **invierte la dirección** de esa discrepancia y por tanto presiona la explicación. En OnlineSim hay cuatro cifras el mismo día: "110+ Countries for Numbers" en la cabecera, "107 countries" en el bloque de tarifas, "98 countries available" en la tarifa de 15 minutos, **107 entradas enumeradas en el pie** y **132 páginas de país en el módulo gratuito** ([[2026-1026-onlinesim-cifras-de-cobertura-98-107-110-y-132]]).

La diferencia estructural es que aquí el conjunto **mayor (132) es el gratuito** y el **menor (98) es un producto de pago concreto**, mientras el marketing (110) queda en medio. En 5sim el rango iba de 180 (marketing) a 76 (producto real). Es decir, la cobertura varía **por producto y en ambos sentidos**, y no es solo marketing inflado por encima del stock vendible.

Refuerza el mismo punto el caso de China: China está en el módulo de números gratuitos de OnlineSim y **no** en el selector de pago ([[2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago]]) — no falta el país, falta el stock pagable. Con esto, la cobertura se lee mejor como **propiedad del par (proveedor, producto)** que como propiedad del proveedor.
