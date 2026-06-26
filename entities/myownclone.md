---
title: myownclone
created: 2026-05-25
updated: 2026-05-25
type: entity
tags: [saas, startup, b2b, b2c, llm, competitor]
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-technical-research.md, raw/articles/myownclone-web-scrape-2026-05-25.md, raw/articles/myownclone-frontend-recon-2026-05-25.md]
confidence: high
---

# myownclone

Plataforma SaaS multi-tenant que permite a creadores con marca personal entrenar clones de IA con su propio contenido. Fundada por [[eugenio-oller]] bajo la LLC [[marea-kiss-llc]].

## Qué es

myownclone convierte el contenido de un creador (cursos, vídeos, podcasts) en un clon de IA que interactúa con su audiencia en tres modos: pedagogía, ventas y soporte al cliente.

## Producto

- **Tres modelos por clon**: aprendizaje, soporte al cliente y ventas, cada uno con su propio retrieval path ^[raw/articles/myownclone-founder-transcript.md]
- **Instancias contextuales**: cada enlace del clon puede apuntar a un contexto específico (ej: un vídeo de YouTube concreto) ^[raw/articles/myownclone-founder-transcript.md]
- **Anti-alucinación**: si el retrieval no alcanza un umbral de similitud, el clon responde "no tengo conocimiento sobre eso" en vez de inventar ^[raw/articles/myownclone-founder-transcript.md]
- **Separación de hablantes**: en entrevistas subidas, detecta quién es el creador y solo usa su voz para responder ^[raw/articles/myownclone-founder-transcript.md]
- **Inbox/Triage**: gestión de emails entrantes con IA que propone respuestas en la voz del creador ^[raw/articles/myownclone-technical-research.md]
- **Insights dashboard**: feedback de usuarios, preguntas frecuentes, gaps de conocimiento, análisis de audiencia ^[raw/articles/myownclone-founder-transcript.md]
- **AI Interview Generator**: agente que entrevista al creador para extraer conocimiento (cosmovisión, valores, opiniones) ^[raw/articles/myownclone-founder-transcript.md]

## Stack Técnico

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 14+ (turbopack), React Server Components |
| Hosting | Vercel (Edge Network) |
| Base de datos | Neon (PostgreSQL serverless) |
| LLMs | Anthropic (Claude) + OpenAI |
| Embeddings | OpenAI embeddings (inferido) |
| Auth | NextAuth.js con JWT/sesiones + OTP |
| Monitoring | Sentry (org_id: 4511315838173184) |
| Analytics | PostHog (eu.i.posthog.com) |
| Pagos | Stripe |

^[raw/articles/myownclone-technical-research.md]

## Precios

- **Plan más barato**: 99 €/mes — 1M palabras de entrenamiento, 4.000 respuestas/mes ^[raw/articles/myownclone-founder-transcript.md]
- Planes: Pro, Scale, Enterprise
- Trial de 30 días con tarjeta (Stripe)

## Tracción

- **Beta cerrada**: sin self-service — `/registro` redirige a `/contacto`. Onboarding caso por caso ^[raw/articles/myownclone-web-scrape-2026-05-25.md]
- [[emprenda-aprendiendo]] genera ~3.000 conversaciones/mes con ~1.200 alumnos ^[raw/articles/myownclone-founder-transcript.md]
- Foco geográfico: mercado US (5% adopción España vs 55% US)
- Deploy ID público: `dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S` (Vercel) ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- Release: `3cd116d948dc38b980833dd9d465bcffbc8fd443` ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- Sin blog, changelog, roadmap ni docs públicos (todo 404) ^[raw/articles/myownclone-web-scrape-2026-05-25.md]

## Panel de Admin (rutas internas)

Rutas descubiertas en el JS bundle (Next.js App Router, ES/EN): ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]

| Sección | Rutas |
|---------|-------|
| Clone | /admin/clone, /admin/identity (general, purpose, style, voice-call) |
| Brain | /admin/brain (knowledge, products, support, terms) |
| Library | /admin/library (contenido del creador) |
| Learning | /admin/learning (audience, feedback, gaps, questions) |
| Products | /admin/products (courses, consulting, downloads, masterclasses) |
| Conversations | /admin/conversations |
| Contacts | /admin/contacts |
| Meetings | /admin/meetings (agenda, availability, integrations, recordings) |
| Inbox | /admin/inbox (triage, signature, memories, templates) |
| Usage | /admin/usage (plan, team, invoices) |
| Platform | /admin/platform (tenants, feedback, FAQs, impersonation) |

## Funcionalidades Avanzadas

- **Inbox Triage con IA**: procesamiento de emails entrantes. La IA propone drafts, memories, templates y labels. Voice notes con transcripción ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- **Videollamadas integradas**: booking público con detección de timezone, grabación con transcripción, ICS para Google/Outlook/Apple ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- **Feedback widget**: captura errores y sugerencias con screenshots (Ctrl+V pegar), límite 5MB ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- **Suplantación (impersonation)**: "Support mode" — 30 min auto-expire, audit trail, banner rojo ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- **Planes gratuitos (comp)**: forever / N meses / hasta fecha, otorgados por platform admin sin Stripe ^[raw/articles/myownclone-frontend-recon-2026-05-25.md]
- **Intercom + Crisp Chat**: integraciones de comunicación con clientes ^[raw/articles/myownclone-web-scrape-2026-05-25.md]

## Arquitectura Multi-Tenant

Cada creador es un tenant con slug propio (`[slug].myownclone.com`). Aislamiento completo entre tenants. Panel de admin de plataforma con suplantación de usuarios (impersonation, 30 min) y audit log.

## Roadmap

- **Fase 1** (actual): solo clonación — enfoque total en calidad del clon
- **Fase 3** (futuro): automatización completa del negocio online — el clon construye funnels, páginas de venta, productos automáticamente

## Conexión Y Combinator

myownclone encaja en el RFS #3 de [[y-combinator]]: "Company Brain" — centralizar el conocimiento disperso de una empresa para automatizarla. ^[raw/articles/myownclone-founder-transcript.md]

## Ver también

- [[delfi]] — competidor directo, inspiración inicial
- [[myownclone-vs-delfi]] — comparativa detallada
- [[ai-clones]] — concepto general
- [[retrieval-augmented-cognition]] — la tecnología core (RAC)
