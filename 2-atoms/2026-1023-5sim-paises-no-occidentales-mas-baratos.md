---
id: 2026-1023-5sim-paises-no-occidentales-mas-baratos
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-prices.md]
links: ["[[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]", "[[2026-1023-5sim-europa-occidental-paga-la-factura]]", "[[2026-1022-instancia-como-captador-de-leads]]"]
---

## Claim
El precio más bajo de cada país (el suelo del país, calculado sobre las filas del CSV) se concentra de forma nítida en países fuera del eje occidental: **Colombia $0.1026** (`virtual34`), **Timor Oriental $0.1436**, **Honduras $0.1538**, **Etiopía $0.2026**, **Angola $0.2218** (5.026.356 unidades), **Gabón $0.2564**, **Camerún $0.2692**, **Senegal $0.2756**, **Sierra Leona $0.2923**, **Hungría $0.3013**, **Malaui $0.3051**, **Nigeria $0.3167** y **Ghana $0.3167**. En total, **38 de los 111 países** tienen un suelo ≤ $0.5 y **81 de 111** un suelo ≤ $1. Las diez filas con `rate = -1.0` más baratas (de $0.1026 Colombia a $0.3051 Malaui) son **todas del mismo operador `virtual34`**: el precio más bajo no viene de operadores exóticos sino del operador dominante del catálogo. La columna `rate` es el porcentaje que la página renderiza junto al precio (Lituania aparece como `58.33%`); 41 filas del CSV lo tienen en `-1.0` y 44 en `0.0`, frente a 90 filas con porcentaje positivo.

## Why It Matters
La geografía del precio es una decisión de producto, no un detalle de proveedor: el mismo servicio de verificación cuesta 30–80 veces más en Italia que en Colombia, así que **elegir país es elegir margen**. Si un flujo de captación necesita volumen de identidades verificadas (ver [[2026-1022-instancia-como-captador-de-leads]]), el suelo por país es el número que fija el coste unitario; 38 países por debajo de $0.5 permiten un margen amplio incluso con reintentos. Contrasta con [[2026-1023-5sim-europa-occidental-paga-la-factura]] y con el mínimo global de [[2026-1023-5sim-piso-de-precio-telegram-01026-usd]].
