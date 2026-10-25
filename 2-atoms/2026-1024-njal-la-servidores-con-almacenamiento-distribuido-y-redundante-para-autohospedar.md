---
id: 2026-1024-njal-la-servidores-con-almacenamiento-distribuido-y-redundante-para-autohospedar
type: atom
certainty: solid
sources: [sources/2026-10-24-njal-la-domains-vpn.md]
links: ["[[2026-1024-njal-la-precios-no-publicados-para-vpn-y-servidores]]", "[[2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
`njal.la` ofrece **servidores** en dos formas: **máquinas virtuales con soporte para "many Linux distributions"** y **servidores físicos bajo encargo** ("if you need a physical server, contact us!"). La característica técnica declarada del almacenamiento es un **backend distribuido**: "We use a distributed storage backend - so your data is stored in a redundant way across multiple machines". El caso de uso que la propia página nombra es el **autoalojamiento de servicios federados y de instancias propias**: "Host your mastodon, matrix, nextcloud and blinking under construction gifs with us!" / "Need a place to put up your own mastodon, matrix, nextcloud or protest blog? We needed it ourselves, so we built it".

## Why It Matters
El vault tiene un **dato de almacenamiento redundante en la familia de proveedores** — 1984 Hosting ofrece snapshots y el Vault tiene BuyVM con "backups automáticos al 10 % del precio base + 5 snapshots gratis" y HostBrr con backups como add-on — pero **el backend distribuido como característica de la plataforma de servidores es nuevo**: la redundancia no es un backup bajo demanda, es la arquitectura del producto. Para un producto SaaS multi-tenant con Postgres + Redis ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), **un backend de almacenamiento redundante entre máquinas es la diferencia entre "backup bajo demanda" y "el disco ya no es un punto único de fallo"**.

El caso de uso declarado es además el **perfil de cliente que el vault es**: mastodon, matrix, nextcloud y "protest blog" — la misma mezcla de proyecto asociativo y servicio autoalojado que el propio producto. Eso es una señal de **encaje de cliente** y, a la vez, la clase de cliente que un proveedor con foco en privacidad tiene que proteger judicialmente.

## Nota de verificación
La captura **no publica ninguna cifra de esta sección de servidores**: ni specs (vCPU, RAM, disco), ni precios, ni número de ubicaciones, ni SLA, ni ancho de banda incluido, ni política de backup. La redundancia del backend es un claim de diseño, no un dato medido ni una garantía con créditos.
