---
id: 2026-1026-suno2openai-cuatro-endpoints-de-gestion-de-cookies
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1026-github-search-suno-pool-de-cookies-y-relay-newapi-oneapi]]", "[[2026-1024-gptgrok2api-sondeo-y-recuperacion-automatica-de-cuentas-grok]]"]
---

## Claim
El README documenta **cinco endpoints** y solo uno es el de generación. Cuatro operan sobre el pool, bajo un **prefijo configurable** (`COOKIES_PREFIX`, con la instrucción de que empiece por `/`): `PUT /<prefijo>/cookies` (**añadir** cookies, cuerpo `{"cookies": [...]}`), `POST /<prefijo>/cookies` (**listar todas**), `DELETE /<prefijo>/cookies` (**borrar** las indicadas, mismo cuerpo) y `GET /<prefijo>/refresh/cookies` (**refrescar** cookies). El quinto, `POST /v1/chat/completions`, es la generación, con `model`, `messages` y `stream` opcional. Los cinco comparten **la misma cabecera de autorización**: `Authorization: Bearer <AUTH_KEY>`.

## Why It Matters
La API documentada delata que **la unidad de capacidad es la cookie y su ciclo de vida es una API de primer nivel**, no un detalle interno: se puede listar el pool entero, borrarlo parcialmente y refrescarlo. Ese `refresh` es la pieza que más importa para el vault, porque es la **renovación de la credencial** —el mismo problema que en `gptGrok2api` se resuelve con sondeo automático cada 60 minutos y una taxonomía de tres estados (inválida / desconocida / no efectiva por cuota) ([[2026-1024-gptgrok2api-sondeo-y-recuperacion-automatica-de-cuentas-grok]]). Aquí la renovación es **un endpoint que alguien (o algo) tiene que llamar**, no un lazo de salud: el README no publica criterio de selección, ni qué cookies se consideran caducadas, ni si el refresco reautentica o solo renueva el token.
El segundo dato de la atomización es el **prefijo de gestión aplicado sobre la ruta del mismo servidor que sirve la inferencia**: `COOKIES_PREFIX` no es un subdominio ni un puerto aparte, es una cadena dentro de la URL pública, lo que significa que **la superficie de administración es adivinable solo por quien configure el despliegue** —una medida de ofuscación barata, no un control de acceso. Combinada con el `AUTH_KEY` único para las cinco rutas, la frontera real de seguridad es **una sola clave compartida** entre administración y serving.
Y para el modelo de negocio del vault esto es la confirmación de lo que la `description` del repo ya anunciaba: **la capa vendible es el pool, y el pool se opera por API** ([[2026-1026-github-search-suno-pool-de-cookies-y-relay-newapi-oneapi]]).
