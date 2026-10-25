---
id: 2026-1024-alexhost-nueve-ubicaciones-sin-ping-ni-ficha
type: atom
certainty: solid
sources: [sources/2026-10-24-alexhost-home.md]
links: ["[[2026-1024-alexhost-dos-cifras-de-ddos-y-dos-de-ancho-de-banda]]", "[[2026-1024-anubiz-doce-ubicaciones-declaradas-frente-a-diez-prometidas]]", "[[2026-1024-hostkey-catorce-datacenters-europa-y-norteamerica]]", "[[2026-1024-alexhost-datacenter-propio-en-chisinau-soterrado]]"]
---

## Claim
El selector "Choose Location" de la home ofrece **nueve ubicaciones**: **MD** (Moldavia), **NL** (Países Bajos), **SE** (Suecia), **BG** (Bulgaria), **CH** (Suiza), **FR** (Francia), **EN** (Inglaterra), **RO** (Rumanía) y **US** (Estados Unidos). Las nueve aparecen como **"Online"** y las nueve muestran **"Ping:—"** (sin espacio y con guion largo), es decir, **ninguna publica latencia medida**. No hay ninguna ficha técnica por ubicación: **ni ASN, ni Test IP, ni dirección, ni precios por ubicación**, ni capacidad por nodo. Detalle de implementación: **ocho de las nueve banderas se sirven desde la ruta `img/dmca/icons/`** (moldova.svg, netherlands.svg, sweden.svg, bulgaria.svg, switzerland.svg, france.svg, england.svg, romania.svg), pero **la de Estados Unidos sale de otra ruta**, `img/icons/usa.svg` — es la única del grupo que no comparte el prefijo heredado. **Ninguna de las nueve tiene texto descriptivo**: cada una se reduce a la bandera, el código, la palabra "Online" y el ping vacío. Justo debajo del selector hay un **conmutador de periodo de facturación** ("1 month / 1 mon. / 3 months / 3 mon. / 6 months / 6 mon. / Yearly / Year"), que es la única pieza de interfaz operativa de la zona.

## Why It Matters
Es el caso más débil de la regla que el thread de hosting barato ya formuló: **"el número de ubicaciones no es una unidad comparable"** ([[2026-1024-anubiz-doce-ubicaciones-declaradas-frente-a-diez-prometidas]], [[2026-1024-hostkey-catorce-datacenters-europa-y-norteamerica]]). AlexHost publica **nueve banderas** y ninguna de ellas tiene ficha; no hay ni un solo dato de red verificable. Y la composición es **europea antes que otra cosa**: de las nueve, **cinco son estados miembros de la UE** (NL, SE, BG, FR, RO), una es del EEE pero no de la UE (**CH**, Suiza), una es el **Reino Unido** (EN, fuera de la UE y del EEE desde 2021), y solo dos quedan fuera de Europa: **Moldavia (MD)** y **Estados Unidos (US)**. Para un producto que busca un proveedor de baja fricción jurídica, esta lista no es "offshore" — es lo contrario.

El detalle fino que el vault debe registrar: el ping aparece literalmente como **"—"**, el símbolo de dato ausente, en las nueve. Ningún otro proveedor del thread publica el ping como vacío; lo publican vacío solo cuando el campo existe y no se ha rellenado. Aquí el propio interfaz **tiene el campo y no lo rellena**, lo que es una pista de que la medición existe en el backend pero no se muestra — o de que nunca existió.

## Nota de verificación
La captura **no** aclara si las ocho ubicaciones no moldavas son centros de datos propios, reventa de terceros o zonas de presencia sobre proveedores externos; el texto de "Why Choose Us" solo describe el datacenter propio de Chisinau. Tampoco hay precios diferenciados por ubicación: los importes de VPS y hosting son únicos, lo que deja abierto si el precio cambia al cambiar la bandera (el patrón de Anubiz, [[2026-1024-anubiz-el-mismo-plan-cuesta-segun-la-jurisdiccion]]). El único artefacto que se puede consultar para resolver la duda es el **Looking Glass** (`lg.alexhost.com`), enlazado pero no capturado.
