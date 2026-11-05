---
id: 2026-1104-aiven-nueve-regiones-seleccionables-frente-al-claim-de-100-mas
type: atom
certainty: tentative
sources: [sources/2026-11-04-aiven-pricing.md]
links: ["[[2026-1102-aiven-disponibilidad-de-nube-y-region-por-plan]]", "[[2026-1104-aiven-la-captura-vuelve-a-ser-completa-e-identica-a-la-del-11-02]]", "[[2026-1031-hetzner-cloud]]"]
---

## Claim
La misma página de precios de Aiven ofrece **dos cifras de cobertura regional que no concuerdan**: el selector de la tarjeta de PostgreSQL nombra **nueve regiones** —Asia Bangalore (blr), Asia Singapore (sgp), Canada Toronto (tor), Europe Frankfurt (fra), Europe London (lon), Europe Amsterdam (ams), Australia Sydney (syd), United States New York (nyc), United States San Francisco (sfo)— mientras que la FAQ de comparación con vendors de una sola tecnología afirma que "Aiven runs on AWS, Google Cloud, Azure, and others, **in 100+ regions** — with the same operational experience everywhere". Ambas cifras conviven en el render completo del 2026-11-04. Además, la fila "Clouds" limita la elección real: **Free y Developer tienen "Limited"** y no pueden elegir nube ni región, Hobbyist solo tiene DigitalOcean/Google Cloud/OVH, y las seis nubes (AWS, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud) solo desde Startup ($75/mes).

## Why It Matters
La cifra "100+ regiones" es un **claim de cobertura global** y las nueve son el **selector efectivo del plan de PostgreSQL**: para el vault, que compara proveedores en una sola región europea ([[2026-1031-hetzner-cloud]]), lo relevante no es la cifra de marketing sino que **la región Frankfurt (fra) está disponible desde el plan Hobbyist ($12/mes) y en las seis nubes desde Startup ($75/mes)**. La distancia entre 9 y 100+ no es un error de redondeo sino dos cosas distintas —región seleccionable por plan vs. footprint publicitario—, y conviene no citarlas como si fueran la misma magnitud. Nota: el recuento de "diez regiones" del átomo [[2026-1102-aiven-disponibilidad-de-nube-y-region-por-plan]] sigue sin cuadrar (enumera nueve); la captura del 11-04 vuelve a listar nueve y no lo corrige.

## [FRICTION]
> [[2026-1102-aiven-disponibilidad-de-nube-y-region-por-plan]] afirma en un mismo átomo que "las regiones listadas en la página son **diez**" y a continuación enumera **nueve** códigos, y en paralelo recoge el claim de "100+ regions" como si ambos números describieran la misma disponibilidad. La captura del 2026-11-04, en render completo, vuelve a mostrar solo nueve regiones seleccionables junto al claim de 100+. Ambas no pueden ser completamente correctas: o el "diez" es un error de conteo y el "100+" es cobertura total de la plataforma (no de un plan), o hay regiones no renderizadas en el selector. Marcado para juicio humano, no auto-resuelto.
