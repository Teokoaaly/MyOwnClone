---
id: 2026-1027-7sim-masked-number-format
type: atom
certainty: solid
sources: [sources/2026-10-27-7sim.md]
links: ["[[2026-1027-7sim-sms-receiving-service]]", "[[2026-1027-7sim-country-coverage]]"]
---

## Claim

7sim.org muestra números de teléfono con formato enmascarado +XX****XXXX, donde solo los últimos 4 dígitos son visibles públicamente, ocultando la mayor parte del número para privacidad.

## Why It Matters

El formato enmascarado equilibra utilidad y privacidad: suficientes dígitos para que el SMS llegue y sea visible, pero suficiente ocultamiento para evitar exposición accidental del número completo. Este diseño es relevante para el vault's trabajo con números de teléfono en flujos de verificación y proxies, donde se necesita visibilidad parcial sin compromiso completo del número.

## [FRICTION]

> Ningún átomo existente en el vault discute el formato enmascarado. Si surge un conflicto futuro sobre la retención de números o su uso en servicios que requieren números completos, este bloque será revisado.