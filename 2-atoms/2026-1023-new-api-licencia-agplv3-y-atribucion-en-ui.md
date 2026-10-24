---
id: 2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md, sources/2026-10-23-new-api-calcium-ion-redirect.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1024-new-api-redirect-calcium-ion-a-quantumnous]]"]
---

## Claim
New API se licencia bajo **GNU AGPL v3.0**, con **términos adicionales bajo la Sección 7** que obligan a las versiones modificadas a:

1. Preservar el aviso de atribución **`Frontend design and development by New API contributors.`** en los avisos legales y en cualquier ubicación prominente de about/legal/footer/atribución que muestre la interfaz.
2. Mostrar **un enlace visible al proyecto original** (`https://github.com/QuantumNous/new-api`).

El README añade que es un proyecto basado en **One API (MIT)** y que existe una vía de contacto (`support@quantumnous.com`) para organizaciones cuyas políticas no permitan AGPLv3 o que quieran evitar las obligaciones de copyleft. La cabecera del repo declara licencia **AGPL-3.0** y la página incluye `LICENSE`, `NOTICE` y `THIRD-PARTY-LICENSES.md` en la imagen Docker.

## Why It Matters
Es el **precio legal del auto-hospedaje** y el vault no lo tenía cuantificado: AGPLv3 no es una licencia "de usar libremente". Si el producto del vault llegara a usar New API como capa de inferencia autoalojada, la obligación de **enlace visible al proyecto original en la interfaz** es visible para el cliente final, no solo un archivo en el repo — lo que choca de frente con una marca propia sin filiación ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]).
Es también la razón por la que el software **no aparece en repositorios públicos** del vault: la ausencia de código público ([[2026-1022-sin-repos-publicos-github]]) convierte cualquier dependencia AGPL con copyleft en un riesgo legal, no en un atajo.
La consecuencia operativa para el self-hosting: la licencia no impide desplegarlo ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]), pero obliga a mantener el aviso y el enlace mientras el fork exista, y a redistribuir el código fuente modificado a los usuarios de la versión modificada.

## [NOTA 2026-10-24 — new-api]
Fuente: `sources/2026-10-23-new-api-calcium-ion-redirect.md`. Esta segunda captura **confirma de forma independiente** dos cosas del átomo original: la licencia declarada es **GNU AGPL v3.0**, y el README **documenta que el proyecto deriva de One API (MIT)** — es decir, la cadena copyleft One API (MIT) → New API (AGPLv3) queda verificada por dos capturas separadas. El elemento nuevo es el **dueño del enlace de atribución**: la obligación de "enlace visible al proyecto original" que la Sección 7 impone en la UI apunta hoy a `https://github.com/QuantumNous/new-api`, y no a `Calcium-Ion/new-api` ([[2026-1024-new-api-redirect-calcium-ion-a-quantumnous]]). Para un fork autoalojado que quiera el mínimo cumplimiento formal, esto obliga a decidir a qué URL se enlaza antes de escribir una línea de UI: enlazar al owner antiguo es una referencia obsoleta por alias, y enlazar al nuevo equivale a declarar dependencia pública de `QuantumNous`.
