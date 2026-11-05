---
id: 2026-1101-tailscale-kb-sin-ninguna-cifra-de-precio-ni-plan
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md, sources/2026-10-31-tailscale-docs.md, sources/2026-11-02-tailscale-docs.md, sources/2026-11-03-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
Ninguna de las tres capturas de `tailscale.com/kb` contiene **una sola cifra de precio, nombre de plan, límite de nodos ni de usuarios**. Lo único que el índice dice del dinero es "the plans we offer" (dentro de "Manage your organization"), y la navegación enlaza páginas tituladas "Manage billing", "Manage your plan", "Pricing", "Contact Sales" y "Get started - it's free!". La captura del 11-01 añade el marketing de producto "WireGuard® for Enterprises" y "Business VPN", y "Support options" / "Release stages" como páginas de soporte y ciclo de vida. Es decir: **el precio de Tailscale no está en la KB; está en otra página**.

## Why It Matters
Cierra el hueco de coste que [[2026-1031-tailscale-docs]] viene cubriendo por inferencia: el vault necesita un número mensual para meter Tailscale en la línea de infraestructura junto al VPS, y **las capturas no lo dan**. La consecuencia práctica para el presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) es que Tailscale solo puede aduciirse hoy como **partida de coste cero o marginal** (el "Get started - it's free!" del CTA de navegación) o como una línea abierta pendiente de medir — no como un número firme. Y al no existir precio por nodo en la fuente, el eje "coste por asiento vs coste por infraestructura" ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]) queda sin dato nuevo: Tailscale aporta control de red por identidad, no una categoría de coste nueva que medir.

## [FRICTION]
> [[2026-1031-tailscale-docs]] afirma que "Tailscale provides zero-config VPN connectivity with **per-node pricing**, creating a node-count cost model rather than per-user seating".
> Este átomo presiona esa creencia porque la fuente que ese átomo cita (`sources/2026-10-31-tailscale-docs.md`) **no contiene ninguna mención de precios, planes ni tarifa por nodo**: es el índice de 26 líneas de la KB, cuyo único texto económico es "the plans we offer".
> Ambas no pueden ser completamente correctas: o el modelo por nodo se sale del pricing real (lo que entonces no está en esta fuente), o la afirmación se dedujo de conocimiento externo al corpus.
> Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
La cuarta captura del mismo URL (`sources/2026-11-03-tailscale-docs.md`) **vuelve a no contener ninguna cifra de precio, nombre de plan ni límite de nodos o usuarios**. El único texto económico sigue siendo exactamente el mismo fragmento dentro de "Manage your organization": *"Manage your contact information, your account, the plans we offer, and how to manage your tailnet DNS name and domain."* No aparece ni la navegación de marketing del 11-01 ("Pricing", "Contact Sales", "Get started - it's free!"), ni ninguna mención a PAM/Enterprise como línea comercial. Refuerza la conclusión: **el precio de Tailscale no está en la KB en ninguna de las cuatro capturas** — queda como línea abierta o coste cero en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]], y el vacío de dato sobre "per-node pricing" que este átomo señala sigue sin resolverse.

## Actualización 2026-11-04
La quinta captura del mismo URL (`sources/2026-11-04-tailscale-docs.md`, 2779 bytes, 55 líneas) **vuelve a no contener ninguna cifra de precio, nombre de plan ni límite de nodos o usuarios**. El único texto económico sigue siendo el mismo fragmento dentro de "Manage your organization": *"Manage your contact information, your account, the plans we offer, and how to manage your tailnet DNS name and domain."* Como el cuerpo de esta captura es **byte a byte idéntico al del 2026-11-02** (`md5` del cuerpo desde la línea 4 = `dfd19d3b301aeb651e1567b1b8d728c4` en ambos), esta re-verificación no depende del modo de renderizado: **el precio de Tailscale no está en la KB en ninguna de las cinco capturas**. El hueco de dato sobre "per-node pricing" que este átomo señala sigue sin resolverse. Ver [[2026-1104-tailscale-quinta-captura-sin-cifras-de-precio-ni-plan]].
