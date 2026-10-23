---
id: 2026-1023-live-verify-modos-pedagogia-ventas-y-soporte-en-el-bundle
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[2026-1022-tres-silos-opt-in-publico]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-live-verify-robots-sitemap-y-404-como-catchall]]"]
---

## Claim
El bundle vivo de [[myownclone]] nombra los tres modos de comportamiento como `pedagogy`, `sales` y `support` —con `Sales` entre los tres botones del grupo "Conversation mode" (`Learn` / `Support` / `Sales`) de la página del clon— y el Aviso Legal lo repite: "Cada clon está organizado en tres modos de comportamiento (pedagogía, ventas y soporte)". La línea de guardarrail vigente es `"notEnoughInfo": "I don't have enough information to answer this question accurately. Would you like me to notify the team?"`.

## Why It Matters
Fija el vocabulario técnico del modo **ventas** en la build actual, que es el que el corpus de mayo no tenía: el marketing público hablaba de "enseña / da soporte / recomienda tus productos" (ver [[2026-1022-tres-silos-opt-in-publico]]) pero el bundle nombra `sales` como modo de primera clase. Es la diferencia entre "recomendación de producto" y "venta" y afecta a cómo se lee el modelo RAC de [[2026-1022-arquitectura-rac-tres-modos-por-clon]]. El guardarrail, por su parte, es la cadena que convierte un gap de conocimiento en una acción (notificar al equipo), y sigue vigente en la plantilla del clon (ver [[2026-1022-live-verify-robots-sitemap-y-404-como-catchall]]).

## [FRICTION]
> [[2026-1022-tres-silos-opt-in-publico]] afirma que el copy público de [[myownclone]] define el producto como tres silos opt-in —"enseña", "soporte al cliente" y "recomienda tus productos"— y advierte explícitamente de que "no menciona 'ventas': el tercer silo público es *recomendación de producto*, no venta directa, un matiz que cambia la lectura comercial del producto".
> Este átomo presiona esa creencia porque la nomenclatura interna y el botón de la interfaz usan literalmente `Sales` / "ventas" como uno de los tres modos, no "recomienda".
> Ambas pueden ser ciertas a la vez y el matiz es el hallazgo: el **copy de marketing** habla de recomendación de producto mientras el **producto y su código** implementan un modo de venta. Eso no es un error del corpus, es una divergencia entre discurso y modelo de datos que conviene tener registrada.
> Marcado para juicio humano, no auto-resuelto.
