---
id: 2026-1023-hetzner-regiones-y-zonas-de-disponibilidad
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-10-23-evoxt-vms.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]"]
---

## Claim
La calculadora ofrece como **Availability Zone** cinco opciones: **HEL1 (FIN)**, **FSN1 (GER)**, **NBG1 (GER)**, **HEL1 (FIN)** y **SIN (SG)**. La página de ubicaciones declara que los servidores cloud están disponibles en **Alemania, Finlandia, Singapore y los USA**, con parques de datacenter propios en **Falkenstein, Nuremberg y Helsinki** (Europa), **Hillsboro (Oregon) y Ashburn (Virginia)** (Norteamérica) y **Singapore desde 2024** (Asia).

## Why It Matters
La zona no es un detalle técnico sino una decisión de coste y de cumplimiento: el recargo de **€1.00 por TB adicional está declarado para la UE**, así que elegir una zona fuera de la UE puede cambiar la partida de egreso ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]). Y para un producto que opera en español y con registro global de eventos, la latencia hacia el usuario europeo y la jurisdicción del dato importan: la página sitúa la operación bajo GDPR con certificación ISO/IEC 27001 en los parques de Alemania y Finlandia, lo que hace de FSN1/NBG1/HEL1 la elección natural si el almacenamiento y el cómputo deben quedar en la UE y con respaldo europeo.

## Nota de verificación
La captura no publica precios de servidor por zona (la calculadora muestra el mismo precio base en las cinco), ni qué zona aplica un recargo de tráfico distinto. La lista de Availability Zones incluye HEL1 dos veces, tal como aparece transcrita en la página.

## [NOTA 2026-10-24 — Evoxt]
Fuente: `sources/2026-10-23-evoxt-vms.md`. Contraste de dispersión geográfica: Evoxt declara **17 regiones** con un IX distinto en cada una (Los Angeles, Montreal, Nueva York, São Paulo, Londres, París, Ámsterdam, Fráncfort, Varsovia, Zúrich, Kuala Lumpur, Yakarta, Sídney, Hong Kong, Seúl, Osaka, Tokio) frente a las **5 zonas / 4 países** de Hetzner, y ofrece como argumento de privacidad **Zúrich** ("país políticamente neutral con leyes de privacidad fuertes"), que es el tipo de ubicación que este átomo concluye necesaria si el dato debe quedar en una jurisdicción defendible. El coste de esa dispersión no está publicado: la captura no indica qué regiones tienen capacidad ni si el precio varía por región (ver [[2026-1024-evoxt-17-regiones-con-peering-de-ix]]).
