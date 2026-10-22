---
id: 2026-1022-posthog-integracion-pesada-sentry
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---
## Claim
[[myownclone]] instrumenta con doble cobertura: Sentry (`@sentry/nextjs`, DSN `6b2d7ed6999454df87ccf844aa85ba70`, org `4511315838173184`, env `vercel-production`, tracing y tunnel activos) **y** PostHog con integración tan pesada que el chunk principal de JS (187KB) está dominado por su SDK — feature flags, session recording con detección de rageclick, surveys, product tours, conversations, web vitals, dead-click autocapture, error tracking (envuelve `onerror`, `unhandledrejection`, `console.error`) y toolbar/editor. PostHog además trae integraciones configuradas de Intercom y Crisp Chat.

## Why It Matters
Duplicar Sentry y PostHog para errores es señal de inmadurez instrumental, no de rigor: el mismo error se reporta dos veces y se paga doble. Al revés, la riqueza de PostHog (flags, surveys, tours, replay) es un tell de que el producto se itera con experimentación de Growth sobre usuarios reales, no solo con llamadas a la API — lo que choca con la ausencia de superficie pública (ver [[2026-1022-onboarding-manual-sin-self-service]]). Delata además que el stack de instrumentación es el mismo que el de [[2026-1022-myclone-stack-tecnologico]], así que no es diferencial técnico.
