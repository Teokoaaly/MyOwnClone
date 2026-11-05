---
id: 2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]", "[[2026-1026-brightdata-creditos-gratis-no-se-acumulan-y-se-reponen-el-1]]"]
---

## Claim
Bright Data declara su modelo de facturación como **wallet prepago**: *"Bright Data operates on a **pre-paid wallet model**: you are only ever charged for funds you have explicitly deposited. A free tier account has a **hard stop** when credits are exhausted, never a surprise bill."* Y la respuesta a si se cobra automáticamente al agotarse los créditos es **"No"**: sin fondos depositados se aplica un corte duro y no se produce ningún cargo; con fondos prepagados, el consumo continúa contra el saldo **a las tarifas PAYG del plan**. La FAQ de transición lo remata: *"Add funds to your account from the Billing page. **There is no minimum commitment.** You stay on PAYG and only pay for what you use."*

## Why It Matters
Es la garantía contractual más fuerte que el vault ha encontrado en el sector de scraping: **"never a surprise bill"**, es decir, un tope duro de gasto sin cláusula de sobreconsumo. Frente al modelo del resto de la página de precios —prepago con **compromiso mínimo de $499/mes** que se cobra por adelantado y se repone el día 1 ([[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]])— el PAYG es un régimen **distinto**, no una modalidad del mismo.
Y hay un detalle de la FAQ que resuelve la fricción de tesorería que el vault había registrado: el compromiso se prorratea por días activos ([[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]), lo que **obliga a un primer desembolso íntegro por adelantado**; en PAYG no hay tal desembolso, solo topping up. Es decir, **el único régimen que respeta un techo de gasto bajo es el que no tiene compromiso** —lo que el vault ya usa para el proxy, y ahora se confirma para toda la capa de API.
Para un producto que consume scrubbing en modo agente, esto es la diferencia entre "se puede dejar una tarjeta en el panel sin vigilar" y "hay que vigilar cada topping up". En un mercado donde el thread de agregador ya registró que cobrar por el **resultado útil** es el modelo que **se está volviendo** la norma comercial ([[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]), este "tope duro" es la contrapartida de seguridad que hace aceptable el prepago.

## [FRICTION]
> [[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]] (escrita el 2026-10-24) afirma que el ciclo de Bright Data arranca el 1 de cada mes, que el **compromiso mínimo se cobra automáticamente** mientras la cuenta esté "active" y que al llegar al 100 % del saldo la cuenta **se suspende** salvo que se añadan fondos.
> Este átomo presiona esa creencia en un punto: **no es un único régimen de facturación, son dos excluyentes**, y el que la página de precios describe (compromiso, suspensión, reposición al día 1) **no aplica a la capa de API**. Aquí el régimen es wallet prepago puro, con **corte duro sin cargo** y **sin compromiso mínimo**. La frase "Bright Data cobra un mínimo de $499/mes" es cierta para los planes de suscripción y falsa como descripción de la cuenta que el vault usaría (PAYG + free tier).
> Ambas no pueden ser completamente correctas: o la página de precios y la documentación de billing describen la misma cuenta, o describen productos distintos con contratos distintos —y el vault no puede citar "$499/mes" como el coste de entrada de Bright Data sin nombrar el plan. Marcado para juicio humano, no auto-resuelto: la captura **no** publica la tariff PAYG de un crédito, con lo que el coste real del régimen prepago queda sin cotizar.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: la tarifa PAYG por crédito, si existe un mínimo de recarga, ni si el "hard stop" corta también el uso de proxies.
