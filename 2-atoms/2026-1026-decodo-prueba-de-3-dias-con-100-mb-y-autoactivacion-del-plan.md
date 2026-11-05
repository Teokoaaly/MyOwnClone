---
id: 2026-1026-decodo-prueba-de-3-dias-con-100-mb-y-autoactivacion-del-plan
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1026-decodo-reembolso-14-dias-con-limite-del-20-y-10-de-trafico]]", "[[2026-1024-mullvad-sin-plan-gratuito-ni-ventas-y-por-que]]", "[[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]"]
---

## Claim
Decodo ofrece una **prueba gratuita de 3 días con 100 MB** ("Enjoy 100 MB for 3 days"), disponible solo para nuevos usuarios, y su FAQ describe el comportamiento de la prueba con una frase explícita: **"after the trial period ends, your chosen plan will activate automatically, and you can cancel anytime before then"**. La página cierra con el mismo mensaje: "Get a 3-day free trial with 100MB". El KB de pruebas repite 100 MB / 3 días en dos sitios distintos.

## Why It Matters
La prueba no es neutra: **es un activador automático del plan de pago**. El flujo de salida del trial —activación automática y cancelación manual antes— es un patrón de dark pattern de suscripción que el vault ya vio en otro sitio del corpus: Proton convierte el descuento en un **"65% off" que caduca y la renovación sube a $6,99/mes** ([[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]]). Aquí el riesgo es de otro tipo: el plan elegido se activa solo, y **la prueba de 3 días es incompatible con la garantía de 14 días** ("a 14-day money-back option doesn't apply with a 3-day free trial", ver [[2026-1026-decodo-reembolso-14-dias-con-limite-del-20-y-10-de-trafico]]), de modo que **quien prueba pierde la única protección que la página publica**.
Y el volumen de la prueba es diminuto: **100 MB** para tres días. Con el criterio del vault —un alta consume el número de sesiones sticky, no 1 GB ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]])— 100 MB alcanzan para **pocas sesiones**, no para medir la calidad del pool en el destino real. Es decir: la prueba sirve para comprobar que el proxy conecta, no para comprobar que **no bloquea** en el sitio de destino, que es la única pregunta que importa para una verificación. Contraste con el sector: el único proveedor del corpus que **no da prueba alguna** lo declara como política, no como efecto colateral ([[2026-1024-mullvad-sin-plan-gratuito-ni-ventas-y-por-que]]).

## Nota de verificación
Frases transcritas literalmente. La captura **no** publica: si los 100 MB son consumption-only, qué tarifa se aplica al superar los 100 MB, ni si el plan enterprise tiene prueba (el plan de 1 TB no ofrece "Start free trial").


## Nota de extensión 2026-10-27
La home confirma la existencia de **dos free tiers distintos** en la misma marca, y el FAQ los separa con precisión: *"Decodo offers a **3-day free trial for proxies**, as well as a **free starter plan for its Web Data API** that includes **$5 in testing credits (up to 10k requests) with no credit card required** to get started."*

Lo que este átomo establece —que la prueba de proxies **auto-activa el plan de pago** al terminar y por tanto **anula la garantía de 14 días**— **se mantiene sin cambio**, pero ahora hay que leerlo junto a un dato nuevo: **la Web Data API no tiene trial sino plan gratuito permanente**, y el banner de cierre de la home dice **"up to 10K free monthly requests"**. Es decir: **la línea de scraping tiene una entrada recurrente y sin tarjeta**, y la línea de proxy tiene una prueba de tres días que **convierte sola en commitment**. El vault debe cotizar **dos mecanismos de entrada distintos** para el mismo actor, con_semántica de riesgo opuesta. Ver [[2026-1027-decodo-plan-gratuito-de-la-web-data-api-con-5-de-credito-y-10k-solicitudes-sin-tarjeta]].
