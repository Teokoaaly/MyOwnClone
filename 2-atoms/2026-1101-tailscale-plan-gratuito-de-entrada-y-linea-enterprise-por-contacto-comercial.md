---
id: 2026-1101-tailscale-plan-gratuito-de-entrada-y-linea-enterprise-por-contacto-comercial
type: atom
certainty: tentative
sources: [sources/2026-11-01-tailscale-docs.md, sources/2026-10-31-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1101-tailscale-kb-sin-ninguna-cifra-de-precio-ni-plan]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Las capturas distinguen **dos vías de entrada** sin publicar cifras: la vía autoservicio, con el CTA de navegación **"Get started - it's free!"** (`login.tailscale.com/start`), y la vía comercial, con **"Contact Sales"** (`/contact/sales`) y el producto de marketing **"WireGuard® for Enterprises"** (`/wireguard-vpn`), junto con líneas de producto separadas: "Business VPN", "Tailscale PAM", "CI/CD Connectivity", "Workload Connectivity", "Edge & IoT" y "Homelab". La página "Invite only features" (`/docs/reference/invite-only-feature`) sugiere además que hay funcionalidades reservadas a cuentas específicas. Ninguna cifra acompaña a ninguna de estas etiquetas.

## Why It Matters
Da la **forma** del modelo comercial sin el número: hay un escalón gratuito de entrada y una vía enterprise cerrada (contacto comercial), lo que encaja con la tesis de coste por asiento que el vault ya maneja en VPN de negocio (ver [[2026-1031-tailscale-docs]] y el contraste con [[2026-1101-tailscale-kb-sin-ninguna-cifra-de-precio-ni-plan]]). Para el trío api + worker + db con presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) la lectura provisional es que **el tailnet de tres nodos cabe holgadamente en el escalón gratuito**, pero eso es una inferencia: la fuente no publica límites de nodos, de usuarios, ni qué funciones van tras "Invite only". La etiqueta "Invite only features" es además la pista de que parte del valor (probablemente PAM, SSO, auditoría) puede quedar fuera del plan gratuito.
