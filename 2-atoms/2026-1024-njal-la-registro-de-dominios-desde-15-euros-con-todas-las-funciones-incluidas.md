---
id: 2026-1024-njal-la-registro-de-dominios-desde-15-euros-con-todas-las-funciones-incluidas
type: atom
certainty: solid
sources: [sources/2026-10-24-njal-la-domains-vpn.md]
links: ["[[2026-1024-njal-la-precios-unicos-por-tld-sin-paquetes-ni-scalones]]", "[[2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro]]", "[[2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios]]"]
---

## Claim
`njal.la` ofrece **registro de dominios desde €15 por año**, con una política de precio opuesta a la del mercado: **no hay precios por paquete** — "We don't do annoying package pricing. We include all features in all registrations". Todos los registros incluyen, sin coste adicional, **privacidad de dominio, DNS anycast, soporte y reenvío de correo**. El precio depende únicamente del TLD ("Pricing starts at €15 per year depending on the top level domain"), y la página afirma soportar "most" TLD con la intención de añadir más.

## Why It Matters
El vault ya tenía un dato de **registro de dominios sin precio publicado**: 1984 Hosting ofrece "registro y traspaso de dominios, con privacidad whois en los TLD que lo permiten" pero **sin publicar la tarifa** ([[2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios]]). `njal.la` es la **primera cifra de precio de registro de dominio con privacidad whois incluida** que el vault puede contrastar, y además rompe la convención de escalones: **una sola cifra de entrada, sin tiers ni paquetes**, lo que hace el coste de un dominio determinable sin simular tres carritos.

Consecuencia operativa para el stack del vault: **€15/año es una partida fija, no marginal** — 1,25 €/mes, un 31 % del techo de ≤ €4/mes del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y, sobre un plan base de 99 al mes, un 1,26 % con un solo tenant. Es decir: **el dominio es de las pocas líneas que el presupuesto de infraestructura no puede absorber, porque no escala con el número de tenants** — un tenant más no añade dominios. Y el bundle de funciones (privacidad + DNS anycast + reenvío de correo) elimina tres líneas de coste independientes que en otros proveedores son add-ons separados.
