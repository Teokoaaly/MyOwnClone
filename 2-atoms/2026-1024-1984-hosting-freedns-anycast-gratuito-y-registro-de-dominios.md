---
id: 2026-1024-1984-hosting-freedns-anycast-gratuito-y-registro-de-dominios
type: atom
certainty: solid
sources: [sources/2026-10-24-1984-hosting-vps.md]
links: ["[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]", "[[2026-1024-1984-hosting-web-hosting-y-wordpress-security-pack]]"]
---

## Claim
1984 Hosting ofrece **FreeDNS**, un servicio DNS Anycast gratuito con: "100 % uptime for 20 years", **zonas ilimitadas** ("as many zones as you like, no limits"), **gestión automática de DNSSEC**, redirecciones web, **historial de zona y opción de restore**, y la posibilidad de **usar el propio master y servir FreeDNS como secundario o backup** de nameservers. La frase del proveedor es explícita: "Free as in freedom and free as in gratis". Además ofrece **registro y traspaso de dominios**, con **privacidad whois** en los TLD que lo permiten.

## Why It Matters
Es la pieza del catálogo de 1984 que **el vault no tenía en ninguna otra fuente**: un DNS Anycast gratuito con DNSSEC automático, historial de zona y la opción de **servir el propio master con FreeDNS como secundario**. Esa última es la característica con consecuencia operativa: **el failover de nameservers pasa a ser un asunto del cliente, sin coste adicional**, lo que elimina la dependencia de un solo proveedor de DNS para la resolución de un dominio propio. Para un producto SaaS multi-tenant, donde la superficie DNS pública está hoy confinada a un pool reducido de IPs y varios subdominios devuelven 404 ([[2026-1022-dns-superficie-publica-myownclone]]), **delegar la resolución a un Anycast con 20 años de uptime declarado y con secundario propio** es un mecanismo de continuidad que no requiere SLA de hosting.

El "100 % uptime for 20 years" es, eso sí, **un claim sin SLA**: ninguna cifra de uptime, ni en este ni en ningún otro proveedor del vault, viene con un documento de créditos salvo Skhron y Hetzner. La captura tampoco publica el precio del registro de dominios —solo remite a una página de precios externa— ni el detalle de la privacidad whois por TLD.

## Nota de verificación
La captura no publica SLA de FreeDNS, ni el número de servidores Anycast, ni el precio de los dominios, ni los TLD concretos que ofrecen privacidad whois.

## Nota fechada — 2026-10-24 (captura `sources/2026-10-24-njal-la-domains-vpn.md`)

Contrapunto de precio, sin modificar lo anterior: **`njal.la` sí publica una tarifa de registro con las funciones incluidas** — "Domain search. Starting at **€15 per year**", "We don't do annoying package pricing. We include all features in all registrations - from the domain privacy and anycasted DNS to support and email forwarding" ([[2026-1024-njal-la-registro-de-dominios-desde-15-euros-con-todas-las-funciones-incluidas]], [[2026-1024-njal-la-privacidad-whois-y-dns-anycast-incluidos-en-el-registro]]). Es decir: la comparación que este átomo dejaba abierta —**¿cuánto cuesta un dominio con privacidad whois y DNS anycast?**— tiene ahora una referencia de **€15/año con todo incluido**, mientras la tarifa de registro de 1984 **sigue sin publicarse**. Esto no cambia el claim de 1984 (FreeDNS es gratuito y con 20 años de uptime declarado); añade que **la comparación absoluta sigue sin poder cerrarse** hasta que 1984 publique su tarifa de registro, y que el bundle equivalente en `njal.la` cuesta €15/año.
