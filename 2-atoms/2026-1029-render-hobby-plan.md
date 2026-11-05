---
id: 2026-1029-render-hobby-plan
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
The Hobby plan at $0/mo provides free compute for personal projects with significant limitations: 512 MB RAM, 1 CPU, 5 GB bandwidth, and no custom domains or firewall, suitable only for prototypes and exploration.

## Why It Matters
The $0 entry barrier lowers the cost of experimentatio for individuals and small teams, but the strict resource limits (512 MB RAM, 1 CPU) and absence of production features (no custom domains, no firewall, no DDoS mitigation) create a hard ceiling between personal projects and production deployment, pushing users toward the Pro plan once prototypes validate.

## [FRICTION]
> [[2026-1022-myclone-limites-plan-free]] asserts that free-tier limits are the primary barrier for user adoption of SaaS tools. The Hobby plan's 512 MB RAM limit is more restrictive than myownclone's free tier, which permits larger baseline resources, creating tension for users whose prototypes outgrow Hobby's constraints before they can justify Pro's $25/mo cost.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md` (captura cruda archivada el 2026-11-03). La lista verbatim de features de Hobby en la captura es: "Connect your repo, and go", "Deploy up to 25 services", "5 GB of bandwidth included", "Single-service previews", "Global regions & CDN", "Custom domains", "Firewall & DDoS mitigation", "Database PITR", "Chat support".

Nota: el claim de este átomo sobre "no custom domains or firewall" **no coincide** con la captura, que sí lista "Custom domains" y "Firewall & DDoS mitigation" en Hobby, y la tabla de features da 2 dominios custom incluidos y mitigación automática de DDoS en Hobby. El texto existente no se modifica (regla del vault: nunca sobrescribir una creencia previa); la discrepancia queda registrada en [[2026-1029-render-planes-pro-scale]].

Otros límites de Hobby verificados en la captura: 1 asiento de equipo, 2 entornos por proyecto, 1 workspace, log retention de 7 días, ventana de PITR de 3 días, 500 min/mes de build pipeline, sin escalado horizontal (la tabla lo marca con "—"), sin IPs dedicadas y sin AWS private links. La captura archivada en `0-raw/archive/2026-11-03-2026-10-29-render-pricing.md` es solo un stub que apunta a `sources/2026-10-29-render-pricing.md`.