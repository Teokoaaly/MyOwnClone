---
id: 2026-1026-heroku-private-y-shield-desde-125-y-150-dolares
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md, sources/2026-10-25-heroku-dyno-sizes.md]
links: ["[[2026-1026-heroku-postgres-premium-200-con-ha-y-15-minutos-de-parada]]", "[[2026-1024-1984-hosting-certificacion-iso-27001]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---

## Claim
Los tiers **Private** y **Shield** de Heroku son los que exigen un **Private Space** ("[Private Space](https://elements.heroku.com/addons/heroku-private-spaces) required") y son, en toda la página, la **frontera de cumplimiento**. En dynos: **Private-S $125** (1 GB, 12x, 5 DU) … **Private-2XL $1,500** (126 GB, 100x, 60 DU), con "Full network isolation", "Available in ten global regions", "Dedicated runtime environment"; y **Shield-S $150** (1 GB, 12x, 6 DU) … **Shield-2XL $1,800**, que añaden "**Dedicated environment for high compliance apps**", "**Ability to sign BAAs for HIPAA compliance**", "**PCI compliance**", "**Keystroke logging**", "**Space level log drains**" y "**Strict TLS enforcement**". En Postgres: **Private-0 $300** … **Private-10 $28,000** y **Shield-0 $350** … **Shield-10 $34,000**, donde Shield declara "**HIPAA and PCI compliant**" y "Everything in Private tier plans".

## Why It Matters
Es la respuesta del vault a una pregunta que estaba abierta: **qué cuesta el cumplimiento auditable cuando se compra a un proveedor grande en vez de construirse**. Aquí está, con precio de lista: **$150/mes** el dyno Shield más pequeño (1 GB, 12x), **$300/mes** el Postgres Private más pequeño, **$350/mes** el Postgres Shield más pequeño — y **el precio del Private Space como tal no está publicado en la captura**, así que esas cifras son **el precio visible de un paquete cuyo complemento no está cuantificado**.
Lo relevante para el producto es que **BAAs de HIPAA, PCI, keystroke logging y strict TLS** son cosas que el Aviso Legal y el DPA de un clon con datos de terceros necesitarían ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), y que **no se consiguen en el tramo VPS barato** ([[2026-1024-1984-hosting-certificacion-iso-27001]] es el caso más cercano: ISO 27001 a $9.66/mes, pero sin GDPR ni SLA ni créditos). El contraste es instructivo: **cumplimiento HIPAA/PCI con keystroke logging cuesta $150-$350/mes como mínimo**, mientras que la certificación ISO 27001 en el tramo barato cuesta $9.66/mes — porque no son lo mismo: una es un marco de gestión de seguridad y la otra un acuerdo regulatorio con auditoría de cliente.
El dato estructural: en Heroku, **aislamiento de red y cumplimiento son productos con línea de precio separada** (Private Space), no atributos incluidos. Es exactamente el patrón "la partida que se paga dos veces" que el thread de hosting barato registraba para el backup y el IPv4.

## Nota de verificación
La captura **no publica el precio del Private Space**, ni el texto de los BAAs, ni el nombre de la entidad que firma el BAA. Los importes de Private y Shield de la tabla de Postgres son los que la fuente publica para los planes "Requires Private Space: Yes".

## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-heroku-dyno-sizes.md` (página "Technical Specifications by Dyno Size"). La tabla de specs **confirma** los seis precios de Private ($125/$250/$500/$500/$750/$1,500) y los seis de Shield ($150/$300/$600/$600/$900/$1,800) y añade **la spec completa** que el catálogo de tiers no publicaba: **"CPU Share 100 %"**, **"Compute"** (S/M 12x, L 50x, L-RAM 24x, XL 50x, 2XL 100x), **"Dedicated"** — con la frase textual "**All Private dynos have dedicated compute resources**" y "**All Shield dynos have dedicated compute resources**" — y los Dyno Units (5/10/20/20/30/60 en Private, 6/12/24/24/36/72 en Shield).
El hallazgo que **añade** este átomo: **Private y Shield tienen specs idénticas fila a fila y Shield cuesta exactamente ×1,2 en los seis tamaños**, así que el cumplimiento se vende como **prima plana del 20 %**, no como capacidad. Detalle en [[2026-1026-heroku-shield-un-20-por-ciento-mas-que-private-con-las-mismas-specs]].
La misma página añade la restricción estructural: "**Private and Shield dynos are only available with Cedar-generation Private Spaces and Shield Spaces**", es decir, **el complemento es por generación y no por producto**. Detalle en [[2026-1026-heroku-espacios-privados-de-cedar-y-de-fir-y-acceso-restringido]].
