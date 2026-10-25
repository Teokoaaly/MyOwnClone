---
id: 2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]", "[[2026-1024-brightdata-cupon-50-off-y-match-del-primer-deposito]]"]
---

## Claim
La recarga automática de Bright Data tiene **dos modos**. (1) **Importe predefinido**: *"When you choose this option, you will manually set a configured amount that is charged when your balance runs low (**at 25% the configured amount**)"* — el ejemplo que da la página es: configuras $100, se te cobran $100, y se te vuelven a cobrar $100 cuando el saldo llega a $25. (2) **Cargo mensual**: si no usas la recarga automática, se te cobra el nuevo compromiso el día 1 de cada mes; y en el plan PAYG, sin compromiso mínimo, **la cuenta no se recarga automáticamente**. El auto-recharge empieza a operar cuando el saldo disponible **cae por debajo del 85 %** del saldo total de la cuenta.

## Why It Matters
La aritmética del modo (1) merece atención porque es contraintuitiva: **el umbral no es un porcentaje del saldo, es un porcentaje del importe configurado**. Con $100 configurados, el corte llega cuando el saldo baja a $25; con $1.000 configurados, el corte llega cuando el saldo baja a $250. Es decir, **configurar más dinero retrasa el corte en términos absolutos pero no protege el saldo** — el gap entre el corte y el cero es siempre el 75 % de lo configurado, y lo que se decide con esa cifra es el tamaño del salto de caja, no su frecuencia relativa al gasto.
Para un vault esto es exactamente el mecanismo que hay que dejar **desactivado**: una recarga automática de $100 sobre un consumo de $40/mes es un multiplicador del gasto sin control externo. Y en PAYG, donde no hay compromiso, no hay recarga automática — lo cual hace que **el PAYG sea el único modo con el gasto acotado por decisión propia** ([[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]), y también el único sin red de seguridad ante un pico de tráfico.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: si el auto-recharge con importe predefinido está disponible en PAYG o solo en planes con compromiso, ni si el umbral del 85 % aplica a ambos modos.
