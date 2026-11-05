---
id: 2026-1026-bitlaunch-destruccion-definitiva-de-vps-y-datos-de-cuenta
type: atom
certainty: tentative
sources: [sources/2026-10-25-bitlaunch-bitcoin-vps.md]
links: ["[[2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad]]", "[[2026-1024-extravm-registro-contable-sin-vinculo-a-wallets]]", "[[2026-1024-flokinet-sin-acceso-del-proveedor-a-los-datos]]", "[[2026-1026-bitlaunch-alta-con-email-y-password-sin-trackers-ni-cookies]]"]
---

## Claim
La sección "Keep your privacy" de la página Bitcoin VPS afirma: **"Further, you can completely destroy your VPS and account data at any point to have it with permanently removed."** Es decir, el proveedor ofrece una vía de **destrucción total tanto de la máquina como de los datos de la cuenta**, a demanda y en cualquier momento. La captura **no publica** el mecanismo (botón, ticket, API), el plazo de ejecución, ni qué queda retenido por separado (facturas, registros de pago, logs de acceso, correspondencia legal).

## Why It Matters
Es el extremo opuesto de la postura de custodia del corpus: donde 1984 Hosting **vende** su política de no logs como argumento de marketing ([[2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad]]) y FlokiNET sostiene que el proveedor **no accede a los datos** del cliente ([[2026-1024-flokinet-sin-acceso-del-proveedor-a-los-datos]]), BitLaunch promete **borrar activamente** lo que ya tiene. Para un producto como MyOwnClone, cuya operación implica datos personales de terceros (voz y chat de usuarios), la promesa de destrucción a demanda es exactamente el control que un proveedor de infraestructura debería ofrecer: permite un flujo de "borrar el servidor y la cuenta" sin quedar residuo. El matiz crítico es que la promesa **cobra su valor justo donde el vault ya tiene una objeción**: la facturación por hora implica registros contables, y una destrucción de cuenta "permanente" no puede abarcar los registros que el proveedor necesita para emitir facturas sin dejar de ser legal.

## [FRICTION]
> [[2026-1024-extravm-registro-contable-sin-vinculo-a-wallets]] afirma que ExtraVM conserva "transaction records (amount and date) for accounting purposes", es decir, **retención contable mínima con desvinculación de wallets**: el proveedor guarda el mínimo legal y nada más.
> Este átomo presiona esa regla: si BitLaunch ofrece "completely destroy your VPS and account data ... permanently removed", esa promesa **no puede ser total** — la facturación por hora y la contabilidad del proveedor exigen conservar el mínimo. Ambas no pueden ser completamente correctas: o la destrucción deja un residuo mínimo de registros contables (y entonces "completely ... permanently" es un claim de marketing), o la destrucción alcanza también a los registros fiscales (y entonces el proveedor está facturando sin traza). Marcado para juicio humano, no auto-resuelto: la captura no publica la política de retención, el plazo de conservación contable ni el alcance real de la destrucción.

## Nota de verificación
Frase literal de la página. "At any point" y "completely" son literales del proveedor. La captura **no** documenta el procedimiento, el SLA de borrado, ni la existencia de una lista de excepciones. No hay evidencia de que el borrado se ejecute; es una declaración de producto, no un hecho verificado.
