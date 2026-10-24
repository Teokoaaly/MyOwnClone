---
id: 2026-1024-extravm-cripto-desde-2014-en-8-ubicaciones
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-crypto-vps.md, sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1024-evoxt-vps-para-china-en-us-y-uk]]", "[[2026-1024-hostbrr-datacenters-alemania-estados-unidos-y-luxemburgo]]"]
---

## Claim
ExtraVM afirma aceptar **cripto desde 2014** —"ExtraVM has accepted cryptocurrency payments since 2014, making us one of the longest-running Bitcoin VPS providers in the industry"— y opera en **8 ubicaciones, todas con aceptación de criptomoneda**: Dallas TX, Los Angeles CA, Miami FL, Secaucus NJ, Amsterdam NL, Singapore, Tokyo JP y Sydney AU. La página resume la presencia como "datacenters across **3 continents**" y muestra una valoración de **4.8/5 en Trustpilot**.

## Why It Matters
La antigüedad es el dato diferencial frente al resto del vault: Hetzner, HostBrr y Evoxt son proveedores modernos comparados por precio y SLA, y ninguno declara una trayectoria en pagos cripto; **ExtraVM es el único actor del vault cuya propuesta de valor central es el canal de pago**, no la infraestructura. Eso reordena el eje de comparación: el vault puede elegir entre "hosting barato con SLA auditable" y "hosting con pago sin identidad y trayectoria de 10+ años", que son dos bienes distintos. La nota geográfica también importa: las 8 ubicaciones de ExtraVM incluyen **Amsterdam, Tokio y Singapur**, que son las zonas que Hetzner no cubre en la misma forma ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]), mientras que los proveedores que el vault sí ha comparado para Asia son los chinos (Evoxt vía US/UK, [[2026-1024-evoxt-vps-para-china-en-us-y-uk]]) y HostBrr (Alemania/EE.UU./Luxemburgo, [[2026-1024-hostbrr-datacenters-alemania-estados-unidos-y-luxemburgo]]). La captura **no** publica SLA, ancho de banda ni specs por ubicación en esta página.

## [NOTA 2026-10-24]
Fuente: `sources/2026-10-23-extravm-vps-pricing.md` (página de precios). La segunda captura **completa la ficha de cada una de las 8 ubicaciones**: facility y dirección postal, **ASN propio** (AS53724 en seis, AS63018 en Dallas, AS136557 en Sydney), IP de test y hardware AMD Ryzen 9 / EPYC 4004-4005 (ver [[2026-1024-extravm-8-datacenters-facilities-asn-y-test-ip]]). También matiza la "presencia global": la diversificación de facility **no** es diversificación de upstream, porque siete de las ocho ubicaciones comparten ASN, y la protección DDoS **varía por ubicación** — Sydney es la única sin mitigación de red nativa, solo filtrado local por debajo de 10 Gbps (ver [[2026-1024-extravm-ddos-varia-por-ubicacion-y-sydney-sin-proteccion-nativa]]). Es decir: las 8 ubicaciones del bloque cripto no son 8 ofertas equivalentes.

## Nota de verificación
El "desde 2014", el "3 continents" y el 4.8/5 de Trustpilot son declaraciones de la propia página; no hay verificación externa en la captura. La lista de ubicaciones es la misma que la de la página de precios del proveedor.
