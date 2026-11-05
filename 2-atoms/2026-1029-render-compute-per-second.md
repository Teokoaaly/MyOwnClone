---
id: 2026-1029-render-compute-per-second
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
Render charges compute on a per-second basis, prorating billing to the second for all active services including Cron Jobs and Workflows, meaning users only pay for compute when services are actually running.

## Why It Matters
This granular billing model differs from competitors that charge hourly or monthly minimum commitments, providing cost efficiency for workloads with variable or short-lived compute needs, such as intermittent batch processing, development environments, or bursty AI inference workloads that would incur unnecessary costs under hourly pricing.

## [FRICTION]
> [[2026-1022-live-verify-alta-y-precios-ya-publicos]] notes that clone services often charge flat monthly fees regardless of actual usage, creating a belief that per-second billing is universally superior. However, for consistently running 24/7 services, the per-second model can accumulate to higher costs than a fixed monthly plan, and users must calculate their own break-even point between hourly minimums and second-precision metering.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md`: la captura confirma los tres puntos del claim —los planes de cómputo se fijan por servicio, el prorrateo es al segundo y Cron Jobs y Workflows solo se facturan mientras ejecutan la carga. Matiz nuevo: la tabla de precios de Cron Jobs se expresa en **$/minuto** ($0,00016/min a $0,02315/min), lo que choca con la formulación "prorated by the second" de la página; la discrepancia queda registrada en [[2026-1029-render-cron-por-minuto]]. La FAQ añade un dato útil para el TCO: si un workspace no tiene servicios (vivos ni suspendidos) ni actividad durante un mes, la cuota de suscripción de ese mes no se cobra.