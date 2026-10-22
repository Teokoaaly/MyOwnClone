---
id: 2026-1022-platform-admin-tenants-costes-mrr
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[multi-tenant-saas]]", "[[myownclone]]"]
---
## Claim
El back-office de plataforma de [[myownclone]] (`/admin/platform/*`) da al operador control sobre la base de tenants (búsqueda, orden y filtrado, "View as" / impersonation, invitación y concesión de planes), además de un buzón de feedback y un gestor de FAQs; incluye tracking de MRR por tiers Pro, Scale y Enterprise y tracking de coste desglosado por proveedor (Anthropic + OpenAI + email) y por eje (chat vs. ops).

## Why It Matters
Es la evidencia de que [[myownclone]] opera como un SaaS con back-office de operador real, no como un panel de creador: la granularidad "chat vs. ops" y por proveedor es exactamente la lectura operativa del modelo de coste descrito en [[2026-1022-costes-por-categoria-tenant]] — lo que la plataforma absorbe y lo que el tenant consume. El "View as" con concesión de planes sobre la misma pantalla conecta directamente con la suplantación de 30 minutos de [[2026-1022-auth-otp-impersonacion-30min]] y es el mecanismo por el que una beta con onboarding manual escala a N tenants en [[multi-tenant-saas]].

## Extensión (nuevos hallazgos, mayo 2026)
El análisis de bundles nombra los módulos de plataforma con su identificador real: `AdminPlatformResumen` (MRR, costes Anthropic+OpenAI+email, gráficos, métricas), `AdminPlatformTenants` (CRUD, invitaciones, cortesías, trials Stripe, impersonación 30 min), `AdminPlatformInbox`, `AdminPlatformSpam`, `AdminPlatformFeedback`, `AdminPlatformFaqs` y `AdminImpersonationBanner` (banner de suplantación en modo soporte). El desglose exacto de coste por proveedor (Anthropic + OpenAI + email) queda por tanto confirmado a nivel de módulo, no solo inferido. Ver [[2026-1022-admin-bandeja-global-y-spam]] y [[2026-1022-mapa-modulos-internos-desde-bundles-js]].
