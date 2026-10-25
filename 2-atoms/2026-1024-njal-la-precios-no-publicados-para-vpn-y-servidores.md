---
id: 2026-1024-njal-la-precios-no-publicados-para-vpn-y-servidores
type: atom
certainty: solid
sources: [sources/2026-10-24-njal-la-domains-vpn.md]
links: ["[[2026-1024-njal-la-registro-de-dominios-desde-15-euros-con-todas-las-funciones-incluidas]]", "[[2026-1024-njal-la-servidores-con-almacenamiento-distribuido-y-redundante-para-autohospedar]]", "[[2026-1024-njal-la-vpn-wireguard-y-openvpn-con-tunel-cifrado-y-15-anos-de-experiencia]]"]
---

## Claim
En la captura de `njal.la` del 2026-10-24, **la única cifra de precio de todo el catálogo es €15/año de dominios** ("Domain search. Starting at €15 per year"). Ni la **VPN** ni los **servidores** tienen precio publicado: el precio solo aparece en el CTA del buscador de dominios, y las páginas de VPN y de servidores (enlazadas como `/vpn/` y `/servers/`) **no están capturadas**. Tampoco hay SLA, uptime, número de ubicaciones, ancho de banda, especificación de CPU/RAM/disco, ni política de reembolso en ninguna de las tres líneas.

## Why It Matters
Con una sola cifra de tres productos, **`njal.la` es incomparable con el resto del catálogo del vault en todos los ejes que el thread de hosting mide** (precio de entrada, egreso, SLA, specs, cumplimiento). Es el caso más limpio del patrón que el vault ya tiene registrado: HostBrr publica un configurador con seis valores de RAM **sin precio**, HOSTKEY **no publica tabla de VPS**, BuyVM no publica métodos de pago, y ExtraVM tiene un "from" cuyo plan real está agotado ([[2026-1024-extravm-stock-casi-todo-agotado-y-solo-cinco-planes-comprables]]). `njal.la` es el mismo patrón aplicado a **tres productos a la vez**, con la diferencia de que **al menos una de las tres cifras sí es un precio real y cerrado** (dominios desde €15/año).

La consecuencia práctica: **`njal.la` no es un candidato cotizable para el hosting del stack**, pero **sí es un candidato cotizable para la línea de dominio**, y la comparación de esa línea tiene un problema conocido: ni 1984 Hosting ni `njal.la` publican la matriz TLD-a-TLD. Lo que sí se puede afirmar con fuente es el bundle: **privacidad whois + DNS anycast + soporte + reenvío de correo por €15/año**, una combinación que en el resto del vault aparece con partes sueltas.
