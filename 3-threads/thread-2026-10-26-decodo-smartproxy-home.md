# Thread de síntesis — captura 2026-10-26-decodo-smartproxy-home

## Procesamiento

Se procesó la captura `2026-10-26-decodo-smartproxy-home.md` y su fuente `sources/2026-10-26-decodo-smartproxy-home.md` (homepage completa de decodo.com, 1158 líneas, 33.071 palabras). La captura documenta la evolución de Smartproxy a Decodo, las ofertas de proxy y API, los precios de catálogo, y el FAQ de preguntas frecuentes.

## Átomos creados (3 total)

Desde la captura original se derivaron 3 nuevos átomos:

1. `2026-1026-decodo-prueba-gratis-3-dias-y-plan-gratuito-api` — Dos mecanismos de entrada gratuitos: trial de 3 días para proxies (auto-activation cancela garantía de 14 días) y plan gratuito starter para Web Data API ($5 créditos, hasta 10K solicitudes, sin tarjeta).

2. `2026-1026-decodo-115m-ips-residenciales` — 115M+ IPs éticamente sourcing en la red residencial de Decodo, con targeting a nivel de continente, país, estado, ciudad y ASN gratis en todos los planes.

3. `2026-1026-do-proxies-proporcionan-anonimato` — El FAQ aclara que los proxies enmascaran la IP pero el nivel de anonimato varía por proveedor; el riesgo de fallo de elusión recae en el cliente salvo que el proveedor lo asuma. También diferencia proxy de VPN por modelo de cobertura y caso de uso.

## Fricciones relevantes

- La prueba de 3 días para proxies **auto-activate el plan de pago** al finalizar, lo que **anula la garantía de 14 días** que la misma home publica. Este patrón de dark pattern de suscripción es consistente con lo visto en ProtonVPN ([[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]]) y contradice la protección que el usuario cree tener. (Ver átomo [[2026-1026-decodo-prueba-gratis-3-dias-y-plan-gratuito-api]])

- Los **precios publicados en la home no siempre son el precio de entrada real**: el titular de "starting at $2/GB" es el mejor caso del catálogo, no el precio mínimo (ver átomo [[2026-1027-decodo-titular-de-2-por-gb-y-entrada-real-de-375]]). La captura del home y la de pricing son fuentes distintas pero complementarias.

- La sección de rebranding del FAQ declara que **Smartproxy.org no es Decodo** y es un dominio de terceros, con el aviso "Just be careful with the old name: Smartproxy.org isn't us". Esto establece la propiedad del dominio `.org` como impersonator, patrón ya visto con SMS-Activate ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]). (Ver átomo [[2026-1027-decodo-smartproxy-org-es-un-impostor-y-el-mismo-equipo-desde-2018]])

- El targeting a nivel de ASN es **gratis en todos los planes de Decodo** (residencial, datacenter, ISP), mientras que competidores como DataImpulse lo cobran por país. Esto hace comparable el modelo de coste IP a IP con proveedores que sí cobran por geolocalización. (Ver átomo [[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]])

## Enlaces transversales

- [[2026-1027-decodo-smartproxy-org-es-un-impostor-y-el-mismo-equipo-desde-2018]] — rebrand, dominio .org, ratings de Trustpilot/G2/Proxyway
- [[2026-1027-decodo-site-unblocker-a-095-por-mil-de-solicitudes-como-producto-de-catalogo]] — Site Unblocker pricing a $0.95/1K req
- [[2026-1026-decodo-prueba-de-3-dias-con-100-mb-y-autoactivacion-del-plan]] — trial de 3 días con 100 MB (fuente distinta: residential pricing)
- [[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]] — targeting granular gratis en todos los planes (fuente distinta: residential pricing)
- [[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]] — patrón de dominio .org impersonator (corpus reference)
- [[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]] — dark pattern de trial auto-activado (corpus reference)
- [[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]] — modelo de riesgo en cobro por captchas resueltos vs requests (corpus reference)