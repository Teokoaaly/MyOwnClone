# Extensiones a átomos existentes — captura 2026-10-26-dataimpulse-docs-home (2026-10-27)

Fuente: `sources/2026-10-26-dataimpulse-docs-home.md` (captura `0-raw/2026-10-26-dataimpulse-docs-home.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1024-dataimpulse-gateway-unico-y-protocolos
## Nota de extensión 2026-10-27
La home de la documentación **nombra por fin la función de autorización por IP** que este átomo solo registraba como una fila de las tablas de precios ("Authorization by IP"). La sección "Jump right in" de `docs.dataimpulse.com/` la titula **"Whitelist Ips"** con la promesa literal: **"Make requests without login and password"**. Es decir, la autorización por IP no es una característica de marketing sino una **sección de documentación propia**, con un nombre de sección publicable.
El detalle operativo que añade es el inverso del que el átomo suponía: la alternativa a `login:password@gw.dataimpulse.com:823` no es una variante de credenciales sino **ausencia de credenciales** — las peticiones se autentican por IP de origen. Para un despliegue autoalojado como el nginx del vault ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) eso significa que el proxy puede consumirse **desde cualquier nodo sin distribuir credenciales por nodo**, tal como anticipaba este átomo, pero por un mecanismo distinto al que daba por hecho: no es "Authorization by IP" como opción de la tabla de precios sino una función documentada con su propia página.
La captura **no** publica: cuántos CIDR se pueden añadir a la whitelist, si la whitelist es por cuenta o por subcuenta, ni si la autenticación por IP es acumulable con `login:password` o excluyente. Ver también [[2026-1027-dataimpulse-puerto-823-http-https-y-824-socks5-en-rotating]].
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-soporte-24-7-y-canal-enterprise
## Nota de extensión 2026-10-27
La home de la documentación aporta los **canales de contacto concretos** que este átomo solo nombraba como categorías ("Chat or email, around the clock, 24/7"): la dirección es **support@dataimpulse.com** y el segundo canal es el **"24/7 live chat on the website"**, con enlace a `dataimpulse.com`. Es decir, el "chat" del que habla el átomo es el chat de la web comercial, no una interfaz dentro del dashboard.
La captura añade además dos recursos de onboarding que el átomo no registra: un **vídeo de YouTube** ("How to manage your DataImpulse account: a step-by-step tutorial", canal DataImpulse, **6.01K** subs) y un **blog post** ("Step-by-Step Guide to Getting Started with DataImpulse"). No son cifras de proveedor, pero son la señal de que el alta de cuenta proxy se gestiona como **producto**, no como signup de API: quien compra capacidad para automatizar altas tiene, por el mismo proveedor, tutorial de gestión de cuenta y canal de soporte 24/7 con personas.
Nota de verificación de esta extensión: la captura **no** publica SLA del chat, horario en zonas horarias concretas ni si el chat 24/7 es el mismo canal de los <1,5 min de respuesta media que este átomo registra.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad
## Nota de extensión 2026-10-27
La documentación publica una sección **"Auto-recharge"** ("Don't worry about balance") que este átomo no registra, y que **cambia la lectura del flujo de compra** que el átomo transcribe: el paso "Top up your balance and activate your proxy" no es necesariamente manual, porque el saldo puede **rellenarse solo**. Ver [[2026-1027-dataimpulse-auto-recharge-publicado-en-la-documentacion]], que registra el dato y su fricción con este átomo.
El efecto combinado con "Traffic never expires" es el que hay que dejar anotado: **saldo que no caduca + recarga automática = gasto recurrente sin decisión por topping-up ni aviso**, es decir, el control de caja que este átomo daba por estructurado (saldo, prepago, sin permanencia) admite en realidad un **pedido recurrente (standing order)** que el propio producto ofrece. La captura **no** publica umbral, importe ni periodicidad de la recarga, de modo que la cifra que falta es la que decide si esa función es un control o un riesgo.
=== END
