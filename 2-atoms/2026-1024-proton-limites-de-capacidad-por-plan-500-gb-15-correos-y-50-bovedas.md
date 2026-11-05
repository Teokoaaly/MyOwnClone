---
id: 2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas
type: atom
certainty: solid
sources: [sources/2026-10-24-protonvpn-pricing.md]
links: ["[[2026-1024-proton-unlimited-7-99-al-mes-bundle-de-7-productos]]", "[[2026-1024-protonvpn-plus-3-49-al-mes-65-de-descuento]]", "[[2026-1024-protonvpn-plus-incluye-planes-free-de-mail-drive-y-pass]]"]
---

## Claim
La tabla "Compare plans" cuantifica los topes de capacidad del ecosistema Proton en los tres planes (Free / VPN Plus / Proton Unlimited): **Proton Drive** — 5 GB / 5 GB / **500 GB**; **Proton Mail** — 1 / 1 / **15 direcciones de correo**, carpetas y etiquetas 3 / 3 / **ilimitadas**, dominios propios 0 / 0 / **3**; **Proton Pass** — 2 / 2 / **50 bóvedas**, alias Hide-my-email 10 / 10 / **ilimitados**, y en Unlimited se activan **2FA integrado, Dark Web Monitoring, Emergency Access y adjuntos de archivo** (vacíos en los otros dos planes).

## Why It Matters
Es la **tabla de límites que convierte el bundle en un paquete cuantificable**, y es lo que permite poner precio a las partidas que el corpus de hosting del vault nunca ha visto: **$7,99/mes por 500 GB cifrados, 15 buzones y 50 bóvedas de contraseñas**. La asimetría es notable: en Drive el salto es de ×100 (5 GB → 500 GB) y en Pass de ×25 (2 → 50 bóvedas), mientras que **en Mail solo cambia el número de direcciones (1 → 15)** y el resto de los ajustes permanece idéntico entre Free y Plus — es decir, **el bundle paga sobre todo en almacenamiento y en gestor de contraseñas**. Para un producto como el del vault, que ya necesita correo y almacenamiento, esta tabla es la que dice qué parte de la suscripción de $7,99 es realmente red y qué parte es servicios de identidad ([[2026-1024-protonvpn-plus-incluye-planes-free-de-mail-drive-y-pass]]).


## Nota de extensión 2026-10-27
Este átomo da la tabla de límites del ecosistema Proton en consumo y concluye que «el bundle paga sobre todo en **almacenamiento y gestor de contraseñas**», con el salto ×100 en Drive (5 GB → 500 GB) y ×25 en Pass (2 → 50 bóvedas), mientras que en Mail «solo cambia el número de direcciones (1 → 15)». La línea B2B **confirma la lectura y añade la partida que en consumo no existía**: los **15 dominios de correo propios** de Workspace Standard, frente a los **3** del plan Unlimited de consumo ([[2026-1027-proton-business-workspace-standard-1-tb-15-dominios-y-todos-los-productos]]). Es decir: en consumo Proton **cobra por buzones** (15 direcciones, 3 dominios) y en B2B **cobra por dominio** (15 dominios de correo propios) — una diferencia de 5× en la unidad de identidad de correo, que es la partida que en un producto multi-tenant protege la dirección real del tenant. La tabla B2B añade además una escala de almacenamiento **por usuario** que no existe en consumo: **2 GB / 2 GB / 10 GB / 1 TB** en los cuatro planes, con los alias Hide-my-email en **10 / 10 / Unlimited / Unlimited** ([[2026-1027-proton-business-vpn-pass-professional-anade-pass-integrado-alias-y-un-cli]]). Ojo al matiz: en B2B el almacenamiento por usuario **sube con el plan** (2 GB → 1 TB), mientras que en consumo el salto grande es entre Free y Unlimited; es la primera vez que el vault ve la capacidad de nube como **función del asiento y del plan a la vez**.
