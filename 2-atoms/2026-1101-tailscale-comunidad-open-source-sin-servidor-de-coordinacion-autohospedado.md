---
id: 2026-1101-tailscale-comunidad-open-source-sin-servidor-de-coordinacion-autohospedado
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
La navegación de la documentación enlaza, dentro de "Resources", la página **"Tailscale Community Projects"** (`/docs/reference/tailscale-community-projects`) y, en "Reference", el repositorio **github.com/tailscale/tailscale**, además de "Interoperability with other software" (`/docs/reference/interoperability`). El pie de la web corporate mantiene un enlace "Open Source" y "Tailscale Insiders" con "Community Projects". **Ninguna de las tres capturas menciona Headscale ni ningún servidor de coordinación autohospedado**, ni describe cómo se despliega el plano de control.

## Why It Matters
Esto fija el límite del corpus con precisión: la vía autohospedada del plano de control **no está documentada en estas capturas**, solo está el enlace a la página que enumera proyectos comunitarios (donde cualquier alternativa self-hosted aparecería). La consecuencia para el vault es de coste: si el objetivo es mantener la infraestructura en ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), la decisión "Tailscale SaaS de pago vs servidor de coordinación propio" **no puede cerrarse con esta evidencia**, porque la fuente no dice ni qué parte del producto es autohospedable ni cuánto cuesta la parte alojada. Queda como pregunta abierta con una URL identificada, no como una opción evaluada. Lo que sí se puede afirmar es que el cliente es open source (repo enlazado), lo que hace plausible —no verificado— un self-hosted, pero eso es inferencia y no debe tratarse como dato.
