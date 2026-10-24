---
id: 2026-1024-dataimpulse-gateway-unico-y-protocolos
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]"]
---

## Claim
El acceso técnico es un **gateway único** con los mismos parámetros en los siete lenguajes que muestra la home (Python, Node.js, PHP, C#, Go, Ruby, curl): `hostname = 'gw.dataimpulse.com'`, `port = 823`, autenticación `login`/`password` en la URL (`http://{login}:{password}@{hostname}:{port}`), timeout 30 s en los ejemplos y consulta de verificación a `http://ip-api.com/json` devolviendo IP, Country, State, City, Zipcode, ASN y Status. Protocolos soportados: **HTTP / HTTPS / SOCKS5** ("Use any protocol depending on your setup"), con fila común en las cuatro tablas de precios. La tabla incluye además **"Authorization by IP"** como característica, y la lista de integraciones de terceros cubre Scrapy, Puppeteer, Selenium, Shadowrocket, Multilogin, AdsPower, Playwright, GoLogin, SwitchyOmega, Octoparse, SessionBox, Zapier, Postman, Hubstudio, Parsehub y Proxifier.

## Why It Matters
Es un detalle de integración con consecuencia operativa: **todos los tipos de proxy comparten el mismo endpoint y el mismo par de credenciales**, así que cambiar de datacenter a residencial premium no obliga a tocar el código — solo el usuario. Eso permite empezar al precio de $0.50/GB ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) y subir a $5/GB solo en los flujos que fallen.
Para un despliegue autoalojado como el nginx del vault ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), la combinación de "Authorization by IP" + gateway único significa que el proxy se puede consumir desde cualquier nodo sin distribuir credenciales por nodo, algo que importa cuando el vault ya tiene [[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]] como precedente de panel de control con sub-cuentas.

## Nota de verificación
Literales transcritos del bloque de código. La captura **no** publica: límite de conexiones simultáneas por cuenta, ancho de banda por conexión, si el puerto 823 es el mismo para los cuatro tipos de proxy, ni política de rotación de credenciales.
