---
id: 2026-1026-brightdata-auto-recharge-dispara-al-85-del-importe-configurado
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]]", "[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida]]"]
---

## Claim
La documentación de billing describe el auto-recharge con un **umbral distinto** del que publicaba la página de precios: *"Auto-recharge triggers when your available balance drops below **85 percent of your configured amount** and tops it back up automatically. You can set any denomination."* Es decir, el disparador es el **85 % del importe configurado**, no un porcentaje del saldo consumido. Se configura en *Billing Settings*.

## Why It Matters
Si el umbral es el 85 % del **importe configurado**, entonces el corte ocurre con un saldo igual al 85 % de lo que se haya configurado — es decir, **el saldo retenido es proporcional a la configuración, no al gasto**. Configurar $100 dispara al bajar de $85; configurar $1.000 dispara al bajar de $850. Es una regla cuyo único parámetro es **la config**, y por tanto controlable por el usuario sin ningún sensor de consumo.
Eso es exactamente lo contrario del modo con "importe predefinido" que la página de precios describía el 2026-10-24, donde el corte llegaba **al 25 % del importe configurado** ([[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]]). Dos umbrales —25 % y 85 %— para el mismo mecanismo en dos páginas del mismo proveedor, y la diferencia no es cosmética: con el 85 % la cuenta **nunca se acerca a cero**, con el 25 % se acerca a agotar el saldo.
Para el vault la lectura de fondo no cambia: **la recarga automática es el mecanismo que multiplica el gasto sin control externo** y es el que hay que dejar desactivado ([[2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida]]). Lo que cambia es la magnitud del riesgo: con el umbral del 85 % del total, la cuenta **nunca llega a suspenderse por saldo** ([[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]) — pero eso solo es cierto si el auto-recharge está activo, que es justo lo que hay que evitar.

## [FRICTION]
> [[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]] (escrita el 2026-10-24) afirma que el auto-recharge con importe predefinido dispara **"at 25% the configured amount"** y da el ejemplo de configurar $100 con corte en $25, y además señala que el auto-recharge "empieza a operar cuando el saldo disponible **cae por debajo del 85 %** del saldo total de la cuenta".
> Este átomo presiona esa creencia en un punto: **el 85 % no es un umbral de activación sobre el saldo total, es el propio disparador del topping up y su base es el importe configurado**. La página de precios lo usaba como condición de arranque; la documentación de billing lo usa como umbral de recarga. Con lo cual, o la documentación de billing describe un **auto-recharge distinto** del de la página de precios (con un 85 % de saldo mínimo en vez de un 25 %), o una de las dos páginas usa "85 %" con dos significados incompatibles.
> Ambas no pueden ser completamente correctas: o el auto-recharge tiene un único umbral verificable, o el proveedor tiene dos mecanismos de recarga con nombres parecidos. Marcado para juicio humano, no auto-resuelto: **la captura no publica la aritmética del ejemplo** (con qué importe configurado y con qué saldo se dispara), de modo que el 85 % **no puede contrastarse** con el 25 % del ejemplo literal de la página de precios.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: el importe mínimo o máximo configurable, si el umbral del 85 % aplica también al modo "cargo mensual", ni qué ocurre si la recarga falla.
