---
id: 2026-1027-dataimpulse-auto-recharge-publicado-en-la-documentacion
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-home.md]
links: ["[[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]]", "[[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]]"]
---

## Claim
La documentación de DataImpulse incluye entre sus enlaces de entrada ("Jump right in") una función llamada **"Auto-recharge"** con el pie **"Don't worry about balance"**. Es decir, el proveedor **publica la recarga automática del saldo como una característica de producto**, junto a "Parameteres", "Examples of requests" y "Whitelist Ips". La captura **no** publica el umbral de recarga, el importe, la periodicidad ni si la función está activa por defecto.

## Why It Matters
Es la pieza que al vault le faltaba para cerrar un agujero que su propia fricción 15 del thread señalaba: el control de gasto del modelo prepago de DataImpulse se apoyaba **solo en el saldo manual** ("Top up your balance and activate your proxy", [[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]), sin umbral ni alerta documentada. Con la recarga automática publicada, **el control de caja se puede delegar**: el gasto deja de requerir una decisión por topping-up y pasa a ser un **pedido recurrente (standing order)** que se ejecuta solo. Y con "No expiry, no subscription" —saldo que no caduca, tráfico que no caduca— ([[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]) más recarga automática, la combinación es **el peor caso de gasto del corpus**: un saldo que se rellena solo, nunca caduca y nunca avisa.
La comparación con el resto del vault es lo que da valor al dato: Bright Data publica su auto-recharge con **cifras** —umbral del 25 % de la carga mensual ([[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]]) y disparo del 85 % del importe configurado ([[2026-1026-brightdata-auto-recharge-dispara-al-85-del-importe-configurado]])—, es decir, el sector **ya tiene el precedente de un auto-recharge parametrizado**, y DataImpulse lo publica **sin una sola cifra**. Para el vault, la diferencia no es de producto sino de **auditabilidad**: el mismo mecanismo que en un proveedor es auditable en otro es una caja negra, y eso es exactamente la asimetría que la §10 del thread ya detectó al comparar modelos de contrato opuestos ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]).
Consecuencia operativa para el patrón de coste del vault: si la recarga es automática y el saldo no caduca, el techo de gasto mensual **no puede expresarse con el saldo**, y la única variable de control que queda es el propio umbral de recarga — que es precisamente el dato que esta captura no publica.

## [FRICTION]
> [[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]] afirma que el modelo comercial es "**No expiry, no subscription**" y "Pay-as-you-go", con el flujo de compra "Top up your balance and activate your proxy", y su Nota de verificación dice que la captura "**no** publica: importe mínimo de recarga, si el saldo prepagado es fungible entre los cuatro tipos de proxy...".
> Este átomo presiona ese dato: la propia documentación publica una **recarga automática** del saldo. O "no subscription" es una afirmación que solo cubre el **tráfico** (que no caduca) y no el **saldo** (que se rellena solo y de forma recurrente), o entonces existe un cargo recurrente no subscription por el que el vault no tiene ninguna cifra.
> Ambas no pueden ser completamente correctas: o "no subscription" describe el contrato de consumo y deja la caja fuera, o la recarga automática es un pedido recurrente equivalente a una suscripción de saldo. Marcado para juicio humano, no auto-resuelto: la captura **no** publica umbral, importe ni periodicidad de la recarga.

## Nota de verificación
Títulos de las secciones de entrada transcritos literalmente. La captura **no** publica: umbral de recarga, importe máximo, periodicidad, si la función está activa por defecto, ni si se puede desactivar o limitar.
