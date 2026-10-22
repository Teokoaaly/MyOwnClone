---
id: 2026-1022-stripe-planes-trial-30-dias
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[myownclone-competitors]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-stripe-webhook-confirmado]]", "[[2026-1022-sin-pagina-precios-ni-docs]]"]
---
## Claim
Los pagos de [[myownclone]] pasan por Stripe con tres planes (Pro, Scale, Enterprise) y un trial de 30 días con tarjeta obligatoria; además existen cortesías sin tarjeta otorgadas por el platform admin (cupones 100% off) y hay tracking de MRR, pagos fallidos y cancelaciones. El recon de bundles confirma el juego completo de estados de suscripción que la app reconoce: `active`, `trialing`, `past_due`, `unpaid`, `canceled`, `incomplete`, `none` y `complimentary`, y que las cortesías se pueden asignar "forever", por N meses o hasta una fecha concreta.
El scrape HTTP del 2026-05-25 confirma la integración en producción por artefacto: `/api/webhooks/stripe` → 405 Method Not Allowed (ver [[2026-1022-stripe-webhook-confirmado]]), aunque no existe ninguna página de precios pública (ver [[2026-1022-sin-pagina-precios-ni-docs]]).

## Why It Matters
El trial con tarjeta frente a las cortesías sin tarjeta revela dos vías de adquisición: self-service vía Stripe y asignación manual desde el panel de plataforma. Ese split es la señal más directa de fricción en el onboarding y contrasta con el estado de beta que reportan los competidores en [[myownclone-competitors]]. La lista de ocho estados de suscripción es el vocabulario real del motor de facturación y permite distinguir "usuario cancelado" de "tenant complimentary sin flujo de pago" — una distinción invisible en las métricas de MRR y que explica el panel de tenants descrito en [[2026-1022-platform-admin-tenants-costes-mrr]].

## Extensión (nuevos hallazgos, mayo 2026)
El paso 1 del registro confirma el catálogo comercial: **Pro, Scale y Enterprise visibles en pantalla con precios dinámicos renderizados como `€{price}`** — el precio no está hardcodeado en el bundle sino resuelto en servidor — y un badge **"Acceso Beta" con precio bloqueado de por vida**. El paso 2 (Stripe Checkout) exige **tarjeta obligatoria, facturación mensual y sin permanencia**. Es decir, la palanca comercial de la beta es "precio congelado + sin permanencia" para reducir el riesgo percibido de entrar, y el precio se sirve dinámico por lo que los tres planes comparten una única ruta de render. Ver [[2026-1022-onboarding-cuatro-pasos-encuestas]].
