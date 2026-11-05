---
id: 2026-1101-tailscale-magicdns-y-nombre-de-dominio-del-tailnet
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---

## Claim
El índice de Tailscale sitúa el DNS **dentro del tailnet**, no como un servicio aparte: en "Manage your organization" la descripción es *"Manage your contact information, your account, the plans we offer, and how to manage your tailnet DNS name and domain"*, y la navegación de "Route Traffic" incluye una página **"Set up MagicDNS"**, otra **"Use DNS"** (`/docs/reference/dns-in-tailscale`), más "Tailnet name" y "Domain ownership" en la sección de organización. El tailnet tiene **un nombre propio y un dominio propio**, con la posibilidad de dominio personalizado.

## Why It Matters
El trío api + worker + db se puede direccionar **por nombre** (`api.tailnet`, `db.tailnet`) sin DNS público, sin certificados Let's Encrypt y sin puertos abiertos: la resolución ocurre dentro del overlay. Eso ataca de raíz el problema que el vault ya verificó en producción, donde el despliegue autoalojado arrastra nginx y una superficie DNS pública de nueve subdominios ([[2026-1022-dns-superficie-publica-myownclone]]) mientras la app corre en dos repos distintos ([[2026-1022-myownclone-dos-repos-flask-nextjs]]). La documentación también ofrece "Set up HTTPS certificates" y "Set up high availability", que son las piezas que un despliegue sin puertos públicos necesita y que el vault aún no tiene verificadas. Límite honesto: la captura **solo prueba la existencia y la ubicación de estas páginas**, no la sintaxis de los nombres, ni si el DNS personalizado requiere plan de pago.
