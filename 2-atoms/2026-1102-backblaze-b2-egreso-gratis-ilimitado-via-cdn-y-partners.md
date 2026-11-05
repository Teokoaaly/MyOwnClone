---
id: 2026-1102-backblaze-b2-egreso-gratis-ilimitado-via-cdn-y-partners
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
Backblaze B2 ofrece **egreso gratuito ilimitado** cuando la descarga se hace "to or through partner content delivery networks (CDNs) and compute services, including **Fastly, Cloudflare, bunny.net, CacheFly, CoreWeave, Equinix Metal, Vultr, and phoenixNAP**"; el bloque de "Free 3x monthly egress" añade que el egreso por encima de 3× el almacenamiento medio "is also free through many CDN and compute partners; otherwise, overage is billed at $0.01 per GB".

## Why It Matters
Es la puerta de salida más relevante para el vault, porque **Cloudflare está en la lista de partners**: una copia de B2 servida a través de Cloudflare no paga el $0.01/GB, lo que hace que B2 + Cloudflare sea una combinación que elimina la penalización de egreso documentada en [[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]] y compite con el "no egress fees" de [[2026-1031-cloudflare-r2-storage]] sin renunciar al almacenamiento más barato. El caso de uso concreto es la distribución de artefactos pesados del producto (clones generados, exportaciones) o el saque de un backup grande durante un incidente sin que la factura de egreso salga del control. El matiz que hay que retener: la exención depende del **socio y del canal** de descarga, no del cliente — una descarga directa desde la API de B2 sigue entrando en la bolsa 3× y luego en el overage.

## 2026-11-03 — re-verificación
La FAQ de egreso se re-verifica **con la misma lista de partners**: "Backblaze B2 offers unlimited free egress when downloading to or through partner content delivery networks (CDNs) and compute services, including **Fastly, Cloudflare, bunny.net, CacheFly, CoreWeave, Equinix Metal, Vultr, and phoenixNAP**. Additionally, B2 Overdrive includes unlimited free egress to any destinations". CoreWeave aparece, por tanto, **como partner de egreso** además de como contraparte del acuerdo multi-exabyte del banner (ver [[2026-1103-backblaze-b2-anuncio-multiexabyte-con-coreweave]]).

**Lo que no aparece en esta captura**: la viñeta de los fundamentos "Egress above 3x monthly average storage is also free through many CDN and compute partners; otherwise, overage is billed at $0.01 per GB", presente en el 11-01 y el 11-02. La FAQ conserva la lista completa de partners, por lo que la afirmación de este átomo **queda re-verificada por la FAQ** pese a la pérdida de la viñeta (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).

## Actualización 2026-11-04 — la viñeta de partners vuelve a renderizarse
La quinta captura (render completo, 1.228 palabras) **restaura** la viñeta de fundamentos que el 11-03 no renderizaba: "Egress above 3x monthly average storage is **also free through many CDN and compute partners**; otherwise, overage is billed at **$0.01 per GB**", además de la FAQ con la lista completa de partners (Fastly, Cloudflare, bunny.net, CacheFly, CoreWeave, Equinix Metal, Vultr, phoenixNAP) y del enlace de detalle de tarifas de API. La afirmación de este átomo queda por tanto **re-verificada en bloque y no solo por la FAQ** (véase [[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]).
