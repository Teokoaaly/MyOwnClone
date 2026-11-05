---
id: 2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1031-workos-radar-primeros-1000-checks-gratis]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
**Audit Logs** de WorkOS tiene dos líneas de precio independientes: **streaming de logs a $125/mes por conexión SIEM** ("Per SIEM connection") y **retención de eventos a $99/mes por cada millón de eventos almacenados** ("Per million events stored").

## Why It Matters
Es el add-on que aparece en el RFP de cualquier cliente corporativo regulado, y su precio no es trivial: **$125/mes por destino SIEM** es exactamente el mismo importe que la primera conexión SSO de WorkOS ([[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]), de modo que un cliente con SSO + un SIEM (Splunk, Datadog) + retención ya está en $250/mes antes de un solo asiento de producto. Y la segunda línea es **consumo acumulativo**: los eventos retenidos no son gratis por el hecho de que el producto no los use, así que un cliente con mucha actividad de login genera coste variable de auditoría. Para el modelo de costes por tenant de MyOwnClone ([[2026-1022-costes-por-categoria-tenant]]) la implication es clara: si el producto ofrece auditoría a un tenant corporativo, esa línea debe aparecer como **coste por tenantBytes de auditoría** (con su propio medidor) y no repartirse como overhead de plataforma.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma **las dos líneas sin cambios**: "Log streaming — Per SIEM connection — $125 / mo" y "Event Retention — Per million events stored — $99 / mo". Matiz nuevo: en el volcado crudo estas dos líneas aparecen **bajo el calculador ("Estimate your costs"), no bajo un encabezado "Audit Logs"**, junto a "Custom Domain $99 / mo" y a los bloques de SSO y Directory Sync — es decir, la página presenta el streaming de logs y la retención de eventos como **partidas de coste independientes del paquete de identidad**, no como un módulo de "Audit Logs" con precio propio ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]). Esto refuerza la lectura operativa de este átomo: para un producto que ofrece auditoría a un tenant corporativo, son dos medidores separados ($125/mes por destino SIEM y $99/mes por millón de eventos) que hay que cotizar por separado.

## Nota de verificación
Sección Audit Logs de la captura del 2026-10-31: "Log streaming / Per SIEM connection / $125 / mo" y "Event Retention / Per million events stored / $99 / mo".
