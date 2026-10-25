---
id: 2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]", "[[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]"]
---

## Claim
Si una cuenta se abre a mitad de mes, Bright Data cobra el **compromiso mínimo completo el día del alta** y luego liquida el mes prorrateado por días activos. El ejemplo publicado es literal: alta el 25 de junio en un plan de $500 de compromiso mínimo → primer pago de $500; el 1 de julio el sistema ve 6 días activos = 20 % del mes → cobra $100, deja $400 en el saldo, y vuelve a cargar $100 para reponer el compromiso de julio.

## Why It Matters
Es un detalle de tesorería que el vault no tenía en ningún otro proveedor: **el compromiso se exige por adelantado íntegro aunque el mes se cobre prorrateado**. La caja de salida es de $500 desde el día uno; la devolución llega a mes siguiente y prorrateada. Para un vault con un techo de gasto recurrente muy bajo, esto significa que el primer desembolso no es el coste del mes, es **el compromiso anual comprimido en un solo movimiento**.
La contrapartida es que el prorrateo funciona en la dirección correcta —nadie paga un mes entero por seis días de uso—, y que el saldo no se pierde: se repone en el día 1 del mes siguiente. Frente al modelo prepago sin caducidad de DataImpulse ([[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]), son dos filosofías opuestas: **saldo que se gasta sin límite natural** frente a **saldo que hay que reponer cada día 1 para no perder el compromiso**.

## Nota de verificación
Ejemplo transcrito literalmente de la página. La captura **no** publica: si el prorrateo se aplica por días naturales o por días facturables, si el umbral es el mes de 30 o 31 días, ni qué ocurre si la cuenta se suspende antes del día 1.
