---
id: 2026-1102-digitalocean-ipv4-publico-incluido-en-bundle-y-cobro-separado-en-v5
type: atom
certainty: solid
sources: [sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]", "[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]"]
---

## Claim
En los **Bundled Plans la IPv4 pública viene incluida sin coste adicional** ("For Bundled Plans, a public IPv4 is included at no extra cost"), pero en los **v5 la IPv4 se factura como línea separada** de la configuración v5, con un **precio introductorio de $0.00/hora "sujeto a cambio según los Términos de Servicio"**. La captura también documenta la **Private Droplet**: una VM **sin IPv4 asignada**, "so there's no IPv4 line item on your bill", recomendada para cargas no accesibles desde Internet.

## Why It Matters
Es exactamente la partida que el thread de hosting barato identificó como **coste recurrente oculto** —en Skhron son €0,65/mes por dirección dedicada, en Hetzner el IPv4 primario va a €0,00 ([[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]])— y aquí la regla es **dependiente del tipo de Droplet, no del proveedor**: el bundle lo regala, el v5 lo factura aparte aunque hoy valga $0,00. Dos consecuencias para MyOwnClone: (1) la opción de **Private Droplet sin IPv4** es la palanca que permite que el nodo de inferencia o el worker interno no obliga a pagar dirección pública, algo que importa cuando el presupuesto es de ≤ €4/mes y cada línea recurrente se cuenta; (2) un **precio de $0,00 "sujeto a cambio"** no es un coste cero — es una partida con techo desconocido, y el vault ya tiene el precedente de que las cifras de DO atribuidas por terceros caducan ([[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]).

## 2026-11-03 — re-verificación
La captura del **2026-11-03** **no re-verifica** este átomo: la FAQ "Do Droplets come with a dedicated IP address?" —que es donde están la inclusión de la IPv4 en los Bundled Plans, el cobro separado en v5 a $0.00/hora "sujeto a cambio" y el Private Droplet sin IPv4— ha sido sustituida por "…" en el render reducido. El átomo sigue sosteniéndose por la captura del 2026-11-02. Lo que sí confirma esta captura, indirectamente, es que el **precio de $0.00/hora de la IPv4 en v5 no es un dato de la página de precios de droplets**: es un dato de la FAQ que el render puede no capturar, lo que refuerza la regla de re-verificar contra la documentación del fabricante y no solo contra la página de precios. Ver [[2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5]].

## Nota de verificación
Transcripción literal. La captura **no publica** el precio futuro de la IPv4 en v5 ni el criterio que lo determinará, ni el número máximo de IPv4 por Droplet, ni el precio de las Floating IP (solo menciona que se pueden asignar para alta disponibilidad).
