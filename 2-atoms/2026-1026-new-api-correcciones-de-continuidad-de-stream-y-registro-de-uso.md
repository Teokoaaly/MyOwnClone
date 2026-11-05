---
id: 2026-1026-new-api-correcciones-de-continuidad-de-stream-y-registro-de-uso
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas]]"]
---

## Claim
Cuatro correcciones de **continuidad y contabilidad del streaming** repartidas en tres versiones:

- **rc.47**: una **transferencia lenta de un evento grande ya no se registra como desconexión**, y una **respuesta de Responses ya terminada ya no se registra como desconexión**; **el uso se registra igualmente**.
- **rc.46**: los **streams de Claude se mantienen vivos durante la preparación y los reintentos** (PR #7857, `mameikagou`).
- **rc.44**: las **métricas de rendimiento cuentan los streams terminados antes de que el cliente desconectara** (PR #7638).

## Why It Matters
Todo el grupo es el mismo error, observado desde tres ángulos: **el gateway confundía "el cliente se fue" con "el stream se rompió"**. La consecuencia no es cosmética: una desconexión mal clasificada puede **marcar la petición como fallida** y, con ello, **no registrar el uso** — es decir, **regalar el coste de una llamada que el upstream sí cobró**.
La frase del release note es la que hay que retener: *"The usage is still recorded"*. Es un **fail-closed del lado del coste** que se apoya en la distinción entre **fin del stream** y **desaparición del cliente**. El cliente que cancela porque ya tiene su respuesta **no debe** cancelar el cobro: el trabajo se hizo.
Y el **keep-alive durante preparación y reintentos** ataca la otra mitad: si el cliente tiene **timeout** mientras el gateway prepara o reintenta, se va; y si se va, el gateway hereda un stream huérfano. Es la razón por la que los clientes de código (Codex, Claude Code) resuelven reintentos reenviando **assistant text ya emitido** — un caso que rc.43 tuvo que tratar aparte con la marca **`trailing_assistant_omitted`** ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]).
Para el vault, la lección de producto es directa: **cualquier gateway que mida "uso" debe definir antes qué es una desconexión**, porque esa definición es la línea entre cobrar y regalar ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
