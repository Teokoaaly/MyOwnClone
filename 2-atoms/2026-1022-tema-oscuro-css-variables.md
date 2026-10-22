---
id: 2026-1022-tema-oscuro-css-variables
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[2026-1022-myclone-widget-personalizacion]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]"]
---
## Claim
[[myownclone]] implementa el tema del producto con una key de `localStorage` llamada `myownclone-theme` (valores `dark`/`light`) y un set de 12 variables CSS (`--bg`, `--fg`, `--fg-muted`, `--bg-muted`, `--surface`, `--border`, `--accent`, `--accent-fg`, `--accent-hover`, `--brand-lime`, `--radius`, `--radius-lg`), tipografías Poppins (texto) y JetBrains Mono (código), y timezone de producto Europe/Madrid.
El scrape público del 2026-05-25 amplía la lista de tokens observados en el CSS servido (`--fg-faint`, `--bg-subtle`, `--surface-hover`) y confirma el mecanismo del tema: clase `dark` alternada en `<html>` + detección por `prefers-color-scheme` + persistencia en `localStorage`. Fija además la identidad de marca: logo SVG (arco + círculo) en verde lima (`--brand-lime`) sobre fondo `#0a0a0c`, favicon en `/myownclone-favicon.svg`, y `theme-color` `#ffffff` (claro) / `#0a0a0c` (oscuro).

## Why It Matters
La variables-as-tokens (`--accent`, `--brand-lime`, `--radius`) son la capa que permite que cada tenant re-tematice su panel sin reconstruirlo, el mismo objetivo que persiguen la pestaña de personalización del widget de [[2026-1022-myclone-widget-personalizacion]]. El timezone único Europe/Madrid es una señal de que la operación es española con timezone detection solo en las páginas públicas de reserva, no en el back-office. Es además la prueba de que [[2026-1022-admin-rutas-bilingues-sin-subdominio]] es una app de producto con design system propio, no un panel de terceros.
