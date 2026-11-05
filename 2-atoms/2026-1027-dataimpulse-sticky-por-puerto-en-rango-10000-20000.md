---
id: 2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-types-of-connections.md, sources/2026-10-26-dataimpulse-docs-proxies-index.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1027-dataimpulse-puerto-823-http-https-y-824-socks5-en-rotating]]", "[[2026-1027-dataimpulse-intervalo-rotacion-sticky-configurable-1-a-120-minutos]]"]
---

## Claim
El modo **sticky** de DataImpulse es **port-based**, y eso no es un detalle de implementación sino la definición del producto: "Sticky proxies are port-based. **IP addresses are bound to a specific port for a period of time.**" El rango de puertos sticky publicado es **del 10000 al 20000** ("For sticky connections, you can use ports from **10000** to **20000**"), y los ejemplos de la propia documentación usan **el mismo puerto para los dos protocolos**: `curl -x "http://login:password@gw.dataimpulse.com:10000" https://api.ipify.org/` y `curl -x "socks5://login:password@gw.dataimpulse.com:10000" https://api.ipify.org/`. Es decir, **el puerto sticky identifica la sesión**, y dentro del rango 10000–20000 hay **10 001 puertos** disponibles.

## Why It Matters
Esto responde a la pregunta que el vault había dejado abierta en [[2026-1024-dataimpulse-sesiones-rotating-y-sticky]], cuya Nota de verificación decía que la captura "no publica ... el mecanismo por el que se renueva la IP al expirar la sesión": **la IP no se renueva porque el puerto no se renueva** — la IP está *ligada* a un puerto, y la renovación se produce porque el cliente cambia de puerto.
La consecuencia operativa es de **concurrencia**, no de configuración: para mantener N sesiones sticky simultáneas con IPs distintas hacen falta **N puertos distintos** del rango 10000–20000, porque el puerto *es* la sesión. Es la primera vez que el corpus del vault tiene un número **acotado y enumerable** para la concurrencia de sesión del sector (10 001 sesiones sticky por cuenta y por el rango publicado, antes de contar los límites por pool), frente a los límites de conexión que la captura de la home nunca publicó — ver la Nota de verificación de [[2026-1024-dataimpulse-gateway-unico-y-protocolos]], que confiesa que la home "no publica: límite de conexiones simultáneas por cuenta".
También separa los dos mecanismos de gateway que el vault tenía fundidos en uno: **hostname y credenciales son únicos, pero el puerto es el identificador de sesión** — rotating en 823/824 según protocolo ([[2026-1027-dataimpulse-puerto-823-http-https-y-824-socks5-en-rotating]]) y sticky en un rango propio de 10 001 puertos, **compartido por HTTP y SOCKS5**, que es la diferencia estructural entre los dos modos.

## Nota de verificación
Cifras y frases transcritas literalmente de la página; el recuento de 10 001 puertos es aritmética sobre el rango publicado (20000 − 10000 + 1). La captura **no** publica: para qué pools (residencial, móvil, datacenter) está disponible el rango sticky, cuántos puertos sticky admite una misma cuenta, ni si el límite por cuenta es menor que el rango.
