---
id: 2026-1101-tailscale-soluciones-oficiales-para-bases-de-datos-y-runners-sin-exposicion
type: atom
certainty: tentative
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
La sección "Solutions" de la documentación de Tailscale incluye páginas que apuntan exactamente al caso de uso del vault: **"Protect production databases"** (`/docs/solutions/protect-postgresql-unencrypted-macbooks`), **"Secure GitHub Actions runners"** (`/docs/solutions/connect-github-cicd-workflows-to-private-infrastructure-without-public-exposure`), **"Lock down a server"** (`/docs/how-to/secure-ubuntu-server-with-ufw`), **"Connect to MongoDB Atlas"** (`/docs/solutions/create-a-secure-connection-to-mongodb-atlas`) y **"Secure external services"** (`/docs/concepts/ip-blocklist-relays`). Son **títulos y URLs de navegación**, sin descripción ni contenido: ninguna de las cinco páginas está capturada en este corpus.

## Why It Matters
Es evidencia de que el patrón "base de datos sin exposición pública" es un caso de uso de primera clase del propio proveedor, no una adaptación: la URL de "Protect production databases" apunta al patrón PostgreSQL cifrado desde máquinas sin disco cifrado, que es justo el caso de MyOwnClone con Postgres + Redis + Weaviate ([[2026-1022-myclone-stack-tecnologico]]). Y "Lock down a server" combina Tailscale con UFW, que es el patrón de endurecimiento que el vault necesita para no perder el firewall del proveedor ni abrir puertos. Límite honesto: son **títulos y URLs**, no contenido; el vault no puede afirmar nada sobre la receta concreta sin capturar esas páginas. La utilidad de este átomo es de backlog: son las cinco URLs concretas que hay que capturar para cerrar el eje de "cero puertos públicos" ([[2026-1022-dns-superficie-publica-myownclone]]).
