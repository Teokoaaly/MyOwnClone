---
id: 2026-1026-ivpn-cinco-dispositivos-en-standard-y-plus-diez-en-pro-suite
type: atom
certainty: solid
sources: [sources/2026-10-25-ivpn-pricing.md]
links: ["[[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]]", "[[2026-1024-mullvad-cinco-dispositivos-por-cuenta-y-sin-port-forwarding]]", "[[2026-1026-ivpn-nueve-precios-en-tres-niveles-y-tres-periodicidades]]"]
---

## Claim
IVPN reparte el límite de dispositivos **por nivel, no por precio**: **Standard** y **Plus** son «IVPN / **5 Devices**» y solo **Pro Suite** sube a «IVPN / **10 Devices**» (a $10/mes, $4/semana o $100/año). El precio por dispositivo implícito no es proporcional: en la modalidad mensual, Standard cuesta **$1,20** por dispositivo/mes, Plus **$1,60** y Pro Suite **$1,00** — es decir, **duplicar el tope de dispositivos (5 → 10) cuesta solo un 66,7 % más** ($6 → $10), y la diferencia restante son servicios anexos (modDNS, Mailx, Portmaster Pro).

## Why It Matters
Es el **tercer régimen de límite de dispositivos** del corpus de privacidad por suscripción, y es el primero que **desacopla capacidad y precio de forma explícita**: en Mullvad el tope de 5 es un límite de capacidad declarado que el precio plano no compra ([[2026-1024-mullvad-cinco-dispositivos-por-cuenta-y-sin-port-forwarding]]); en Proton los 10 dispositivos son una prestación del plan, con la misma cifra en Plus y Unlimited ([[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]]); aquí los 5 dispositivos vienen en dos niveles con precios distintos ($6 y $8) y los 10 solo en el tercero. La consecuencia práctica para el vault es que **el dispositivo simultáneo se comporta como un tope de segmentación, no como el recurso que se compra**: si el criterio de elección del proveedor fuera "coste por dispositivo", el ranking sería Pro Suite primero ($1,00/dispositivo) y Plus el peor ($1,60), mientras que si el criterio es "cuántos dispositivos concurrentes necesito" Standard y Plus ya cubren cinco a un precio menor.

## [FRICTION]
> [[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]] (escrita el 2026-10-24) sostiene que "la **unidad de capacidad del VPN es el número de dispositivos simultáneos, no el tráfico**: 10 dispositivos es el 'recurso' que se compra con la suscripción, el equivalente funcional del vCPU en un VPS", y de ahí deduce que la comparación de precio con el hosting debe hacerse sobre esa base.
> Este átomo presiona eso porque en IVPN el número de dispositivos **no funciona como recurso comprado**: los mismos 5 dispositivos se compran a dos precios distintos ($6 y $8) y el doble de dispositivos cuesta un 66,7 % más, no el 100 %. O la unidad de capacidad del VPN es el **dispositivo simultáneo** y entonces el precio marginal del dispositivo no debería ser plano en ningún proveedor del corpus, o la analogía con el vCPU del VPS se rompe porque en el VPN el tope es un **segmento de plan** y no una cantidad escalar.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto: la captura no publica qué ocurre al superar el tope (se bloquea, se factura extra, se avisa) ni qué servicios anexos explica exactamente el escalón de $10.
