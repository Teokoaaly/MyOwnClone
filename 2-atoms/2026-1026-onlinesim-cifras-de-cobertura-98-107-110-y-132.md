---
id: 2026-1026-onlinesim-cifras-de-cobertura-98-107-110-y-132
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]", "[[2026-1023-herosms-20-paises-enumerados-contra-180-declarados]]", "[[2026-1023-5sim-openai-76-paises-y-130-operadores]]"]
---

## Claim
La página da **cuatro cifras de cobertura geográfica distintas para el mismo proveedor el mismo día**: el contador de cabecera dice **"110+ Countries for Numbers"**; el bloque de tarifas dice **"107 countries"** y la tarifa de 15 minutos **"98 countries available"**; el selector del pie enumera **exactamente 107 entradas** de país con prefijo (Algeria+213 … Islandia+354, sin duplicados); y el módulo de números gratuitos abre **132 páginas de país**. Cuatro cifras, ninguna con contador de stock que las respalde.

El confronto nombre a nombre entre las dos listas enumerables da un resultado que ninguna de las cuatro cifras revela: **el conjunto de 107 del pie es un subconjunto estricto del gratuito de 132**, con **25 países exclusivos del gratuito** (China, Cuba, Israel, Cambodia, Pakistan, Tayikistán, Iraq…) y **ninguno exclusivo del pie** ([[2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago]]). Es decir, **"pago" y "gratis" no son dos lecturas de la misma cobertura: son dos conjuntos distintos**, y el segundo contiene al primero.

## Why It Matters
Confirma que el patrón de cobertura del sector es una **propiedad del proveedor, no del número de la home**, y esta captura es el caso más limpio hasta ahora porque el pie **sí** enumera: se puede contar. Es el mismo problema que el vault ya tenía medido en 5sim (180 declarados en la home, 153 en el catálogo, 111 en el CSV de precios de `telegram`, 76 para el servicio OpenAI — [[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]], [[2026-1023-5sim-openai-76-paises-y-130-operadores]]) y en HeroSMS (180 declarados frente a 20 enumerados en el pie, [[2026-1023-herosms-20-paises-enumerados-contra-180-declarados]]).
La observación que **no** encaja con la lectura heredada del vault es la dirección de la discrepancia: aquí la cifra **mayor** (132) es la del módulo gratuito y la **menor** (98) es la de un producto de pago concreto. En 5sim el rango iba de 180 (marketing) a 76 (producto real); en OnlineSim el marketing (110) queda en medio. Ninguna de las dos puede ser "países disponibles" sin especificar de qué se habla.

## [FRICTION]
> [[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]] (escrita hace tres días) explica la discrepancia de cobertura de 5sim con la hipótesis de que **"180" cuenta cobertura potencial y no stock vendible**, es decir, que los países no listados en el selector sí existen pero no tienen unidades disponibles.
> Este átomo presiona esa explicación porque en OnlineSim la relación es **inversa**: los 132 países del módulo gratuito **superan** los 107 enumerados en el pie de pago, y los 98 de la tarifa de 15 minutos quedan por debajo de ambos. Es decir, el conjunto "disponible" varía **por producto** y en ambos sentidos, no solo como marketing inflado por encima del stock real.
> Ambas no pueden ser la misma regla: o la cobertura es siempre una propiedad del proveedor (y entonces OnlineSim tiene 132 países y 5sim 153), o es una propiedad del producto-servicio (y entonces "180" y "110+" son cifras de marketing sin ninguna relación con lo vendible). Marcado para juicio humano, no auto-resuelto.
