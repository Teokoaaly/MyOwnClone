---
id: 2026-1031-tailscale-docker-y-automatizacion-por-iac
type: atom
certainty: solid
sources: [sources/2026-10-31-tailscale-docs.md, sources/2026-11-02-tailscale-docs.md, sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-myclone-stack-tecnologico]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La sección "Expand your tailnet" del índice de Tailscale incluye tres entradas con descripción explícita que configurem la infraestructura, no solo la conectividad: **"Docker — Explore how to use Tailscale inside Docker containers"**, **"Automations — Automate your tailnet using infrastructure-as-code providers, webhooks, and other integrations"** e **"Integrations — How to use Tailscale to various kinds of servers, services, or devices"**. Las tres descripciones son frases completas del índice, no títulos sueltos de navegación.

## Why It Matters
Es la diferencia entre "una VPN más" y "una capa de red operable": Tailscale documenta explícitamente el camino de **contenedores** y el de **infraestructura como código** (proveedores IaC, webhooks). Para el stack de MyOwnClone —Flask, Postgres, Redis, Weaviate, Next.js (ver [[2026-1022-myclone-stack-tecnologico]])— el caso de uso inmediato es el worker y el api corriendo en contenedores que se redeployan, con el tailnet declarado como código para que el alta de un nodo sea un artefacto versionado y no un paso manual. Y todo eso ocurre en la misma línea de coste de infraestructura que el vault está intentando mantener en ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): si el tailnet se declara por IaC sobre el VPS ya pagado, el coste incremental del overlay es el de la licencia, no el de un servicio adicional.
