---
id: 2026-1022-myclone-competidor-arquitectura
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-stack-tecnologico]]", "[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1022-myclone-widget-embed-modos]]", "[[myownclone]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]"]
---
## Claim
El dashboard autenticado de MyClone.is se organiza en 12 secciones con rutas propias: Overview (`/dashboard`), Personas, Knowledge Library (`/dashboard/knowledge`), Voice Clone, Conversations, Widgets, Whitelabel, Workflows BETA, Integrations (Zapier + webhooks, bloqueado en Free), Access Control, Limits & Usage (`/dashboard/usage`) y Profile. El onboarding consta de registro con verificación por email (link temporal de 24h), un setup wizard visual de 3 pasos (Knowledge Library → Voice Clone opcional → completado), un checklist de completitud en el dashboard principal y una página pública por usuario en `app.myclone.is/{username}`.

## Why It Matters
[[myownclone]] está en beta cerrada con onboarding caso por caso (`entities/myownclone.md`): MyClone.is ofrece el ciclo completo self-service que a [[myownclone]] le falta. La sección "Public Persona Pages" (URL propia por clon, compartible sin embed) es el mecanismo de viralidad pasiva que el propio informe señala, y el mismo informe lista "páginas públicas que generan tráfico orgánico" como palanca estratégica. Las secciones Whitelabel (dominio y email propios) y Access Control (equipos) son bloques que el informe de [[myownclone-competitors]] no registra para ningún competidor directo.

## Extensión (API OSINT 2026-06-24)
Cada sección del dashboard tiene su **contrapartida en la API**: Whitelabel → `/custom-domains` (con `verify`), Access Control → `PATCH /personas/{id}/access-control` + `check-access`/`request-access`/`verify-access` por username, Widgets → `/users/me/widget-config` + `/users/me/widget-tokens`, Limits & Usage → `/tier/usage` + `/tier/subscription`, Workflows → `/workflows*`, Integrations → `/account/webhook` + `/webhooks/stripe`. La superficie total es de **227 endpoints** (ver [[2026-1022-myclone-api-superficie-227-endpoints]]), lo que confirma que el dashboard no es una fachada: cada pestaña tiene superficie de API.
