---
id: 2026-1101-tailscale-servicios-tailscale-y-nodos-compartidos-para-publicar-sin-publicar
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
La sección "Access & Share Services" de la documentación de Tailscale ofrece tres primitivas distintas de publicación: **"Tailscale services"**, **"Endpoint collection"** y **"Share nodes"**, más "Use Taildrop". En paralelo, la sección "Share a web server" distingue dos páginas distintas: **"Tailscale Serve"** y **"Tailscale Funnel"**. La captura **solo contiene los títulos** de estas páginas: el índice no explica la diferencia entre Serve y Funnel, ni define qué hace "Tailscale services" frente a "Endpoint collection".

## Why It Matters
Es el punto donde el requisito del vault ("api, worker, db sin puertos públicos") se convierte en una elección entre dos funciones con nombre —servir dentro del tailnet frente a exponer públicamente— pero **el vault no puede elegir con esta evidencia**: haría falta capturar las dos páginas. Lo que sí queda sugerido por el título de la sección ("Access & Share Services") es que el producto tiene tres modos de dar acceso a un servicio, lo que multiplica las opciones de exposición y, con ello, las que hay que auditar. La consecuencia para la postura de seguridad que el vault ya tiene medida —nueve subdominios públicos y un nginx autoalojado con TLS de Let's Encrypt (ver [[2026-1022-dns-superficie-publica-myownclone]] y [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]])— es que cualquier función de publicación de Tailscale hay que contrastarla con esa superficie, no asumirla equivalente. Límite honesto adicional: la captura no dice si "Tailscale services" o "Share nodes" requieren plan de pago, ni sus límites.
