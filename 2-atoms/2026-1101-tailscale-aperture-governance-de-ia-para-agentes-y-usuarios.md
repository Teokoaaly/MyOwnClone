---
id: 2026-1101-tailscale-aperture-governance-de-ia-para-agentes-y-usuarios
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
La captura incluye una sección **"Aperture: Secure AI"** (`/docs/aperture`), con el único tagline descriptivo de producto del corpus: *"Aperture by Tailscale — Unified AI governance for AI agents and users."* Sus páginas: "What is Aperture?", "Get started with Aperture", "Connect devices outside your tailnet", "Set up LLM clients", "Set up LLM providers", "Connectors", "Chat", "Admin dashboard", "Control AI access", "Manage AI spending", "Observe and export AI usage", "Privacy and data retention", "Integrate with external tools", "Reference" y "Troubleshooting".

## Why It Matters
Es el único punto del corpus donde Tailscale toca explícitamente el gasto en IA, y por tanto el eje abierto del vault —coste por asiento (SaaS) vs coste por infraestructura ([[2026-1022-costes-por-categoria-tenant]]). Las páginas "Manage AI spending", "Control AI access" y "Observe and export AI usage" son, por título, funciones de **control de coste y de observabilidad del uso de LLM**, es decir exactamente lo que Langfuse y Sentry cubren hoy a nivel de aplicación en el stack de MyOwnClone ([[2026-1022-myclone-stack-tecnologico]]), pero portable a nivel de **gobierno de agentes**: qué modelos, qué conversaciones, qué datos salen. "Connect devices outside your tailnet" sugiere además un modelo de agentes que consumen recursos de red del tailnet —el worker llama a Postgres y Weaviate por IP privada—, lo que conecta esta sección con el requisito de cero puertos públicos. Límite honesto: la captura da el tagline y los títulos, **no** una sola frase sobre cómo se cobra ni sobre qué proveedores de LLM cubre; el valor de este átomo es de backlog y de señal de posicionamiento, no de especificación.
