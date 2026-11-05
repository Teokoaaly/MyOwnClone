---
id: 2026-1102-auth0-precios-sin-cambios-en-48-horas
type: atom
certainty: solid
sources: [sources/2026-11-02-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]"]
---

## Claim
Las capturas de la página de precios de Auth0 del **2026-11-01 y del 2026-11-02 son idénticas salvo la fecha de captura**: mismo contenido, mismas tablas, mismas cifras ($35 / $150 / $240 / $800 en el escalón de 500 MAU, mismos add-ons, mismo feature matrix). En 48 horas **no cambió ni un precio ni una feature** en auth0.com/pricing.

## Why It Matters
Es un dato de **estabilidad de precios**, no de contenido: el vault puede tratar la escalera de Auth0 como una referencia firme para el horizonte de un trimestre, sin la incertidumbre de rogar un recargo por cambio de tarifa a mitad de ciclo de facturación. La comparación con el resto del corpus del vault es lo que lo hace relevante: los proveedores de infra baratos que el vault ha documentado (HostBrr, Evoxt, ExtraVM, Skhron, BuyVM) **sí** han mostrado movimientos de precio entre capturas, mientras que Auth0 —que es la pieza que más cara se paga si se cruza el umbral— se ha mantenido constante en la ventana medida. La consecuencia operativa: si el founder decide meter Auth0 en el stack, el número del presupuesto se puede fixear ahora; si no se decide, no hay penalización por esperar. Y para la pregunta abierta del vault sobre si domina el coste por asiento o el coste de infraestructura, la estabilidad de Auth0 refuerza que **cualquier cambio de coste del stack en el futuro vendrá del hosting, no de la identidad**.

## Nota de verificación
La identidad de los dos archivos se verificó por diff directo: la única diferencia es la línea `captured:` del frontmatter. Las cifras citadas son las de las tablas de la captura del 2026-11-02, idénticas a las del 2026-11-01.

## 2026-11-03 — re-verificación (con salvedad)
Fuente: `sources/2026-11-03-auth0-pricing.md`.

La captura del **2026-11-03** de auth0.com/pricing **no es byte-idéntica** a las del 2026-11-01 y 2026-11-02: es un render **reducido a 540 palabras** que contiene las tarjetas de los cuatro planes y el catálogo de add-on, pero **no** las tablas de precios por MAU ni el feature matrix (ver [[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]).

Esto **no** contradice el Claim de este átomo (que se refiere a la ventana del 2026-11-01 → 2026-11-02) pero acota su alcance: la "estabilidad" observada era la de **dos renders completos consecutivos**, no una propiedad de la página. La diferencia del 2026-11-03 es de render, no de precio: las cifras visibles ($35, $240, $0) coinciden con las ya registradas. La consecuencia operativa es la regla que se deriva en [[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]: una captura reducida no es evidencia ni de estabilidad ni de cambio de precio.
