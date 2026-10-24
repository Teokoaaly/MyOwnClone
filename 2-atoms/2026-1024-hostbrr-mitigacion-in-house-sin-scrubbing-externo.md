---
id: 2026-1024-hostbrr-mitigacion-in-house-sin-scrubbing-externo
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]", "[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]"]
---

## Claim
La diferencia técnica que HostBrr plantea en su sección de DDoS es **dónde** ocurre la mitigación, no cuánto: "Some hosts reroute traffic to external scrubbing providers, adding latency to every request. Our mitigation runs inside the datacenter itself, filtering attacks on-site with no added latency." El diseño declarado tiene cuatro piezas: (1) **Real-Time Detection** — el tráfico pasa permanentemente por la capa de protección, sin análisis aguas arriba ni retardo de conmutación; (2) **Multi-Layered Defense** — los ataques volumétricos se descartan en el borde de red y un centro de scrubbing aplica filtrado granular de capa 4 a capa 7; (3) **In-House Mitigation** — filtrado dentro del propio datacenter; (4) **Automatic Filter Profiles** — escaneo continuo que reconoce los servicios en ejecución y aplica dinámicamente los umbrales exactos sin configuración manual. La página marca esto como "Always-On Mitigation: Inline Mitigation, 24/7/365".

## Why It Matters
El argumento "sin scrubbing externo" es una diferencia de latencia **en la ruta normal, no durante el ataque**: si el scrubbing de un tercero añade latencia a cada request, cualquier comparativa de latencia entre proveedores que mida el camino completo tiene que incluir ese factor. Y los "Automatic Filter Profiles" son, en la práctica, un auto-tuning de umbrales que en un VPS autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) hay que operar a mano — que es exactamente el tipo de tarea recurrente que el vault tiende a externalizar como coste operativo. Interesa además el encuadre de confianza: es la misma página que promete 99,9 % de uptime ([[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]), así que ambas afirmaciones se leen como promesas de marketing sin SLA publicado.

## Nota de verificación
La captura no publica diagrama de arquitectura, ni nombres de proveedores de scrubbing, ni el punto exacto de inserción en el backbone. Las cuatro mecánicas son copy de la home.

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La página de precios **reproduce la misma arquitectura de mitigación** con dos añadidos: la sección se titula "**Always-On Mitigation**" y la FAQ (pregunta 03) la reitera como incluida sin coste. La frase clave se mantiene literal: "Some hosts reroute traffic to external scrubbing providers, adding latency to every request. Our mitigation runs inside the datacenter itself, filtering attacks on-site with no added latency." Los dos indicadores numéricos del panel son **3.6 Tbps Capacity** y **< 1ms Latency**. Lo que la página de precios añade no es la mecánica sino la **salvedad explícita**: "\* DDoS protection and capacity may vary between services and location" y, en la FAQ, "Protection and capacity may vary between services and locations". Es la misma promesa con la misma red de seguridad —nunca publicadas— que el átomo de DDoS ya documentaba.
