---
id: 2026-1027-mail-tm-limite-de-8-qps-por-ip-address
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-docs.md]
links: ["[[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]", "[[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]]", "[[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]"]
---

## Claim
La sección "Access to the API" de `docs.mail.tm/` publica un único techo de cuota, explícito y con unidad: "**8 QPS rate limit**" y "The general quota limit is **8 queries per second (QPS) per IP address**". La misma sección declara el acceso sin credenciales: "Completely free. **No API key, no signup, no paid tiers.**" y "Just call the endpoints. **No signup, no tokens to start.**"

## Why It Matters
Es la **primera cifra de rendimiento del sector de correo desechable del vault**, y por eso mismo cambia lo que la tabla de coste por insumo puede afirmar. Hasta ahora el corpus del correo publicaba **capacidad y ciclo de vida** (40 MB por buzón, "kept forever", "no limit" de unidades) pero **ningún techo de throughput**: mail.tm declara ahora un límite de llamadas por segundo, que es el límite que realmente decide si un flujo de alta puede externalizar el buzón.

La aritmética que se deriva de las dos cifras publicadas, con el flujo de cuatro llamadas por buzón ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]): **8 QPS ÷ 4 llamadas = 2 buzones por segundo y 7.200 buzones por hora desde una sola IP**; si el `GET /domains` se cachea y sólo quedan cuenta + token + mensajes, el techo sube a **2,67 buzones/s y 9.600 buzones/hora**. El contraste con el otro techo de correo medido en el vault es el dato: el sidecar de iCloud Privacy Mail del bot de registro tiene un contrato de **20 buzones/hora** ([[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]]), es decir **360 veces menos**. Un proveedor gratuito sin clave llega a multiplicar por dos órdenes de magnitud el ritmo de buzones de la línea internalizada.

Pero el límite es de **cadencia, no de unidades**: mail.tm no publica ningún tope de buzones por cuenta, coherente con "no limit on how many disposable addresses you create" ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]). Es decir, la restricción operativa real es "a qué ritmo puedo crear y leer", y el techo de unidades sigue siendo virtualmente infinito: **un flujo de alta puede crear miles de buzones y solo se ve frenado por el 8 QPS**.

## [FRICTION]
> [[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]] sostiene que el valor del sidecar de iCloud Privacy Mail es que **el contrato explícito —20/5/25 buzones por hora y tope de 750 acumulados por cuenta— es lo que hace que el recurso sea gobernable**, y que sin contrato el buzón es un coste sin techo.
> Este átomo presiona esa lectura en un punto: mail.tm publica un contrato **de otro tipo** —8 QPS por IP— y ese contrato **no acota el número de buzones**, solo la velocidad. O el contrato útil es el que limita **unidades** —y entonces el 8 QPS es irrelevante para el gobierno del recurso y mail.tm es de nuevo un pasivo acumulativo— o el contrato útil es el que limita **cadencia** —y entonces el sidecar, que limita unidades pero no el ritmo, es el diseño incompleto y el proveedor gratuito tiene el contrato más adecuado para un pipeline de alta. Ambas no pueden ser la misma regla de lectura. Marcado para juicio humano, no auto-resuelto: la captura **no** publica el comportamiento del límite al superarse (¿429? ¿cola?), ni si el límite es por IP compartida, ni SLA.

## Nota de verificación
"8 QPS rate limit", "The general quota limit is 8 queries per second (QPS) per IP address", "Completely free. No API key, no signup, no paid tiers." y "Just call the endpoints. No signup, no tokens to start." están transcritos literalmente. Los caudales derivados (2 buzones/s, 7.200/h, 2,67/s, 9.600/h, ×360) son **aritmética del vault sobre las cuatro llamadas documentadas y el 8 QPS publicado**, no cifras de la fuente.
