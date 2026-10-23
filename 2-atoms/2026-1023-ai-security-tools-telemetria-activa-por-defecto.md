---
id: 2026-1023-ai-security-tools-telemetria-activa-por-defecto
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-sentry-dsn-publico-contamina-dashboards]]", "[[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]", "[[2026-1023-ai-security-tools-repo-cc0-readme-generado-y-metricas-estaticas]]"]
---

## Claim
Once de las 422 entradas del README mencionan explícitamente telemetría, y en todas las casos el patrón es **telemetría activada por defecto con opt-out documentado**: *ModelAudit* — "installed usage enables telemetry by default; disable with `PROMPTFOO_DISABLE_TELEMETRY=1` or `NO_ANALYTICS=1`"; *OpenShell* — "Anonymous operational telemetry is enabled by default but can be disabled at deployment time or compiled out"; *Future AGI* — telemetría de despliegue que "defaults to account emails/domains for owners/admins/staff/superusers", y aun con `FUTURE_AGI_TELEMETRY_DISABLED=true` "still permits a minimal registration containing instance ID, version, deployment type, timestamp and the disabled flag", cuya supresión exige restringir el egreso al endpoint; *node9* — `node9 init` pregunta antes de enviar un ping de instalación pero con "Yes preselected", y el payload incluye "a persistent machine ID, detected agents, OS, and version, so it is pseudonymous rather than anonymous".

## Why It Matters
Es la convención del sector para herramientas que manejan código, prompts y credenciales de clientes: se instrumenta, se documenta el interruptor y se acepta un identificador persistente. El vault tiene esto ya registrado en su propio producto y en un tono de sospecha — ver el bloque siguiente —, pero el listado aporta la línea base contra la que comparar: en herramientas de seguridad el opt-out es la norma, no la excepción. También da la razón por la que la ausencia total de instrumentación observada en el bundle vivo ([[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]) es, en sí misma, una señal de reconstrucción y no solo una ausencia.

Y hay un ángulo de higiene que el listado aporta: la telemetría viene ligada a metadatos de publicación que hay que poder auditar. La entrada de `Future AGI` documenta hasta el identificador de instancia que se envía en el registro mínimo, lo que hace posible escribir una política de egreso — es el mismo nivel de detalle que el listado usa para declarar que sus propias estrellas son snapshots estáticos y que el índice es CC0 con licencia propia por entrada ([[2026-1023-ai-security-tools-repo-cc0-readme-generado-y-metricas-estaticas]]).

## [FRICTION]
> [[2026-1022-sentry-dsn-publico-contamina-dashboards]] califica la DSN pública de Sentry de [[myownclone]] como "un canal de escritura no autenticado" que permite "enviar eventos falsos … y contaminar los dashboards de error del producto".
> Este átomo presiona esa lectura con el precedente del campo: en el listado, telemetría activada por defecto con clave de identificación persistente y opt-out documentado se presenta como práctica normal y aceptada en herramientas que manejan material mucho más sensible (código fuente, credenciales, prompts).
> Ambas no pueden ser completamente correctas sin matizar: o la DSN pública del clon es un descuido de configuración y no una superficie de riesgo (y entonces conviene arreglarlo igualmente), o "telemetría por defecto" es un vector de riesgo aceptable solo cuando el proveedor es un tercero con SLA y el identificador no permite escribir en el sistema de la víctima. Marcado para juicio humano, no auto-resuelto.
