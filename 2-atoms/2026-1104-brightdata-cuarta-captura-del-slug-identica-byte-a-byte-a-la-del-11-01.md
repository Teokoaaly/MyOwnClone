---
id: 2026-1104-brightdata-cuarta-captura-del-slug-identica-byte-a-byte-a-la-del-11-01
type: atom
certainty: solid
sources: [sources/2026-11-04-brightdata-pricing.md]
links: ["[[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]]", "[[2026-1104-clerk-cuarta-captura-identica-byte-a-byte-a-la-del-11-01]]", "[[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]]"]
---

## Claim
La captura del **2026-11-04** de `brightdata.com/pricing` (371 líneas, 11.724 bytes, `word_count: 743` declarado) es **byte a byte idéntica a la del 2026-11-01**: la única diferencia entre ambos ficheros es la línea 3 del frontmatter (`captured: 2026-11-01` → `captured: 2026-11-04`). md5: 11-01 `a363641c3c79335aa75cbb4e89bd822e`, 11-04 `39c133b1ddac6c4cc947a8dd004f51c7`, 11-02 `8622809fd84d20517f350ea349a82d33`. Es la **cuarta captura del slug** (2026-10-31, 2026-11-01, 2026-11-02 y 2026-11-04 — la noche del 2026-11-03 no capturó esta URL) y la **tercera con el mismo cuerpo de texto**: las ocho fichas de producto, los ocho enlaces "See Pricing", el titular "Trusted by 50,000+ customers worldwide", los trece huecos de logo SVG, las 21 referencias a YouTube y el bloque del chat de Sophie son los mismos, sin un carácter de diferencia.

## Why It Matters
Confirma el patrón de estabilidad del vault con un dato más fuerte que "no cambió el precio": **la página y su captura no cambiaron**. Es la misma observación que ya se registró para Clerk en este mismo turno de captura ([[2026-1104-clerk-cuarta-captura-identica-byte-a-byte-a-la-del-11-01]]) y el mismo mecanismo de separación "contenido estable / render variable" que se había medido en Hetzner ([[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]]): cuando el hash del cuerpo se repite, el slug puede salir de la lista de lectura sin pérdida de información.
Para el agregador de precios ([[2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra]]) esto significa algo concreto y accionable: **esta URL puede pausarse**. Cuatro capturas del slug (10-31, 11-01, 11-02, 11-04) producen siempre el mismo índice sin cifras; el único número que sale de aquí es "400M+ monthly Residential IPs" y el titular "50,000+ customers". El coste de captura de este slug es una captura por noche para obtener cero filas cotizables, mientras que el dato de coste vive en las ocho subpáginas a un clic de distancia. Es un argumento directo a favor de rotar la lista de lectura, que es exactamente lo que lleva cinco turnos sin ocurrir.

## Nota de verificación
Comparación literal con `diff` sobre `sources/2026-11-01-brightdata-pricing.md`, `sources/2026-11-02-brightdata-pricing.md` y `sources/2026-11-04-brightdata-pricing.md`: contra el 11-01 la única diferencia es la línea 3; contra el 11-02 difieren la línea 3 y toda la capa de imágenes (el 11-02 resuelve las URLs de `media.brightdata.com`, el 11-04 vuelve a SVG inline vacío) — ver [[2026-1104-brightdata-el-render-de-imagenes-alterna-y-la-captura-pierde-los-doce-logos]].
El `word_count` del frontmatter es fiable en esta serie salvo en la captura más antigua: 11-01 declara 743 y el cuerpo tiene 743 palabras; 11-02 declara 750 y tiene 750; 11-04 declara 743 y tiene 743; **el 2026-10-31 declara 3.892 palabras y su cuerpo tiene 343** — un desfase de más de diez veces. La captura **no** publica: ningún precio, umbral, mínimo ni unidad de cobro; tampoco qué parte de las ocho fichas es autoservicio y qué parte es "contact sales".
