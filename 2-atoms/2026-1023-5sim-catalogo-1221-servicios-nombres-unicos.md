---
id: 2026-1023-5sim-catalogo-1221-servicios-nombres-unicos
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-products-catalog.md]
links: ["[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]", "[[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]", "[[2026-1022-instancia-como-captador-de-leads]]"]
---

## Claim
El catálogo de 5sim (`/en/products`, capturado el 2026-10-22) enumera en su propio cuerpo de página **1221 nombres de servicio únicos**, contados sobre las líneas de la captura: 245 con la plantilla `Temporary Phone Number for X`, 975 con la plantilla `Get a Temporary Phone Number for X` y 1 con `Virtual Number for X` (`Dropped-Call & Flash Call Verification`). No hay ni un solo nombre repetido entre esas tres plantillas (1221 líneas, 1221 nombres distintos; 0 colisiones también al normalizar mayúsculas y espacios). El botón de la página dice `Show all 1329`, así que **el número que el proveedor exhibe (1329) no es verificable desde la lista de servicios de la propia página**: entre la cifra del botón y los nombres enumerables quedan 108 servicios sin nombre legible en la captura. La captura tampoco expone precios individuales para ninguno de esos 1221 servicios: los únicos importes de la página son los ocho `from $…` del selector.

## Why It Matters
Convierte "5sim tiene 1329 servicios" en una cifra de marketing y en un conjunto de 1221 fichas comprobables, que es el número usable para medir cobertura real de un flujo de captación ([[2026-1022-instancia-como-captador-de-leads]]). La diferencia entre 1329 y 1221 importa cuando se decide si un servicio está soportado: el catálogo **solo garantiza** los 1221 nombres que se pueden leer, y el botón solo declara cobertura total. Los ocho precios de escaparate del selector ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]) y el stock de `OpenAI/ChatGPT` ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]) están calculados sobre ese mismo universo, no sobre los 1329 anunciados.

## [FRICTION]
> [[2026-1023-5sim-catalogo-servicios-precios-y-stock]] (escrita hoy, desde la home) afirma que el catálogo de 5sim tiene **1329 servicios**, tomando el botón `Show all 1329` como el recuento del catálogo.
> Este átomo presiona esa creencia porque el cuerpo de la página del catálogo solo hace enumerable un conjunto de **1221 nombres** (y sin duplicados), de modo que la cifra de 1329 no es verificable desde la lista de servicios: 108 servicios adicionales quedan fuera de lo legible.
> Ambas no pueden ser completamente correctas: o los 108 restantes existen y la captura no los incluye (listado renderizado en cliente o paginado), o `Show all 1329` es una cifra publicitaria superior al catálogo real. Marcado para juicio humano, no auto-resuelto.
