---
id: 2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-ip-management-floating-ip-y-reasignacion]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---

## Claim
La cobertura declarada es de **195+ países** con **90M+ IPs** éticos, y el targeting **por país es gratis**: "No extra fee for the country targeting", "Target countries for free", "Free country-targeting" (fila común de las cuatro tablas de precios). El targeting fino —State/City/ZIP/ASN— es de pago: "City, state, ZIP code, and ASN targeting are offered for a small extra fee" y "advanced options such as city, state, ASN, and ZIP are available at a small extra fee", salvo en Premium Residential donde "All targeting options included". La página de localizaciones publica el número de IPs por país, con los doce primeros: India **2 374 712**, Brasil **1 252 375**, Marruecos **1 234 810**, Arabia Saudí **829 325**, Argelia **783 817**, Uruguay **759 498**, Turquía **676 335**, Pakistán **674 254**,Vietnam **662 872**, México **646 937**, Egipto **540 746**, EE. UU. **533 615**. El FAQ añade un detalle de implementación: "Target location is a URL parameter, so you don't need a separate dashboard setting for each location."

## Why It Matters
El dato duro que sale de la tabla de países es que **el pool no es uniforme**: India, Brasil y Marruecos tienen entre 2 y 4 veces más IPs que EE. UU. (533 615). Eso significa que "una IP por cuenta en un país dado" es barato en unos países y caro en otros, y que elegir país no es solo una condición de la verificación SMS sino una palanca de coste del proxy.
Y el caso de uso declarado que más conecta con el vault es el de **tracking de citas en respuestas de IA**: "Query ChatGPT, Perplexity, and Google AI Overviews at scale from real IPs to monitor citations and AI-search visibility" — exactamente el botón que el vault necesita para saber si sus clones aparecen en las respuestas de los LLM, un ángulo que ningún otro átomo del vault cubre todavía.

## Nota de verificación
Cifras de IPs transcritas literalmente de la sección "Locations". La captura **no** publica: el precio del targeting fino por estado/ciudad/ZIP/ASN, ni el número de IPs por ciudad dentro de cada país.


## Nota de extensión 2026-10-27
**El pool móvil es un segundo pool con su propia geografía, y no coincide con el residencial.** La página móvil publica su propio top-12 con número de IPs por país: India **1 244 618**, Arabia Saudí **546 940**, Italia **204 038**, Marruecos **176 647**, Argelia **142 073**, Irán **123 768**, Estados Unidos **122 971**, Kazajistán **119 723**, Uruguay **96 054**, Pakistán **89 226**, Angola **81 030**, Chile **79 849**. Los cuatro países **compartidos** con el top-12 residencial son India, Arabia Saudí, Marruecos y Argelia; **Brasil, México, Turquía, Vietnam y Egipto no aparecen** en el top-12 móvil, y el móvil incorpora Italia, Irán, Kazajistán, Chile y Angola. Uruguay cae de 759 498 (6.º residencial) a 96 054 (9.º móvil). Es decir: **la geografía de stock del móvil es un mapa distinto**, y "cuántas IPs hay en el país X" **depende del pool** — un matiz que este átomo, al presentar el desglose como único, deja sin cubrir. Ver [[2026-1027-dataimpulse-pool-movil-16m-con-geografia-propia]].
La página móvil confirma además el **targeting por país incluido en el precio** ("Country targeting is already included in the price", "$0 country-targeting", "Free country-targeting") y añade una fila de targeting fino ausente de la home: **"NEW State/City/Zip/ASN Targeting"**, con la tabla comparativa matizando que **City ✓*, ASN ✓*, ZIP ✓* con "*extra costs"** — es decir, en el móvil el country va gratis y **el targeting fino tiene coste**, igual que en el resto de pools salvo el premium residencial. Átomos nuevos: [[2026-1027-dataimpulse-tabla-comparativa-con-el-promedio-movil]].
Nota de verificación de esta extensión: la captura móvil **no** publica el precio del targeting fino por estado/ciudad/ZIP/ASN, ni el número de IPs por ciudad dentro de cada país.
