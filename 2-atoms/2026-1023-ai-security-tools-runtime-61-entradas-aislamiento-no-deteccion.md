---
id: 2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-ia-y-auth-totalmente-servidor]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]"]
---

## Claim
**Runtime Protection & Enforcement** es la subsección más grande del listado (61 entradas) y su eje no es la detección de prompt injection sino la **contención**: sandboxes por nivel (Landlock/seccomp en Linux, Seatbelt en macOS, microVM, contenedores), gateways de egreso y **proxies de credenciales** que inyectan el secreto real en el último momento (`onecli`, `TAP`, `Earl`, `piighost`). El README repite la misma advertencia en casi todas las fichas: estas herramientas **no son protección semántica contra prompt injection**. Ejemplos literales: *Vetto* — "this is not semantic prompt-injection protection"; *Sandlock* — "Linux-kernel process isolation rather than prompt-injection detection"; *Agent Safehouse* — "the default profile permits inbound and outbound networking; exfiltration prevention is explicitly out of scope"; *Coi* — "shared-kernel containers are not a microVM boundary".

## Why It Matters
Es la lección estructural que el vault necesita: la industria separa explícitamente **aislar la ejecución** de **detectar la manipulación del prompt**, y ninguna ficha del README afirma que el aislamiento por sí solo previene la inyección. Para un producto con toda la IA en servidor ([[2026-1022-ia-y-auth-totalmente-servidor]]), esto significa que "el LLM no está expuesto en el cliente" protege el modelo pero no protege el prompt: si el contexto recuperado o un documento arrastran instrucciones ajenas, el servidor sigue ejecutando el resultado.

Y hay un segundo movimiento en la misma dirección: cuando estas herramientas sí activan el bloqueo, lo hacen en modo opt-in y fail-open por defecto ([[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]). Contención y enforcement son, en el campo, dos capas separadas y ninguna viene activada.

## [FRICTION]
> [[2026-1022-ausencia-csp-xss-sin-mitigacion]] señala que la nota de entidad de [[myownclone]] afirma "aislamiento completo entre tenants" y que el aislamiento "se observa a nivel de datos pero no a nivel de superficie HTTP".
> Este átomo presiona esa lectura desde el lado de la industria: el propio listado de herramientas de referencia califica de forma rutinaria las afirmaciones de aislamiento — "shared-kernel containers are not a microVM boundary", "exfiltration prevention is explicitly out of scope" — porque el aislamiento de runtime y el aislamiento de datos son dos cosas distintas y verificables por separado.
> Ambas no pueden ser completamente correctas: o "aislamiento completo" describe únicamente el aislamiento de filas en base de datos (y el término se está usando con más fuerza que la evidencia), o hay un límite de runtime no documentado. Marcado para juicio humano, no auto-resuelto.
