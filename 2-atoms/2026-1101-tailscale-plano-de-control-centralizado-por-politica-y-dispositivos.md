---
id: 2026-1101-tailscale-plano-de-control-centralizado-por-politica-y-dispositivos
type: atom
certainty: tentative
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-myclone-access-control-por-persona]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---

## Claim
La organización de la documentación de Tailscale revela un **plano de control centralizado por tailnet**, no por servicio: "Manage your tailnet" agrupa "Manage access" (administrar el acceso a los recursos de Tailscale), "Manage users" (invitar usuarios, asignar o cambiar roles) y "Manage your organization" (cuenta, planes, nombre de tailnet y dominio); dentro de "Manage Access" están "Manage access control", "Manage just-in-time access", "Manage devices", "Manage users" y "Tailnet Lock"; y la configuración se materializa en **un único fichero de política** ("Tailnet policy file syntax") del que hay ejemplos separados de ACL y de grants. La documentación ofrece además "Set up an identity provider" para SSO externo.

## Why It Matters
Es la diferencia de arquitectura que decide si Tailscale sirve al trío api + worker + db: un plano de control único significa que **la política de red se audita en un sitio**, mientras que el control de acceso de negocio por tenant sigue quedando en la app (Flask/Next.js, dos repos, ver [[2026-1022-myownclone-dos-repos-flask-nextjs]] y [[2026-1022-myclone-access-control-por-persona]]). El vault no puede deducir de esta captura cómo se autentica cada nodo del tailnet (auth key, OIDC, tags), porque esas páginas no están capturadas: de ahí `certainty: tentative`. El valor de la captura es más bien **de mapa de superficie**: nombra las nueve páginas que gobiernan acceso y dispositivos, que es exactamente el checklist que hay que revisar antes de exponer cualquier servicio a una red de terceros.
