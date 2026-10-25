---
id: 2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro
type: atom
certainty: solid
sources: [sources/2026-10-24-njal-la-domains-vpn.md]
links: ["[[2026-1024-njal-la-registro-de-dominios-desde-15-euros-con-todas-las-funciones-incluidas]]", "[[2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios]]", "[[2026-1022-dns-superficie-publica-myownclone]]"]
---

## Claim
El bundle de privacidad de `njal.la` no es "privacidad whois" a secas: el registro incluye **DNS anycast** ("from the domain privacy and anycasted DNS to support and email forwarding"), **soporte** y **reenvío de correo electrónico**. La página describe la privacidad como "The most famous privacy protection ever. Ever!" y se autodeclara "**the most trusted privacy provider in the world, with a track record to prove it**". El proveedor **no publica en esta página qué TLDs concretos ofrecen privacidad ni el mecanismo** (proxy de whois, RDAP, titular registral).

## Why It Matters
Esta es la intersección que el vault no tenía: **DNS anycast y registro de dominio en el mismo bundle**, y con un precio único. El vault tenía el DNS anycast **gratuito** en 1984 Hosting (FreeDNS, zonas ilimitadas, DNSSEC automático, 20 años de uptime declarado) pero **sin precio de registro**, y tenía registro con **privacidad whois en los TLD que lo permiten** pero sin cifra ([[2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios]]). `njal.la` ofrece las dos cosas juntas por **€15/año**, lo que permite responder a una pregunta que el vault tenía abierta: **¿cuánto cuesta un dominio con DNS anycast y privacidad whois?** Respuesta con fuente: €15/año, con todo incluido — lo que hace de esta combinación la alternativa más barata medida en el vault para un dominio con resolución anycast.

La operación para MyOwnClone es relevante porque la superficie DNS pública del producto vive hoy confinada a un pool reducido de IPs, con varios subdominios devolviendo 404 ([[2026-1022-dns-superficie-publica-myownclone]]). Delegar resolución y privacidad a un mismo registrador reduce la superficie a **un solo punto de cambio**, y el propio proveedor es quien declara que sus usuarios "are the ones that make us have to go to court to protect them" — es decir, **la privacidad se presenta como el producto central, no como un añadido**.

## [FRICTION]
> [[2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios]] (escrita el 2026-10-24) establece que el DNS anycast **gratuito** de 1984 ofrece "100 % uptime for 20 years" y que el registro de dominios de ese proveedor **no tiene precio publicado**. Este átomo no lo contradice en cifras, pero **le cambia el marco**: si un DNS anycast con privacidad whois cuesta **€15/año** en un bundle único, la comparación relevante no es "1984 regala el DNS" sino **"1984 da DNS anycast gratis pero cobra el registro, mientras njal.la da los dos por 15 euros al año"** — y la cifra de 1984 sigue siendo un dato ausente que impide cerrar la comparación. Marcado para juicio humano, no auto-resuelto: falta la tarifa de registro de 1984.
