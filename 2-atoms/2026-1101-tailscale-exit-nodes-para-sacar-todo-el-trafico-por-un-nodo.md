---
id: 2026-1101-tailscale-exit-nodes-para-sacar-todo-el-trafico-por-un-nodo
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]"]
---

## Claim
La sección "Expand your tailnet" define los **exit nodes** con una frase explícita: *"Route all internet traffic through a specific device on your network"*, y la navegación incluye "Set up an exit node", "Route selection", "Set up an app connector" y "Set up high availability". La distinción entre ambos (el subnet router **importa** un rango hacia el tailnet, el exit node **exporta** el egress del tailnet) es una lectura cruzada de las dos frases del índice, no una afirmación literal de la fuente.

## Why It Matters
Es la pieza que convierte "sin puertos públicos" en una postura completa: los servicios se exponen solo al tailnet, y el egress del tailnet sale por un punto de salida elegido y auditable en lugar de por la IP del servidor. Para un despliegue en un VPS barato en la UE ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) el nodo de salida puede ser ese mismo VPS, lo que además centraliza el filtrado junto al firewall stateless del proveedor ([[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]) — pero también concentra el tráfico en un único punto, que es una consideración de disponibilidad y de coste de ancho de banda que la captura no cuantifica. La captura da la definición de una línea y los nombres de las páginas ("Route selection" sugiere resolución de rutas cuando hay varios candidatos), no los límites operativos: cuántos nodos, qué SLA, qué coste.
