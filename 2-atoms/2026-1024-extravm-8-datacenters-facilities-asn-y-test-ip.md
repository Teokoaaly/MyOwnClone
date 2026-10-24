---
id: 2026-1024-extravm-8-datacenters-facilities-asn-y-test-ip
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-cripto-desde-2014-en-8-ubicaciones]]", "[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1024-hostbrr-datacenters-alemania-estados-unidos-y-luxemburgo]]"]
---

## Claim
La página de precios publica la ficha de red de cada uno de los **8 datacenters** con nombre de facility, dirección postal, IP de test y ASN: **Dallas TX** (Evocative DAL6, 1221 Coit Rd, Plano TX 75075, test IP 216.146.25.35, **AS63018**), **Los Angeles CA** (Digital Realty BUR10, Burbank CA, test IP 104.156.154.14, **AS53724**), **Miami FL** (Equinix MI6 / Digital Realty MIA10, test IP 169.128.190.1, AS53724), **Secaucus NJ** (Evocative EWR1, 1 Enterprise Ave N, test IP 199.119.137.14, AS53724), **Amsterdam NL** (Digital Realty AMS5, Tupolevlaan 101, Schiphol-Rijk, test IP 45.59.170.5, AS53724), **Singapore** (Equinix SG3, 26A Ayer Rajah Crescent, test IP 216.146.26.1, AS53724), **Tokyo JP** (Equinix TY8, Shinagawa City, test IP 103.214.68.1, AS53724) y **Sydney AU** (Equinix SY3, 47 Bourke Rd, Alexandria NSW, test IP 206.245.167.5, **AS136557**). El hardware declarado por ubicación es **AMD Ryzen 9 / AMD EPYC 4004-4005** (Amsterdam solo Ryzen 9). Cada ubicación tiene un **Network Looking Glass** propio.

## Why It Matters
Es el nivel de detalle de red que el vault no tenía para ExtraVM: la página de cripto declaraba las 8 ubicaciones pero sin specs ([[2026-1024-extravm-cripto-desde-2014-en-8-ubicaciones]]); aquí cada una es **una facility identificable con su propio ASN y test IP**, lo que hace posible medir latencia y pérdida hacia cada zona antes de decidir dónde alojar el stack del despliegue vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]). El dato estructural relevante es la **concentración de ASN**: siete de las ocho ubicaciones cuelgan de **AS53724** y solo Dallas (AS63018) y Sydney (AS136557) tienen ASN propio — es decir, la "red global de 8 ubicaciones" es en realidad un backbone mayoritario único con dos puntos de salida, lo que la diversificación de facility **no** convierte en diversificación de upstream. Contraste con el vault: Hetzner publica regiones y zonas con su propia nomenclatura ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]) y HostBrr solo publica tres países ([[2026-1024-hostbrr-datacenters-alemania-estados-unidos-y-luxemburgo]]).

## Nota de verificación
La captura no publica capacities, número de racks, tránsito contracted, MTU, ni relación contractual con los proveedores de facility; las direcciones e IPs son lectura literal de la página.
