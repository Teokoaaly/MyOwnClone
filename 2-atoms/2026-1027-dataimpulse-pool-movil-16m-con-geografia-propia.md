---
id: 2026-1027-dataimpulse-pool-movil-16m-con-geografia-propia
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-mobile-proxies.md, sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]", "[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]", "[[2026-1023-5sim-catalogo-desviado-hacia-india-y-asia]]", "[[2026-1027-dataimpulse-tabla-comparativa-con-el-promedio-movil]]"]
---

## Claim
La página de proxies **móviles** de DataImpulse da por primera vez el pool móvil con cifras: **"over 16 million ethically-sourced mobile IP addresses"**, **"3G/4G/5G/LTE networks. 195 countries"**, y en el bloque Key Facts **"Dataimpulse.com maintains a pool of over 16 million carrier IPs in 195 countries"**, con el desglose por país: India **1 244 618**, Arabia Saudí **546 940**, Italia **204 038**, Marruecos **176 647**, Argelia **142 073**, Irán **123 768**, Estados Unidos **122 971**, Kazajistán **119 723**, Uruguay **96 054**, Pakistán **89 226**, Angola **81 030**, Chile **79 849**. La misma página separa el pool móvil del residencial en el FAQ: **"DataImpulse offers 16 million mobile IPs at $2/GB"** frente a **"DataImpulse offers 90 million IPs at $1/GB"** (residencial), y **"With DataImpulse, these proxy types are available under one user account"**.

## Why It Matters
El pool móvil **no es un subconjunto geography-neutral del residencial**: tiene su propio ranking y **no coincide con el del pool residencial**. El top-12 residencial (India 2 374 712, Brasil 1 252 375, Marruecos 1 234 810, Arabia Saudí 829 325, Argelia 783 817, Uruguay 759 498, Turquía 676 335, Pakistán 674 254, Vietnam 662 872, México 646 937, Egipto 540 746, EE.UU. 533 615) y el top-12 móvil comparten **cuatro** países —India, Arabia Saudí, Marruecos, Argelia— y divergen en los otros ocho: **Brasil, México, Turquía, Vietnam y Egipto no aparecen en el top-12 móvil**, mientras el móvil incorpora **Italia, Irán, Kazajistán, Chile y Angola**. Uruguay cae de 759 498 (6.º residencial) a 96 054 (9.º móvil). Es decir: **elegir pool cambia el mapa de países disponibles**, y por tanto el margen de precios y de stock por país que el vault tenía anotado ([[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]).
El otro dato duro es de escala relativa: **16 M móviles frente a 90 M residenciales**, con el móvil al doble de precio por GB. El móvil es ~1/5,6 del residencial y es el pool que el vault **no tenía cotizado con cifras** — y el que coincide con el sesgo de catálogo que 5sim ya tenía registrado (India y el sudeste Asiático, [[2026-1023-5sim-catalogo-desviado-hacia-india-y-asia]]): elegir India como país de destino es la intersección de mayor stock en ambas capas de proveedor.

## [FRICTION]
> [[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]] afirma que "La cobertura declarada es de **195+ países** con **90M+ IPs** éticos" y presenta el desglose por país como **la** cobertura del proveedor, con India 2 374 712, Brasil 1 252 375 y Marruecos 1 234 810 al frente.
> Este átomo **divide esa cifra en dos pools que el átomo viejo trataba como uno**: los 90M+ son **residenciales** ($1/GB) y los 16M son **móviles** ($2/GB), con **rankings por país distintos**. O la cifra de "90M+ IPs" del átomo viejo era una cifra total sin desglose (y entonces el total real es ~106M), o era solo residencial y el móvil estaba sin cotizar; la lectura "India tiene 2,37 M de IPs, luego India es el país con más IPs" **no vale para el pool móvil**, donde India tiene 1 244 618.
> Ambas no pueden ser completamente correctas: o la cobertura de 195 países se lee como un único pool uniforme, o hay **dos geografías** con dos rankings y dos precios, y cualquier cálculo de "cuántas IPs hay en el país X" debe declarar para qué pool. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Cifras transcritas literalmente de la sección "Top Mobile Proxies locations" y del FAQ "What is the main difference between mobile and residential proxies?". La captura **no** publica: el número de IPs por ciudad dentro de cada país, la fecha de actualización del desglose, ni si el pool móvil es también first-party con consentimiento (la home sí lo afirma para el residencial).
