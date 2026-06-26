# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-25] create | Wiki initialized
- Domain: Ingeniería de software, startups, automatización empresarial, ciberseguridad
- Path: ~/wiki
- Dual-purpose: LLM wiki + Obsidian vault (mismo directorio)
- Structure created with SCHEMA.md, index.md, log.md

## [2026-05-25] ingest | myownclone Research (batch)
- Sources ingested:
  - raw/articles/myownclone-founder-transcript.md (transcript podcast ~1h30m con Euge Oller)
  - raw/articles/myownclone-technical-research.md (investigación técnica: stack, DNS, endpoints)
- Pages created: 11
  - Entities: myownclone.md, delfi.md, eugenio-oller.md, marea-kiss-llc.md, emprenda-aprendiendo.md, y-combinator.md
  - Concepts: ai-clones.md, retrieval-augmented-cognition.md, context-aware-instances.md, synthetic-data-testing.md, multi-tenant-saas.md
  - Comparisons: myownclone-vs-delfi.md
- Index and log updated

## [2026-05-25] ingest | myownclone Recon Batch 2 — Web scraping + frontend analysis
- Sources ingested:
  - raw/articles/myownclone-web-scrape-2026-05-25.md (scrape de landing, sitemap, meta tags, JS bundles)
  - raw/articles/myownclone-frontend-recon-2026-05-25.md (rutas admin, features, bundles)
- Corrections:
  - delfi.md → delphi.md (nombre real: Delphi, delphi.ai)
  - Actualizado myownclone.md con rutas de admin, funcionalidades avanzadas, beta status
- Pages created: 3
  - Entities: coachvox-ai.md
  - Concepts: ai-clones-market.md
- Index and log updated

## [2026-05-25] query | myownclone Blueprint — Cómo replicarlo
- Created queries/myownclone-blueprint.md (19KB)
- Contenido: arquitectura completa, stack capa por capa, RAC (3 silos), multi-tenant SQL, instancias contextuales con código, plan de fases (0-4), estimación de costes, estructura de archivos inferida, oportunidades de diferenciación

## [2026-05-25] research | Deep-dive Mayo 2026 — JS bundles, onboarding, competidores
- Descargados y analizados 15 bundles JS de myownclone.com (~1.2 MB)
- Mapeados todos los módulos internos: AdminPlatform (7 módulos), Tenant App (8 módulos)
- Flujo de registro/onboarding completamente documentado
- Stack confirmado: Next.js 16.2.4, Neon + PGvector, Anthropic + OpenAI, Stripe, Sentry, PostHog, Clerk
- Competidores analizados: Personify (80% similitud), Coachvox (60%), Cpycat (40%)
- Perfiles Euge Oller: LinkedIn, Delphi original
- Páginas creadas:
  - comparisons/myownclone-competitors.md
  - raw/articles/myownclone-new-findings-may-2026.md
- Archivos generados: myownclone_chunks/ (15 bundles), myownclone_main.html, myownclone_login.html, myownclone_contacto.html, myownclone_registro.html
