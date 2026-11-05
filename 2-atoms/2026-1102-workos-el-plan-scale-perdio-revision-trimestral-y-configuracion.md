---
id: 2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion
type: atom
certainty: solid
sources: [sources/2026-11-02-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]", "[[2026-1102-clerk-precios-sin-cambios-en-48-horas]]", "[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]"]
---

## Claim
Entre las capturas del **2026-11-01** y la del **2026-11-02** de workos.com/pricing, la tabla de soporte cambia en dos filas del plan **Scale**: la **"Quarterly architecture review"** y el **"End-user configuration support"** aparecen con ✓ en Scale el 11-01 y con — en Scale (solo Enterprise) el 11-02. **Todos los precios** (base, AuthKit por MAU, SSO y Directory Sync por conexión, Audit Logs, Radar, Custom Domain, Scale a $1.000/mes) son **idénticos** en ambas capturas.

## Why It Matters
Es la diferencia real entre las dos capturas condensadas, y es una **reducción de alcance del plan de soporte**, no un cambio de precio. Si el 11-02 reflejaba el estado real de la página, entonces WorkOS removed del plan de $1.000/mes dos entregables que un cliente enterprise valoriza mucho (revisión de arquitectura con un ingeniero y soporte de configuración para los usuarios finales del cliente) — lo que degrada la relación valor/precio de ese plan y lo aleja del perfil "enterprise-ready" que vende la página. Si en cambio es un error de transcripción de la captura, la página cambió entre ambas fechas. En cualquiera de los dos casos la consecuencia operativa para MyOwnClone es la misma: **no se puede cotizar un SLA de soporte de WorkOS sin confirmar línea por línea qué incluye el plan Scale**, porque en el vault la diferencia entre $0 y $1.000/mes de soporte decide si el producto tiene presupuesto para identidad empresarial. Es además un recordatorio metodológico: dos capturas "condensadas" del mismo día en días consecutivos no son redundantes si difieren en una celda.

## [FRICTION]
> [[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]] afirma, con la tabla del 2026-11-01, que el plan Scale incluye "revisión de arquitectura trimestral" y "soporte de configuración para end-users".
> Este átomo presiona esa creencia porque la captura del 2026-11-02, de la misma URL, marca ambas filas con — para Scale y las mantiene solo en Enterprise.
> Ambas no pueden ser simultáneamente correctas: o la página cambió entre el 11-01 y el 11-02, o una de las dos capturas transcribió mal la tabla. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
La cuarta captura de workos.com/pricing (2026-11-03) **no aporta ninguna evidencia sobre esta fricción**: al ser un volcado crudo de la página, **no incluye la sección "Support Plans"**, de modo que ni la "Quarterly architecture review" ni el "End-user configuration support" aparecen en ella, y el rung "101+ | Custom | Contact sales" se enuncia como "Need additional scale? Talk to us". La fricción abierta aquí **queda sin resolver** y se documenta en detalle en [[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]; no se modifica este átomo para zanjarla.

## Nota de verificación
Diff literal entre sources/2026-11-01-workos-pricing.md y sources/2026-11-02-workos-pricing.md: las únicas dos líneas divergentes son las de "Quarterly architecture review" y "End-user configuration support" en la columna Scale; la cabecera de fecha "captured" también difiere.

## Actualización 2026-11-04
La quinta captura (2026-11-04) **aporta por fin evidencia de página cruda** sobre esta fricción: su escala de niveles de soporte deja **"Quarterly architecture review"** y **"End-user configuration support"** **solo en "Enterprise plan"**, y el "Scale plan" se limita a Video calls, Private Slack channel, Technical onboarding guidance y Guaranteed response SLAs. La captura cruda del **2026-10-31** traía **exactamente la misma lista de niveles**, de modo que **dos volcados crudos independientes** coinciden con la tabla del **11-02** y la tabla del **11-01** es la única que discrepa. Esto sugiere que no hubo cambio real de oferta el 11-02 sino un **error de transcripción en la tabla del 11-01** — aunque el dato no se resuelve solo: ni el precio de $1.000/mes ni los tiempos P1/P2 ni el horario hábil aparecen en ninguna captura cruda. Ver [[2026-1104-workos-el-render-de-soporte-confirma-que-scale-no-incluye-revision-trimestral]].
