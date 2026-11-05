---
id: 2026-1029-render-sandboxes-pricing
type: atom
certainty: tentative
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
Render Sandboxes (beta) provide isolated microVMs at $0.12 per active CPU hour + memory hourly rates, with a 24-hour maximum session length, 40 GB disk included per sandbox, and snapshot storage available at $0.08/GB per month.

## Why It Matters
The per-hour billing for sandboxes, even when idle (with automatic suspend/resume), creates cost predictability for short-lived testing environments but can become expensive for always-on development workflows. The 24-hour session limit makes sandboxes unsuitable for long-running workloads, directing those toward dedicated compute plans.

## [FRICTION]
> [[2026-1024-proton-captura-con-placeholders-xx-y-tabla-en-neerlandes]] documents that some pricing pages use placeholder pricing ($XX.XX) that prevents immediate cost comparison, creating friction for users evaluating alternatives. Render's published per-hour rates are more concrete, but the memory hourly rate is not published in the capture, leaving a gap in complete cost modeling for workloads that require significant RAM during sandbox execution.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md`. Corrección factual: la tarifa de memoria **sí está publicada** en la captura, como "+$0.038/hour for memory" por GB (2 GB), "+$0.076/hour" (4 GB), "+$0.152/hour" (8 GB) y "+$0.304/hour" (16 GB), siempre sobre "$0.12 / active CPU hour". El texto anterior del bloque [FRICTION] no se modifica; la afirmación queda corregida aquí.

Otros datos verificados: el límite de sesión de 24 horas aplica **solo a Hobby**; Pro y Scale indican "No limit", y la captura añade que los sandboxes "can run up to 30 days on Pro and above". Sandboxes concurrentes por defecto: 100 en Hobby, 1.000 en Pro, hasta 5.000 en Scale bajo petición, 1.000 en Enterprise y hasta 10.000 en Enterprise bajo petición. 40 GB de disco incluidos por sandbox y snapshot storage a $0.08/GB/mes.