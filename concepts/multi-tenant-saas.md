---
title: Multi-Tenant SaaS
created: 2026-05-25
updated: 2026-05-25
type: concept
tags: [saas, architecture, database, backend]
sources: [raw/articles/myownclone-technical-research.md]
confidence: high
---

# Multi-Tenant SaaS

Arquitectura donde una única instancia de software sirve a múltiples clientes (tenants) con aislamiento completo entre ellos. [[myownclone]] es un ejemplo maduro de esta arquitectura.

## Implementación en myownclone

| Componente | Detalle |
|-----------|---------|
| Tenant ID | Slug único por creador (`[slug].myownclone.com`) |
| Dominio personalizado | Soportado como add-on |
| Aislamiento | Completo entre tenants (mencionado en aviso legal) |
| Panel de admin | admin.myownclone.com — gestión de plataforma |
| Impersonation | Suplantación de usuarios con expiration 30 min + audit log |
| Cost tracking | Por tenant: clone responses, ingestion, platform ops |

^[raw/articles/myownclone-technical-research.md]

## Stack Serverless/Managed

myownclone no tiene servidores propios visibles:

- **Frontend + API**: Vercel serverless functions
- **Base de datos**: Neon (PostgreSQL serverless)
- **LLMs**: Anthropic + OpenAI (API)
- **Pagos**: Stripe
- Todo el stack es managed, sin infraestructura propia que mantener

## Cost Tracking por Tenant

Tres categorías de coste:

1. **categoryCloneResponses**: respuestas del clon → facturable al tenant
2. **categoryIngestion**: ingesta de contenido → facturable al tenant
3. **categoryPlatformOps**: operaciones internas (embeddings, clasificadores, memoria) → pagado por myownclone

## Ver también

- [[myownclone]]
