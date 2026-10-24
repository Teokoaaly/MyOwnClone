---
id: 2026-1024-skhron-smtp-25-tcp-inbound-sin-restriccion
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]", "[[2026-1024-skhron-kvm-root-y-iso-personalizada-en-minutos]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
Skhron abre el **puerto 25/tcp entrante sin restricción**: "Unlike some providers we have unconditionally unrestricted inbound 25/tcp port for your SMTP server hosting needs. Please note that **outgoing 25/tcp is restricted** due to strict anti-spam policies, which are covered in our Terms of Service."

## Why It Matters
Distinción importante para cualquier producto que necesite enviar correo desde su propio dominio: Skhron es un proveedor de **hosting de servidor SMTP de entrada**, no de envío. Para MyOwnClone, que es es-first y gestiona alta de tenants con correo ([[2026-1022-i18n-es-first-jurisdiccion-es]]), esto significa que el envío saliente seguiría dependiendo de un servicio transaccional externo mientras que la recepción de correo propio sí puede alojarse en el VPS con root. Es también un ejemplo del patrón del vault: la fuente declara explícitamente la **asimetría** en lugar de un "SMTP permitido" genérico, lo que evita el error de leer "mail permitido" como "mail saliente permitido".
