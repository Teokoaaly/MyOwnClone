---
id: 2026-1026-brightdata-al-agotar-creditos-dos-desenlaces-segun-haya-saldo
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida]]", "[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1026-brightdata-creditos-gratis-no-se-acumulan-y-se-reponen-el-1]]"]
---

## Claim
Agotados los créditos, el comportamiento depende **solo de si hay saldo depositado**, y hay exactamente dos desenlaces: **con fondos**, *"usage transitions automatically to your pre-paid balance at your plan's PAYG rates. There is no interruption in service"*; **sin fondos**, *"requests return an error and you are prompted to add funds to continue"*. En ambos casos *"your 5,000 free credits renew on the first of the following month"*. La misma lógica se repite en la FAQ: *"If you have no deposited funds, a **hard stop** is applied and no charges will occur. If you have pre-deposited funds, usage continues against your balance at standard PAYG rates."*

## Why It Matters
Es un **interruptor binario** de continuidad, y la parte relevante es que la transición a PAYG es **automática y sin interrupción de servicio**: el fallo silencioso no existe, pero **el gasto tampoco está acotado** si hay saldo. Para el vault esto significa que un cuenta con $50 depositados y 5.000 créditos gratuitos **no tiene tope de gasto en el mes**: consume los 5.000 créditos y luego sigue hasta agotar los $50.
La asymmetrical que la fuente explicita es que larenewal es **inmediata al mes siguiente**, pero el corte **no avisa**: sin fondos, la API empieza a devolver error; con fondos, empieza a gastar dinero. Y el hardening que el vault ya tenía registrado —el aviso por email al 85 % del saldo consumido ([[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]])— no aparece en esta página para el caso free tier.
Y hay un matiz de coherencia con el propio wording: *"your 5,000 free credits renew on the first of the following month"* implica que **la cuota gratuita depende de la existencia de la cuenta, no del gasto** — pero como no se acumula ([[2026-1026-brightdata-creditos-gratis-no-se-acumulan-y-se-reponen-el-1]]), un mes de poco uso se pierde y no compensa al siguiente.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: si existe aviso previo al corte duro, si el error es un 4xx concreto, ni si el saldo depositado puede repatriarse.
