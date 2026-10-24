---
id: 2026-1024-skhron-sin-ddos-por-cliente-ni-garantia
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-skhron-sin-backups-ni-snapshots-gestionados]]", "[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]"]
---

## Claim
Skhron **no ofrece mitigación DDoS como servicio por cliente**: "We protect our own network to keep the platform stable for all customers, but we do not offer DDoS mitigation as a per-customer service or guarantee. Services that draw sustained attacks may be **filtered or temporarily null-routed** to protect other customers on the same infrastructure."

## Why It Matters
Es el extremo opuesto al de HostBrr, que incluye mitigación L4+L7 de hasta 3,6 Tbps "automatically at no extra cost" ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]). La diferencia no es de precio sino de riesgo: en Skhron, un servicio que sufre un ataque sostenido **puede ser filtrado o null-routed**, es decir, el propio proveedor puede cortar el tráfico de un tenant para proteger al resto. Para un panel de clones de IA expuesto en Internet, eso convierte un incidente de DDoS en una caída silenciosa del tenant sin SLA de protección que lo cubra. Coincide con el resto del patrón del vault: lo que se publica es la infraestructura propia (aquí "protegemos nuestra propia red"), y lo que no se publica es la cobertura por cliente.
