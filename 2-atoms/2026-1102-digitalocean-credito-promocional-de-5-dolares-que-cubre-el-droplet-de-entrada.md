---
id: 2026-1102-digitalocean-credito-promocional-de-5-dolares-que-cubre-el-droplet-de-entrada
type: atom
certainty: solid
sources: [sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1101-digitalocean-facturacion-por-segundo-con-minimo-de-60-segundos]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
DigitalOcean documenta un **crédito promocional de $5 válido 90 días**: se aplica automáticamente a la cuenta, la tarjeta solo se cobra cuando el crédito se agota o expira, y el importe no gastado se pierde al vencer ("you won't be able to use any remaining credit after the 90-day period expires"). La FAQ de crédito aparece **completa y con la misma redacción en las tres capturas** (2026-10-31, 2026-11-01 y 2026-11-02).

## Why It Matters
Es la única forma en que el presupuesto de ≤ €4/mes puede tocar un Droplet de DigitalOcean **sin gastar un euro**: **$5 cubren íntegramente el plan de entrada de $4.00** y sobran $1 para el segundo mes o para un backup al 20 %. En la práctica, el voucher convierte el umbral de entrada en **$0 durante 90 días**, y eso habilita una prueba que de otro modo no cabría en el presupuesto: levantar el droplet de 512 MiB y el de 2 GiB ($12) midiendo si el stack cabe, sin comprometer gasto recurrente. La ventana de 90 días es también un límite reales —el crédito se pierde, no se renueva— y encaja con el patrón que el vault ya detectó en el tramo barato de los planes anuales prepagados: **aquí el descuento no está en el precio, está en el período de prueba**.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** vuelve a publicar la FAQ del crédito **con redacción idéntica** a las del 2026-10-31, 11-01 y 11-02: "$5 credit for 90 days", la tarjeta cobrada "only after you have utilized the free credits or after the credit expiration period", y el expiry que inutiliza el saldo restante. El bloque de "…" de esta captura afecta a la sección intermedia, **no** a esta FAQ: es la cuarta captura consecutiva con la misma redacción, lo que confirma que la redacción de la FAQ es estable y que el mecanismo del crédito (monto, ventana y orden de cobro) **no ha cambiado**. La atomización se mantiene en `solid` sobre el mecanismo documentado; sigue sin publicarse el importe habitual del crédito ni sus condiciones de elegibilidad. Ver también [[2026-1103-digitalocean-alertas-de-facturacion-por-email-al-superar-un-umbral]].

## Nota de verificación
El importe de $5 y la ventana de 90 días son **el ejemplo de la propia FAQ** ("if you received a $5 credit for 90 days..."), no una promoción garantizada en curso: la FAQ de "free trial" dice que DigitalOcean "often provides promotional credits for new users" y que hay que **consultar el sitio web para las ofertas vigentes**. La página **no publica** el importe habitual del crédito ni sus condiciones de elegibilidad. Por eso el átomo afirma el mecanismo documentado, no la existencia actual de la oferta.
