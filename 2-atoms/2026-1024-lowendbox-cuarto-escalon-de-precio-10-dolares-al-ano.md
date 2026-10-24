---
id: 2026-1024-lowendbox-cuarto-escalon-de-precio-10-dolares-al-ano
type: atom
certainty: tentative
sources: [sources/2026-10-23-lowendbox-1-usd-vps.md, sources/2026-10-23-lowendbox-2-usd-vps.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]", "[[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]"]
---

## Claim
El artículo de LowEndBox añade un **cuarto escalón** a la escala de precios de hosting del vault, por debajo de los tres ya registrados: VPS de 768 MB–1 GB a **$10–11,28 al año** (~€8,6–9,5/año, ~$0,83–0,88/mes) frente a VPS chinos a decenas de yuanes/año (marketing de sponsor, sin SLA), **HostBrr desde €2,00/mes** (~€24/año) y **Hetzner desde €5,99/mes sin IVA** (~€71,88/año). Los tres escalones más caros, escalonados, son los documentados en [[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]], [[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]] y [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]].

## Why It Matters
Ordena por magnitud lo que el vault puede gastar en infraestructura propia: hay un orden de diferencia entre el suelo de $10/año y el de €5,99/mes de Hetzner, y ese orden se paga en SLA, GDPR/ISO 27001, egreso y SLA con créditos ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]). Para MyOwnClone, cuyo stack activo (Flask + Next.js + Postgres + Redis, cf. [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) **no cabe en 768 MB ni en 1 GB de RAM**, el valor de este escalón no es alojar el stack sino **distinguir**: los $10/año son un nodo auxiliary, un relay o un worker, no el host principal. El escalón de Evoxt ($2,99 con specs declaradas, [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]) se sitúa entre HostBrr y Hetzner y confirma que el rango $1–$6/mes tiene ya cuatro proveedores documentados, no uno.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] (escrita hace 1 día) afirma que "ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de ≤ €4/mes" y que "el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en un punto nuevo: **el cuarto escalón es más barato que HostBrr (€2,00/mes) y que Evoxt ($2,99/mes)**, no solo más barato que Hetzner — $10/año es ~€0,72/mes. La conclusión del átomo viejo no queda refutada (sigue siendo cierta *dentro* del catálogo de Hetzner), pero sí pierde fuerza como excepción: el umbral de €4/mes no es un suelo raro sino que lo cruzan tres proveedores documentados, y este con specs declaradas y coupon explícito.
> Ambas no pueden ser completamente correctas si la creencia vieja se lee como "hay que pagar ~€6/mes por un VPS": o eso es una particularidad de Hetzner, o el vault ha estado comparando contra el proveedor más caro sin saberlo. Marcado para juicio humano, no auto-resuelto: los precios de LowEndBox son de una **lista editorial con una oferta agotada** (RackNerd, OUT OF STOCK) y **sin SLA ni specs de SLA publicados**, frente a una página de calculadora de Hetzner.

## Nota de verificación
Las conversiones a euros de los $10–11,28 son una estimación del átomo (no están en la fuente) y no aplican tipo de cambio ni IVA. La lista del artículo es de **junio de 2020, actualizado en septiembre de 2026**, con al menos una oferta sin stock, así que los precios pueden no ser vigentes.

## [NOTA 2026-10-24 — LowEndBox $2]
Fuente: `sources/2026-10-23-lowendbox-2-usd-vps.md`. La lista hermana de $2 **añade un escalón intermedio** entre el piso de $10–11,28/año y HostBrr (€2,00/mes): cinco ofertas a **$16.88 / $20.88 / $20.98 / $21.88 / $23.88 al año** (RackNerd 1.5 GB, DediRock 2 GB, RackNerd 2 GB, ServerHost 2 GB, CloudServer 2 GB), es decir ~$1,41–$1,99/mes pagando el año por adelantado (ver [[2026-1024-lowendbox-2-usd-escalon-16-88-a-23-88-al-ano]]). El patrón se confirma: **duplicar el precio de la lista de $1 duplica la capacidad** (768 MB–1 GB / 10–20 GB / 1 TB → 1,5–2 GB / 20–50 GB / 2–5 TB), pero **el techo de egreso sigue siendo pequeño** (5 TB/mes como máximo) frente a los 20 TB del CPX02 de Hetzner o los 2,5 TB con SLA de HostBrr. La escala del vault queda: **LowEndBox ~$10/año < LowEndBox $2 ~$17–24/año < HostBrr €2,00/mes < Evoxt $2,99 < ExtraVM $4,50 nominal / $8,00 comprable < Hetzner €5,99 sin IVA**. La conclusión operativa no cambia: **ninguno de los proveedores por debajo de €4/mes publica SLA con créditos, GDPR/ISO 27001 ni specs comparables** — el sobrecoste real es el riesgo, no el precio.
