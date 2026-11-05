---
id: 2026-1101-lambda-presupuesto-4-euros-ordena-de-magnitud-gpu
type: atom
certainty: tentative
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1101-lambda-instancias-1x-precios-de-gpu-de-consumo]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]"]
---

## Claim
Con los precios publicados por Lambda, **ninguna configuración de GPU cabe en el presupuesto duro de ≤ €4/mes de infraestructura del vault**: la GPU más barata del catálogo (Quadro RTX 6000 a $0,69/GPU-hora) cuesta **$503,70/mes** funcionando 24/7 (~€463 con cambio 0,92), es decir **~116 veces el presupuesto**; la A6000 a $1,09 son $795,70/mes (~183×); un H100 SXM 1x a $4,29 son **$3.131,70/mes** (~724×); un cluster B200 de 16 GPUs a $9,86 son $157,76/hora y **~$115.165/mes**. Incluso el V100 8x a $0,79/GPU-hora son $4.613,60/mes.

## Why It Matters
Cierra cuantitativamente la pregunta que el vault se estaba haciendo: **la nube GPU no es una alternativa al autoalojamiento dentro de este presupuesto, es un orden de magnitud completamente distinto**. El eje abierto "coste por asiento vs coste por infraestructura" (anclas: [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) tiene aquí su respuesta práctica: si MyOwnClone necesitara GPU, tendría que (a) dejar de ser un SaaS de ≤ €4/mes de infra y pagar dos o tres órdenes de magnitud, (b) facturarlo como coste variable por tenant en la línea `categoryCloneResponses`/ops del panel ([[2026-1022-costes-por-categoria-tenant]]), o (c) seguir con inferencia por API. La comparación relevante para el vault no es Lambda vs Hetzner, sino **Lambda vs API de inferencia por token** para el mismo trabajo: ahí el cálculo cambia por completo.

## Nota de extensión 2026-11-03
Los importes mensuales son aritmética sobre precios por hora publicados (×730 h/mes, cambio USD→EUR 0,92 como aproximación no declarada en la fuente); `certainty: tentative` por ese carácter derivado. Los precios por hora son verbatim de `sources/2026-11-01-lambda-gpu-pricing.md`.
