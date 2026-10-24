---
id: 2026-1024-evoxt-17-regiones-con-peering-de-ix
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]", "[[2026-1024-evoxt-vps-para-china-en-us-y-uk]]"]
---

## Claim
Evoxt afirma servir **"High CPU Frequency Virtual Machines from 17 different regions across the world"**, y la home enumera 17 localizaciones con su peering declarado: Los Angeles (Equinix LA), Montreal (QIX), Nueva York (NYIX), São Paulo (DE-CIX São Paulo, PTT São Paulo, PTT Fortaleza), Londres (LINX), París (France-IX), Ámsterdam (AMS-IX, ERA-IX, NL-IX), Fráncfort (DE-CIX), Varsovia (Thinx, TPIX), Zúrich (SwissIX), Kuala Lumpur (MyIX, Google, Cloudflare), Yakarta (JKT-IX), Sídney (peering con IXes australianos), **Hong Kong (routing optimizado a China vía red CN2)**, Seúl (KINX, tránsito por Korea Telecom), Osaka (BBIX, JPIX, tránsito por Softbank) y Tokio (Tier 1 + BBIX).

## Why It Matters
Evoxt es el extremo opuesto de Hetzner en cobertura: allí el catálogo se concentra en **5 availability zones y 4 países** ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]), y aquí hay 17 regiones con un IX distinto en cada una. Dos puntos tienen lectura directa para el vault: **Zúrich** se describe explícitamente como "un país políticamente neutral con leyes de privacidad fuertes" — que es exactamente el argumento que el vault usa cuando necesita una jurisdicción de dato defendible frente a clientes de la UE y de fuera, junto a la capa es-first y la jurisdicción española ([[2026-1022-i18n-es-first-jurisdiccion-es]]); y **Hong Kong con CN2** es la única vía explícita a China continental, irrelevante para el producto actual pero relevante como precedente si en algún momento el relay fuese autohospedado en Asia. La dispersión también es un argumento de resiliencia: un proveedor que reparte 17 puntos de peering reduce la dependencia de un solo datacenter.

## Nota de verificación
La captura **no** publica qué regiones tienen capacidad disponible, qué planes se ofrecen en cada una, ni si el precio varía por región. "17 regiones" es el número declarado por el proveedor y la lista enumera efectivamente 17 localizaciones.

## [NOTA 2026-10-24]
La página de precios (`sources/2026-10-23-evoxt-vps-pricing.md`) no contradice el número pero sí lo matiza: la línea comercial que publica es **"VPS plans for China customers"** y sitúa sus centros de datos en **Estados Unidos y Reino Unido**, no en Asia — es decir, la dispersión global de 17 regiones y la línea de precio en USD de esta página **no son la misma cosa**: la tabla de planes se ofrece para clientes de China desde datacenters en US/UK (ver [[2026-1024-evoxt-vps-para-china-en-us-y-uk]]). La captura de la home tampoco publica qué región sirve cada plan, así que **no se puede asignar un datacenter concreto a un precio concreto** con lo registrado hasta ahora.
