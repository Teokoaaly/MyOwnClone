---
id: 2026-1028-newapi-documentation-home
type: atom
certainty: tentative
sources: [sources/2026-10-28-newapi-docs-home.md]
links: ["[[2026-1028-astrlink-api-protocols]]", "[[2026-1028-astrlink-conversation-trail]]"]
---

## Claim

New API documentation home (docs.newapi.pro) serves as the central gateway for connecting all AI providers, managing AI assets, and building the future of agentic workflows. It documents a unified platform that integrates multiple LLM providers through protocol conversion and unified API surfaces.

## Why It Matters

The home page establishes that AI providers can be connected and managed through a single interface, with AstrLink ensuring that secrets stay local on the user's machine and agents keep working without exposing sensitive data externally. The platform supports Docker deployment, panel management, cluster configuration, and environment setup for both development and production use. Partners and clients span education (Peking University), cloud providers (UCloud, Alibaba Cloud, IO.NET), and studio companies (Cherry Studio, AionUi), demonstrating broad ecosystem adoption. Sponsor partners like RixAPI further extend the platform's reach. The contributor network — including development contributors and documentation contributors — shows active community participation in maintaining and extending the platform's capabilities.

## [FRICTION]

> [[2026-1028-astrlink-api-protocols]] documenta los protocolos de conversión (OpenAI Responses, Chat Completions, Anthropic Messages, Gemini) pero la creencia de que una sola gateway puede convertir sin pérdidas entre todos los esquemas ignora la realidad de proyectos con licencias fragmentadas y historiales de commits discontinuos (como GPTGrok2API, 285 estrellas, último commit julio 2026). AstrLink's protocol conversion opera a nivel de gateway y asume que el proveedor upstream admite alguna variante del modelo solicitado; repositorios secundarios pueden tener protocolos no documentados o personalizados. Ambas afirmaciones pueden ser ciertas —AstrLink cubre los protocolos documentados de los proveedores principales, mientras que repositorios secundarios pueden tener protocolos no documentados o personalizados— pero la creencia de que todas las APIs son igualmente convertibles ignora la realidad de esquemas de licencia distinta y contratos de proveedor variables. Marcado para juicio humano.

> El claim de "conectar todos los proveedores de IA" presiona la creencia de que every AI provider can be equally integrated through a single gateway. The documented partnerships span specific providers (OpenAI, Anthropic, Google Gemini, Azure, AWS, DeepSeek, Qwen) with declared capabilities, but the ecosystem's partner list operates in "no particular order" without explicit SLA guarantees. La creencia de que routing técnico = viabilidad operativa completa ignora la dimensión de compliance y licensing que los partners introducen. Enterprise adopción depende de acuerdos de nivel de servicio y requisitos regulatorios que van más allá de la compatibilidad técnica de protocolos. No hay contradicción técnica, pero sí fricción en la suposición de que integración unificada resuelve todos los casos de uso organizacional. Marcado para juicio humano.