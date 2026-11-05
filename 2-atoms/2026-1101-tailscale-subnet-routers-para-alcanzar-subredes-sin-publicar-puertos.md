---
id: 2026-1101-tailscale-subnet-routers-para-alcanzar-subredes-sin-publicar-puertos
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
La sección "Expand your tailnet" del índice de Tailscale describe los **subnet routers** con una frase explícita: *"Use subnet routers to give devices outside your local network access to services within specific subnets. Extend your private network with Tailscale."* Es la función documentada para dar a dispositivos externos acceso a servicios de una subred local **sin convertir esos servicios en públicos**.

## Why It Matters
Es exactamente el patrón que necesita el trío api + worker + db cuando db vive en una red privada o en un contenedor con IP interna: el router de subred publica el rango dentro del tailnet, no en Internet. Evita la alternativa que el vault ya detectó como deuda en producción —nginx autoalojado con DNS público (ver [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] y [[2026-1022-dns-superficie-publica-myownclone]])— y no añade ninguna línea de coste al presupuesto de ≤ €4/mes: es una función del cliente, no un servicio aparte. La limitación honesta es que esta captura **solo da la frase del índice**, no el comportamiento del enrutado (qué protocolos, qué Advertisement Routes, qué límites tiene un subnet router), así que queda como definición de objetivo, no como especificación verificada.
