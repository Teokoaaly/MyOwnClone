---
id: 2026-1027-proton-business-mail-vpn-1-conexion-en-essentials-y-10-en-workspace
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-mail-pricing.md, sources/2026-10-26-proton-business-plans.md]
links: ["[[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]]", "[[2026-1024-proton-unlimited-no-cambia-la-red-pero-cambia-todo-lo-otro]]", "[[2026-1027-proton-business-mail-essentials-es-el-plan-solo-correo-y-calendario]]"]
---

## Claim
La tabla B2B no mide el VPN en **dispositivos**, sino en **"Encrypted VPN connections per user"** y en **"Countries"**: Mail Essentials da **1 conexión cifrada por usuario** y **10 países**; Workspace Standard y Premium dan **10 conexiones cifradas por usuario** y **140 países**. La fila "Countries" es exactamente la misma cifra (140) que la del VPN de consumo, y la captura B2B **no publica ningún número de servidores**. En la tabla de `/business/plans` aparecen además "Central control panel" y "**Stealth protocol**", ambos "Included" en los dos planes Workspace.

## Why It Matters
Es el **cambio de unidad de capacidad entre el consumo y la empresa**: el consumo mide "10 devices at a time" y 20.000+ servidores, la empresa mide **conexiones cifradas por usuario** y solo países. La consecuencia práctica es que **el límite se reparte por persona**: en un equipo de 20 personas con Workspace Standard son 200 conexiones cifradas simultáneas, mientras que con Mail Essentials serían 20 — y el número de servidores deja de ser una cifra citable porque la página no la publica. Para el vault esto importa porque el corpus ya establecía que la unidad del VPN es el dispositivo concurrente ([[2026-1024-protonvpn-diez-dispositivos-y-20000-servidores-en-140-paises]]); en la línea B2B **la unidad correcta es el asiento × conexiones por asiento**, que es otra fórmula de coste y otra partida para un producto multi-tenant. Y el "Stealth protocol" más el "Central control panel" aparecen **solo en la tabla de Workspace**, no en la de Mail Essentials, lo que confirma que el escalón de $6,99 no compra red, sino correo.
