---
id: 2026-1024-evoxt-ip-management-floating-ip-y-reasignacion
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]"]
---

## Claim
Evoxt ofrece gestión de direcciones IP como función de plataforma: *"Easily swap and reassign IP address between servers. Migrate your production servers and manage your failover clusters at ease. Order additional Floating IP Address to cater your growing business"*. Es decir, la IP se puede **reasignar entre servidores** y se pueden pedir **IP flotantes adicionales** por separado.

## Why It Matters
Responde a una restricción que el vault ya tiene documentada como riesgo operativo: HeroSMS exige que la IP registrada coincida con el país del número y prohíbe registrar varias cuentas desde la misma IP ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]), mientras que el despliegue vivo de [[myownclone]] es un nginx autoalojado en **una sola IP de servidor** ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]). Un proveedor con IP flotante comprable y reasignable es exactamente la pieza que falta para pasar de "una IP fija" a "un pool de IPs" sin rehacer la arquitectura. Ojo al matiz: la captura **no publica el precio de las IP flotantes adicionales**, así que no se puede saber si "additional" significa céntimos o una partida fija mensual — y con un plan base de $2.99 ([[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]) cualquier extra fijo por IP puede elevar el coste real por encima del precio anunciado.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: número máximo de IP flotantes por servidor, precio de cada IP adicional, si hay que devolverlas, ni si la reasignación es instantánea.
