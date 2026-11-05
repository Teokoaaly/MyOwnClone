---
id: 2026-1101-digitalocean-facturacion-por-segundo-con-minimo-de-60-segundos
type: atom
certainty: solid
sources: [sources/2026-11-01-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]"]
---

## Claim
Desde el **1 de enero de 2026** DigitalOcean factura los Droplets **por segundo**, con un **mínimo de 60 segundos o $0.01, el mayor de los dos**. Los **Bundled Plans tienen techo mensual** ("you'll never pay more than the flat monthly price for that plan"), mientras que los **v5 Droplets se facturan por las horas realmente usadas y no están topados a 672 horas**.

## Why It Matters
Es el mismo eje de granularidad que el vault ya había medido en Hetzner —$0.0096/h con un mínimo igualmente pequeño— pero aquí la granularidad llega un orden de magnitud más abajo: **el segundo**, lo que habilita el patrón de "trabajo efímero" que la propia página declara como caso de uso ("batch jobs and automated testing"). Para MyOwnClone esto importa en un escenario concreto: si el stack de clon se factura por minuto real de inferencia y el resto del tiempo el servidor está parado, la factura mensual se acerca al **coste variable de la inferencia** y se aleja del **coste fijo de plataforma** que hoy no aparece en ninguna categoría del back-office ([[2026-1022-costes-por-categoria-tenant]]). La distinción con Hetzner es operativa y no cosmética: **Hetzner factura la hora de VM viva ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]); DO facturaría el segundo de Droplet encendido, lo que hace que "apagar el servidor" sea una palanca de coste y no solo de riesgo**.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** conserva **verbatim el banner de facturación por segundo**: "Effective January 1, 2026, we're moving to per-second billing (with a minimum charge of 60 seconds or $0.01, whichever is higher) for Droplets". La redacción es idéntica a la del 11-01 y del 11-02, con un único cambio de formato (las comillas tipográficas del original pasan a apóstrofos rectos por el render). El mínimo de 60 s / $0.01 **queda re-verificado**.

Lo que esta captura **no** re-verifica son las dos reglas que completan el modelo de facturación y que el render del 11-03 sustituye por "…": el **techo mensual de los Bundled Plans** ("you'll never pay more than the flat monthly price for that plan") y la exención de los **v5**, que se facturan por horas realmente usadas y **no están topados a 672 horas**. Ambas siguen sostenidas por las capturas del 11-01 y del 11-02 ([[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]). Ver [[2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5]].

## Nota de verificación
Cifras y reglas transcritas literalmente de la FAQ y del banner de droplets pricing. La captura **no publica** el umbral exacto de facturación ni el prorrateo por segundo en las tablas de precio; solo la regla de mínimo y el topado de los Bundled Plans.
