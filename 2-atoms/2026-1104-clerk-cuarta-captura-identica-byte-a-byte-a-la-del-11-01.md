---
id: 2026-1104-clerk-cuarta-captura-identica-byte-a-byte-a-la-del-11-01
type: atom
certainty: solid
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-1102-clerk-precios-sin-cambios-en-48-horas]]", "[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1031-clerk-la-tabla-parcial-ya-mostraba-gating]]"]
---

## Claim
La captura del **2026-11-04** de `clerk.com/pricing` (556 líneas, 2.994 palabras) es **byte a byte idéntica a la del 2026-11-01**: la única diferencia es la línea `captured:` del frontmatter. Frente a la del **2026-11-02** difiere únicamente en un salto de línea final. Es decir, es la **cuarta captura del slug** (10-31, 11-01, 11-02, 11-04 — el 2026-11-03 no capturó esta URL) y la **tercera con render completo** (la del 10-31 estaba truncada a 229 líneas, cortándose en la fila "Sign in tokens"), y en ella **no ha cambiado ni un precio, ni un tramo de sobrecoste, ni una fila de la feature matrix, ni una respuesta de la FAQ**.

## Why It Matters
Confirma por tercera vez el patrón de estabilidad que el vault ya había medido entre el 11-01 y el 11-02 ([[2026-1102-clerk-precios-sin-cambios-en-48-horas]]) y, sobre todo, separa dos cosas que hasta ahora venían confundidas en la serie: **la página no ha cambiado y la captura tampoco ha cambiado**. La distinción importa porque la captura del 10-31 fue parcial y ya había inducido al vault a una creencia falsa sobre el gating de features ([[2026-1031-clerk-la-tabla-parcial-ya-mostraba-gating]]); a partir de ahora, la serie completa 11-01 / 11-02 / 11-04 es **un único render repetido tres veces**, y por tanto cualquier dato de Clerk que se cite en el vault es citable sin fecha de caducidad a corto plazo. Operativamente, para el eje "identidad vs infraestructura" del vault, **el número de identidad puede fixearse en el presupuesto** con la misma confianza con que ya se fijaron los precios base ([[2026-1101-clerk-precios-base-hobby-pro-business]]).

## Nota de verificación
Verificado por `diff` literal entre `sources/2026-11-01-clerk-pricing.md`, `sources/2026-11-02-clerk-pricing.md` y `sources/2026-11-04-clerk-pricing.md`: la única diferencia contra el 11-01 es la línea 3 (`captured: 2026-11-01` → `captured: 2026-11-04`); contra el 11-02, esa misma línea más el salto de línea final que el 11-02 sí lleva. md5: 11-01 `ec7d2258bb47716425fea6a6ae51a1ae`, 11-02 `238c59bdfbde3e70b499ed7c3cdf1e55`, 11-04 `351f9282bb21e56cee40ba7450e7fcc6`. La captura del 10-31 tiene 229 líneas y md5 `c31c1c8eba3822a7d708cd5ddef14341`.
