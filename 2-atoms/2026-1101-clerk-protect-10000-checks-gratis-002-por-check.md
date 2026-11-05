---
id: 2026-1101-clerk-protect-10000-checks-gratis-002-por-check
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error]]", "[[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]"]
---

## Claim
El add-on **Protect** de Clerk incluye **gratis en todos los planes** la prevención de fuerza bruta (activa por defecto) y las protecciones básicas (captcha, device checks); las **protecciones avanzadas** (rate limits, bloqueo por tipo de red, restricciones por país) están **solo en Business**. Los **protection checks** incluyen **10.000 gratis al mes** y después se cobran **$0,002 por check**, con **precio custom por encima de 1M de checks**.

## Why It Matters
El precio del anti-abuso es **$0,002 por verificación**, es decir, un céntimo de dólar por 10 checks: para MyOwnClone es marginal en términos de euros (1.000 checks al mes = $2), pero su valor real es **técnico, no de precio**: el vault ya registró que la app **no tiene rate limiting** ([[2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error]]) y que el abuse control es hoy manual. El matiz importante para la decisión es de **gating**: la protección avanzada (rate limits, restricciones por país) es exclusiva de Business a **$300/mes o $250/mes anual** — 60x el presupuesto de hosting del vault —, de modo que la opción realista es Clerk Hobby con **captcha + device checks** y 10.000 checks/mes, lo que obliga a medir el volumen real de sign-ins antes de comprometer el plan Business. Para un producto con tenants públicos, esa es una decisión de riesgo que conviene tomarla con el dato de tráfico, no con el precio.

## Nota de verificación
Sección "Protect" y fila "Protection checks" de la captura del 2026-11-01: "10,000 free per month, then $0.002 per check / Custom pricing above 1M checks". La conversión a euros y la comparación con el presupuesto son lectura operativa del átomo.
