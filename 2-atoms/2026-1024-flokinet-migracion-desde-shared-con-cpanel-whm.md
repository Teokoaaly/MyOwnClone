---
id: 2026-1024-flokinet-migracion-desde-shared-con-cpanel-whm
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-hostbrr-cpanel-reseller-5-00-white-label-blesta-whmcs]]", "[[2026-1024-buyvm-directadmin-gratuito-con-licencia-restringida-a-sus-ips]]", "[[2026-1024-flokinet-nombres-servidor-ns1-a-ns4-y-panel-de-dns]]", "[[2026-1024-flokinet-ubicaciones-offshore-ripe-e-isnic]]"]
---

## Claim
FlokiNET declara ser **CPanel Authorized Partner** y su FAQ de migración **desde shared hosting** es explícita: *"we generally recommend that you install CPanel/WHM on your VPS/Dedicated Server (license not included by default). With this application running, FlokiNET's support team will be able to export your shared hosting account in its entirety and import it into your server in a matter of minutes"*, con asistencia del equipo en cada paso. **Sin CPanel**, la migración es enteramente manual y **sin asistencia**. Como alternativas a CPanel, cita **Webuzo, Plesk, DirectAdmin, ISPmanager y Virtualmin**, con "support for migrating to these platforms is limited". En sentido inverso, migrar **de** VPS/Dedicated **a** shared hosting con CPanel sí tiene asistencia; sin CPanel, también es manual.

## Why It Matters
Es la **política de migración del vault convertida en cláusula operativa**: el proveedor **sí ofrece el servicio de migración, pero solo si el cliente instala la misma pila de software que el proveedor**, y la licencia de CPanel/WHM **no viene incluida**. Eso significa dos costes ocultos en la partida de migración: la licencia de cPanel y el trabajo de un cliente que hoy tiene shared hosting pero no sabe Panel. Es exactamente el patrón que el vault ya aisló con BuyVM, donde el DirectAdmin "gratis" **restringe su licencia a las IP de BuyVM** ([[2026-1024-buyvm-directadmin-gratuito-con-licencia-restringida-a-sus-ips]]) — aquí la restricción es de sentido inverso: la licencia es tuya, pero **la migración asistida depende de que instales esa misma pila**. Para el vault esto importa en un punto concreto: la trayectoria documentada de HostBrr es **shared → VPS con root** ([[2026-1024-hostbrr-cpanel-reseller-5-00-white-label-blesta-whmcs]] es la línea de reseller equivalente), y FlokiNET ofrece el mismo tramo, pero con el condicionante de que **el panel se paga aparte**.

## Nota de verificación
La captura **no** publica: precio de la licencia de CPanel/WHM, si FlokiNET la revende con descuento, ni el precio del servicio de migración. "License not included by default" sugiere que puede contratarse aparte, pero no consta el mecanismo. La frase "in a matter of minutes" es del proveedor y no tiene cifra de throughput.
